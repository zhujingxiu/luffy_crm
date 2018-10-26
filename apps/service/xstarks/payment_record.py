#!/usr/bin/env python
# -*- coding:utf-8 -*-
# _AUTHOR_  : zhujingxiu
# _DATE_    : 2018/10/24

from service.models import Student, PaymentRecord

from xstark.sites import StarkAdminModel, Option, get_choice_text
from xstark.utils.response import XStarkSuccessResponse, XStarkErrorResponse
from django import forms
from django.shortcuts import reverse, redirect, render
from django.conf import settings
from django.utils.safestring import mark_safe
from django.template.loader import render_to_string


class PaymentRecordForm(forms.ModelForm):
    confirm_date = forms.DateField(label='确认日期', widget=forms.SelectDateWidget(years=(('2018','2019','2020')),attrs={'class':'datepicker'}))
    class Meta:
        model = PaymentRecord
        exclude = ['customer']


class PaymentRecordAdmin(StarkAdminModel):

    list_display = ['customer', 'consultant', 'classinfo', get_choice_text('pay_type'), 'paid_fee', get_choice_text('status')]

    filter_list = ['classinfo']

    model_form_class = PaymentRecordForm

    def get_site_title(self):
        student = None
        params = self.request.session.get(self.request_get_key)
        if params:
            from django.http import QueryDict
            params = QueryDict(params)
            student = Student.objects.filter(pk=params.get('student')).first()
        return '%s:%s' % (student.customer.name, super().get_site_title()) if student else super().get_site_title()

    def save(self, form, modify=False):
        params = self.request.session.get(self.request_get_key)
        if params:
            from django.http import QueryDict
            params = QueryDict(params)
            form.instance.customer_id = params.get('student')

        form.save()