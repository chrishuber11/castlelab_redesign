from django.contrib import admin
from .models import Talk, Meeting, Website, Archive, Setting

@admin.register(Talk)
class TalkAdmin(admin.ModelAdmin):
    list_display = ('title', 'speaker', 'date','approved')

@admin.register(Meeting)
class TalkAdmin(admin.ModelAdmin):
    list_display = ('date', 'time', 'type')

@admin.register(Archive)
class TalkAdmin(admin.ModelAdmin):
    list_display = ('date', 'description', 'type')

@admin.register(Website)
class TalkAdmin(admin.ModelAdmin):
    list_display = ('url', 'meeting_date')
    
@admin.register(Setting)
class TalkAdmin(admin.ModelAdmin):
    list_display = ('setting', 'description','toggle')