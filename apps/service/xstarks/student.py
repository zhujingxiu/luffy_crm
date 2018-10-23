#!/usr/bin/env python
# -*- coding:utf-8 -*-
# _AUTHOR_  : zhujingxiu
# _DATE_    : 2018/10/22

from service.models import Student
from xstark.sites import StarkAdminModel, Option, get_choice_text
from xstark.utils.response import XStarkSuccessResponse, XStarkErrorResponse
from django import forms
from django.shortcuts import reverse
from django.conf import settings
from django.db import transaction
from django.utils.safestring import mark_safe
from django.template.loader import render_to_string


class StudentAdmin(StarkAdminModel):
    list_display = ['username', 'customer__gender']

    filter_list = [
        Option('customer__gender', is_choice=True)
    ]