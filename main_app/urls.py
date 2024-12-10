from django.urls import path
from . import views 

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('stories/', views.story_index, name='story-index'),
    path('stories/<int:story_id>', views.story_details, name='story-detail'),
]
