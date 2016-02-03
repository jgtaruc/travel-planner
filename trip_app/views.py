from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse

from custom_auth.models import MyUser

from trip_app.forms import LoginForm, SignUpForm

# Create your views here.
def home(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect(reverse('dashboard'))
    if request.method == 'GET':
        login_form = LoginForm()
        signup_form = SignUpForm()
    elif 'login-btn' in request.POST:
        login_form = LoginForm(request.POST)
        signup_form = SignUpForm(request.POST)
        if login_form.is_valid():
            user = authenticate(username=request.POST['email'],
                password=request.POST['password'])
            login(request,user)
            return HttpResponseRedirect(reverse('dashboard'))
    elif 'signup-btn' in request.POST:
        login_form = LoginForm(request.POST)
        signup_form = SignUpForm(request.POST)
        if signup_form.is_valid():
            user = MyUser()
            user.email = signup_form.cleaned_data['email']
            if signup_form.cleaned_data['password'] == signup_form.cleaned_data['password_conf']:
                user.set_password(signup_form.cleaned_data['password'])
                user.save()
                user = authenticate(username=signup_form.cleaned_data['email'],
                        password=signup_form.cleaned_data['password'])
                login(request, user)
                return HttpResponseRedirect(reverse('dashboard'))
    return render(request, 'trip_app/main.html', {'login_form':login_form, 'signup_form':signup_form})


@login_required(login_url='login')
def dashboard(request):
    user = request.user
    return render(request, 'trip_app/dashboard.html',{'user':user})


@login_required(login_url='login')
def signout(request):
    logout(request)
    return HttpResponseRedirect(reverse('home'))
