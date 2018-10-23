#!/usr/bin/env python
# -*- coding:utf-8 -*-
# _AUTHOR_  : zhujingxiu
# _DATE_    : 2018/10/19

from xstark.sites import site
from service.xstarks.student import Student, StudentAdmin
from service.xstarks.customer import Customer, CustomerAdmin, PublicCustomerAdmin, PrivateCustomerAdmin
from service.xstarks.consult_record import ConsultRecord, ConsultRecordAdmin, PrivateConsultRecordAdmin


site.register(Customer, CustomerAdmin)


site.register(Customer, PublicCustomerAdmin, 'pub')


site.register(Customer, PrivateCustomerAdmin, 'pri')


site.register(Student, StudentAdmin)

site.register(ConsultRecord, ConsultRecordAdmin)
site.register(ConsultRecord, PrivateConsultRecordAdmin, 'pri')