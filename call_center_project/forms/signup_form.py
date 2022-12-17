from django.contrib.auth.forms import UserCreationForm

from call_center_project.models import User


class SignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username', 'email')
