#!/usr/bin/env python
# -*- coding:utf-8 -*-
# _AUTHOR_  : zhujingxiu
# _DATE_    : 2018/10/19

from xstark.sites import site
from service.xstarks.student import Student, StudentAdmin
from service.xstarks.customer import Customer, CustomerAdmin, PublicCustomerAdmin, PrivateCustomerAdmin
from service.xstarks.consult_record import ConsultRecord, ConsultRecordAdmin, PrivateConsultRecordAdmin
from service.xstarks.payment_record import PaymentRecord, PaymentRecordAdmin
from service.xstarks.change_recode import ChangeRecord, ChangeRecordAdmin
from service.xstarks.course_record import CourseRecord, CourseRecordAdmin
from service.xstarks.study_record import StudyRecord, StudyRecordAdmin

site.register(Customer, CustomerAdmin)


site.register(Customer, PublicCustomerAdmin, 'pub')


site.register(Customer, PrivateCustomerAdmin, 'pri')


site.register(Student, StudentAdmin)

site.register(ConsultRecord, ConsultRecordAdmin)

site.register(ConsultRecord, PrivateConsultRecordAdmin, 'pri')

site.register(CourseRecord, CourseRecordAdmin)

site.register(PaymentRecord, PaymentRecordAdmin)

site.register(ChangeRecord, ChangeRecordAdmin)
site.register(StudyRecord, StudyRecordAdmin)