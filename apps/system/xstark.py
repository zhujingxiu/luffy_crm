#!/usr/bin/env python
# -*- coding:utf-8 -*-
# _AUTHOR_  : zhujingxiu
# _DATE_    : 2018/10/15
from .forms import ResetPwdForm
from .models import *
from xstark.sites import site, StarkAdminModel, Option, get_choice_text
from xstark.utils.response import XStarkSuccessResponse, XStarkErrorResponse
from django import forms
from django.conf import settings
from django.template.loader import render_to_string


class DepartAdmin(StarkAdminModel):
    list_display = ['title']


site.register(Department, DepartAdmin)


class UserForm(forms.ModelForm):
    class Meta:
        model = UserInfo
        fields = '__all__'
        exclude = ['password']


class UserAdmin(StarkAdminModel):

    list_display = ['name', get_choice_text('gender'), 'phone', 'depart', 'roles', 'email']
    model_form_class = UserForm

    def extra_urls(self):
        from django.urls import path
        return [
            path('reset/', self.wrapper(self.bulk_reset), name='system_userinfo_reset'),
        ]

    def bulk_reset(self, request):
        from django.contrib.auth.hashers import make_password
        pks = request.POST.get('pks')
        if not pks:
            return XStarkErrorResponse('pk 参数错误').json()
        password = request.POST.get('password') or settings.DEFAULT_PWD
        new_pwd = make_password(password, hasher='pbkdf2_sha256')
        UserInfo.objects.filter(pk__in=pks.split(',')).update(password=new_pwd)
        return XStarkSuccessResponse(new_pwd).json()

    def bulk_reset_view(self, request):
        entities = request.POST.getlist('pk')
        if not request.POST.getlist('pk'):
            return XStarkErrorResponse('请选择一项').json()
        return XStarkSuccessResponse(tpl=render_to_string('system/reset_pwd.html', {
            'form': ResetPwdForm({'pks': ','.join(entities)}),
            'users': UserInfo.objects.filter(pk__in=entities).values('name')
        }, request=request), title='将为%s位用户重置密码' % len(entities)).json()

    bulk_reset_view.text = '重置默认密码'
    action_list = [bulk_reset_view]
    filter_list = [
        Option('gender', is_choice=True),
        Option('depart', is_multi=True),
        Option('roles', is_multi=True),
    ]
    search_list = ['name', 'phone']


site.register(UserInfo, UserAdmin)


class CollegeAdmin(StarkAdminModel):
    list_display = ['title', 'cover', ]


site.register(College, CollegeAdmin)


class ClassAdmin(StarkAdminModel):
    list_display = ['title', 'openday', 'tutor', 'college']

    filter_list = [
        'college'
    ]


site.register(ClassInfo, ClassAdmin)


class CourseAdmin(StarkAdminModel):
    list_display = ['title', ]


site.register(Course, CourseAdmin)