#!/usr/bin/env python
# -*- coding:utf-8 -*-
import re

from django.shortcuts import render, redirect
from xstark.utils.response import XStarkErrorResponse


class MiddlewareMixin(object):
    def __init__(self, get_response=None):
        self.get_response = get_response
        super(MiddlewareMixin, self).__init__()

    def __call__(self, request):
        response = None
        if hasattr(self, 'process_request'):
            response = self.process_request(request)
        if not response:
            response = self.get_response(request)
        if hasattr(self, 'process_response'):
            response = self.process_response(request, response)
        return response


class RbacMiddleware(MiddlewareMixin):

    def process_request(self, request):
        """
        验证用户
        :param request:
        :return:
        """
        from django.conf import settings
        from django.utils.module_loading import import_string
        from rbac.service.init_permission import init_permission

        user_class = import_string(settings.USER_MODEL_PATH)
        user = request.session.get('user_info')
        if user:
            current_user = user_class.objects.filter(pk=user.get('id')).first()
            request.user = current_user
            # 也可及时更新权限
            init_permission(current_user, request)

        # 1. 获取白名单，让白名单中的所有url和当前访问url匹配
        for reg in settings.PERMISSION_VALID_URL:
            if re.match(reg, request.path_info):
                return None

        # 2. 获取权限
        permission_dict = request.session.get(settings.PERMISSION_SESSION_KEY)
        if not permission_dict:
            msg = '无权限信息，请重新登录'
            return XStarkErrorResponse(msg).json() if request.is_ajax() else redirect(settings.XSTARK_EXIT)

        flag = False

        # 3. 对用户请求的url进行匹配
        request.current_breadcrumb_list = [
            {'title': '首页', 'url': '#'}
        ]
        for name, item in permission_dict.items():
            url = item['url']
            regex = "^%s$" % (url,)
            if re.match(regex, request.path_info):
                flag = True
                parent = item['parent']
                parent_name = item['parent_name']
                parent_url = item['parent_url']
                if parent:
                    request.current_permission_parent = item['parent']
                    request.current_breadcrumb_list.extend([
                        {'title': permission_dict[parent_name]['title'], 'url': parent_url},
                        {'title': item['title'], 'url': url, 'class': 'active'}
                    ])
                else:
                    request.current_permission_parent = item['id']
                    request.current_breadcrumb_list.append(
                        {'title': item['title'], 'url': url, 'class': 'active'}
                    )
                break

        if not flag:
            from django.conf import settings
            deny_tpl = settings.PERMISSION_DENY_TPL if hasattr(settings, 'PERMISSION_DENY_TPL') else 'rbac/denied.html'
            msg = '无权访问，%s' % request.path_info
            context = {
                'msg': msg,
                'redirect': request.META['HTTP_REFERER'] if hasattr(request.META, 'HTTP_REFERER') else settings.XSTARK_HOME
            }
            return XStarkErrorResponse(msg).json() if request.is_ajax() else render(request, deny_tpl, context)
