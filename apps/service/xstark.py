#!/usr/bin/env python
# -*- coding:utf-8 -*-
# _AUTHOR_  : zhujingxiu
# _DATE_    : 2018/10/19

from .models import *
from xstark.sites import site, StarkAdminModel, Option, get_choice_text
from xstark.utils.response import XStarkSuccessResponse, XStarkErrorResponse


class CustomerAdmin(StarkAdminModel):
    list_display = ['name', get_choice_text('gender'), get_choice_text('status'), 'course', get_choice_text('source')]
    search_list = ['name', 'phone', 'sns']
    filter_list = [
        Option('gender', is_choice=True),
        Option('source', is_choice=True),
        Option('education', is_choice=True),
        Option('course', is_multi=True),
    ]


site.register(Customer, CustomerAdmin)


class PublicCustomerAdmin(StarkAdminModel):
    list_display = ['name', get_choice_text('gender'), get_choice_text('status'), 'course', get_choice_text('source')]
    search_list = ['name', 'phone', 'sns']
    filter_list = [
        Option('gender', is_choice=True),
        Option('source', is_choice=True),
        Option('education', is_choice=True),
        Option('course', is_multi=True),
    ]


site.register(Customer, PublicCustomerAdmin, 'pub')


class PrivateCustomerAdmin(StarkAdminModel):
    list_display = ['name', get_choice_text('gender'), get_choice_text('status'), 'course', get_choice_text('source')]
    search_list = ['name', 'phone', 'sns']
    filter_list = [
        Option('gender', is_choice=True),
        Option('source', is_choice=True),
        Option('education', is_choice=True),
        Option('course', is_multi=True),
    ]


site.register(Customer, PrivateCustomerAdmin, 'pri')


class StudentAdmin(StarkAdminModel):
    list_display = ['username', 'customer__gender']

    filter_list = [
        Option('customer__gender', is_choice=True)
    ]


site.register(Student, StudentAdmin)