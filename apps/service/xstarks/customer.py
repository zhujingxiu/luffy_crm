#!/usr/bin/env python
# -*- coding:utf-8 -*-
# _AUTHOR_  : zhujingxiu
# _DATE_    : 2018/10/22
from system.rbac import RbacPermission
from service.models import Customer, CustomerInfo
from service.forms import CustomerForm, CustomerInfoForm, PublicCustomerForm, PrivateCustomerForm
from xstark.sites import StarkAdminModel, Option, get_choice_text
from xstark.utils.response import XStarkSuccessResponse, XStarkErrorResponse
from django.shortcuts import reverse, redirect, render
from django.conf import settings
from django.db import transaction
from django.utils.safestring import mark_safe
from django.template.loader import render_to_string


class CustomerAdmin(RbacPermission, StarkAdminModel):

    def display_follow(self, entity=None, header=False):
        if header:
            return '操作'
        url = reverse("xstark:service_consultrecord_changelist")
        return mark_safe('''
        <a href='%s?customer=%s' class="btn btn-default"><i class="fa fa-book"></i> 跟进记录</a>
        ''' % (url, entity.pk,))

    list_display = ['name', get_choice_text('gender'), get_choice_text('status'), 'course', get_choice_text('source'), get_choice_text('customerinfo__education'), display_follow]
    search_list = ['name', 'phone', 'sns']
    filter_list = [
        Option('gender', is_choice=True),
        Option('source', is_choice=True),
        Option('course', is_multi=True),
        Option('customerinfo__education', is_choice=True, is_multi=True),
    ]

    def change_view(self, request, entity_id):
        list_url = self.reverse_display_list()
        entity = Customer.objects.filter(pk=entity_id).first()
        if not entity:
            return redirect(list_url)
        msg = '{0} '.format(Customer._meta.verbose_name)
        form = CustomerForm(instance=entity)
        info_form = CustomerInfoForm()
        info_entity = CustomerInfo.objects.filter(customer=entity).first()
        if info_entity:
            info_form = CustomerInfoForm(instance=info_entity)
        if request.method == 'POST':
            form = CustomerForm(request.POST, instance=entity)
            info_form = CustomerInfoForm(request.POST, instance=info_entity)
            if form.is_valid():
                _customer = self.save(form)
                info_form.instance.customer = _customer
                info_form.save()
                return redirect(self.reverse_display_list())
            else:
                print(form.errors)
        return render(request, 'service/customer_set.html', {'form': form, 'info_form': info_form, 'list_url': list_url, 'msg': msg})


class PublicCustomerAdmin(RbacPermission, StarkAdminModel):
    display_option = False
    has_bulk_delete = False
    list_display = ['name', 'phone', get_choice_text('gender'), get_choice_text('status'), 'course', get_choice_text('source')]
    search_list = ['name', 'phone', 'sns']
    filter_list = [
        Option('gender', is_choice=True),
        Option('source', is_choice=True),
        Option('course', is_multi=True),
    ]
    model_form_class = PublicCustomerForm

    def extra_urls(self):
        from django.urls import path
        return [
            path('apply/', self.wrapper(self.bulk_apply), name='service_customer_pub_apply'),
        ]

    def bulk_apply(self, request):
        """
        申请客户
        :param request:
        :return:
        """
        user = self.request.session.get('user_info')
        current_user_id = user.get('id')
        pks = request.POST.get('pks')
        pks = pks.split(',')
        if not pks:
            return XStarkErrorResponse('pk 参数错误').json()
        # 事务
        with transaction.atomic():
            origin = Customer.objects.filter(pk__in=pks, consultant__isnull=True).select_for_update()
            if len(origin) == len(pks):
                Customer.objects.filter(pk__in=pks).update(consultant_id=current_user_id)
                return XStarkSuccessResponse('申请成功').json()

        return XStarkErrorResponse('已被其他顾问申请（手速太慢）').json()

    def bulk_apply_view(self, request):
        """
        申请客户
        :param request:
        :return:
        """
        entities = request.POST.getlist('pk')
        user = self.request.session.get('user_info')
        current_user_id = user.get('id')

        privates = Customer.objects.filter(consultant_id=current_user_id, status=2).count()

        if (privates + len(entities)) > settings.MAX_PRIVATE_CUSTOMER:
            return XStarkErrorResponse('做人别太贪心').json()
        return XStarkSuccessResponse(tpl=render_to_string('service/action_confirm.html', {
            'action': reverse('xstark:service_customer_pub_apply'),
            'pks':  ','.join(entities),
            'entities': [item['name'] for item in Customer.objects.filter(pk__in=entities).values('name')],
            'submit_text': '确认申请'
        }, request=request), title='将申请以下%s位用户' % len(entities)).json()

    bulk_apply_view.text = "申请客户"
    bulk_apply_view.url = 'xstark:service_customer_pub_apply'

    action_list = [bulk_apply_view, ]

    def get_queryset(self):
        return self.admin_model.objects.filter(consultant__isnull=True)


class PrivateCustomerAdmin(RbacPermission, StarkAdminModel):
    display_option = False
    has_bulk_delete = False

    def display_follow(self, entity=None, header=False):
        if header:
            return '操作'
        url = reverse("xstark:service_consultrecord_pri_changelist")
        return mark_safe('''
        <a href="%s?customer=%s" class="btn btn-sm btn-info">跟进记录</a>
        ''' % (url, entity.pk))

    list_display = ['name', get_choice_text('gender'), get_choice_text('status'), 'course', get_choice_text('source'), display_follow]
    search_list = ['name', 'phone', 'sns']
    filter_list = [
        Option('gender', is_choice=True),
        Option('source', is_choice=True),
        Option('course', is_multi=True),
    ]
    model_form_class = PrivateCustomerForm

    def get_queryset(self):
        current_user_id = 1
        return self.admin_model.objects.filter(consultant__pk=current_user_id)

    def extra_urls(self):
        from django.urls import path
        return [
            path('remove/', self.wrapper(self.bulk_remove), name='service_customer_pri_remove'),
        ]

    def bulk_remove(self, request):
        pks = request.POST.get('pks')
        pks = pks.split(',')
        if not pks:
            return XStarkErrorResponse('pk 参数错误').json()
        user = self.request.session.get('user_info')
        current_user_id = user.get('id')
        Customer.objects.filter(id__in=pks, status=2, consultant_id=current_user_id).update(consultant=None)
        return XStarkSuccessResponse('已经移除成功').json()

    def bulk_remove_view(self, request):
        """
        移除客户
        :param request:
        :return:
        """
        entities = request.POST.getlist('pk')
        return XStarkSuccessResponse(tpl=render_to_string('service/action_confirm.html', {
            'action': reverse('xstark:service_customer_pri_remove'),
            'pks': ','.join(entities),
            'entities': [item['name'] for item in Customer.objects.filter(pk__in=entities).values('name')],
            'submit_text': '确认移除'
        }, request=request), title='将移除以下%s位用户' % len(entities)).json()

    bulk_remove_view.text = "移除客户"

    action_list = [bulk_remove_view, ]