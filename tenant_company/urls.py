from django.urls import path
from django.views.generic import TemplateView

from tenant_company.views import CallLogView

urlpatterns = [
    path('home', TemplateView.as_view(
        template_name="tenant_company/workflow/home.html"), name='tenant_company.home'),
    path('call-logs', CallLogView.as_view(), name='tenant_company.call_logs'),
    path('operators', TemplateView.as_view(
        template_name="tenant_company/workflow/home.html"), name='tenant_company.operators'),
    path('work-places', TemplateView.as_view(
        template_name="tenant_company/workflow/home.html"), name='tenant_company.work_places'),
    path('phone-numbers', TemplateView.as_view(
        template_name="tenant_company/workflow/home.html"), name='tenant_company.phone_numbers')
]
