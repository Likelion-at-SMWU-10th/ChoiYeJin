from django.contrib import admin
from django.urls import path, include
from diaryapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('myrecord/', views.myrecord, name='myrecord'),
    path('diary/', views.diary, name='diary'),
    path('detail/<int:diary_id>', views.detail, name='detail'),
    path('recordkeeper/', include('recordkeeper.urls')),
    path('result', views.result, name='result'),
    path('accounts/', include('accounts.urls')),
    path('new/', views.new, name='new'),
    path('modelformcreate/', views.modelformcreate, name='modelformcreate'),
    path('edit/', views.edit, name='edit'),
    path('diaryupdate/<int:diary_id>', views.diaryupdate, name='diaryupdate'),
    path('diarydelete/<int:diary_id>', views.diarydelete, name='diarydelete'),
]