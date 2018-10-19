#!/usr/bin/env python
# -*- coding:utf-8 -*-
# _AUTHOR_  : zhujingxiu
# _DATE_    : 2018/10/10
from django.template import Library

register = Library()


@register.inclusion_tag('xstark/table.html')
def table(cl):

    return {'header_list': cl.gen_list_header, 'record_list': cl.gen_list_body}