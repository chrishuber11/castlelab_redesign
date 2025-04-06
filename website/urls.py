from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('archive/', views.archive, name='archive'),
    path('events/', views.events, name='events'),
    path('projects/', views.projects, name='projects'),
]

if settings.DEBUG:  # Only in development
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

