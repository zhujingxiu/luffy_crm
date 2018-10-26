#!/usr/bin/env python
# -*- coding:utf-8 -*-
# _AUTHOR_  : zhujingxiu
# _DATE_    : 2018/10/24

from service.models import Student, StudyRecord

from xstark.sites import StarkAdminModel, Option, get_choice_text
from xstark.utils.response import XStarkSuccessResponse, XStarkErrorResponse
from django.shortcuts import reverse, redirect, render
from django.conf import settings
from django.db import transaction
from django.utils.safestring import mark_safe
from django.template.loader import render_to_string


class StudyRecordAdmin(StarkAdminModel):

    filter_list = [Option('score', is_choice=True, is_multi=True)]