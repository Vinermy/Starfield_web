from django.contrib.auth.models import User
from django.forms import *


class SignupForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']
        widgets = {
            'password': PasswordInput
        }
