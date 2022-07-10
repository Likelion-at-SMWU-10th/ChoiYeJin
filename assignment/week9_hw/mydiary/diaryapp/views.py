from django.shortcuts import get_object_or_404, render, redirect
from .models import Diary
from django.utils import timezone
from .forms import DiaryForm

# Create your views here.

def home(request):
    return render(request, 'diaryapp/home.html')

def myrecord(request):
    return render(request, 'diaryapp/myrecord.html')

def diary(request):
    diaries = Diary.objects
    return render(request, 'diaryapp/diary.html', {'diaries': diaries})

def detail(request, diary_id):
    diary_detail = get_object_or_404(Diary, pk = diary_id)
    return render(request, 'diaryapp/detail.html', {'diary': diary_detail})

def formcreate(request):
    if request.method == 'POST':
        form = DiaryForm(request.POST)
        if form.is_valid():
            post = Diary()
            post.title = form.cleaned_data['title']
            post.body = form.cleaned_data['body']
            post.pub_date = timezone.now()
            post.save()
            return redirect('diary')
    if request.method == 'GET':
        form = DiaryForm()
        return render(request, 'diaryapp/form_create.html', {'form':form})