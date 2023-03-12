from django import forms
from django.core.validators import RegexValidator
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
        required=False,
    )

    class Meta:
        model = User
        fields = ("username", "first_name", "last_name")


class PhoneNumberField(forms.CharField):
    phone_regex = RegexValidator(
        regex=r"^\d{3}-\d{3}-\d{4}$",
        message="Phone number must be entered in the format: '000-000-0000'. Up to 12 digits allowed.",
    )

    def __init__(self, *args, **kwargs):
        kwargs.setdefault("validators", []).append(self.phone_regex)
        super().__init__(*args, **kwargs)


class TenantCompanyPhoneNumberCreateForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(TenantCompanyPhoneNumberCreateForm, self).__init__(*args, **kwargs)

    phone_number = PhoneNumberField()

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
