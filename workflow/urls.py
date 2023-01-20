from django.urls import path
from django.views.generic import TemplateView

from workflow.views import (CallLogListView, CallLogUpdateRetrieveView,
                            OperatorListView, TenantCompanyPhoneNumberListView,
                            WorkflowRedirectView, WorkflowUnactiveTemplateView,
                            WorkPlaceListView)

urlpatterns = [
    path('', WorkflowRedirectView.as_view(), name='workflow'),
    path('unactive', WorkflowUnactiveTemplateView.as_view(),
         name='workflow.unactive'),

    path('home', TemplateView.as_view(
        template_name="workflow/home.html"),
        name='workflow.home'),

    path('call-logs', CallLogListView.as_view(),
         name='workflow.call_logs'),
    path('call-logs/<int:call_log_id>', CallLogUpdateRetrieveView.as_view(),
         name='workflow.call_logs_edit'),


    path('operators', OperatorListView.as_view(),
         name='workflow.operators'),
    path('work-places', WorkPlaceListView.as_view(),
         name='workflow.work_places'),
    path('phone-numbers', TenantCompanyPhoneNumberListView.as_view(),
         name='workflow.phone_numbers')
]
