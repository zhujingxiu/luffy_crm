from django.urls import path, re_path
from rbac.views import permission
app_name = 'rbac'
urlpatterns = [

    path('menu/list/', permission.menu_list, name='menu_list'), # rbac:menu_list
    path('menu/add/', permission.menu_add, name='menu_add'),
    re_path('menu/edit/(?P<pk>\d+)/', permission.menu_edit, name='menu_edit'),
    re_path('menu/del/(?P<pk>\d+)/', permission.menu_del, name='menu_del'),
    path('permission/add/', permission.permission_add, name='permission_add'),
    re_path('permission/edit/(?P<pk>\d+)/', permission.permission_edit, name='permission_edit'),
    re_path('permission/del/(?P<pk>\d+)/', permission.permission_del, name='permission_del'),

    path('multi/permissions/', permission.multi_permissions, name='multi_permissions'),

    path('distribute/permissions/', permission.distribute_permissions, name='distribute_permissions'),
    path('role/list/', permission.role_list, name='role_list'),
    re_path('role/edit/(?P<pk>\d+)/', permission.role_edit, name='role_edit'),
    re_path('role/del/(?P<pk>\d+)/', permission.role_del, name='role_del'),

]
