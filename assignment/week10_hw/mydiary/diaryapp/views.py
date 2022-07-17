from django.shortcuts import get_object_or_404, render, redirect
from .models import Diary
from django.utils import timezone
from .forms import DiaryModelForm

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

def new(request):
    return render(request, 'diaryapp/new.html')

def modelformcreate(request):
    if request.method == 'POST':
        form = DiaryModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('diary')
    else:
        form = DiaryModelForm()
    return render(request, 'diaryapp/new.html', {'form':form})

def edit(request):
    return render(request, 'diaryapp/edit.html')

def diaryupdate(request, diary_id):
    post = get_object_or_404(Diary, pk=diary_id)
    if request.method == 'POST':
        form = DiaryModelForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('detail', diary_id=post.pk)
    else:
        form = DiaryModelForm(instance=post)
        return render(request, 'diaryapp/edit.html', {'form':form})

def diarydelete(request, diary_id):
    post = get_object_or_404(Diary, pk=diary_id)
    post.delete()
    return redirect('diary')