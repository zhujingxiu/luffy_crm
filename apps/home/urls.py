#!/usr/bin/env python
# -*- coding:utf-8 -*-
# _AUTHOR_  : zhujingxiu
# _DATE_    : 2018/11/2

from django.urls import path, re_path
from home.views import my
app_name = 'home'
urlpatterns = [
    path('profile/', my.ProfileView.as_view(), name='my_profile'),
    path('password/', my.PasswordView.as_view(), name='my_password'),
    path('avatar/', my.AvatarView.as_view(), name='my_avatar'),
    re_path('homework/', my.HomeworkView.as_view(), name='my_homework'),
    re_path('homework/(?P<pk>\d+)/', my.ProfileView.as_view(), name='my_homework_detail'),
]