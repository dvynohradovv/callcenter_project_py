from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import TemplateView

from call_center_project.models import (
    AccountType,
    TenantCompanyPhoneNumber,
    User,
    WorkPlace,
)
from workflow.forms import CallLogForm
from workflow.services import CallLogService


class WorkflowRedirectView(LoginRequiredMixin, View):
    login_url = "/accounts/login/"

    def get(self, request):
        if request.user.type == AccountType.Unactive:
            return HttpResponseRedirect(reverse_lazy("workflow.unactive"))
        elif request.user.type == AccountType.Admin:
            return HttpResponseRedirect(reverse_lazy("admin:index"))
        else:
            return HttpResponseRedirect(reverse_lazy("workflow.home"))


class WorkflowUnactiveTemplateView(LoginRequiredMixin, TemplateView):
    template_name = "workflow/unactive.html"


class CallLogListView(LoginRequiredMixin, TemplateView):
    template_name = "workflow/call-logs.html"

    def __init__(self) -> None:
        self.call_log_service = CallLogService()

    def get(self, request):
        user: User = request.user

        call_logs = self.call_log_service.find_all(user)

        data = {"data": call_logs, "count": len(call_logs)}
        return render(request, self.template_name, data)


class CallLogUpdateRetrieveView(LoginRequiredMixin, TemplateView):
    template_name = "workflow/call-logs-update.html"

    def __init__(self) -> None:
        self.call_log_service = CallLogService()

    def get(self, request, call_log_id: int):
        user = request.user
        call_log = self.call_log_service.find_by_id(user, call_log_id)

        form = CallLogForm(instance=call_log)

        data = {"form": form}
        return render(request, self.template_name, data)

    # But this is put method
    def post(self, request, call_log_id: int):
        user = request.user
        call_log = self.call_log_service.find_by_id(user, call_log_id)
        form = CallLogForm(request.POST, instance=call_log)
        if form.is_valid():
            form.save()

        data = {"form": form}
        return render(request, self.template_name, data)


class OperatorListView(LoginRequiredMixin, TemplateView):
    template_name = "workflow/operators.html"

    def get(self, request):
        user = request.user
        operators = User.objects.filter(
            Q(tenant_company__id=user.tenant_company.id)
            & Q(type=AccountType.Operator.value)
        )

        data = {"data": operators, "count": len(operators)}
        return render(request, self.template_name, data)


class OperatorDisableView(LoginRequiredMixin, View):
    def post(self, request, operator_id):
        user = request.user
        operator = get_object_or_404(
            User,
            Q(id=operator_id)
            & Q(tenant_company__id=user.tenant_company.id)
            & Q(type=AccountType.Operator.value),
        )

        operator.isdisabled = True
        operator.save()

        return HttpResponseRedirect(reverse_lazy("workflow.operators"))


class OperatorActivateView(LoginRequiredMixin, View):
    def post(self, request, operator_id):
        user = request.user
        operator = get_object_or_404(
            User,
            Q(id=operator_id)
            & Q(tenant_company__id=user.tenant_company.id)
            & Q(type=AccountType.Operator.value),
        )

        operator.isdisabled = False
        operator.save()

        return HttpResponseRedirect(reverse_lazy("workflow.operators"))


class WorkPlaceListView(LoginRequiredMixin, TemplateView):
    template_name = "workflow/work-places.html"

    def get(self, request):
        user = request.user
        work_places = WorkPlace.objects.prefetch_related("operators").filter(
            tenant_company__id=user.tenant_company.id
        )

        data = {"data": work_places, "count": len(work_places)}
        return render(request, self.template_name, data)


class TenantCompanyPhoneNumberListView(LoginRequiredMixin, TemplateView):
    template_name = "workflow/phone-numbers.html"

    def get(self, request):
        user = request.user
        tc_phone_numbers = TenantCompanyPhoneNumber.objects.filter(
            tenant_company__id=user.tenant_company.id
        )

        data = {"data": tc_phone_numbers, "count": len(tc_phone_numbers)}
        return render(request, self.template_name, data)


class TenantCompanyPhoneNumberDisableView(LoginRequiredMixin, View):
    def post(self, request, phone_number_id):
        user = request.user
        tc_phone_number = get_object_or_404(
            TenantCompanyPhoneNumber,
            Q(id=phone_number_id) & Q(tenant_company__id=user.tenant_company.id),
        )

        tc_phone_number.isdisabled = True
        tc_phone_number.save()

        return HttpResponseRedirect(reverse_lazy("workflow.phone_numbers"))


class TenantCompanyPhoneNumberActivateView(LoginRequiredMixin, View):
    def post(self, request, phone_number_id):
        user = request.user
        tc_phone_number = get_object_or_404(
            TenantCompanyPhoneNumber,
            Q(id=phone_number_id) & Q(tenant_company__id=user.tenant_company.id),
        )

        tc_phone_number.isdisabled = False
        tc_phone_number.save()

        return HttpResponseRedirect(reverse_lazy("workflow.phone_numbers"))
