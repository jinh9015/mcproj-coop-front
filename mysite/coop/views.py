from django.shortcuts import render
from django.http import HttpResponse

from .models import coop

# Create your views here.


def index(request):
    return render(request,'coop_cooperation.html')

def platform(request):
    return render(request,'coop_platform.html')

def locate(request):
    return render(request,'coop_locate.html')

def login(request):
    return render(request,'login.html')

def signup(request):
    return render(request,'signup.html')