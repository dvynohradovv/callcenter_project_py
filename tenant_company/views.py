from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.shortcuts import render
from django.views.generic import TemplateView

from call_center_project.models import AccountType, CallLog, User


class CallLogListCreateView(TemplateView, LoginRequiredMixin):
    template_name = "tenant_company/workflow/call_logs.html"

    def get(self, request):
        user = request.user
        call_logs = CallLog.objects.filter(
            tenant_company_phone_number__tenant_company__id=user.tenant_company.id
        )

        data = {'data': call_logs}
        return render(request, self.template_name, data)


class OperatorListCreateView(TemplateView, LoginRequiredMixin):
    template_name = "tenant_company/workflow/operators.html"

    def get(self, request):
        user = request.user
        operators = User.objects.filter(
            Q(tenant_company__id=user.tenant_company.id)
            &
            Q(type=AccountType.Operator.value)
        )

        data = {'data': operators}
        return render(request, self.template_name, data)
