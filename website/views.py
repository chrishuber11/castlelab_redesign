from django.shortcuts import render
from .models import Talk

def index(request):
    specific_date = '3/4/2025'  # Replace with the desired date
    talks = Talk.objects.filter(date=specific_date)
    return render(request, 'index.html', {'talks': talks, 'specific_date': specific_date})

def archive(request):
    return render(request, 'archive.html')

def events(request):
    return render(request, 'events.html')

def projects(request):
    return render(request, 'projects.html')