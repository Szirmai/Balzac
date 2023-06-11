from django.urls import path
from . import views

urlpatterns = [
    path('',  views.home, name='create-home'),
    path('aboutus/', views.aboutUs, name='aboutus-creation'),
    path('categories/', views.cats, name='create-categories'),
    path('add/', views.add, name='add'),
    path('article/', views.createArticle, name='create-article'),
    path('author/', views.createAuthor, name="author"),
    path('team/', views.team, name='team'),
    path('video', views.video, name='video'),
    path('bek-cikk-index/', views.whatAboutArticleForm, name='whaa-article'),
]