from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('archive/', views.archive, name='archive'),
    path('events/', views.events, name='events'),
    path('projects/', views.projects, name='projects'),
]

