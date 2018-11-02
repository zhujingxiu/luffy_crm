#!/usr/bin/env python
# -*- coding:utf-8 -*-
# _AUTHOR_  : zhujingxiu
# _DATE_    : 2018/10/24
from system.rbac import RbacSiteAdmin
from service.models import Student, StudyRecord
from xstark.sites import StarkAdminModel, Option, get_choice_text
from xstark.utils.response import XStarkSuccessResponse, XStarkErrorResponse
from django.shortcuts import reverse, redirect, render
from django.urls import path
from django.forms import ModelForm, modelformset_factory, widgets as Fwidgets
from django.utils.safestring import mark_safe
from django.template.loader import render_to_string


class StudyRecordForm(ModelForm):
    class Meta:
        model = StudyRecord
        fields = ['checking', 'score', 'homework_note']
        widgets = {
            'checking': Fwidgets.Select(attrs={'class': 'form-control'}),
            'score': Fwidgets.Select(attrs={'class': 'form-control'}),
            'homework_note': Fwidgets.TextInput(attrs={'class': 'form-control'}),
        }


class StudyRecordAdmin(RbacSiteAdmin):

    def get_urls(self):
        return [path('', self.wrapper(self.changelist_view), name=self.get_list_url_name), ]

    def changelist_view(self, request):
        ccid = request.GET.get('ccid')
        model_formset_cls = modelformset_factory(StudyRecord, StudyRecordForm, extra=0)
        queryset = StudyRecord.objects.filter(course_record_id=ccid)
        if request.method == "POST":
            formset = model_formset_cls(data=request.POST)
            if formset.is_valid():
                formset.save()
                return redirect(request.get_full_path())
        else:
            formset = model_formset_cls(queryset=queryset)
        return render(request, 'service/study_record.html', {'formset': formset})