from .models import Story
from django.contrib.auth.views import LoginView
from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def story_index(request):
    stories = Story.objects.all()
    return render(request, 'stories/index.html', {'stories': stories})

def story_details(request, story_id):
    story = Story.objects.get(id=story_id)
    return render(request, 'stories/detail.html', {'story': story})

class StoryCreate(CreateView):
    model = Story
    fields = '__all__'
    success_url = '/stories/'

class StoryUpdate(UpdateView):
    model = Story
    fields = '__all__'

class StoryDelete(DeleteView):
    model = Story
    success_url = '/stories/'

class Home(LoginView):
    template_name = 'home.html'
