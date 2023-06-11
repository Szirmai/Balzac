from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Task
from .forms import TaskForm, AdminUserArticle, AdminArticle, AdminVideo
from loginsystem.decorators import allowed_users
from loginsystem import models
from django.contrib.auth.models import User, Group
from creationboard.models import Article, AboutUs, Video, Team, Category, WhatAboutArticle
from creationboard.forms import ArticleForm, AboutForm, VideoForm, TeamForm, WhatAboutArticleForm
from django.contrib import messages
from main.models import ContactUs
from django.core.exceptions import ObjectDoesNotExist

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def home(request):
    users = User.objects.all().order_by('-last_login')[0:7]
    user_count = User.objects.count()
    article_count = Article.objects.filter(status='approved').count()
    article = Article.objects.filter(status='pending')[0:2]
    videos = Video.objects.filter(status='pending')[0:2]
    videos_count = Video.objects.filter(status="approved").count()
    tasks = Task.objects.all()[0:7]
    tasks_count = Task.objects.count()
    mail_count = ContactUs.objects.count()
    pendingaritlce = Article.objects.filter(status='pending').count()
    pendingvideo = Video.objects.filter(status='pending').count()
    pendingua = models.ArticleUser.objects.filter(status='pending').count()
    
    context = {'pendingua':  pendingua, 'pendingvideo': pendingvideo, 'pendingarticle': pendingaritlce, 'tasks_count': tasks_count, 'mail_count': mail_count, 'users': users, 'user_count': user_count, 'article_count': article_count, 'articles': article, 'videos': videos, 'videos_count': videos_count, 'tasks': tasks}
    return render(request, 'dash/index.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def tasks(request):
    tasks = Task.objects.all().order_by('-id')[0:20]
    form = TaskForm()
    if request.method == 'POST':
        form = TaskForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'A frissítés sikeres volt!')
            return redirect('tasks')
        else:
            messages.info(request, 'Valami nem simmelt, próbáld újra vagy hívj ezen a számon: +36 70 941 4321')

    context = {'tasks': tasks, 'form': form}
    return render(request, 'dash/task.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def task(request, pk):
    task = Task.objects.get(id=pk)
    
    context = {'task': task}
    return render(request, 'dash/certain-task.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def taskPage(request):
    
    context = {}
    return render(request, 'dash/task.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def allUsers(request):
    users = User.objects.all().order_by('-last_login')[0:20]
    
    context = {'users': users}
    return render(request, 'dash/users.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def upload(request):
    article = Article.objects.all()[0:10]
    video = Video.objects.all()[0:10]
    aboutus = AboutUs.objects.all()[0:1]
    team = Team.objects.all()[0:20]
    whaaa = WhatAboutArticle.objects.all()[0:1]
    
    context = {'articles': article, 'videos': video, 'aboutuss': aboutus, 'teams': team, 'whaaa': whaaa}
    return render(request, 'dash/charts.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def updateArticleForm(request, pk):
    article = Article.objects.get(id=pk)
    form = ArticleForm(instance=article)
    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES, instance=article)
        if form.is_valid():
            form.save()
            messages.success(request, 'A frissítés sikeres volt!')
            return redirect('update')
        else:
            messages.info(request, 'Valami nem simmelt, próbáld újra vagy hívj ezen a számon: +36 70 941 4321')
            
    context = {'form': form}
    return render(request, 'dash/update-article-form.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def updateVideoForm(request, pk):
    video = Video.objects.get(id=pk)
    form = VideoForm(instance=video)
    if request.method == 'POST':
        form = VideoForm(request.POST, request.FILES, instance=video)
        if form.is_valid():
            form.save()
            messages.success(request, 'A frissítés sikeres volt!')
            return redirect('update')
        else:
            messages.info(request, 'Valami nem simmelt, próbáld újra vagy hívj ezen a számon: +36 70 941 4321')
            
    context = {'form': form}
    return render(request, 'dash/update-article-form.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def updateTeamForm(request, pk):
    team = Team.objects.get(id=pk)
    form = TeamForm(instance=team)
    if request.method == 'POST':
        form = TeamForm(request.POST, request.FILES, instance=team)
        if form.is_valid():
            form.save()
            messages.success(request, 'A frissítés sikeres volt!')
            return redirect('update')
        else:
            messages.info(request, 'Valami nem simmelt, próbáld újra vagy hívj ezen a számon: +36 70 941 4321')
            
    context = {'form': form}
    return render(request, 'dash/update-article-form.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def updateAboutForm(request, pk):
    about = AboutUs.objects.get(id=pk)
    form = AboutForm(instance=about)
    if request.method == 'POST':
        form = AboutForm(request.POST, request.FILES, instance=about)
        if form.is_valid():
            form.save()
            messages.success(request, 'A frissítés sikeres volt!')
            return redirect('update')
        else:
            messages.info(request, 'Valami nem simmelt, próbáld újra vagy hívj ezen a számon: +36 70 941 4321')
            
    context = {'form': form}
    return render(request, 'dash/update-article-form.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def updateWhaaForm(request, pk):
    whaa = WhatAboutArticle.objects.get(id=pk)
    form = WhatAboutArticleForm(instance=whaa)
    if request.method == 'POST':
        form = WhatAboutArticleForm(request.POST, request.FILES, instance=whaa)
        if form.is_valid():
            form.save()
            messages.success(request, 'A frissítés sikeres volt!')
            return redirect('update')
        else:
            messages.info(request, 'Valami nem simmelt, próbáld újra vagy hívj ezen a számon: +36 70 941 4321')
            
    context = {'form': form}
    return render(request, 'dash/update-article-form.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def updateTaskForm(request, pk):
    task = Task.objects.get(id=pk)
    form = TaskForm(instance=task)
    if request.method == 'POST':
        form = TaskForm(request.POST, request.FILES, instance=task)
        if form.is_valid():
            form.save()
            messages.success(request, 'A frissítés sikeres volt!')
            return redirect('task')
        else:
            messages.info(request, 'Valami nem simmelt, próbáld újra vagy hívj ezen a számon: +36 70 941 4321')
            
    context = {'form': form}
    return render(request, 'dash/update-article-form.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def deleteArticle(request, pk):
    article = Article.objects.get(id=pk)
    if request.method == 'POST':
        article.delete()
        messages.success(request, 'The object has been deleted!')
        return redirect('update')
        
    context = {'obj': article}
    return render(request, 'dash/delete.html', context)



@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def deleteVideo(request, pk):
    video = Video.objects.get(id=pk)
    if request.method == 'POST':
        video.delete()
        messages.success(request, 'The object has been deleted!')
        return redirect('update')
        
    context = {'obj': video}
    return render(request, 'dash/delete.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def deleteTeam(request, pk):
    team = Team.objects.get(id=pk)
    if request.method == 'POST':
        team.delete()
        messages.success(request, 'The object has been deleted!')
        return redirect('update')
        
    context = {'obj': team}
    return render(request, 'dash/delete.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def deleteTask(request, pk):
    task = Task.objects.get(id=pk)
    if request.method == 'POST':
        task.delete()
        messages.success(request, 'The object has been deleted!')
        return redirect('tasks')
        
    context = {'obj': task}
    return render(request, 'dash/delete.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def notYet(request):
    contact = ContactUs.objects.all()
    
    context = {'contact': contact}
    return render(request, 'dash/not-yet.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def contact(request, pk):
    contact = ContactUs.objects.filter(id=pk)
    
    context = {'contact': contact}
    return render(request, 'dash/contact.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def DeleteContact(request, pk):
    contact = ContactUs.objects.get(id=pk)
    if request.method == 'POST':
        contact.delete()
        messages.success(request, 'The object has been deleted!')
        return redirect('not-yet')
        
    context = {'obj': contact}
    return render(request, 'dash/delete.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def manage_groups(request):
    if request.method == 'POST':
        user_id = request.POST.get('user_id')
        user = User.objects.get(id=user_id)
        selected_groups = request.POST.getlist('groups')
        current_groups = user.groups.all()

        if 'remove' in request.POST:
            for group in current_groups:
                if group.name not in selected_groups:
                    user.groups.remove(group)

            messages.success(request, 'User groups updated successfully.')
            return redirect('groups')

        elif 'save' in request.POST:
            try:
                for group_id in selected_groups:
                    group = Group.objects.get(id=group_id)
                    user.groups.add(group)
                for group in current_groups:
                    if group.id not in selected_groups:
                        user.groups.remove(group)
            except ObjectDoesNotExist:
                messages.error(request, 'Invalid group ID. Please select valid groups.')

            messages.success(request, 'User groups updated successfully.')
            return redirect('groups')

    users = User.objects.all()
    groups = Group.objects.all()
    context = {'users': users, 'groups': groups}
    return render(request, 'dash/groups.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def manageArticle(request):
    context = {}
    return render(request, 'dash/manage-user-articles.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def ApprovedAllow(request, pk):
    form = AdminUserArticle(instance=instance)
    instance = models.ArticleUser.objects.all()
    context = {'form': form}
    return render(request, 'dash/approved.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def Approved(request):
    articles = models.ArticleUser.objects.filter(status='approved').order_by('-created')
    
    context = {'articles': articles}
    return render(request, 'dash/pre-manage-article.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def Rejected(request):
    articles = models.ArticleUser.objects.filter(status='rejected').order_by('-created')
    
    context = {'articles': articles}
    return render(request, 'dash/pre-manage-article.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def Pending(request):
    articles = models.ArticleUser.objects.filter(status='pending').order_by('-created')
    
    context = {'articles': articles}
    return render(request, 'dash/pre-manage-article.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def editUserArticleStatus(request, pk):
    article = models.ArticleUser.objects.get(title=pk)
    form = AdminUserArticle(instance=article)
    if request.method == 'POST':
        form = AdminUserArticle(request.POST, instance=article)
        if form.is_valid():
            form.save()
            messages.success(request, 'The object\'s status has been updated!')
            return redirect('manage-article')
        else:
            messages.info(request, 'Someting wasn\'t as good as I expected. Try again!')
    
    
    context = {'articleuser': article, 'form': form}
    return render(request, 'dash/change-user-article-status.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def Vau(request):
    
    context = {}
    return render(request, 'dash/vau.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def ChoosePending(request):
    
    return render(request, 'dash/ChoosePending.html')

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def LocalVideo(request):
    
    return render(request, 'dash/local-video.html')

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def LocalArticle(request):
    
    return render(request, 'dash/local-article.html')

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def ArticlePending(request):
    articles = Article.objects.filter(status='pending')
    
    context = {'articles': articles}
    return render(request, 'dash/article-pending.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def ArticleRejected(request):
    articles = Article.objects.filter(status='rejected')
    
    context = {'articles': articles}
    return render(request, 'dash/article-pending.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def ArticleApproved(request):
    articles = Article.objects.filter(status='approved')
    
    context = {'articles': articles}
    return render(request, 'dash/article-pending.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def VideoRejected(request):
    videos = Video.objects.filter(status='rejected')
    
    context = {'videos': videos}
    return render(request, 'dash/video-pending.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def VideoApproved(request):
    videos = Video.objects.filter(status='approved')
    
    context = {'videos': videos}
    return render(request, 'dash/video-pending.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def VideoPending(request):
    videos = Video.objects.filter(status='pending')
    
    context = {'videos': videos}
    return render(request, 'dash/video-pending.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def ChangeArticleStatus(request, pk):
    article = Article.objects.get(id=pk)
    form = AdminArticle(instance=article)
    if request.method == 'POST':
        form = AdminArticle(request.POST, instance=article)
        if form.is_valid():
            form.save()
            messages.success(request, 'The object\'s status has been updated!')
            return redirect('local-article')
        else:
            messages.info(request, 'Someting wasn\'t as good as I expected. Try again!')
    
    
    context = {'articleuser': article, 'form': form}
    return render(request, 'dash/change-article-status.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def ChangeVideoStatus(request, pk):
    video = Video.objects.get(id=pk)
    form = AdminVideo(instance=video)
    if request.method == 'POST':
        form = AdminVideo(request.POST, instance=video)
        if form.is_valid():
            form.save()
            messages.success(request, 'The object\'s status has been updated!')
            return redirect('local-video')
        else:
            messages.info(request, 'Someting wasn\'t as good as I expected. Try again!')
    
    
    context = {'video': video, 'form': form}
    return render(request, 'dash/change-video-status.html', context)