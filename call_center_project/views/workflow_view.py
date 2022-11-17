from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View


class WorkflowView(LoginRequiredMixin, View):
    login_url = '/accounts/login/'
