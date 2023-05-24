from django.urls import path
from . import views

app_name = 'kakaomap'       # 네임스페이스 이름

urlpatterns = [
    path('kakaomap/', views.index, name='coopmap'),
    # path('locate/', views.locate, name='locate'),
]