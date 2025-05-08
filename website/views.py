from django.shortcuts import render, redirect
from .models import Talk, Meeting, Archive, Website, Project, Event
from datetime import datetime
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib import messages
from datetime import datetime, timedelta
from django.utils.html import escape
import re
from django.core.validators import validate_email
from django.core.exceptions import ValidationError

def index(request):
    current_date = datetime.now().date()
    print('It is ' + str(current_date))
    # Query for the next meeting on or after today
    meeting = Meeting.objects.filter(date__gte=current_date).order_by('date', 'time').first()
    next_available_date = meeting.date if meeting else None
    talks = Talk.objects.filter(date=next_available_date)
    print('Next Available Date: ', next_available_date)
    
    # Retrieve submission count and last submission time from the session for Cooldown period
    submission_count = request.session.get('submission_count', 0)
    last_submission_time = request.session.get('last_submission_time')
    cooldown_period = timedelta(hours=4) #Cooldown period
    if last_submission_time:
        last_submission_time = datetime.fromisoformat(last_submission_time)  # Parse from ISO format
        if datetime.now() - last_submission_time > cooldown_period:
            # Reset the count if the cooldown period has passed
            submission_count = 0
            
    if meeting:
        print(f"Next meeting: {meeting}")
        print('Talks found, ', talks)
    else:
        print("No upcoming meetings found.")
    if request.method == 'POST':
        name = escape(request.POST.get('name'))
        title = escape(request.POST.get('title'))
        email = escape(request.POST.get('email'))
        #remove any special characters
        name = re.sub(r'[^a-zA-Z0-9\s]', '', name)
        title = re.sub(r'[^a-zA-Z0-9\s]', '', title)
        # Validate email format
        try:
            validate_email(email)
        except ValidationError:
            email = None  # Invalid emails become None
        if next_available_date:
            if submission_count >= 3:  # Limit submissions to 3 per 4 hours
                context = 'Submission limit reached. Try again later.'
                messages.error(request, context)
                return redirect('index')
            if name and title:
                Talk.objects.create(speaker=name, title=title, email=email if email else None, date=next_available_date, approved='No Decision')
                context = 'Talk submitted successfully!'
                messages.success(request, context)
                # Update the session with the new submission count and timestamp
                request.session['submission_count'] = submission_count + 1
                request.session['last_submission_time'] = datetime.now().isoformat()
                return redirect('index')
            elif name == '' and title == '' and email == '':
                context = ''
                messages.error(request, context)
                return redirect('index')
            else:
                context = 'Error: Please fill in all fields.'
                messages.error(request, context)
                return redirect('index')
        else:
            context = 'Please wait for a meeting to be planned before submitting a talk.'
            messages.error(request, context)
            return redirect('index')
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

    return render(request, 'events.html', {'page_obj': page_obj}) 
