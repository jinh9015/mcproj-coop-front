"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include     # (1) include 여기 선언
from coop import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),    # / 페이지에 해당하는 urlpatterns
    path('coop/', include('coop.urls')),    # (1) 페이지 요청을 coop/urls.py의 url 매핑으로 처리
    path('common/', include('common.urls')),
    path('kakaomap/', include('kakaomap.urls')),
    path('coopplatform/', include('coopplatform.urls')),
]
