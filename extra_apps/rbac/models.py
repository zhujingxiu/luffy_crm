from django.db import models


class Menu(models.Model):
    """
    菜单
    """
    title = models.CharField('菜单', max_length=32)
    icon = models.CharField('图标', max_length=32)

    class Meta:
        verbose_name_plural = verbose_name = '菜单管理'

    def __str__(self):
        return self.title


class Permission(models.Model):
    """
    权限表
    """
    title = models.CharField('标题', max_length=32)
    url = models.CharField('含正则的URL', max_length=128, unique=True)
    name = models.CharField('代码', max_length=64, unique=True, null=False, blank=False)
    parent = models.ForeignKey('self', verbose_name='默认选中权限', related_name='ps', null=True, blank=True,
                            help_text="对于无法作为菜单的URL，可以为其选择一个可以作为菜单的权限，那么访问时，则默认选中此权限",
                            limit_choices_to={'menu__isnull': False}, on_delete=models.SET_NULL)
    menu = models.ForeignKey(Menu, verbose_name='菜单', null=True, blank=True, help_text='null表示非菜单', on_delete=models.SET_NULL)

    class Meta:
        verbose_name_plural = verbose_name = '权限节点'

    def __str__(self):
        return self.title


class Role(models.Model):
    """
    角色
    """
    title = models.CharField('角色名称', max_length=32)
    code = models.CharField('唯一标识', max_length=16, blank=True)
    permissions = models.ManyToManyField(Permission, verbose_name='拥有的所有权限', blank=True)

    class Meta:
        verbose_name_plural = verbose_name = '角色管理'

    def __str__(self):
        return self.title


class UserInfo(models.Model):
    """
    用户表
    """
    username = models.CharField('用户名', max_length=32, null=True, blank=True)
    password = models.CharField('密码', max_length=128, null=True, blank=True)
    email = models.CharField('邮箱', max_length=32, null=True, blank=True)
    roles = models.ManyToManyField(Role, verbose_name='拥有的所有角色', blank=True)

    class Meta:
        abstract = True
