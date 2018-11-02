#!/usr/bin/env python
# -*- coding:utf-8 -*-
# _AUTHOR_  : zhujingxiu
# _DATE_    : 2018/11/2
from django.shortcuts import render, reverse
from django.views import View
from service.models import StudyRecord


class ProfileView(View):

    def get(self, request):

        return render(request, 'my/profile.html', {})


class PasswordView(View):

    def get(self, request):
        return render(request, 'my/profile.html', {})


class AvatarView(View):

    def get(self, request):
        return render(request, 'my/profile.html', {})


class HomeworkView(View):

    def get(self, request):
        student = request.session.get('student_info')

        records = StudyRecord.objects.filter(student__pk=student.get('id'))
        print(records)
        return render(request, 'my/homework.html', {'records': records})
