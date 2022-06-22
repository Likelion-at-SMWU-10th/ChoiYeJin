
from django.shortcuts import render, get_object_or_404
from .models import Diary

# Create your views here.

def home(request):
    return render(request, 'diaryapp/home.html')

def myrecord(request):
    return render(request, 'diaryapp/myrecord.html')

def diary(request):
    diaries = Diary.objects
    return render(request, 'diaryapp/diary.html', {'diaries' : diaries})

def detail(request, diary_id):
    diary_detail = get_object_or_404(Diary, pk = diary_id)
    return render(request, 'diaryapp/detail.html', {'diary' : diary_detail})
