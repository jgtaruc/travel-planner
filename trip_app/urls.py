from django.conf.urls import url, patterns

from . import views

app_name = 'trip_app'
urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^dashboard$', views.dashboard, name='dashboard'),
    url(r'^delete_trip(?P<trip_id>\d+)/$', views.delete_trip, name='signout'),
    url(r'^profile$', views.profile, name='profile'),
    url(r'^signout$', views.signout, name='signout'),
    ]
