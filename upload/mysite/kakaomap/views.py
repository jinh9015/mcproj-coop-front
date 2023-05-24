from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request,'kakaomap/map.html')

# def locate(request):
#     return render(request,'coop/coop_locate.html')