from django.urls import path
from recordkeeper import views

urlpatterns = [
    path('', views.index, name='index'),  # recordkeeper/ 뒤에 아무것도 없을 때, index 함수 실행
    path('about/', views.about, name='about'),  # recordkeeper/about 일 때, about 함수 실행
]