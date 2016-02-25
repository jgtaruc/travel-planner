from django import forms
from django.forms import ModelForm
from django.forms.extras.widgets import SelectDateWidget
from datetime import datetime

from custom_auth.models import MyUser
from trip_app.models import Trip, Activity

class LoginForm(forms.Form):
    email = forms.EmailField(label='Email')
    password = forms.CharField(widget = forms.PasswordInput())


class SignUpForm(forms.Form):
    email = forms.EmailField(label='Email')
    password = forms.CharField(widget=forms.PasswordInput())
    password_conf = forms.CharField(widget=forms.PasswordInput())


class TripForm(forms.Form):
    trip_name = forms.CharField(label="Trip name", max_length=256)
    trip_location = forms.CharField(label="Trip location", max_length=256)
    trip_desc = forms.CharField(widget=forms.Textarea, label="Trip description", max_length=1024)
    trip_start_date = forms.DateField(initial=datetime.now, widget=SelectDateWidget(), label="Trip start date")
    trip_end_date = forms.DateField(initial=datetime.now, widget=SelectDateWidget(), label="Trip end date")


class ActivityForm(forms.Form):
    activ_name = forms.CharField(label="Activity name", max_length=256)
    activ_location = forms.CharField(label="Activity location", max_length=256)
    activ_description = forms.CharField(widget=forms.Textarea, label="Activity description", max_length=1024)
    activ_expense = forms.DecimalField(label="Activity Expense")
    activ_start_datetime = forms.DateField(initial=datetime.now, widget=SelectDateWidget())
    activ_end_datetime = forms.DateField(initial=datetime.now, widget=SelectDateWidget())


class ProfileForm(forms.Form):
    email = forms.EmailField(label='Email')
    first_name = forms.CharField(label='First Name')
    last_name = forms.CharField(label='Last Name')
    password = forms.CharField(widget=forms.PasswordInput())
    password_conf = forms.CharField(widget=forms.PasswordInput())
