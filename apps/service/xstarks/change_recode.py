#!/usr/bin/env python
# -*- coding:utf-8 -*-
# _AUTHOR_  : zhujingxiu
# _DATE_    : 2018/10/24

from service.models import Student, ChangeRecord

from xstark.sites import StarkAdminModel, Option, get_choice_text
from xstark.utils.response import XStarkSuccessResponse, XStarkErrorResponse
from django.shortcuts import reverse, redirect, render
from django.conf import settings
from django.db import transaction
from django.utils.safestring import mark_safe
from django.template.loader import render_to_string


class ChangeRecordAdmin(StarkAdminModel):
    list_display = ['student', 'origin_class', 'target_class', 'add_date', ]

    filter_list = ['origin_class']

    def get_site_title(self):
        student = None
        params = self.request.session.get(self.request_get_key)
        if params:
            from django.http import QueryDict
            params = QueryDict(params)
            student = Student.objects.filter(pk=params.get('student')).first()
        return '%s:%s' % (student.customer.name, super().get_site_title()) if student else super().get_site_title()