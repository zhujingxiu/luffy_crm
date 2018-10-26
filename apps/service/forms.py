#!/usr/bin/env python
# -*- coding:utf-8 -*-
# _AUTHOR_  : zhujingxiu
# _DATE_    : 2018/10/18
from django import forms
from django.conf import settings
from django.core.exceptions import ValidationError
from service.models import Customer, CustomerInfo


class ResetPwdForm(forms.Form):
    pks = forms.CharField(widget=forms.HiddenInput())
    password = forms.CharField(min_length=6, label='密码',
                               widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': '留空将使用默认密码'}))
    confirm = forms.CharField(min_length=6, label='确认',
                              widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': '留空将使用默认密码'}))

    def clean(self):
        password = self.cleaned_data.get('password')
        confirm = self.cleaned_data.get('confirm')
        if password != confirm:
            raise ValidationError('两次密码不匹配！')


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'


class CustomerInfoForm(forms.ModelForm):
    class Meta:
        model = CustomerInfo
        exclude = ['customer']


class PublicCustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        exclude = ['consultant', 'status']
        error_messages = {
            'phone': {
                'unique': '手机号已存在'
            }
        }


class PrivateCustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        exclude = ['consultant', ]