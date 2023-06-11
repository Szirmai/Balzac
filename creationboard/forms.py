from django.forms import ModelForm
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Article, Category, Video, AboutUs, Team, WhatAboutArticle

choices = Category.objects.all().values_list('name', 'name')

choice_list = []

for item in choices:
    choice_list.append(item)

class ArticleForm(ModelForm):
    class Meta:
        model = Article
        fields = ('title', 'articletype', 'indeximg', 'category', 'body')
        labels = {
            'title': '',
            'articletype': '',
            'indeximg': '',
            'category': '',
            'body': '',
            #'author': '',
        }
        widgets = {
            'title': forms.TextInput(attrs={'class': 'input-design', 'placeholder': '*Title'}),
            #'author': forms.TextInput(attrs={'class': 'input-design', 'placeholder': '*Author'}),
            'articletype': forms.TextInput(attrs={'class': 'input-design', 'placeholder': '*Type of the article'}),
            'indeximg': forms.FileInput(attrs={'class': 'input-design'}),
            'category': forms.Select(choices=choice_list, attrs={'class': 'input-design', 'placeholder': '*Please select a category'}),
        }
          
class CategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = ('name',)
        labels = {
            'name': ''
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'input-design', 'placeholder': '*Install a Category'}),
        }
        
        
class AboutForm(ModelForm):
    class Meta:
        model = AboutUs
        fields = ('title', 'body')
        labels = {
            'title': '',
            'body': '',
        }
        widgets = {
            'title': forms.TextInput(attrs={'class': 'input-design', 'placeholder': '*The title goes here'}),
        }
        
class VideoForm(ModelForm):
    class Meta:
        model = Video
        fields = ('title', 'category', 'videocat', 'url', 'indeximg')
        labels = {
            'title': '',
            'category': '',
            'videocat': '',
            'url': '',
            'indeximg': '',
        }
        widgets = {
            'title': forms.TextInput(attrs={'class': 'input-design', 'placeholder': '*The title goes here'}),
            'category': forms.TextInput(attrs={'class': 'input-design', 'placeholder': '*The category goes here'}),
            'videocat': forms.TextInput(attrs={'class': 'input-design', 'placeholder': '*The video category goes here'}),
            'url': forms.URLInput(attrs={'class': 'input-design', 'placeholder': '*The link goes here'}),
            'indeximg': forms.FileInput(attrs={'class': 'input-design'}),
        }
        
class TeamForm(ModelForm):
    class Meta:
        model = Team
        fields = ('name', 'description',  'img', 'bio')
        labels = {
            'name': '',
            'description': '',
            'bio': '',
            'img': '',
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'input-design', 'placeholder': '*Title goes here'}),
            'img': forms.FileInput(attrs={'class': 'input-design'}), 
            'description': forms.TextInput(attrs={'class': 'input-design', 'placeholder': '*Title goes here'}),
        }
        
class WhatAboutArticleForm(ModelForm):
    class Meta:
        model = WhatAboutArticle
        fields = ('body', )
        labels = {
            
        }