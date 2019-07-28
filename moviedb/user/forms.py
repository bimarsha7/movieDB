from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from .models import user_profile

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

class login_form(forms.Form):
    username = forms.CharField(label="Username", max_length=150)
    password = forms.CharField(label="Password" , widget = forms.PasswordInput)

# 'user_edit_form()': This will allow users to edit their first name, last
# name, and email, which are attributes of the built-in Django
# user model
class user_edit_form(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')

# Users will be able to edit
# their date of birth and upload a picture for their profile.
class profile_edit_form(forms.ModelForm):
    class Meta:
        model = user_profile
        fields = ('date_of_birth', 'photo')
    
