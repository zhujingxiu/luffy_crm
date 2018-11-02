#!/usr/bin/env python
# -*- coding:utf-8 -*-
# _AUTHOR_  : zhujingxiu
# _DATE_    : 2018/9/12
import functools
from types import FunctionType, MethodType
from django.forms import ModelForm
from django.utils.safestring import mark_safe
from django.template.loader import render_to_string
from django.shortcuts import render, reverse, HttpResponse, redirect
from django.db.models.fields.related import ForeignKey, ManyToManyField
from .utils.response import XStarkErrorResponse, XStarkSuccessResponse


def get_choice_text(field, head=None):
    """
    获取choice对应的内容，可由双下划线模式获取关联字段内容，暂时仅支持跨单表查询
    :param field:  字段名称
    :param head: 表头名称
    :return:
    """
    def inner(self, entity=None, header=False):
        try:
            model_field = self.admin_model._meta.get_field(field)
            func_name = "get_%s_display" % field
            _related_field = False
        except:
            _related_field, _field = field.split('__')
            _relate_cls = self.admin_model._meta.get_field(_related_field).related_model
            model_field = _relate_cls._meta.get_field(_field)
            func_name = "get_%s_display" % _field
        if header:
            return head or model_field.verbose_name
        try:
            entity_obj = entity if not _related_field else getattr(entity, _related_field)
        except:
            return ''
        else:
            return getattr(entity_obj, func_name)()

    return inner


class SiteMapping(object):
    def __init__(self, model, site, prefix):
        self.model = model
        self.site = site
        self.prefix = prefix


class Row(object):
    def __init__(self, data_list, option, query_dict, verbose_name=None):
        """
        元组
        :param data_list:元组或queryset
        """
        self.data_list = data_list
        self.option = option
        self.query_dict = query_dict
        self.verbose_name = verbose_name

    def __iter__(self):
        yield '<div class="allof">'

        total_query_dict = self.query_dict.copy()
        total_query_dict._mutable = True
        origin_value_list = self.query_dict.getlist(self.option.field)  # [2,]
        if origin_value_list:
            total_query_dict.pop(self.option.field)
            yield '<a href="?%s">全部 %s</a>' % (total_query_dict.urlencode(), self.verbose_name)
        else:
            yield '<a class="active" href="?%s">全部 %s</a>' % (total_query_dict.urlencode(), self.verbose_name)

        yield '</div>'
        yield '<div class="others">'

        for item in self.data_list:  # item=(),queryset中的一个对象
            val = self.option.get_value(item)
            text = self.option.get_text(item)

            query_dict = self.query_dict.copy()
            query_dict._mutable = True

            if not self.option.is_multi:  # 单选
                if str(val) in origin_value_list:
                    query_dict.pop(self.option.field)
                    yield '<a class="active" href="?%s">%s</a>' % (query_dict.urlencode(), text)
                else:
                    query_dict[self.option.field] = val
                    yield '<a href="?%s">%s</a>' % (query_dict.urlencode(), text)
            else:  # 多选
                multi_val_list = query_dict.getlist(self.option.field)
                if str(val) in origin_value_list:
                    # 已经选，把自己去掉
                    multi_val_list.remove(str(val))
                    query_dict.setlist(self.option.field, multi_val_list)
                    yield '<a class="active" href="?%s">%s</a>' % (query_dict.urlencode(), text)
                else:
                    multi_val_list.append(val)
                    query_dict.setlist(self.option.field, multi_val_list)
                    yield '<a href="?%s">%s</a>' % (query_dict.urlencode(), text)

        yield '</div>'


class Option(object):
    def __init__(self, field, condition=None, is_choice=False, is_multi=False, text_func=None, value_func=None, verbose_name=None):
        self.field = field
        self.is_choice = is_choice
        if not condition:
            condition = {}
        self.condition = condition
        self.is_multi = is_multi
        self.text_func = text_func
        self.value_func = value_func
        self.verbose_name = verbose_name

    def get_queryset(self, _field, model_class, query_dict):
        '''
        获取结果集
        :param _field:
        :param model_class:
        :param query_dict:
        :return:
        '''
        verbose = self.verbose_name or _field.verbose_name
        if isinstance(_field, ForeignKey) or isinstance(_field, ManyToManyField):
            row = Row(_field.related_model.objects.filter(**self.condition), self, query_dict, verbose_name=verbose)
        else:
            if self.is_choice:
                row = Row(_field.choices, self, query_dict, verbose_name=verbose)
            else:
                row = Row(model_class.objects.filter(**self.condition), self, query_dict, verbose_name=verbose)
        return row

    def get_text(self, item):
        '''
        获取模型实例指定字段文本
        :param item:
        :return:
        '''
        if self.text_func:
            return self.text_func(item)
        if self.is_choice:
            return item[1]
        return str(item)

    def get_value(self, item):
        '''
        获取模型实例指定字段值
        :param item:
        :return:
        '''
        if self.value_func:
            return self.value_func(item)
        if self.is_choice:
            return item[0]
        return item.pk


class ChangeList(object):
    def __init__(self, site_model, queryset, q, search_list, page):
        self.q = q
        self.search_list = search_list
        self.page = page
        self.site = site_model
        self.add_button = site_model.display_add()
        self.action_list = [{'name': action.__name__, 'text': action.text} for action in site_model.get_action_list()]
        self.queryset = queryset

        self.list_display = site_model.get_list_display()
        self.list_filter = site_model.get_filter_list()

    def get_model_field(self, field):
        '''
        获取模型字段，可由双下划线模式（model__field）获取关联字段内容，暂时仅支持跨单表查询
        :param field:
        :return:
        '''
        try:
            model_field = self.site.admin_model._meta.get_field(field)
        except:
            _relate_field, _field = field.split('__')
            _relate_cls = self.site.admin_model._meta.get_field(_relate_field).related_model
            model_field = _relate_cls._meta.get_field(_field)
        return model_field

    def gen_list_filters(self):
        '''
        获取组合搜索项
        :return:
        '''

        if self.list_filter:
            for option in self.list_filter:
                if isinstance(option, str):
                    option = Option(option)
                _field = self.get_model_field(option.field)
                yield option.get_queryset(_field, self.site.admin_model, self.site.request.GET)

    def gen_list_header(self):
        '''
        获取列表表头
        :return:
        '''
        if not self.list_display:
            yield self.site.admin_model._meta.model_name
        else:
            for field in self.list_display:
                if isinstance(field, FunctionType) or isinstance(field, MethodType):
                    yield field(self.site, header=True)
                else:
                    yield self.get_model_field(field).verbose_name

    def gen_list_body(self):
        '''
        获取模型实例列表
        :return:
        '''
        for item in self.queryset:
            row = []
            if not self.list_display:
                row.append(item)
            else:
                for field in self.list_display:
                    if isinstance(field, FunctionType) or isinstance(field, MethodType):
                        row.append(field(self.site, entity=item))
                    else:
                        model_field = self.get_model_field(field)
                        if isinstance(model_field, ManyToManyField):
                            _all_related = getattr(getattr(item, field), 'all')()
                            row.append([_related for _related in _all_related])
                        else:
                            row.append(getattr(item, field))
            yield row


class StarkAdminModel(object):
    '''
    list_display: 模型实例的显示字段
    order_by: 模型实例的排序规则
    action_list: 模型实例的批量操作
    filter_list: 关键字搜索涉及到的模型实例的字段
    model_form_class: 指定实例的模型
    display_option：是否显示编辑删除合并项，默认显示
    request_get_key：自定义session存储request数据的键
    '''
    list_display = []
    order_by = []
    action_list = []
    search_list = []
    filter_list = []
    model_form_class = None
    display_option = True
    request_get_key = 'xstark_get'

    admin_title = ''

    def __init__(self, model_cls, site_cls, prefix=None):
        self.admin_model = model_cls
        self.admin_site = site_cls
        self.prefix = prefix
        self.request = None

    def get_site_title(self):
        return self.admin_model._meta.verbose_name

    @property
    def site_app(self):
        return self.admin_model._meta.app_label

    @property
    def site_model(self):
        return self.admin_model._meta.model_name

    def bulk_delete(self, request):
        pk_ids = request.POST.getlist('pk')
        queryset = self.admin_model.objects.filter(pk__in=pk_ids)
        return HttpResponse('delete { %s }' % (','.join([item.__str__() for item in queryset])))

    bulk_delete.text = '批量删除'

    def get_action_list(self):
        actions = []
        actions.append(StarkAdminModel.bulk_delete)
        actions.extend(self.action_list)
        return actions

    def get_action_dict(self):
        data = {}
        for action in self.get_action_list():
            data[action.__name__] = action
        return data

    def get_filter_list(self):
        fields = []
        fields.extend(self.filter_list)
        return fields

    def get_filter_condition(self):
        comb_condition = {}
        for option in self.get_filter_list():
            if isinstance(option, str):
                option = Option(option)
            element = self.request.GET.getlist(option.field)
            if element:
                comb_condition['%s__in' % option.field] = element

        return comb_condition

    def get_search_list(self):
        fields = []
        fields.extend(self.search_list)
        return fields

    def get_search_condition(self, request):
        from django.db.models import Q
        search_list = self.get_search_list()
        condition = Q()
        condition.connector = 'OR'
        q = request.GET.get('q', '')
        if q:
            for field in self.get_search_list():
                condition.children.append(('%s__contains' % field, q))
        return search_list, q, condition

    def wrapper(self, func):
        @functools.wraps(func)
        def inner(request, *args, **kwargs):
            if request.GET:
                request.session[self.request_get_key] = request.GET.urlencode()
            self.request = request
            return func(request, *args, **kwargs)

        return inner

    def get_urls(self):
        from django.urls import path

        urlpatterns = [
            path('', self.wrapper(self.changelist_view), name=self.get_list_url_name),
            path('add/', self.wrapper(self.add_view), name=self.get_add_url_name),
            path('<path:entity_id>/delete/', self.wrapper(self.delete_view), name=self.get_del_url_name),
            path('<path:entity_id>/change/', self.wrapper(self.change_view), name=self.get_change_url_name),
        ]

        extra_urls = self.extra_urls()

        if extra_urls:
            urlpatterns.extend(extra_urls)
        return urlpatterns

    @property
    def urls(self):

        return self.get_urls()

    def extra_urls(self):
        return []

    def get_order_by(self):
        return self.order_by

    def get_list_display(self):
        display = []
        display.append(StarkAdminModel.display_checkbox)
        display.extend(self.list_display)
        if StarkAdminModel.display_edit not in display and StarkAdminModel.display_delete \
                not in display and StarkAdminModel.display_option:
            display.append(StarkAdminModel.display_options)
        return display

    def display_checkbox(self, entity=None, header=False):
        if header:
            return mark_safe('<input type=checkbox id="id-all">')
        return mark_safe('<input type=checkbox name=pk value="%s">' % entity.pk)

    def get_queryset(self):
        return self.admin_model.objects

    def changelist_view(self, request):
        '''
        模型实例列表视图
        :param request:
        :return:
        '''
        if request.method == 'POST':
            method_name = request.POST.get('action')
            method_dict = self.get_action_dict()
            if method_name in method_dict:
                return getattr(self, method_name)(request)

        search_list, q, condition = self.get_search_condition(request)
        total_count = self.get_queryset().filter(condition).filter(**self.get_filter_condition()).count()
        from xstark.utils.pagination import Pagination

        query_params = request.GET.copy()
        query_params._mutable = True
        page = Pagination(request.GET.get('page'), total_count, request.path_info, query_params, per_page=8)

        queryset = self.get_queryset().filter(condition).filter(**self.get_filter_condition()).order_by(
            *self.get_order_by()).distinct()[page.start:page.end]
        context = {'cl': ChangeList(self, queryset, q, search_list, page)}
        return render(request, 'xstark/changelist.html', context)

    def display_add(self):
        return mark_safe('<a href="%s" class="btn btn-primary"><i class="fa fa-plus"></i> 添加</a>'
                         % self.reverse_display_add())

    def display_edit(self, entity=None, header=False):
        if header:
            return mark_safe('编辑')
        return mark_safe('<a href="%s" class="btn btn-info btn-sm"><i class="fa fa-edit"></i> 编辑</a>'
                         % self.reverse_display_edit(entity=entity))

    def display_delete(self, entity=None, header=False):
        if header:
            return mark_safe('删除')
        return mark_safe('<a data-href="%s" class="btn btn-danger btn-sm btn-perm"><i class="fa fa-trash"></i> 删除</a>'
                         % self.reverse_display_delete(entity=entity))

    def display_options(self, entity=None, header=False):
        if header:
            return mark_safe('操作')
        return mark_safe('''<a href="%s" class="btn btn-info btn-sm"><i class="fa fa-edit"></i> 编辑</a>
            <a data-href="%s" class="btn btn-danger btn-sm btn-perm"><i class="fa fa-trash"></i> 删除</a>
            ''' % (self.reverse_display_edit(entity=entity), self.reverse_display_delete(entity=entity)))

    def reverse_display_list(self):
        return reverse('%s:%s' % (self.admin_site.namespace, self.get_list_url_name))

    def reverse_display_add(self):
        return reverse('%s:%s' % (self.admin_site.namespace, self.get_add_url_name))

    def reverse_display_edit(self, entity):
        return reverse('%s:%s' % (self.admin_site.namespace, self.get_change_url_name), kwargs={'entity_id': entity.pk})

    def reverse_display_delete(self, entity):
        return reverse('%s:%s' % (self.admin_site.namespace, self.get_del_url_name), kwargs={'entity_id': entity.pk})

    @property
    def get_list_url_name(self):
        if self.prefix:
            name = '%s_%s_%s_changelist' % (self.site_app, self.site_model, self.prefix)
        else:
            name = '%s_%s_changelist' % (self.site_app, self.site_model)
        return name

    @property
    def get_add_url_name(self):
        if self.prefix:
            name = '%s_%s_%s_add' % (self.site_app, self.site_model, self.prefix)
        else:
            name = '%s_%s_add' % (self.site_app, self.site_model)
        return name

    @property
    def get_change_url_name(self):
        if self.prefix:
            name = '%s_%s_%s_change' % (self.site_app, self.site_model, self.prefix)
        else:
            name = '%s_%s_change' % (self.site_app, self.site_model)
        return name

    @property
    def get_del_url_name(self):
        if self.prefix:
            name = '%s_%s_%s_delete' % (self.site_app, self.site_model, self.prefix)
        else:
            name = '%s_%s_delete' % (self.site_app, self.site_model)
        return name

    def get_model_form(self, request=None):
        '''
        通过request传参获取不同的实例模型
        :param request:
        :return:
        '''
        if self.model_form_class:
            return self.model_form_class

        class EntityModelForm(ModelForm):
            class Meta:
                model = self.admin_model
                fields = '__all__'

        return EntityModelForm

    def save(self, form, modify=False):
        entity = form.save()
        return entity

    def get_form_instance(self, data=None, instance=None, request=None):
        '''
        通过request传参获取不同的FORM表单
        :param data: 提交的新数据
        :param instance: 原实例数据
        :param request: 请求参数
        :return:
        '''
        form = self.get_model_form(request=request)
        return form(data=data, instance=instance)

    def add_view(self, request):
        '''
        模型实例的添加视图
        :param request:
        :return:
        '''
        list_url = self.reverse_display_list()
        form = self.get_form_instance(request=request)
        if request.method == 'POST':
            form = self.get_form_instance(data=request.POST, request=request)
            if form.is_valid():
                self.save(form)
                return redirect(self.reverse_display_list())
            else:
                print(form.errors)
        return render(request, 'xstark/change.html', {'form': form, 'list_url': list_url})

    def change_view(self, request, entity_id):
        '''
        模型实例的编辑视图
        :param request:
        :param entity_id:
        :return:
        '''
        entity = self.admin_model.objects.filter(pk=entity_id).first()
        if not entity:
            return XStarkErrorResponse('不存在').json()
        if request.method == 'POST':
            form = self.get_form_instance(data=request.POST, instance=entity, request=request)
            self.save(form,  modify=True)
            return redirect(self.reverse_display_list())
        list_url = self.reverse_display_list()
        form = self.get_form_instance(instance=entity, request=request)
        return render(request, 'xstark/change.html', {'form': form, 'list_url': list_url})

    def delete_view(self, request, entity_id):
        '''
        模型实例的删除视图，使用ajax弹窗
        :param request:
        :param entity_id:
        :return:
        '''
        entity = self.admin_model.objects.filter(pk=entity_id).first()
        if not entity:
            return XStarkErrorResponse('不存在').json()
        link = self.reverse_display_list()
        if request.method == 'POST':
            entity.delete()
            return XStarkSuccessResponse('{%s} 已删除' % entity, redirect=link).json()
        return XStarkSuccessResponse(title='删除%s' % self.get_site_title(),
                                     dialog=render_to_string('xstark/delete.html', {'redirect': link, 'entity': entity},
                                                          request=request)).json()


class StarkAdminSite(object):
    app_code = 'xstark'
    namespace = 'xstark'

    def __init__(self):
        self._registry = []

    def get_urls(self):
        from django.urls import path, include
        urlpatterns = [
        ]
        for item in self._registry:
            if item.prefix:
                tmp = path('%s/%s/%s/' % (item.model._meta.app_label, item.model._meta.model_name, item.prefix),
                           include(item.site.urls))
            else:

                tmp = path('%s/%s/' % (item.model._meta.app_label, item.model._meta.model_name),
                           include(item.site.urls))
            urlpatterns.append(tmp)
        return urlpatterns

    @property
    def urls(self):
        return self.get_urls(), self.app_code, self.namespace

    def register(self, model_cls, admin_model_cls=None, prefix=None):
        if not admin_model_cls:
            admin_model_cls = StarkAdminModel

        self._registry.append(SiteMapping(model_cls, admin_model_cls(model_cls, self, prefix), prefix))


site = StarkAdminSite()
