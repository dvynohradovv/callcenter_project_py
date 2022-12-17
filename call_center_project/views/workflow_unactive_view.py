from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView


class WorkflowUnactiveView(LoginRequiredMixin, TemplateView):
    template_name = 'call_center_project/workflow/unactive.html'
