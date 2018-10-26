from service.models import Customer, ConsultRecord
from system.models import UserInfo
from xstark.sites import StarkAdminModel
from django import forms


class ConsultRecordAdmin(StarkAdminModel):
    list_display = ['customer', 'note', 'consultant']

    def get_queryset(self):
        customer = self.request.GET.get('customer')
        if customer:
            return ConsultRecord.objects.filter(customer_id=customer)
        return None


class PrivateConsultRecordlForm(forms.ModelForm):
    class Meta:
        model = ConsultRecord
        exclude = ['customer', 'consultant']


class PrivateConsultRecordAdmin(StarkAdminModel):
    list_display = ['customer', 'note', 'consultant', 'date']

    model_form_class = PrivateConsultRecordlForm

    def get_queryset(self):
        customer = self.request.GET.get('customer')
        current_user_id = 1  # 以后要改成去session中获取当前登陆用户ID
        if customer:
            return ConsultRecord.objects.filter(customer_id=customer, customer__consultant_id=current_user_id)
        return ConsultRecord.objects.filter(customer__consultant_id=current_user_id)

    def save(self, form, modify=False):
        if not modify:
            params = self.request.session.get(self.request_get_key)
            if params:
                from django.http import QueryDict
                params = QueryDict(params)
                customer_id = params.get('customer')

                form.instance.customer = Customer.objects.get(id=customer_id)
            current_user_id = 1
            form.instance.consultant = UserInfo.objects.get(id=current_user_id)
        form.save()

    def get_site_title(self):
        customer = None
        params = self.request.session.get(self.request_get_key)
        if params:
            from django.http import QueryDict
            params = QueryDict(params)
            customer_id = params.get('customer')
            customer = Customer.objects.filter(pk=customer_id).first()
        return '%s:%s' % (customer.name, super().get_site_title()) if customer else super().get_site_title()