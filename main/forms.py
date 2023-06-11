from django.forms import ModelForm
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Impression, ContactUs
from creationboard.models import Category

choices = Category.objects.all().values_list('name', 'name')

choice_list = []

for item in choices:
    choice_list.append(item)

class ImpressionForm(ModelForm):
    class Meta:
        model = Impression
        fields = '__all__'
        
class ContactForm(ModelForm):
    class Meta:
        model = ContactUs
        fields = ('fullname', 'email', 'obj', 'body', 'cookieaccept')
        labels = {
            'fullname': '',
            'email': '',
            'obj': '',
            'body': '',
            'cookieaccept': '',
        }
        widgets = {
            'fullname': forms.TextInput(attrs={'class': 'first-input', 'placeholder': '* Teljes név...'}),
            'email': forms.EmailInput(attrs={'class': 'first-input', 'placeholder': '* E-mail...'}),
            'obj': forms.TextInput(attrs={'class': 'first-input', 'placeholder': '* Tárgy...'}),
            'body': forms.Textarea(attrs={'class': '', 'placeholder': '* Üzenet...'}),
            'cookieaccept': forms.CheckboxInput(attrs={'required': 'required'}),
        }
        
# class UploadArticleForm(ModelForm):
#     class Meta:
#         model = UploadArticle
#         fields = ('title', 'body', 'indeximg', 'category')
#         labels = {
#             'title': '',
#             'body': '',
#             'indeximg': '',
#             'category': '',
#         }
#         widgets = {
#             'title': forms.TextInput(attrs={'class': 'first-input', 'placeholder': '* Ide írd a címét'}),
#             'body': forms.Textarea(attrs={'placeholder': '* Ide írd a cikket (Mi megszerkesztjük!)'}),
#             'indeximg': forms.FileInput(attrs={'class': 'first-input'}),
#             'category': forms.Select(choices=choice_list, attrs={'class': 'first-input', 'placeholder': '*Please select a category'}),
#         }