from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=300)
    description = models.CharField(max_length=500)
    details = models.CharField(max_length=100000, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True, null=True)
    
    
    
#I need here the database of the calendar