#!/usr/bin/env python
# -*- coding:utf-8 -*-
# _AUTHOR_  : zhujingxiu
# _DATE_    : 2018/10/24
from system.rbac import RbacSiteAdmin
from service.models import CourseRecord, Student, StudyRecord
from system.models import UserInfo
from xstark.sites import StarkAdminModel, Option, get_choice_text
from xstark.utils.response import XStarkSuccessResponse, XStarkErrorResponse
from django.shortcuts import reverse, redirect, render
from django import forms
from django.utils.safestring import mark_safe
from django.template.loader import render_to_string


class CourseRecordForm(forms.ModelForm):

    teacher = forms.ChoiceField(label='讲师', widget=forms.Select, choices=UserInfo.objects.filter(roles__code='teacher').values_list('pk', 'name'))

    class Meta:
        model = CourseRecord
        fields = '__all__'

    def clean_teacher(self):
        teacher = self.cleaned_data['teacher']
        if not isinstance(teacher, UserInfo):
            return UserInfo.objects.get(pk=teacher)


class CourseRecordAdmin(RbacSiteAdmin):

    def display_study_record(self, entity=None, header=False):
        if header:
            return "记录"
        url = reverse('xstark:service_studyrecord_changelist')
        return mark_safe('''<a href="%s?ccid=%s" class="btn btn-default">%s S%s Day%s</a>''' % (
        url, entity.pk, entity.classinfo.course.title, entity.classinfo.semester, entity.day_num,))

    list_display = ['classinfo', 'teacher', 'course_title', 'date', display_study_record]

    filter_list = [Option('teacher', condition={'roles__code': 'teacher'})]

    model_form_class = CourseRecordForm

    def extra_urls(self):
        from django.urls import path
        urlpatterns = [path('init/', self.wrapper(self.bulk_init), name='service_courserecord_init'), ]
        return urlpatterns

    def bulk_init(self, request):
        user = self.request.session.get('user_info')
        current_user_id = user.get('id')
        pks = request.POST.get('pks')
        pks = pks.split(',')
        if not pks:
            return XStarkErrorResponse('pk 参数错误').json()
        num = 0
        for nid in pks:
            courserecord = CourseRecord.objects.get(id=nid)

            exists = StudyRecord.objects.filter(course_record=courserecord).exists()
            if exists:
                continue

            stu_list = Student.objects.filter(classinfo=courserecord.classinfo)
            study_record_list = []
            for stu in stu_list:
                study_record_list.append(StudyRecord(course_record=courserecord, student=stu))
                num += 1

            StudyRecord.objects.bulk_create(study_record_list)
        return XStarkSuccessResponse('初始化成功,执行%s次' % (str(num))).json()

    def bulk_init_view(self, request):
        """
        批量初始化
        :param request:
        :return:
        """
        entities = request.POST.getlist('pk')
        if not request.POST.getlist('pk'):
            return XStarkErrorResponse('请选择一项').json()
        # 找到选中上课记录的班级
        # 找到班级下所有人
        # 为每个人生成一条学习记录
        options = []
        for nid in entities:
            _entity = CourseRecord.objects.get(id=nid)

            exists = StudyRecord.objects.filter(course_record=_entity).exists()
            if exists:
                continue
            options.append({
                'title': '%s S%s Day%s' % (_entity.classinfo.course.title, _entity.classinfo.semester, _entity.day_num),
                'entities': [item['customer__name'] for item in Student.objects.filter(classinfo=_entity.classinfo).values('customer__name')]
            })

        return XStarkSuccessResponse(dialog=render_to_string('service/action_confirm.html', {
            'action': reverse('xstark:service_courserecord_init'),
            'pks': ','.join(entities),
            'entities_set': options,
            'submit_text': '确认初始化'
        }, request=request), title='将为%s位用户初始化上课记录' % len(entities)).json()
    bulk_init_view.text = "批量初始化"
    bulk_init_view.url = "xstark:service_courserecord_init"

    action_list = [bulk_init_view, ]
