from django.urls import path,include
from coop import views

app_name = 'coop'       # 네임스페이스 이름

urlpatterns = [
    path('',views.index, name='index'),     # name : url 별칭
    path('cooperation/', views.index, name='cooperation'),
    path('locate/', views.locate, name='locate'),
    path('platform/', views.platform, name='platform'),
]
