from django.shortcuts import render, redirect, HttpResponse
from . import forms
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from  .decorators import unauthenticated_user, allowed_users
from django.contrib.auth.models import Group
from django.contrib.auth.models import User
from . import forms
from creationboard import models
from .models import ArticleUser
from django.views.generic import ListView, View
# from .models import Profile, ArticleUser
# Create your views here.

@unauthenticated_user
def loginPage(request):
    if request.method == 'POST':
        username = request.POST["username"]
        password = request.POST["password"]
        
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            messages.success(request, 'Üdvözlünk a Balzak-on')
            return redirect('index')
        else:
            messages.info(request, 'Helytelen felhasználónév vagy jelszó')
    else:
        HttpResponse('Sztem próbáld újra néha szarakszik a rendszer')
    context = {}
    return render(request, 'log/login.html', context)

@unauthenticated_user
def register(request, *args, **kwargs):
    form = forms.CreateUserForm()
    
    if request.method == 'POST':
        form = forms.CreateUserForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            user = form.save(*args, **kwargs)
            
            group = Group.objects.get(name='customer')
            user.groups.add(group)
            print('fine')

            messages.success(request, 'Az fiók elészült ' + username + ' számára')
            return redirect('login')

    context = {'form': form}
    return render(request, 'log/register.html', context)

def logoutUser(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
def forgottenPwd(request):
    
    context = {}
    return render(request, 'log/forgotten-pwd.html', context)

def profilePage(request, pk):
    footarticle = models.Article.objects.all()[0:2]
    navcategory = models.Category.objects.all()[0:5]
    user = User.objects.get(username=pk)
    articles = user.articleuser_set.filter(status='approved').order_by('-created')
    teamArticles = user.article_set.filter(status='approved').order_by('-created')
        
    context = {'teamarticles': teamArticles,'user': user, 'articles': articles, 'category2': navcategory, 'article4': footarticle}
    return render(request, 'log/profile-page.html', context)

def allUserArticles(request):
    footarticle = models.Article.objects.all()[0:2]
    navcategory = models.Category.objects.all()[0:5]
    approved = request.user.articleuser_set.filter(status='approved').order_by('-created')
    pending = request.user.articleuser_set.filter(status='pending').order_by('-created')
    rejected = request.user.articleuser_set.filter(status='rejected').order_by('-created')
    
    context = {'approved': approved, 'category2': navcategory, 'article4': footarticle, 'pending': pending, 'rejected': rejected}
    return render(request, 'log/all-articles.html', context)

@login_required(login_url='login')
def profileUpdate(request):
    if request.method == 'POST':
        userUpdate = forms.UserUpdateForm(request.POST, instance=request.user)
        profileUpdate = forms.ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if userUpdate.is_valid() and profileUpdate.is_valid():
            userUpdate.save() and profileUpdate.save()
            messages.success(request, 'A frissítés sikeres volt')
            return redirect('profile-page', request.user)
        else:
            messages.info(request, 'A művelet valamilyen okból nem végrehajtható!')
    else:
        userUpdate = forms.UserUpdateForm(instance=request.user)
        profileUpdate = forms.ProfileUpdateForm(instance=request.user.profile)
        
    context = {'userupdate': userUpdate, 'profileupdate': profileUpdate}
    return render(request, 'log/profile-update.html', context)

@login_required(login_url='login')
def uploadArticle(request):
    form = forms.UploadArticleForm()
    if request.method == 'POST':
        form = forms.UploadArticleForm(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.save()
            messages.success(request, 'A cikk sikeresen fel lett töltve!')
            return redirect('profile-page', request.user)
        else:
            messages.info(request, 'Valami probláma volt a cikk elküldése során!')
    
    context = {'form': form}
    return render(request, 'log/upload-article.html', context)

@login_required(login_url='login')
def deleteArticle(request, pk):
    article = ArticleUser.objects.get(id=pk)
    if request.method == 'POST':
        article.delete()
        messages.success(request, 'The object has been deleted!')
        return redirect('profile-page', request.user)
        
    context = {'obj': article}
    return render(request, 'main/delete.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def updateArticle(request, pk):
    article = ArticleUser.objects.get(id=pk)
    form = forms.UploadArticleForm(instance=article)
    if request.method == 'POST':
        form = forms.UploadArticleForm(request.POST, request.FILES, instance=article)
        if form.is_valid():
            form.save()
            messages.success(request, 'A frissítés sikeres volt!')
            return redirect('profile-page', request.user)
        else:
            messages.info(request, 'Az eljárás nem foganatosítható!')
            
    context = {'form': form}
    return render(request, 'main/update-article-form.html', context)

class userArticlePage(View):
    template_name = "main/user-article.html"
    def dispatch(self, request, *args, **kwargs):
        footarticle = ArticleUser.objects.all()[0:2]
        navcategory = models.Category.objects.all()[0:5]
        article = ArticleUser.objects.get(title=kwargs['pk'])
        
        context = {'article': article, 'category2': navcategory, 'article4': footarticle,}
        return render(request, self.template_name, context)