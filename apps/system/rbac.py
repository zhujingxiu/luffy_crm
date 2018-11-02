#!/usr/bin/env python
# -*- coding:utf-8 -*-
# _AUTHOR_  : zhujingxiu
# _DATE_    : 2018/10/30

from django.conf import settings
from xstark.sites import StarkAdminModel


class RbacSiteAdmin(StarkAdminModel):
    '''
    若作为独立组件，最好不直接继承xstark组件的StarkAdminModel，从而使得耦合度增加
    但此处要覆盖的授权操作函数皆是xstark组件的方法：display_add，get_list_display，get_action_list，...，而非独立的自定义方法
    所以此处直接继承了StarkAdminModel
    '''

    def display_add(self):
        '''
        模型实例添加按钮权限
        :return:
        '''
        name = "%s:%s" % (self.admin_site.namespace, self.get_add_url_name,)
        permission_dict = self.request.session.get(settings.PERMISSION_SESSION_KEY)
        if name in permission_dict:
            return super().display_add()

    def get_list_display(self):
        '''
        模型实例列表中编辑删除权限
        :return:
        '''
        _list_display = super().get_list_display()
        permission_dict = self.request.session.get(settings.PERMISSION_SESSION_KEY)
        edit_name = "%s:%s" % (self.admin_site.namespace, self.get_change_url_name,)
        del_name = "%s:%s" % (self.admin_site.namespace, self.get_del_url_name,)
        if edit_name not in permission_dict:
            if StarkAdminModel.display_edit in _list_display:
                _list_display.remove(StarkAdminModel.display_edit)
            if StarkAdminModel.display_options in _list_display:
                _list_display.remove(StarkAdminModel.display_options)

        if del_name not in permission_dict:
            if StarkAdminModel.display_delete in _list_display:
                _list_display.remove(StarkAdminModel.display_delete)
            if StarkAdminModel.display_options in _list_display:
                _list_display.remove(StarkAdminModel.display_options)

        return _list_display

    def get_action_list(self):
        '''
        模型实例批量操作权限
        :return:
        '''
        _action_list = [{'action': action, 'path_name': action.path_name if hasattr(action, 'path_name') else ''}
                        for action in super().get_action_list()]
        permission_dict = self.request.session.get(settings.PERMISSION_SESSION_KEY)
        actions = []
        for _action in _action_list:
            if _action['path_name'] and _action['path_name'] in permission_dict:
                actions.append(_action['action'])
        return actions
