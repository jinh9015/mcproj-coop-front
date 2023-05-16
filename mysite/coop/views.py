from django.shortcuts import render
from django.http import HttpResponse

from .models import coop

# Create your views here.


def index(request):
    return render(request,'coop_cooperation')

def platform(request):
    return render(request,'coop_platform')

def locate(request):
    return render(request,'coop_locate')

def login(request):
    return render(request,'login')

def signup(request):
    return render(request,'signup')

def btn1_page(request):
    return render(request,'btn1_page')