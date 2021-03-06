from django.urls import path
from django.contrib import admin
from django.contrib.auth import views as auth_views

from f2kens import views as f2kens 
from frontend_token import views

urlpatterns = [
    path('', auth_views.login, {'template_name': 'login.html'}, name='login'),
    path('logout/', auth_views.logout, name='logout'),
    path('checking_user/', views.check_user_group_before_login, name='check_user'),
    path('preceptor/', views.index_preceptor, name='index_preceptor'),
    path('director/', views.index_director, name="index_director"),
    path('tutor/', views.index_tutor, name='index_tutor'),
    path('guard/', views.index_guard, name='index_guard'),
    path('profile/', views.profile, name="profile"),
]
	
