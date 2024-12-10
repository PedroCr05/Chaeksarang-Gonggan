from django.shortcuts import render
from .models import Stories

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def story_index(request):
    stories = Stories.objects.all()
    return render(request, 'stories/index.html', {'stories': stories})

def story_details(request):
    stories = Stories.objects.get(id=story_id)
    return render(request, 'stories/detail.html', {'stories': stories})
