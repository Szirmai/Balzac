from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from ckeditor.fields import RichTextField
from django.contrib.contenttypes.fields import GenericRelation
from django.contrib.auth.models import User

STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
    )

class Category(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name
    class Meta:
        ordering = ['-id']

class Article(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True, null=True)
    updated = models.DateTimeField(auto_now=True, null=True)
    articletype = models.CharField(null=False, blank=False, max_length=100)
    body = RichTextUploadingField(max_length=1000000) #ez itt lehetne RichTextUploadingField is
    indeximg = models.ImageField(upload_to="images/", default="images/home9.jpg")
    category = models.CharField(max_length=100, null=False, blank=False)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['-created']
       

class Video(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True, null=True)
    update = models.DateTimeField(auto_now=True, null=True)
    indeximg = models.ImageField(upload_to="images/", default="images/home9.jpg")
    category = models.CharField(max_length=100, null=False, blank=False, default='Közélet')
    videocat = models.CharField(max_length=100, null=False, blank=False, default='Utcai Interview')
    url = models.URLField(max_length=400)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')
    
    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['-id']

class AboutUs(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    title = models.CharField(max_length=200, null=True, blank=False)
    body = RichTextUploadingField(max_length=1000000) #ez itt lehetne RichTextUploadingField is

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['-id']
        
class Team(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=True, blank=False)
    description = models.CharField(max_length=500, null=True, blank=False)
    bio = RichTextUploadingField(null=False, blank=False)
    img = models.ImageField( upload_to="images/", default="images/home9.jpg")

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['-id']
        
        
class WhatAboutArticle(models.Model):
    body = RichTextUploadingField(max_length=1000000)
    created = models.DateTimeField(auto_now_add=True, null=True)
    
    class Meta:
        ordering = ['-id']