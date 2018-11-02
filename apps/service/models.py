from django.db import models
from system.models import ClassInfo, Course, UserInfo


# Create your models here.
class Customer(models.Model):
    """
    客户表
    """
    phone = models.CharField('手机号', max_length=32, unique=True,)
    sns = models.CharField('其他联系方式', max_length=64, help_text='QQ号/微信/手机号')
    name = models.CharField('姓名', max_length=16)
    status = models.IntegerField("状态", default=2, help_text="选择客户此时的状态", choices=((1, "已报名"), (2, "未报名")))
    gender = models.SmallIntegerField('性别', choices=((1, '男'), (2, '女')))
    SOURCES = (
        (1, "QQ群"),
        (2, "内部转介绍"),
        (3, "官方网站"),
        (4, "百度推广"),
        (5, "360推广"),
        (6, "搜狗推广"),
        (7, "腾讯课堂"),
        (8, "高校宣讲"),
        (9, "渠道代理"),
        (10, "51cto"),
        (11, "SEO"),
        (12, "其它"), )
    source = models.SmallIntegerField('客户来源', choices=SOURCES, default=1)
    referral_from = models.ForeignKey('self', blank=True, null=True, verbose_name="转介绍自学员", on_delete=models.SET_NULL,
        help_text="若此客户是转介绍自内部学员,请在此处选择内部学员姓名", related_name="internal_referral", )
    course = models.ManyToManyField(Course, verbose_name="咨询课程", related_name='courses')
    consultant = models.ForeignKey(UserInfo, on_delete=models.SET_NULL, verbose_name="课程顾问", related_name='consultant',
                                   null=True, blank=True, limit_choices_to={'depart__code': 'marketing'})

    date = models.DateField("咨询日期", auto_now_add=True)
    last_consult_date = models.DateField("最后跟进日期", auto_now_add=True)

    class Meta:
        verbose_name_plural = verbose_name = '客户管理'

    def __str__(self):
        return self.name


class CustomerInfo(models.Model):
    customer = models.OneToOneField(Customer, on_delete=models.CASCADE, verbose_name='客户ID', null=True, blank=True)
    EDUCATIONS = (
        (1, '重点大学'),
        (2, '普通本科'),
        (3, '独立院校'),
        (4, '民办本科'),
        (5, '大专'),
        (6, '民办专科'),
        (7, '高中'),
        (8, '其他')
    )
    education = models.IntegerField('学历', choices=EDUCATIONS, blank=True, null=True, )
    graduation_school = models.CharField('毕业学校', max_length=64, blank=True, null=True)
    major = models.CharField('所学专业', max_length=64, blank=True, null=True)
    EXPERIENCES = (
        (1, '在校生'),
        (2, '应届毕业'),
        (3, '半年以内'),
        (4, '半年至一年'),
        (5, '一年至三年'),
        (6, '三年至五年'),
        (7, '五年以上'),
    )
    experience = models.IntegerField('工作经验', blank=True, null=True, choices=EXPERIENCES)
    work_status = models.IntegerField("职业状态", choices=((1, '在职'), (2, '无业')), default=1, blank=True, null=True)
    company = models.CharField("目前就职公司", max_length=64, blank=True, null=True)
    salary = models.CharField("当前薪资", max_length=64, blank=True, null=True)


class ConsultRecord(models.Model):
    """
    客户跟进记录
    """
    customer = models.ForeignKey(Customer, verbose_name="所咨询客户", on_delete=models.CASCADE)
    consultant = models.ForeignKey(UserInfo, verbose_name="跟踪人", on_delete=models.CASCADE)
    date = models.DateField("跟进日期", auto_now_add=True)
    note = models.TextField("跟进内容", blank=True)

    class Meta:
        verbose_name_plural = verbose_name = '客户跟进记录'


class PaymentRecord(models.Model):
    """
    缴费记录
    """
    customer = models.ForeignKey(Customer, verbose_name="客户", on_delete=models.CASCADE)
    consultant = models.ForeignKey(UserInfo, verbose_name="课程顾问", on_delete=models.CASCADE, help_text="谁签的单就选谁")
    classinfo = models.ForeignKey(ClassInfo, verbose_name="分配班级", on_delete=models.CASCADE, null=True, blank=True)
    pay_type = models.IntegerField("费用类型", choices=((1, "报名费"), (2, "学费"), (3, "转班"), (4, "退学")), default=1)
    paid_fee = models.IntegerField("金额", default=0)
    status = models.IntegerField('审核', default=1, choices=((1, '未审核'), (2, '已审核'),))
    confirm_date = models.DateTimeField("确认日期", null=True, blank=True)
    confirm_user = models.ForeignKey(UserInfo, verbose_name="确认人", on_delete=models.CASCADE, related_name='confirms',
                                     null=True, blank=True)
    note = models.TextField("备注", blank=True, null=True)
    apply_date = models.DateTimeField("申请日期", auto_now_add=True)

    class Meta:
        verbose_name_plural = verbose_name = '付款记录'


class Student(models.Model):
    """
    学生表（已报名）
    """
    customer = models.OneToOneField(Customer, verbose_name='客户信息', on_delete=models.CASCADE)
    username = models.CharField('用户名', max_length=32)
    password = models.CharField('密码', max_length=128)
    emergency_contract = models.CharField(max_length=32, blank=True, null=True, verbose_name='紧急联系人')
    classinfo = models.ManyToManyField(ClassInfo, verbose_name="已报班级",  blank=True)
    company = models.CharField('公司', max_length=128, blank=True, null=True)
    position = models.CharField('岗位', max_length=64, blank=True, null=True)
    salary = models.IntegerField('薪资', blank=True, null=True)
    welfare = models.CharField('福利', max_length=255, blank=True, null=True)
    date = models.DateField('入职时间', help_text='格式yyyy-mm-dd', blank=True, null=True)
    memo = models.CharField('备注', max_length=255, blank=True, null=True)

    class Meta:
        verbose_name_plural = verbose_name = '学员管理'

    def __str__(self):
        return self.username


class ChangeRecord(models.Model):
    """
    转班记录
    """
    student = models.OneToOneField(Student, verbose_name='学生信息', on_delete=models.CASCADE)
    origin_class = models.ForeignKey(ClassInfo, verbose_name="原班级", on_delete=models.CASCADE, related_name='x1')
    target_class = models.ForeignKey(ClassInfo, verbose_name="目标班级", on_delete=models.CASCADE, related_name='x2')
    admin = models.ForeignKey(UserInfo, verbose_name='处理人', on_delete=models.CASCADE)
    memo = models.TextField('原因', blank=True)
    add_date = models.DateTimeField("申请日期", auto_now_add=True, blank=True)

    class Meta:
        verbose_name_plural = verbose_name = '转班记录'


class CourseRecord(models.Model):
    """
    上课记录表
    """
    classinfo = models.ForeignKey(ClassInfo, verbose_name="班级", on_delete=models.CASCADE)
    day_num = models.IntegerField("节次", default=1)
    teacher = models.ForeignKey(UserInfo, verbose_name="讲师", on_delete=models.CASCADE)
    date = models.DateField("上课日期", auto_now_add=True)
    course_title = models.CharField('本节课程标题', max_length=64, blank=True, null=True)
    course_memo = models.TextField('本节课程内容概要', blank=True, null=True)
    homework_title = models.CharField('作业标题', max_length=64)
    homework_memo = models.TextField('作业描述')
    exam = models.TextField('踩分点', blank=True)

    class Meta:
        verbose_name_plural = verbose_name = '上课记录'

    def __str__(self):
        return "{0} day{1}".format(self.classinfo, self.day_num)


class StudyRecord(models.Model):
    course_record = models.ForeignKey(CourseRecord, verbose_name="第几天课程", on_delete=models.CASCADE)
    student = models.ForeignKey(Student, verbose_name="学员", on_delete=models.CASCADE)
    record_choices = (
        ('signed', "已签到"),
        ('vacate', "请假"),
        ('late', "迟到"),
        ('noshow', "缺勤"),
        ('leave_early', "早退"),
    )
    checking = models.CharField("考勤结果", choices=record_choices, default="signed", max_length=64)
    SCORES = (
        (100, 'A+'),
        (90, 'A'),
        (85, 'B+'),
        (80, 'B'),
        (70, 'B-'),
        (60, 'C+'),
        (50, 'C'),
        (40, 'C-'),
        (0, ' D'),
        (-1, 'N/A'),
        (-100, 'COPY'),
        (-1000, 'FAIL'),
    )
    score = models.IntegerField("本节成绩", choices=SCORES, default=-1)
    homework_note = models.CharField('作业评语', max_length=255, blank=True, null=True)
    homework = models.FileField('作业文件', blank=True, null=True)
    stu_memo = models.TextField('学员备注', blank=True, null=True)
    date = models.DateTimeField('提交作业日期', blank=True, null=True)

    class Meta:
        verbose_name_plural = verbose_name = '学习记录'

    def __str__(self):
        return "{0}-{1}".format(self.course_record, self.student)
