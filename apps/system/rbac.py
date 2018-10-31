#!/usr/bin/env python
# -*- coding:utf-8 -*-
# _AUTHOR_  : zhujingxiu
# _DATE_    : 2018/10/30

from django.conf import settings
from xstark.sites import StarkAdminModel


class RbacPermission(object):

    def display_add(self):
        name = "%s:%s" % (self.admin_site.namespace, self.get_add_url_name,)
        permission_dict = self.request.session.get(settings.PERMISSION_SESSION_KEY)
        if name in permission_dict:
            return super().display_add()

    def get_list_display(self):
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
        _action_list = [{'name': action.__name__, 'action': action, 'url': action.url if hasattr(action, 'url') else ''} for action in super().get_action_list()]
        permission_dict = self.request.session.get(settings.PERMISSION_SESSION_KEY)
        del_name = "%s:%s" % (self.admin_site.namespace, self.get_del_url_name,)
        if del_name not in permission_dict:
            pass
            #_action_list.remove(StarkAdminModel.bulk_delete)
        for _action in _action_list:
            if _action['url'] not in permission_dict:
                print('not in ', _action, _action_list)
                #_action_list.remove()
        return super().get_action_list()