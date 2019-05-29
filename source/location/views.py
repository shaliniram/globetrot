from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.views import generic
from .models import *
from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.conf import settings
import os,subprocess
from . import prints
from django.contrib.auth.models import User
from django.views.generic import TemplateView
# Create your views here.

def index(request):
    user = request.user
    if request.POST and 'current-location' in request.POST:
        print(request.POST)
        curloc = request.POST.get('current-location')
        distance = request.POST.get('distance')
        days = request.POST.get('days')
        budget = request.POST.get('Budget')
        r1= int(request.POST.get('reason1'))
        r2= int(request.POST.get('reason2'))
        r3= int(request.POST.get('reason3'))
        r4= int(request.POST.get('reason4'))
        r5= int(request.POST.get('reason5'))
        r6= int(request.POST.get('reason6'))
        r7= int(request.POST.get('reason7'))
        r8= int(request.POST.get('reason8'))
        findloc_ = userlocation(user=user,curloc=curloc,  radius=distance, days=days,budget=budget,reason1=r1, reason2=r2, reason3=r3,reason4=r4,reason5=r5,reason6=r6,reason7=r7,reason8=r8)
        findloc_.save()
        distance = int(distance)
        curloc = str(curloc).lower()
        outstr = prints.geek(distance, curloc,r1,r2,r3,r4,r5,r6,r7,r8)
        return render(request, 'location/selectlocation.html',{'cities':outstr,})
    if request.POST and 'location' in request.POST:
        location = request.POST.get('location')
        print(location)
        places_ = prints.apr(location)
        print(len(places_))
        return render(request, 'location/selectlocation1.html',{'cities':places_,})
    else:
        user = request.user
        print(user.email)
        return render(request, 'location/location.html')

class LocationView(TemplateView):
    template_name = 'location/location.html'