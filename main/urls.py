from django.urls import path
from . import views

urlpatterns = [
    path('', views.index.as_view(), name='index'),
    path('kapcsolat/', views.contactUs, name='contact-us'),
    path('mirol-irjak/', views.WhatAboutArticle.as_view(), name='what-about-article'),
    path('rolunk', views.AboutUs.as_view(), name='about-us'),
    path('munkatars/<str:pk>/', views.Collega.as_view(), name='munkatars'),
    path('csapatunk/', views.TeamView.as_view(), name='team-index'),
    path('cikkek/<str:pk>/', views.articles.as_view(), name='article-page'),
    path('cikk/<str:pk>/', views.article.as_view(), name='article'),
    path('kategoriak/', views.categoryPage, name='cats')
]
