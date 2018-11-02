#!/usr/bin/env python
# -*- coding:utf-8 -*-
# _AUTHOR_  : zhujingxiu
# _DATE_    : 2018/11/2


def G(request):
    """
    Return context variables required by apps that use Django's authentication
    system.

    """
    info = request.session.get('student_info')
    if info:
        from service.models import Student
        student = Student.objects.get(pk=info.get('id'))
    else:
        from django.contrib.auth.models import AnonymousUser
        student = AnonymousUser()
    return {
        'student': student,
    }
