"""call_center_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from django.views.generic import TemplateView

from call_center_project.views.workflow import Workflow


urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path("accounts/", include("django.contrib.auth.urls"), name='accounts'),
    path("", TemplateView.as_view(
        template_name="call_center_project/main/index.html"), name='index'),
    path("workflow", Workflow.as_view(), name='workflow'),
    path('workflow/tenant_company/',
         include("tenant_company.urls")),
    path('workflow/tenant_company_operator/',
         include("tenant_company_operator.urls")),
]
