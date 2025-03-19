from django import forms
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Talk, Meeting, Archive, Website
from datetime import datetime
import sqlite3
# class EntryForm(forms.ModelForm):
#     class Meta:
#         model = Talk
#         fields = ['title', 'speaker']

def index(request):
    current_date = datetime.now().date()
    print('It is ' + str(current_date))
    specific_date = '2025-03-18'  # Replace with the desired date
    #1 is current, 2 is specified
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
    archives = Archive.objects.all()
    archive_websites = {
        book: Website.objects.filter(meeting_date=book.date) for book in archives
    }
    return render(request, 'archive.html', {'archive_websites':archive_websites})

def events(request):
    return render(request, 'events.html')

def projects(request):
    return render(request, 'projects.html')