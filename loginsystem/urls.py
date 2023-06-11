from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('bejelentkezes/', views.loginPage, name='login'),
    path('kijelentkezes/', views.logoutUser, name='logout'),
    path('regiszracio/', views.register, name='register'),
    path('elfelejtett-jeszo/', views.forgottenPwd, name='forgotten'),
    path('profil/<str:pk>/', views.profilePage, name='profile-page'),
    path('profile-update/', views.profileUpdate, name='profile-update'),
    path('upload-article/', views.uploadArticle, name='upload-article'),
    path('user-article/<str:pk>', views.userArticlePage.as_view(), name='user-article'),
    path('delete/article/<str:pk>', views.deleteArticle, name='delete-article-main'),
    path('upload/article/<str:pk>', views.updateArticle, name='update-article-main'),
    path('all-articles/', views.allUserArticles, name="all-articles"),
    
    path('elfelejtett-jelszo/', auth_views.PasswordResetView.as_view(template_name="log/password_reset.html"), name="reset_password"),
    path('elfelejtett-jelszo-elkuldve/', auth_views.PasswordResetDoneView.as_view(template_name="log/password_reset_sent.html"), name='password_reset_done'),
    path('elfelejtett-jelszo/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='log/password_reset_form.html'), name='password_reset_confirm'),
    path('elfelejtett-jelszo-completed/', auth_views.PasswordResetCompleteView.as_view(template_name='log/password_reset_complete.html'), name='password_reset_complete'),
]
