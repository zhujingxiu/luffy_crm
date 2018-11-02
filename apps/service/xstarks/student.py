#!/usr/bin/env python
# -*- coding:utf-8 -*-
# _AUTHOR_  : zhujingxiu
# _DATE_    : 2018/10/22
from system.rbac import RbacSiteAdmin
from service.forms import ResetPwdForm
from service.models import Student, Customer, ClassInfo
from xstark.sites import Option, get_choice_text
from xstark.utils.response import XStarkSuccessResponse, XStarkErrorResponse
from django import forms
from django.shortcuts import reverse
from django.conf import settings
from django.utils.safestring import mark_safe
from django.template.loader import render_to_string


class StudentForm(forms.ModelForm):
    customer = forms.ChoiceField(label='客户', widget=forms.Select, choices=Customer.objects.exclude(
        pk__in=Student.objects.all().values('customer_id')).values_list('pk', 'name'))

    class Meta:
        model = Student
        fields = '__all__'
        exclude = ['password']


class StudentAdmin(RbacSiteAdmin):

    def display_payment_change(self, entity=None, header=False):
        if header:
            return '记录'
        payment_url = reverse("xstark:service_paymentrecord_changelist")
        change_url = reverse("xstark:service_changerecord_changelist")
        return mark_safe('''
        <a href="%s?student=%s" class="btn btn-sm btn-default"><i class="fa fa-book"></i> 缴费</a>
        <a href="%s?student=%s" class="btn btn-sm btn-default"><i class="fa fa-book"></i> 转班</a>
        ''' % (payment_url, entity.pk, change_url, entity.pk))

    list_display = [
        'customer',
        get_choice_text('customer__gender'),
        'classinfo',
        display_payment_change,
        RbacSiteAdmin.display_edit
    ]

    filter_list = [
        Option('customer__gender', is_choice=True),
        Option('classinfo', is_multi=True, verbose_name='班级')
    ]
    model_form_class = StudentForm

    def get_form_instance(self, data=None, instance=None, request=None):
        form = super().get_form_instance(data, instance, request)
        if request:
            params = request.resolver_match.kwargs
            entity_id = params.get('entity_id')
            if entity_id:
                form.fields['customer'].choices = Customer.objects.filter(pk=entity_id).values_list('pk', 'name')
        return form

    def extra_urls(self):
        from django.urls import path
        return [
            path('reset/', self.wrapper(self.bulk_reset), name='service_student_reset'),
        ]

    def bulk_reset(self, request):
        from django.contrib.auth.hashers import make_password
        pks = request.POST.get('pks')
        if not pks:
            return XStarkErrorResponse('pk 参数错误').json()
        password = request.POST.get('password') or settings.DEFAULT_PWD
        new_pwd = make_password(password, hasher='pbkdf2_sha256')
        Student.objects.filter(pk__in=pks.split(',')).update(password=new_pwd)
        return XStarkSuccessResponse(new_pwd).json()

    def bulk_reset_view(self, request):
        entities = request.POST.getlist('pk')
        if not request.POST.getlist('pk'):
            return XStarkErrorResponse('请选择一项').json()
        return XStarkSuccessResponse(dialog=render_to_string('system/reset_pwd.html', {
            'action': reverse('xstark:service_student_reset'),
            'form': ResetPwdForm({'pks': ','.join(entities)}),
            'users': Student.objects.filter(pk__in=entities).values('name')
        }, request=request), title='将为%s位用户重置密码' % len(entities)).json()

    bulk_reset_view.text = '重置默认密码'
    bulk_reset_view.path_name = 'xstark:service_student_reset'

    action_list = [bulk_reset_view, ]