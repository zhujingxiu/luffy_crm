from django.db import models
from rbac.models import UserInfo as RbacUserInfo


# Create your models here.
class Department(models.Model):
    """
    部门表
    """
    title = models.CharField('部门名称', max_length=16)
    code = models.CharField('唯一标识', max_length=16, blank=True)

    class Meta:
        verbose_name_plural = verbose_name = '员工部门'

    def __str__(self):
        return self.title


class UserInfo(RbacUserInfo):
    """
    员工表
    """
    name = models.CharField('真实姓名', max_length=16)
    phone = models.CharField('手机号', max_length=32)

    GENDERS = (
        (1, '男'),
        (2, '女'),
    )
    gender = models.IntegerField('性别', choices=GENDERS, default=1)
    depart = models.ForeignKey(Department, verbose_name='部门', on_delete=models.SET_NULL, null=True)

    class Meta:
        verbose_name_plural = verbose_name = '员工账户'

    def __str__(self):
        return self.name


class College(models.Model):
    title = models.CharField('校区名称', max_length=32)
    alias = models.CharField('简称', max_length=12, blank=True)
    cover = models.FileField('封面图', upload_to='image/%y%m%d', blank=True, default='')
    phone = models.CharField('联系电话', max_length=16, blank=True)
    address = models.CharField('联系地址', max_length=64, blank=True)
    openday = models.DateField('开业日期', null=True, blank=True)
    note = models.TextField('备注说明', null=True, blank=True)
    admin = models.ForeignKey(UserInfo, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='添加人')
    addtime = models.DateTimeField('添加时间', auto_now_add=True, blank=True)
    lasttime = models.DateTimeField('修改时间', auto_now=True, blank=True)

    class Meta:
        verbose_name_plural = verbose_name = '校区管理'

    def __str__(self):
        return self.title


class Course(models.Model):
    title = models.CharField('课程名称', max_length=32)
    admin = models.ForeignKey(UserInfo, on_delete=models.SET_NULL, null=True, blank=True)
    addtime = models.DateTimeField('添加时间', auto_now_add=True)
    lasttime = models.DateTimeField('修改时间', auto_now=True)

    class Meta:
        verbose_name_plural = verbose_name = '课程管理'

    def __str__(self):
        return self.title


class ClassInfo(models.Model):
    title = models.CharField('班级名称', max_length=32)
    course = models.ForeignKey(Course, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='课程')
    semester = models.SmallIntegerField('学期数', default=1)
    price = models.DecimalField('价格', max_digits=10, decimal_places=2)
    openday = models.DateField('开班日期', null=True, blank=True)
    endday = models.DateField('结业日期', null=True, blank=True, default='')
    note = models.TextField('备注说明', null=True, blank=True)
    college = models.ForeignKey(College, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='校区')
    tutor = models.ForeignKey(UserInfo, on_delete=models.SET_NULL, null=True, blank=True, related_name='tutor_user',
                              verbose_name='班主任', limit_choices_to={'roles__code': 'tutor', 'depart__code': 'training'})
    admin = models.ForeignKey(UserInfo, on_delete=models.SET_NULL, null=True, blank=True, related_name='admin_user',
                              verbose_name='添加人', limit_choices_to={'roles__pk': 1})
    addtime = models.DateTimeField('添加时间', auto_now_add=True)
    lasttime = models.DateTimeField('修改时间', auto_now=True)

    class Meta:
        verbose_name_plural = verbose_name = '班级管理'

    def __str__(self):
        return self.title
