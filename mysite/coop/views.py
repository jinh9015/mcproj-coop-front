from django.shortcuts import render
from django.http import HttpResponse

from .models import coop

# Create your views here.


def index(request):
    return render(request,'coop/index.html')

def cooperation(request):
    return render(request,'coop/coop_cooperation.html')

def platform(request):
    return render(request,'coop/coop_platform.html')

# def locate(request):
#     return render(request,'coop/coop_locate.html')

# def login(request):
#     return render(request,'login.html')

# def signup(request):
#     return render(request,'signup.html')

def btn1_page(request):
    return render(request,'coop/btn1_page.html')

def btn2_page(request):
    return render(request,'coop/btn2_page.html')

def btn3_page(request):
    return render(request,'coop/btn3_page.html')

def btn4_page(request):
    return render(request,'coop/btn4_page.html')