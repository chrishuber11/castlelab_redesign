from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def archive(request):
    return render(request, 'archive.html')

def events(request):
    return render(request, 'events.html')

def projects(request):
    return render(request, 'projects.html')