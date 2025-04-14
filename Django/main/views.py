from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from django.views.generic import ListView
from .models import pmsReadings

from collections import Counter
from math import ceil 

# Create your views here.

def home(request):
    return render(request, 'home.html')

def index(request):
    stats = pmsReadings.objects.orderby('time')
    
    data={
        "pm10": 10,
        "pm25": 25,
        "pm100": 100,
    }
    return JsonResponse(data)

def chart_view(request):
    return render(request, "graph.html")

