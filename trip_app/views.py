from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse

from trip_app.forms import LoginForm, SignUpForm

# Create your views here.
def landing(request):
    if request.method == 'GET':
        login_form = LoginForm()
        signup_form = SignUpForm()
    return render(request, 'trip_app/main.html', {'login_form':login_form, 'signup_form':signup_form})
