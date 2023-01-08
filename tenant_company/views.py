from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import TemplateView

from call_center_project.models import AccountType, CallLog


class CallLogView(TemplateView):
    template_name = "tenant_company/workflow/call_logs.html"

    def get(self, request):
        user = request.user
        call_logs = CallLog.objects.filter(
            tenant_company_phone_number__tenant_company__id=user.tenant_company.id
        )

        data = {'data': call_logs}
        return render(request, self.template_name, data)
