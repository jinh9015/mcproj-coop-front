from django.urls import path,include
from coop import views

app_name = 'coop'       # 네임스페이스 이름

urlpatterns = [
    path('',views.index, name='index'),     # name : url 별칭
    path('cooperation/', views.cooperation, name='cooperation'),
    path('locate/', views.locate, name='locate'),
    path('platform/', views.platform, name='platform'),
    path('cooperation/btn1_page/', views.btn1_page, name='btn1_page'),
    path('cooperation/btn2_page/', views.btn2_page, name='btn2_page'),
    path('cooperation/btn3_page/', views.btn3_page, name='btn3_page'),
    path('cooperation/btn4_page/', views.btn4_page, name='btn4_page'),
]
