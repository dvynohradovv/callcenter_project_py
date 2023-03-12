from random import randint
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import TemplateView

from call_center_project.mixins import UserTypeMixin
from call_center_project.models import (
    AccountType,
    OperatorToWorkPlace,
    TenantCompanyPhoneNumber,
    User,
    WorkPlace,
)
from workflow.forms import (
    CallLogMessagesUpdateForm,
    OperatorWorkPlaceUpdateForm,
    TenantCompanyPhoneNumberCreateForm,
)
from workflow.services import CallLogService

DAYS = ["day", "month", "year"]


class WorkflowRedirectView(LoginRequiredMixin, UserTypeMixin, View):
    login_url = "/accounts/login/"
    user_types = []

    def get(self, request):
        if request.user.type == AccountType.Unactive:
            return HttpResponseRedirect(reverse_lazy("workflow.unactive"))
        elif request.user.type == AccountType.Admin:
            return HttpResponseRedirect(reverse_lazy("admin:index"))
        else:
            return HttpResponseRedirect(reverse_lazy("workflow.home"))


class WorkflowUnactiveTemplateView(LoginRequiredMixin, UserTypeMixin, TemplateView):
    template_name = "workflow/unactive.html"
    user_types = [AccountType.Unactive]


class HomeTemplateView(LoginRequiredMixin, UserTypeMixin, TemplateView):
    template_name = "workflow/home.html"
    user_types = [AccountType.TenantCompanyOwner, AccountType.Operator]

    def get(self, request):
        data = {}
        for attr in ["sum_duration", "avg_cost"]:
            for d in DAYS:
                data[f"{attr}_{d}"] = randint(0, 1000)
                data[f"{attr}_{d}_rnd"] = randint(0, 100)

        return render(request, self.template_name, data)


class CallLogListView(LoginRequiredMixin, UserTypeMixin, TemplateView):
    template_name = "workflow/call-logs.html"
    user_types = [AccountType.TenantCompanyOwner, AccountType.Operator]

    def __init__(self) -> None:
        self.call_log_service = CallLogService()

    def get(self, request):
        user: User = request.user

        call_logs = self.call_log_service.find_all(user)

        data = {"data": call_logs, "count": len(call_logs)}
        return render(request, self.template_name, data)


class CallLogUpdateRetrieveView(LoginRequiredMixin, UserTypeMixin, TemplateView):
    template_name = "workflow/call-logs-update.html"
    user_types = [AccountType.TenantCompanyOwner, AccountType.Operator]

    def __init__(self) -> None:
        self.call_log_service = CallLogService()

    def get(self, request, call_log_id: int):
        user = request.user
        call_log = self.call_log_service.find_by_id(user, call_log_id)

        form = CallLogMessagesUpdateForm(instance=call_log)

        data = {"form": form}
        return render(request, self.template_name, data)

    # But this is put method
    def post(self, request, call_log_id: int):
        user = request.user
        call_log = self.call_log_service.find_by_id(user, call_log_id)
        form = CallLogMessagesUpdateForm(request.POST, instance=call_log)
        if form.is_valid():
            form.save()

        data = {"form": form}
        return render(request, self.template_name, data)


class OperatorListView(LoginRequiredMixin, UserTypeMixin, TemplateView):
    template_name = "workflow/operators.html"
    user_types = [AccountType.TenantCompanyOwner]

    def get(self, request):
        user = request.user
        operators = User.objects.filter(
            Q(tenant_company__id=user.tenant_company.id)
            & Q(type=AccountType.Operator.value)
        )

        data = {"data": operators, "count": len(operators)}
        return render(request, self.template_name, data)


class OperatorWorkPlaceEdit(LoginRequiredMixin, UserTypeMixin, View):
    user_types = [AccountType.TenantCompanyOwner]
    template_name = "workflow/operators-work-place-edit.html"

    def get(self, request, operator_id: int):
        user = request.user
        operator = get_object_or_404(
            User,
            Q(id=operator_id)
            & Q(tenant_company__id=user.tenant_company.id)
            & Q(type=AccountType.Operator.value),
        )

        work_place = operator.work_place.first()
        current_work_place = str(work_place) if operator.work_place.first() else "None"

        form = OperatorWorkPlaceUpdateForm(
            instance=operator, initial={"current_work_place": current_work_place}
        )

        data = {"form": form}
        return render(request, self.template_name, data)

    # But this is put method
    def post(self, request, operator_id: int):
        user = request.user
        operator = get_object_or_404(
            User,
            Q(id=operator_id)
            & Q(tenant_company__id=user.tenant_company.id)
            & Q(type=AccountType.Operator.value),
        )

        form = OperatorWorkPlaceUpdateForm(request.POST, instance=operator)
        if form.is_valid():
            old_work_place = operator.work_place.first()
            if old_work_place:
                old_work_place.tenant_company = None
                old_work_place.save()
                operator.work_place.remove(old_work_place)

            if form.cleaned_data.get("new_work_place"):
                new_work_place = form.cleaned_data.get("new_work_place")
                new_work_place.tenant_company = user.tenant_company
                new_work_place.save()
                operator.work_place.add(new_work_place)

        return HttpResponseRedirect(
            reverse_lazy(
                "workflow.operators.work-place-edit",
                kwargs={"operator_id": operator_id},
            )
        )


class OperatorDisableView(LoginRequiredMixin, UserTypeMixin, View):
    user_types = [AccountType.TenantCompanyOwner]

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


class OperatorActivateView(LoginRequiredMixin, UserTypeMixin, View):
    user_types = [AccountType.TenantCompanyOwner]

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


class WorkPlaceListView(LoginRequiredMixin, UserTypeMixin, TemplateView):
    template_name = "workflow/work-places.html"
    user_types = [AccountType.TenantCompanyOwner]

    def get(self, request):
        user = request.user
        work_places = WorkPlace.objects.prefetch_related("operators").filter(
            tenant_company__id=user.tenant_company.id
        )

        data = {"data": work_places, "count": len(work_places)}
        return render(request, self.template_name, data)


class TenantCompanyPhoneNumberListView(LoginRequiredMixin, UserTypeMixin, TemplateView):
    template_name = "workflow/phone-numbers.html"
    user_types = [AccountType.TenantCompanyOwner]

    def get(self, request):
        user = request.user
        tc_phone_numbers = TenantCompanyPhoneNumber.objects.filter(
            tenant_company__id=user.tenant_company.id
        )

        data = {"data": tc_phone_numbers, "count": len(tc_phone_numbers)}
        return render(request, self.template_name, data)


class TenantCompanyPhoneNumberCreateView(
    LoginRequiredMixin, UserTypeMixin, TemplateView
):
    template_name = "workflow/phone-numbers-create.html"
    user_types = [AccountType.TenantCompanyOwner]

    def get(self, request):
        user = request.user
        form = TenantCompanyPhoneNumberCreateForm()

        data = {"form": form}
        return render(request, self.template_name, data)

    # But this is put method
    def post(self, request):
        user = request.user

        form = TenantCompanyPhoneNumberCreateForm(request.POST)
        print("form invalid")
        if form.is_valid():
            print("form valid")
            tc_phone_number = TenantCompanyPhoneNumber(
                phone_number=form.cleaned_data["phone_number"],
                description=form.cleaned_data["description"],
                tenant_company=user.tenant_company,
            )
            tc_phone_number.save()

        data = {"form": form}
        return render(request, self.template_name, data)


class TenantCompanyPhoneNumberDisableView(LoginRequiredMixin, UserTypeMixin, View):
    user_types = [AccountType.TenantCompanyOwner]

    def post(self, request, phone_number_id):
        user = request.user
        tc_phone_number = get_object_or_404(
            TenantCompanyPhoneNumber,
            Q(id=phone_number_id) & Q(tenant_company__id=user.tenant_company.id),
        )

        tc_phone_number.isdisabled = True
        tc_phone_number.save()

        return HttpResponseRedirect(reverse_lazy("workflow.phone_numbers"))


class TenantCompanyPhoneNumberActivateView(LoginRequiredMixin, UserTypeMixin, View):
    user_types = [AccountType.TenantCompanyOwner]

    def post(self, request, phone_number_id):
        user = request.user
        tc_phone_number = get_object_or_404(
            TenantCompanyPhoneNumber,
            Q(id=phone_number_id) & Q(tenant_company__id=user.tenant_company.id),
        )

        tc_phone_number.isdisabled = False
        tc_phone_number.save()

        return HttpResponseRedirect(reverse_lazy("workflow.phone_numbers"))
