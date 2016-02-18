from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, render_to_response
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse

from custom_auth.models import MyUser
from trip_app.models import Trip, Activity

from trip_app.forms import LoginForm, SignUpForm, TripForm, ActivityForm

from datetime import datetime

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
            if user is None:
                return render(request, 'trip_app/main.html', {'login_form':login_form, 'signup_form':signup_form, 'invalid': "True"})
            login(request,user)
            return HttpResponseRedirect(reverse('dashboard'))

    elif 'signup-btn' in request.POST:
        login_form = LoginForm(request.POST)
        signup_form = SignUpForm(request.POST)
        if signup_form.is_valid():
            user = MyUser()
            user.email = signup_form.cleaned_data['email']
            if MyUser.objects.filter(email=user.email).exists():
                return render(request, 'trip_app/main.html', {'login_form':login_form, 'signup_form':signup_form,
                    'not_unique_email':"not_unique_email"})
            if signup_form.cleaned_data['password'] == signup_form.cleaned_data['password_conf']:
                user.set_password(signup_form.cleaned_data['password'])
                user.save()
                user = authenticate(username=signup_form.cleaned_data['email'],
                        password=signup_form.cleaned_data['password'])
                login(request, user)
                return HttpResponseRedirect(reverse('dashboard'))
            else:
                return render(request, 'trip_app/main.html', {'login_form':login_form, 'signup_form':signup_form,
                    'password_not_match':"password_not_match"})
    return render(request, 'trip_app/main.html', {'login_form':login_form, 'signup_form':signup_form, 'invalid': "False"})


@login_required(login_url='login')
def dashboard(request):
    user = request.user
    trips = Trip.objects.filter(user=user)
    activities = Activity.objects.filter(trip=trips)
    if request.method == 'GET':
        trip_form = TripForm()
        activity_form = ActivityForm()

    elif 'add-btn' in request.POST:
        trip_form = TripForm(request.POST)
        activity_form = ActivityForm()
        if trip_form.is_valid():
            trip = Trip()
            trip.trip_name = trip_form.cleaned_data['trip_name']
            trip.trip_location = trip_form.cleaned_data['trip_location']
            trip.description = trip_form.cleaned_data['trip_desc']
            trip.start_date = trip_form.cleaned_data['trip_start_date']
            trip.end_date = trip_form.cleaned_data['trip_end_date']
            trip.total_expenses = 0
            trip.user = user
            trip.save()
            return HttpResponseRedirect(reverse('dashboard'))
   
    return render(request, 'trip_app/dashboard.html',{'user':user, 'trips':trips, 'activities':activities,
        'trip_form': trip_form, "activity_form": activity_form})


@login_required(login_url='login')
def signout(request):
    logout(request)
    return HttpResponseRedirect(reverse('home'))
