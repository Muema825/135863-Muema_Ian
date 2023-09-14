from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from .views import home,register,login_user,otp_view,logout_user

urlpatterns = [
    path('',home,name="home"),
    path('register/',register,name='register'),
    path("login_user/",login_user,name="login_user"),
    path('otp/',otp_view, name='otp'),
    path('logout_user/',logout_user,name="logout_user" ),
]
