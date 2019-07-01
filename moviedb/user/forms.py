from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class sign_up_form(UserCreationForm):
    email = forms.EmailField(label="Email", max_length=150)

    class Meta:
        model = User
        fields = ['email', 'username', 'password1', 'password2']

