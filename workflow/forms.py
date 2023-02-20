from django import forms
from django.db.models import Q

from call_center_project.models import (
    CallLog,
    TenantCompanyPhoneNumber,
    User,
    WorkPlace,
)


class CallLogMessagesUpdateForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(CallLogMessagesUpdateForm, self).__init__(*args, **kwargs)
        self.fields["duration"].disabled = True
        self.fields["caller_person"].disabled = True
        self.fields["tenant_company_phone_number"].disabled = True
        self.fields["operator"].disabled = True
        self.fields["disconnect_initiator"].disabled = True
        self.fields["response"].disabled = True
        self.fields["paid"].disabled = True
        self.fields["address"].disabled = True

    class Meta:
        model = CallLog
        fields = "__all__"


class OperatorWorkPlaceUpdateForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(OperatorWorkPlaceUpdateForm, self).__init__(*args, **kwargs)
        self.fields["username"].disabled = True
        self.fields["first_name"].disabled = True
        self.fields["last_name"].disabled = True
        self.fields["current_work_place"].disabled = True

    current_work_place = forms.CharField(required=False)
    new_work_place = forms.ModelChoiceField(
        queryset=WorkPlace.objects.filter(Q(operators=None) & Q(tenant_company=None)),
    )

    class Meta:
        model = User
        fields = ("username", "first_name", "last_name")


class TenantCompanyPhoneNumberCreateForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(TenantCompanyPhoneNumberCreateForm, self).__init__(*args, **kwargs)

    class Meta:
        model = TenantCompanyPhoneNumber
        fields = ("phone_number", "description")


class TenantCompanyPhoneNumberUpdateForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(TenantCompanyPhoneNumberCreateForm, self).__init__(*args, **kwargs)
        self.fields["phone_number"].disabled = True

    class Meta:
        model = TenantCompanyPhoneNumber
        fields = ("phone_number", "description")
