from django.conf.urls import url, patterns

from . import views

app_name = 'trip_app'
urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^dashboard$', views.dashboard, name='dashboard'),
    url(r'^signout$', views.signout, name='signout'),
    url(r'^hello/', 'trip_app.views.hello'),
    ]
