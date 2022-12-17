from django.urls import path
from django.views.generic import TemplateView

urlpatterns = [
    path('home', TemplateView.as_view(
        template_name="tenant_company_operator/home.html"), name='tenant_company_operator.home'),
]
