from django.shortcuts import render, redirect, HttpResponse
from . import forms
from django.contrib.auth.decorators import login_required
from loginsystem.decorators import allowed_users
from django.contrib import messages
from django.views.generic import ListView, DeleteView

# Create your views here.

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin', 'editor'])
def home(request):
    return render(request, 'create/index.html')

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def aboutUs(request):
    form = forms.AboutForm()
    
    if request.method == "POST":
        form = forms.AboutForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('add')
        else:
            return HttpResponse('form is not valid')

    context = {'form': form}
    return render(request, 'create/about-form.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def cats(request):
    form = forms.CategoryForm()
    
    if request.method == "POST":
        form = forms.CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('add')
        else:
            return HttpResponse('form is not valid')

    context = {'form': form}
    return render(request, 'create/category-form.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin', 'editor'])
def add(request):
    return render(request, 'create/add.html')

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin', 'editor'])
def createArticle(request):
    if request.method == "POST":
        form = forms.ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            article = form.save(commit=False)
            article.user = request.user  # Assign the logged-in user instance
            article.save()
            return redirect('add')
        else:
            return HttpResponse('Valami nem jó!')
    else:
        form = forms.ArticleForm()
    
    context = {'form': form}
    return render(request, 'create/article-form.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def createAuthor(request):
    form = forms.WriterForm()
    
    if request.method == "POST":
        form = forms.WriterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('add')
        else:
            return HttpResponse('form is not valid')

    context = {'form': form}
    return render(request, 'create/create-author.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def team(request):
    form = forms.TeamForm()
    
    if request.method == "POST":
        form = forms.TeamForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('add')
        else:
            return HttpResponse('form is not valid')
        
    context = {'form': form}
    return render(request, 'create/team-form.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin', 'editor'])
def video(request):
    form = forms.VideoForm()

    if request.method == "POST":
        form = forms.VideoForm(request.POST, request.FILES)
        if form.is_valid():
            video = form.save(commit=False)
            video.user = request.user  # Set the current user to the user field of the Video instance
            video.save()
            return redirect('add')
        else:
            return HttpResponse('Form is not valid.')

    context = {'form': form}
    return render(request, 'create/video-form.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def whatAboutArticleForm(request):
    form = forms.WhatAboutArticleForm()
    
    if request.method == 'POST':
        form = forms.WhatAboutArticleForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'A feltöltés sikeres volt')
            return redirect('whaa-article')
        else:
            messages.info(request, 'Valami nem jó, reméltem, hogy ezt az üzenetet sosem kapd meg!')
        
    context = {'form': form}
    return render(request, 'create/whaa-form.html', context)