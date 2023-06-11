from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.contenttypes.fields import GenericRelation
from django.contrib.auth.models import User

      
class Impression(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True, null=True)
    updated = models.DateTimeField(auto_now=True, null=True)
    email = models.CharField(null=True, blank=False, max_length=100)
    object = models.TextField(null=True, blank=False)
    
    def __str__(self):
        return self.object
    
    class Meta:
        ordering = ['-created']
    
class ContactUs(models.Model):
    created = models.DateTimeField(auto_now_add=True, null=True)
    fullname = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    obj = models.CharField(max_length=400)
    body = models.CharField(max_length=1000000)
    cookieaccept = models.BooleanField(default=True)
    
    def __str__(self):
        return self.fullname
    
    class Meta:
        ordering = ['-created']
    
    