from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, render_to_response
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse

from custom_auth.models import MyUser
from trip_app.models import Trip, Activity

from trip_app.forms import LoginForm, SignUpForm, TripForm, ActivityForm, ProfileForm

from datetime import datetime

from hashlib import sha1

# Create your views here.
def home(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect(reverse('dashboard', kwargs={"trip_id": 0}))
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
            return HttpResponseRedirect(reverse('dashboard', kwargs={"trip_id": 0}))

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
                return HttpResponseRedirect(reverse('dashboard', kwargs={"trip_id": 0}))
            else:
                return render(request, 'trip_app/main.html', {'login_form':login_form, 'signup_form':signup_form,
                    'password_not_match':"password_not_match"})
    return render(request, 'trip_app/main.html', {'login_form':login_form, 'signup_form':signup_form, 'invalid': "False"})



@login_required(login_url='login')
def dashboard(request, trip_id):
    user = request.user
    trips = Trip.objects.filter(user=user)
    activities = Activity.objects.filter(trip=trips)
    if request.method == 'GET':
        trip_form = TripForm()
        activity_form = ActivityForm()

    else:
        trip_form = TripForm(request.POST)
        activity_form = ActivityForm(request.POST)

    trip_id = trip_id
    return render(request, 'trip_app/dashboard.html',{'user':user, 'trips':trips, 'activities':activities,
        'trip_form': trip_form, "activity_form": activity_form, "trip_id": trip_id})


@login_required(login_url='login')
def add_trip(request):
    user = request.user
    if request.method == "POST":
        trip_form = TripForm(request.POST)
        if trip_form.is_valid():
            trip = Trip()
            trip.trip_name = trip_form.cleaned_data['trip_name']
            trip.trip_location = trip_form.cleaned_data['trip_location']
            trip.trip_description = trip_form.cleaned_data['trip_desc']
            trip.start_date = trip_form.cleaned_data['trip_start_date']
            trip.end_date = trip_form.cleaned_data['trip_end_date']
            trip.total_expenses = 0
            trip.user = user
            trip.save()
    return HttpResponseRedirect(reverse('dashboard', kwargs={"trip_id": trip.id}))


@login_required(login_url='login')
def trip_detail(request, trip_id):
    user = request.user
    if request.method == "POST":
        trip_form = TripForm(request.POST)
        if trip_form.is_valid():
            trip = get_object_or_404(Trip, id=trip_id)
            trip.trip_name = trip_form.cleaned_data['trip_name']
            trip.trip_location = trip_form.cleaned_data['trip_location']
            trip.trip_description = trip_form.cleaned_data['trip_desc']
            trip.start_date = trip_form.cleaned_data['trip_start_date']
            trip.end_date = trip_form.cleaned_data['trip_end_date']
            trip.save()
    return HttpResponseRedirect(reverse('dashboard', kwargs={"trip_id": trip_id}))



@login_required(login_url='login')
def delete_trip(request, trip_id):
    trip = get_object_or_404(Trip, id=trip_id)
    trip.delete()
    return HttpResponseRedirect(reverse('dashboard', kwargs={"trip_id": 0}))


@login_required(login_url='login')
def add_activity(request):
    user = request.user
    if request.method == "POST":
        activity_form = ActivityForm(request.POST)
        if activity_form.is_valid():
            activity = Activity()
            activity.trip = Trip.objects.get(pk=request.POST.get('trip_activ_id'))
            activity.activ_name = activity_form.cleaned_data['activ_name']
            activity.activ_location = activity_form.cleaned_data['activ_location']
            activity.activ_description = activity_form.cleaned_data['activ_description']
            activity.expenses = activity_form.cleaned_data['activ_expense']
            activity.start_datetime = activity_form.cleaned_data['activ_start_datetime']
            activity.end_datetime = activity_form.cleaned_data['activ_end_datetime']
            activity.save()
            trip_id = request.POST.get('trip_activ_id')
    return HttpResponseRedirect(reverse('dashboard', kwargs={"trip_id": trip_id}))



@login_required(login_url='login')
def edit_activity(request):
    user = request.user
    if request.method == "POST":
        activity_form = ActivityForm(request.POST)
        if activity_form.is_valid():
            activity_id = request.POST.get('trip_activ_id')
            activity = get_object_or_404(Activity, id=activity_id)
            activity.activ_name = activity_form.cleaned_data['activ_name']
            activity.activ_location = activity_form.cleaned_data['activ_location']
            activity.activ_description = activity_form.cleaned_data['activ_description']
            activity.expenses = activity_form.cleaned_data['activ_expense']
            activity.start_datetime = activity_form.cleaned_data['activ_start_datetime']
            activity.end_datetime = activity_form.cleaned_data['activ_end_datetime']
            activity.save()
            trip_id = request.POST.get('trip_activ_id')
    return HttpResponseRedirect(reverse('dashboard', kwargs={"trip_id": trip_id}))


@login_required(login_url='login')
def delete_activity(request, activ_id):
    activ = get_object_or_404(Activity, id=activ_id)
    trip_id = activ.trip.id
    activ.delete()
    return HttpResponseRedirect(reverse('dashboard', kwargs={"trip_id": trip_id}))


@login_required(login_url='login')
def profile(request):
    user = request.user
    profile_form = ProfileForm()
    return render(request, 'trip_app/profile.html',{'user':user, 'profile_form':profile_form})


@login_required(login_url='login')
def signout(request):
    logout(request)
    return HttpResponseRedirect(reverse('home'))