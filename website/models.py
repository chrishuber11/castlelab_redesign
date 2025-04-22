from django.db import models

class Talk(models.Model):
    date = models.DateField()
    title = models.CharField(max_length=40)
    speaker = models.CharField(max_length=40)
    email = models.CharField(max_length=40)
    
    YES = 'Yes'
    NO = 'No'
    NO_DECISION = 'No Decision'
    APPROVED_CHOICES = [
        (YES, 'Yes'),
        (NO, 'No'),
        (NO_DECISION, 'No Decision')
        ]
    approved = models.CharField(max_length=12,choices=APPROVED_CHOICES,default=NO_DECISION)
    
    class Meta:
        db_table = 'talks'

    def __str__(self):
        return f"{self.title} on {self.date} by {self.speaker}, approval= {self.approved}"
    
class Meeting(models.Model):
    date = models.DateField()
    time = models.TimeField()

    CASTLE = 'CASTLE'
    COMPETITION = 'Competition'
    SPEAKER = 'Speaker'
    OTHER = 'Other'
    TYPE_CHOICES = [
        (CASTLE, 'Castle'),
        (COMPETITION, 'Competition'),
        (SPEAKER, 'Speaker'),
        (OTHER, 'Other')
        ]
    type = models.CharField(max_length=12,choices=TYPE_CHOICES,default=CASTLE)
    class Meta:
        db_table = 'meetings'
    def __str__(self):
        return f"{self.type} Meeting on {self.date} at {self.time}"

class Archive(models.Model):
    date = models.DateField()
    description = models.CharField(max_length=100)

    CASTLE = 'CASTLE'
    COMPETITION = 'Competition'
    SPEAKER = 'Speaker'
    OTHER = 'Other'
    TYPE_CHOICES = [
        (CASTLE, 'Castle'),
        (COMPETITION, 'Competition'),
        (SPEAKER, 'Speaker'),
        (OTHER, 'Other')
        ]
    type = models.CharField(max_length=12,choices=TYPE_CHOICES,default=CASTLE)
    class Meta:
        db_table = 'archive'
    def __str__(self):
        return f"{self.type} Meeting on {self.date}, description: {self.description}"


class Website(models.Model):
    url = models.URLField()
    meeting_date = models.DateField()
    def __str__(self):
        return self.url
    class Meta:
        db_table = 'websites'
    def __str__(self):
        return f"({self.url}) for archive use on {self.meeting_date}"
    
class Setting(models.Model):
    setting = models.CharField(max_length=20)
    description = models.CharField(max_length=100)
    
    ON = 'On'
    OFF = 'Off'
    TOGGLE = [
        (ON, 'On'),
        (OFF, 'Off')
        ]
    toggle = models.CharField(max_length=3,choices=TOGGLE,default=OFF)
    
    class Meta:
        db_table = 'settings'

    def __str__(self):
        return f"{self.setting}, Description: {self.description}, Toggled: {self.toggle}"
    
class Project(models.Model):
    title = models.CharField(max_length=50)
    start_date = models.DateField()
    finish_date = models.DateField(blank=True, null=True)
    description = models.CharField(blank=True, max_length=400)
    github = models.URLField(blank=True)
    
    class Meta:
        db_table = 'projects'
    def __str__(self):
        return f"{self.title} Project"

class Event(models.Model):
    title = models.CharField(max_length=50)
    date = models.DateField()
    description = models.CharField(max_length=400)
    img = models.ImageField(upload_to='photos/', blank=True, null=True)
    
    class Meta:
        db_table = 'events'
    def __str__(self):
        return f"{self.title} Event"