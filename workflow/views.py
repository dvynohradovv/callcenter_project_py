from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import TemplateView

from call_center_project.models import AccountType, CallLog, TenantCompanyPhoneNumber, User, WorkPlace


class WorkflowRedirectView(LoginRequiredMixin, View):
    login_url = '/accounts/login/'

    def get(self, request):
        if request.user.type == AccountType.Unactive:
            return HttpResponseRedirect(reverse_lazy('workflow.unactive'))
        elif request.user.type == AccountType.Admin:
            return HttpResponseRedirect(reverse_lazy('admin:index'))
        else:
            return HttpResponseRedirect(reverse_lazy('workflow.home'))


class WorkflowUnactiveTemplateView(LoginRequiredMixin, TemplateView):
    template_name = 'workflow/unactive.html'


class CallLogListView(TemplateView, LoginRequiredMixin):
    template_name = "workflow/call-logs.html"

    def get(self, request):
        user = request.user
        call_logs = CallLog.objects.filter(
            tenant_company_phone_number__tenant_company__id=user.tenant_company.id
        )

        data = {'data': call_logs}
        return render(request, self.template_name, data)


class OperatorListView(TemplateView, LoginRequiredMixin):
    template_name = "workflow/operators.html"

    def get(self, request):
        user = request.user
        operators = User.objects.filter(
            Q(tenant_company__id=user.tenant_company.id)
            &
            Q(type=AccountType.Operator.value)
        )

        data = {'data': operators}
        return render(request, self.template_name, data)


class WorkPlaceListView(TemplateView, LoginRequiredMixin):
    template_name = "workflow/work-places.html"

    def get(self, request):
        user = request.user
        work_places = WorkPlace.objects.prefetch_related('operators').filter(
            tenant_company__id=user.tenant_company.id
        )

        data = {'data': work_places}
        return render(request, self.template_name, data)


class TenantCompanyPhoneNumberListView(TemplateView, LoginRequiredMixin):
    template_name = "workflow/phone-numbers.html"

    def get(self, request):
        user = request.user
        tc_phone_numbers = TenantCompanyPhoneNumber.objects.filter(
            tenant_company__id=user.tenant_company.id
        )

        data = {'data': tc_phone_numbers}
        return render(request, self.template_name, data)
