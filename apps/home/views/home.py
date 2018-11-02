#!/usr/bin/env python
# -*- coding:utf-8 -*-
# _AUTHOR_  : zhujingxiu
# _DATE_    : 2018/11/2
from django.shortcuts import render, HttpResponse, redirect
from django.views import View
from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse, Http404
from django.urls import reverse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from system.models import College, ClassInfo, Course


class IndexView(View):

    def get(self, request):

        classes = ClassInfo.objects.all().order_by('-openday')[:10]
        colleges = College.objects.all()
        return render(request, 'index.html', {'classes': classes, 'colleges': colleges})