#!/usr/bin/env python
# -*- coding:utf-8 -*-
# _AUTHOR_  : zhujingxiu
# _DATE_    : 2018/10/18

from django.http import JsonResponse


class XStarkResponse(object):
    def __init__(self, errcode, msg='', title='', data=None, dialog=None, redirect=None):
        self.errcode = errcode
        self.msg = msg
        self.title = title
        self.data = data
        self.dialog = dialog
        self.redirect = redirect

    def json(self):
        return JsonResponse({
            'errcode': self.errcode,
            'msg': self.msg,
            'title': self.title,
            'data': self.data,
            'dialog': self.dialog,
            'redirect': self.redirect,
        }, safe=True)


class XStarkSuccessResponse(XStarkResponse):
    def __init__(self, msg='', title='', data=None, dialog=None, redirect=None):
        super().__init__(0, msg, title or '操作成功', data, dialog, redirect)


class XStarkErrorResponse(XStarkResponse):
    def __init__(self, msg='', title='', data=None, dialog=None, redirect=None):
        super().__init__(1, msg, title or '操作失败', data, dialog, redirect)
