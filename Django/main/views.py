from django.shortcuts import render
from django.http import HttpResponse
import MySQLdb
# Create your views here.

def home(request):
    conn = MySQLdb.connect("")
    return render(request, 'home.html')
