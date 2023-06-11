from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from ckeditor_uploader.fields import RichTextUploadingField
from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    img = models.ImageField(upload_to="images/", default="images/home8.jpg")
    bio = models.CharField(null=True, max_length=1000000, default='Bio:')
    name = models.CharField(null=True, max_length=300)
    phone = models.CharField(max_length=15, blank=True, null=True)
    
    def __str__(self):
        return str(self.user.username)

    
def create_profile(sender, instance, created, **kwargs):
    if created:
        user_profile = Profile(user=instance)
        user_profile.save()
        
post_save.connect(create_profile, sender=User)

class ArticleUser(models.Model):
    
    STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
    )
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True, null=True)
    updated = models.DateTimeField(auto_now=True, null=True)
    body = RichTextUploadingField(max_length=1000000, null=True)
    indeximg = models.ImageField(upload_to="images/", default="images/home9.jpg")
    category = models.CharField(max_length=100, null=True, blank=False)
    title = models.CharField(max_length=200, null=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')
    
    def __str__(self):
        return str(self.title)
    
    class Meta:
        ordering = ['created']
