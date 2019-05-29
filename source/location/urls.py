from django.conf.urls import url
from . import views
from django.urls import path, include
from location.views import LocationView

app_name = 'location'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    #path('location/',  LocationView.as_view(), name='location'),
    ]