from django.forms import ModelForm
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Task
from loginsystem.models import ArticleUser
from creationboard.models import Article, Video

class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ('title', 'description', 'details')
        labels = {
            'title': '',
            'description': '',
            'details': ''
        }
        widgets = {
            'title': forms.TextInput(attrs={'class': 'input-design', 'placeholder': 'Title...*'}),
            'description': forms.TextInput(attrs={'class': 'input-design', 'placeholder': 'Desciption...*'}),
            'details': forms.TextInput(attrs={'class': 'input-design', 'placeholder': 'Details...'})
        }
        
class AdminUserArticle(ModelForm):
    class Meta:
        model = ArticleUser
        fields = ('status', )
        labels = {}
        widgets = {
            'status': forms.Select(attrs={'class': 'input-design'})
        }

class AdminArticle(ModelForm):
    class Meta:
        model = Article
        fields = ('status', )
        labels = {}
        widgets = {
            'status': forms.Select(attrs={'class': 'input-design'})
        }

class AdminVideo(ModelForm):
    class Meta:
        model = Video
        fields = ('status', )
        labels = {}
        widgets = {
            'status': forms.Select(attrs={'class': 'input-design'})
        }