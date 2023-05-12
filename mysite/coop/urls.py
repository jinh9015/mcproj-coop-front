from django.urls import path,include
from coop import views

urlpatterns = [
    path('',views.index),
    path('cooperation/', views.index),
    path('locate/', views.locate),
    path('platform/', views.platform),
    path('login/', views.login),
    path('signup/', views.signup),
]
