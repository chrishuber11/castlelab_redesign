from django import forms
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Talk, Meeting, Archive, Website, Project, Event
from datetime import datetime
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def index(request):
    current_date = datetime.now().date()
    print('It is ' + str(current_date))
    specific_date = '2025-03-18'  # Replace with the desired date
    #1 is current, 2 is specified, 3 is next up
    use = 3
    if use == 1:
        meeting = Meeting.objects.filter(date=current_date).first()
        talks = Talk.objects.filter(date=current_date)
        return render(request, 'index.html', {'talks': talks, 'specific_date': current_date, 'meeting':meeting})
    elif use == 2:
        meeting = Meeting.objects.filter(date=specific_date).first()
        talks = Talk.objects.filter(date=specific_date)
        return render(request, 'index.html', {'talks': talks, 'specific_date': specific_date, 'meeting':meeting})
    elif use == 3:
        # Query for the next meeting on or after today
        meeting = Meeting.objects.filter(date__gte=current_date).order_by('date', 'time').first()
        next_available_date = meeting.date if meeting else None
        talks = Talk.objects.filter(date=next_available_date)
        print(next_available_date, 'Next Available Date')
        if meeting:
            print(f"Next meeting: {meeting}")
            print('Talks found, ', talks)
        else:
            print("No upcoming meetings found.")
        return render(request, 'index.html', {'talks': talks, 'specific_date': next_available_date, 'meeting':meeting})

def archive(request):
    archives = Archive.objects.all().order_by('-date') 
    # Pagination
    per_page = 8  # Number of meetings per page
    paginator = Paginator(archives, per_page)
    page_number = request.GET.get('page', 1)  # Get the current page number

    try:
        page_obj = paginator.page(page_number)
    except PageNotAnInteger:
        page_obj = paginator.page(1)
    except EmptyPage:
        page_obj = paginator.page(paginator.num_pages)

    # Create a dictionary for archive websites limited to the current page
    archive_websites = {
        book: Website.objects.filter(meeting_date=book.date) for book in page_obj
    }

    return render(request, 'archive.html', {'archive_websites': archive_websites, 'page_obj': page_obj})

def projects(request):
    projects = Project.objects.all().order_by('-start_date') 
    # Pagination
    per_page = 4  # Number of meetings per page
    paginator = Paginator(projects, per_page)
    page_number = request.GET.get('page', 1)  # Get the current page number

    try:
        page_obj = paginator.page(page_number)
    except PageNotAnInteger:
        page_obj = paginator.page(1)
    except EmptyPage:
        page_obj = paginator.page(paginator.num_pages)

    # Create a dictionary for archive websites limited to the current page
    # project_dict = {
    #     project: Project.objects.filter(start_date=project.start_date) for project in page_obj
    # }

    return render(request, 'projects.html', {'page_obj': page_obj})

def events(request):
    events = Event.objects.all().order_by('-date') 
    # Pagination
    per_page = 6  # Number of meetings per page
    paginator = Paginator(events, per_page)
    page_number = request.GET.get('page', 1)  # Get the current page number

    try:
        page_obj = paginator.page(page_number)
    except PageNotAnInteger:
        page_obj = paginator.page(1)
    except EmptyPage:
        page_obj = paginator.page(paginator.num_pages)

    # Create a dictionary for archive websites limited to the current page
    # event_dict = {
    #     events: Event.objects.filter(date=event.date) for event in page_obj
    # }

    return render(request, 'events.html', {'page_obj': page_obj})
