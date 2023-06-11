from django.shortcuts import render, redirect, HttpResponse
from . import models
from creationboard import models
from .forms import ContactForm
from django.contrib.auth.models import User
from . import forms
from django.contrib import messages
from django.views.generic import ListView, View
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from loginsystem.models import ArticleUser

class index(View):
    template_name = "main/index.html"
    
    def get(self, request,  *args, **kwargs):
        WelcomeArticle = models.Article.objects.filter(status='approved')[0:1]
        footarticle = models.Article.objects.filter(status='approved')[0:2]
        sidearticle = models.Article.objects.filter(status='approved')[4:7]
        picsidearticle = models.Article.objects.filter(status='approved')[1:4]
        category = models.Category.objects.all()[0:9]
        navcategory = models.Category.objects.all()[0:5]
        video1 = models.Video.objects.filter(status='approved')[0:2]
        video2 = models.Video.objects.filter(status='approved')[2:4]
        video3 = models.Video.objects.filter(status='approved')[4:8]
        video4 = models.Video.objects.filter(status='approved')[0:5]
        article5 = models.Article.objects.filter(status='approved')[1:4]
        article8 = models.Article.objects.filter(status='approved')[4:6]
        article9 = models.Article.objects.filter(status='approved')[6:8]
        article6 = models.Article.objects.filter(status='approved')[8:10]
        article7 = models.Article.objects.filter(status='approved')[10:12]
        context = {'video1': video1,
                'video2': video2,
                'video3': video3,
                'article1': WelcomeArticle,
                'article2': sidearticle,
                'article3': picsidearticle,
                'article4': footarticle,
                'category1': category,
                'category2': navcategory,
                'video4': video4,
                'article5': article5,
                'article6': article6,
                'article7': article7,
                'article8': article8,
                'article9': article9,
                }
        
        return render(request, self.template_name, context)
    
    
class articles(View):
    template_name = "main/topic.html"
    def dispatch(self, request, *args, **kwargs):
        footarticle = models.Article.objects.filter(status='approved')[0:2]
        navcategory = models.Category.objects.all()[0:5]
        url = models.Article.objects.filter(category=kwargs['pk'])
        
        # user_url = ArticleUser.objects.filter(category=kwargs['pk'])
        user_url = ArticleUser.objects.filter(status='approved')
        
        context = {'url': url, 'category': kwargs['pk'], 'category2': navcategory, 'article4': footarticle, "url1": user_url,}
        return render(request, self.template_name, context)

class article(View):
    template_name = "main/article.html"
    def dispatch(self, request, *args, **kwargs):
        footarticle = models.Article.objects.filter(status='approved')[0:2]
        navcategory = models.Category.objects.all()[0:5]
        article = models.Article.objects.get(id=kwargs['pk'])
        
        context = {'article': article, 'category2': navcategory, 'article4': footarticle,}
        return render(request, self.template_name, context)

def contactUs(request):
    footarticle = models.Article.objects.filter(status='approved')[0:2]
    navcategory = models.Category.objects.all()[0:5]
    form = ContactForm()

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Köszönjük, üzenetedet fogadtuk!')
            return redirect('index')
        else:
            messages.error(request, 'Az üzenet küldése sikertelen volt. Kérjük, próbáld újra!')
        
    context = {'form': form, 'category2': navcategory, 'article4': footarticle}
    return render(request, 'main/contact-us.html', context)

class WhatAboutArticle(View):
    template_name = 'main/what-about-article.html'
    
    def get(self, request):
        footarticle = models.Article.objects.filter(status='approved')[0:2]
        navcategory = models.Category.objects.all()[0:5]
        whaa = models.WhatAboutArticle.objects.all()[0:1]
        context = {'category2': navcategory, 'article4': footarticle, 'whaa': whaa}
        return render(request, self.template_name, context)


class AboutUs(View):
    template_name = "main/about-us.html"

    def get(self, request):
        footarticle = models.Article.objects.filter(status='approved')[0:2]
        navcategory = models.Category.objects.all()[0:5]
        about = models.AboutUs.objects.all()[0:1]

        context = {'category2': navcategory, 'article4': footarticle, 'about': about}
        return render(request, self.template_name, context)

class TeamView(View):
    template_name = "main/team-members.html"
    
    def get(self, request):
        footarticle = models.Article.objects.filter(status='approved')[0:2]
        navcategory = models.Category.objects.all()[0:5]
        teams = models.Team.objects.all()[0:9]
        context = {'category2': navcategory, 'article4': footarticle, 'teams': teams}
        return render(request, self.template_name, context)

class Collega(View):
    template_name = "main/munkatars.html"

    def get(self, request, pk):
        footarticle = models.Article.objects.filter(status='approved')[0:2]
        navcategory = models.Category.objects.all()[0:5]
        team = models.Team.objects.get(id=pk)

        context = {'category2': navcategory, 'article4': footarticle, 'team': team}
        return render(request, self.template_name, context)
    
def categoryPage(request):
    navcategory = models.Category.objects.all()[0:5]
    footarticle = models.Article.objects.filter(status='approved')[0:2]
    category = models.Category.objects.all()
    
    context = {'cats': category, 'category2': navcategory, 'article4': footarticle,}
    return render(request, 'main/cats.html', context)

