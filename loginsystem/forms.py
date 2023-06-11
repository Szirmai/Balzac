from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from .models import Profile, ArticleUser
from creationboard.models import Category

choices = Category.objects.all().values_list('name', 'name')

choice_list = []

for item in choices:
    choice_list.append(item)

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        labels = {
            'password1': '* Jelszó',
            'password2': '* Jelszó újra'
        }
        widgets = {
            'username': forms.TextInput(attrs={'class': 'first-input', 'placeholder': '* Felhasználónév'}),
            'email': forms.EmailInput(attrs={'class': 'first-input', 'placeholder': '* E-mail'}),
            'password1': forms.PasswordInput(attrs={'class': 'first-input', 'placeholder': '* Jelszó'}),
            'password2': forms.PasswordInput(attrs={'class': 'first-input', 'placeholder': '* jelszó újra'}),
        }
        
        
class UserUpdateForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email']
        labels = {
            
        }
        widgets = {
            'username': forms.TextInput(attrs={'class': 'first-input', 'placeholder': '* Új felhasználónév...'}),
            'email': forms.EmailInput(attrs={'class': 'first-input', 'placeholder': '* Új email...'}),
        }
        
        
class ProfileUpdateForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['img', 'bio', 'name']
        labels = {
            
        }
        widgets = {
            'img': forms.FileInput(attrs={'class': 'first-input'}),
            'bio': forms.Textarea(attrs={'class': '', 'placeholder': '* Bio'}),
            'name': forms.TextInput(attrs={'class': 'first-input', 'placeholder': '* Név'}),
        }
       
class UploadArticleForm(ModelForm):
    class Meta:
        model = ArticleUser
        fields =  ['body', 'indeximg', 'title', 'category']
        labels = {
            'indeximg': 'Index-kép:'
        }
        widgets = {
            'indeximg': forms.FileInput(attrs={'class': 'first-input'}),
            'title': forms.TextInput(attrs={'class': 'first-input', 'placeholder': '* Cím...'}),
            'category': forms.Select(choices=choice_list, attrs={'class': 'input-design', 'placeholder': '*Please select a category'}),
        }