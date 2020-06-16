from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='imagery-home'),
    path('about/', views.about, name='imagery-about'),
    path('resources/', views.resources, name='imagery-resources'),
    path('resource/', views.resource, name='imagery-resource'),
    path('projects/', views.projects, name='imagery-projects'),
    path('project/', views.project, name='imagery-project'),
]