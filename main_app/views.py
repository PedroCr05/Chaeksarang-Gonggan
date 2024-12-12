from .models import Story
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

@login_required
def story_index(request):
    stories = Story.objects.filter(user=request.user)
    return render(request, 'stories/index.html', {'stories': stories})

@login_required
def story_details(request, story_id):
    story = Story.objects.get(id=story_id)
    return render(request, 'stories/detail.html', {'story': story})


class StoryCreate(LoginRequiredMixin, CreateView):
    model = Story
    fields = ['name', 'description', 'story', 'photo']

    def form_valid(self, form):
        form.instance.user = self.request.user 
        return super().form_valid(form)
    
    success_url = '/stories/'

class StoryUpdate(LoginRequiredMixin, UpdateView):
    model = Story
    fields = ['name', 'description', 'story', 'photo']

class StoryDelete(LoginRequiredMixin, DeleteView):
    model = Story
    success_url = '/stories/'

class Home(LoginView):
    template_name = 'home.html'

def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('story-index')
        else:
            error_message = 'Invalid sign up - try again'
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'signup.html', context)
