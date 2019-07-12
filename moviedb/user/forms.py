from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError

class sign_up_form(UserCreationForm):
    email = forms.EmailField(label="Email", max_length=150)

    class Meta:
        model = User
        fields = ['email', 'username', 'password1', 'password2']

    def clean_email(self):
        email = self.cleaned_data['email'].lower()
        r = User.objects.filter(email=email)
        if r.count():
            raise ValidationError('Email already exist. Check your Email and Try again.')
        return email
    
    def clean_username(self):
        username  = self.cleaned_data['username'].lower()
        r = User.objects.filter(username = username)
        if r.count():
            raise ValidationError('Username already exist. Try another one')
        return username
