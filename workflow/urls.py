from django.urls import path
from django.views.generic import TemplateView

from workflow.views import (
    CallLogListView,
    CallLogUpdateRetrieveView,
    OperatorActivateView,
    OperatorDisableView,
    OperatorListView,
    TenantCompanyPhoneNumberActivateView,
    TenantCompanyPhoneNumberDisableView,
    TenantCompanyPhoneNumberListView,
    WorkflowRedirectView,
    WorkflowUnactiveTemplateView,
    WorkPlaceListView,
)

urlpatterns = [
    path("", WorkflowRedirectView.as_view(), name="workflow"),
    path("unactive", WorkflowUnactiveTemplateView.as_view(), name="workflow.unactive"),
    path(
        "home",
        TemplateView.as_view(template_name="workflow/home.html"),
        name="workflow.home",
    ),
    path("call-logs", CallLogListView.as_view(), name="workflow.call_logs"),
    path(
        "call-logs/<int:call_log_id>/update",
        CallLogUpdateRetrieveView.as_view(),
        name="workflow.call_logs.update",
    ),
    # Operators
    path("operators", OperatorListView.as_view(), name="workflow.operators"),
    path(
        "operators/<int:operator_id>/disable",
        OperatorDisableView.as_view(),
        name="workflow.operators.disable",
    ),
    path(
        "operators/<int:operator_id>/activate",
        OperatorActivateView.as_view(),
        name="workflow.operators.activate",
    ),
    path("work-places", WorkPlaceListView.as_view(), name="workflow.work_places"),
    # Phone numbers
    path(
        "phone-numbers",
        TenantCompanyPhoneNumberListView.as_view(),
        name="workflow.phone_numbers",
    ),
    path(
        "phone-numbers/<int:phone_number_id>/disable",
        TenantCompanyPhoneNumberDisableView.as_view(),
        name="workflow.phone-numbers.disable",
    ),
    path(
        "phone-numbers/<int:phone_number_id>/activate",
        TenantCompanyPhoneNumberActivateView.as_view(),
        name="workflow.phone-numbers.activate",
    ),
]
