from django.urls import path
from django.contrib import admin
from f2kens.views import check_user_group_before_login
from frontend_token.views import *
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', auth_views.login, {'template_name': 'login.html'}, name='login'),
    path('bye/', auth_views.logout, name='logout'),
    path('checking_user/', check_user_group_before_login, name='check_user'),
    path('main_preceptor/', index_preceptor, name='index_preceptor'),
    path('main_director/', index_director, name="index_director"),
    path('main_tutor/', index_tutor, name='index_tutor'),
    path('main_guard/', index_guard, name='index_guard'),
    path('get_f2/', get_forms2, name='get_f2'),
    path('modal_preceptor/', modalpre, name="modalpre")
]