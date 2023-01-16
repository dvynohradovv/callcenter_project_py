from django.urls import reverse_lazy
from django.views import generic

from call_center_project.forms.signup_form import SignUpForm


class SignUpView(generic.CreateView):
    form_class = SignUpForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"

    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)
