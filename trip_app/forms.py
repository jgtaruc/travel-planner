from django import forms
from django.forms import ModelForm
from django.forms.extras.widgets import SelectDateWidget
from datetime import datetime

from custom_auth.models import MyUser

class LoginForm(forms.Form):
    email = forms.EmailField(label='Email')
    password = forms.CharField(widget = forms.PasswordInput())


class SignUpForm(forms.Form):
    email = forms.EmailField(label='Email')
    password = forms.CharField(widget=forms.PasswordInput())
    password_conf = forms.CharField(widget=forms.PasswordInput())
