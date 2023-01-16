from django.urls import path
from django.views.generic import TemplateView

from workflow.views import (CallLogListCreateView, OperatorListCreateView,
                            WorkflowUnactiveView, WorkflowView)

urlpatterns = [
    path('', WorkflowView.as_view(), name='workflow'),
    path('/unactive', WorkflowUnactiveView.as_view(),
         name='workflow.unactive'),

    path('/home', TemplateView.as_view(
        template_name="workflow/home.html"),
        name='workflow.home'),
    path('/call-logs', CallLogListCreateView.as_view(),
         name='workflow.call_logs'),
    path('/operators', OperatorListCreateView.as_view(),
         name='workflow.operators'),
    path('/work-places', TemplateView.as_view(
        template_name="workflow/home.html"),
        name='workflow.work_places'),
    path('/phone-numbers', TemplateView.as_view(
        template_name="workflow/home.html"),
        name='workflow.phone_numbers')
]
