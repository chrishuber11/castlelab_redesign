from django.db import models

class Talk(models.Model):
    date = models.CharField(max_length=10)
    title = models.CharField(max_length=20)
    speaker = models.CharField(max_length=30)
    
    class Meta:
        db_table = 'talks'

    def __str__(self):
        return self.title