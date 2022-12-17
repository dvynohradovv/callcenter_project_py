from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views import View

from call_center_project.models import AccountType


class WorkflowView(LoginRequiredMixin, View):
    login_url = '/accounts/login/'

    def get(self, request):
        if request.user.type == AccountType.Unactive:
            return HttpResponseRedirect(reverse_lazy('workflow_unactive'))
        elif request.user.type == AccountType.Admin:
            return HttpResponseRedirect(reverse_lazy('admin:index'))
        elif request.user.type == AccountType.Operator:
            return HttpResponseRedirect(reverse_lazy('tenant_company.home'))
        elif request.user.type == AccountType.TenantCompanyOwner:
            return HttpResponseRedirect(reverse_lazy('tenant_company.home'))
