from django.conf.urls import url, patterns

from . import views

app_name = 'trip_app'
urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^dashboard$', views.dashboard, name='dashboard'),
    url(r'^delete_trip(?P<trip_id>\d+)/$', views.delete_trip, name='delete_trip'),
    url(r'^delete_activity(?P<activ_id>\d+)/$', views.delete_activity, name='delete_activity'),
    url(r'^edit_activity$', views.edit_activity, name='edit_activity'),
    url(r'^profile$', views.profile, name='profile'),
    url(r'^signout$', views.signout, name='signout'),
    ]
