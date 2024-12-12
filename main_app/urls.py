from django.urls import path
from . import views 

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('stories/', views.story_index, name='story-index'),
    path('stories/<int:story_id>', views.story_details, name='story-detail'),
    path('stories/create/', views.StoryCreate.as_view(), name='story-create'),
    path('stories/<int:pk>/update/', views.StoryUpdate.as_view(), name='story-update'),
    path('stories/<int:pk>/delete/', views.StoryDelete.as_view(), name='story-delete'),
]
