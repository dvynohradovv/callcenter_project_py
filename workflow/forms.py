from django import forms

from call_center_project.models import CallLog


class CallLogForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(CallLogForm, self).__init__(*args, **kwargs)
        self.fields['duration'].disabled = True
        self.fields['caller_person'].disabled = True
        self.fields['tenant_company_phone_number'].disabled = True
        self.fields['operator'].disabled = True
        self.fields['disconnect_initiator'].disabled = True
        self.fields['response'].disabled = True
        self.fields['paid'].disabled = True
        self.fields['address'].disabled = True

    class Meta:
        model = CallLog
        fields = '__all__'
