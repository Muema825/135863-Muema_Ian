from django.contrib import admin
from django.urls import path , include
from .import views
from django.contrib.auth import views as auth_views
urlpatterns = [
   path('',views.home, name="home" ),
   path('signup', views.signup, name="signup"),
   path('signin', views.signin, name="signin"),
   path('signout', views.signout, name="signout"),
   path('about', views.about, name="about" ),
   path('contact', views.contact, name="contact"),
   path('departments', views.departments, name="departments"),
   path('doctors', views.doctors, name="doctors"),
   path('Questionnaire', views.Questionnaire, name="Questionnaire"),
   path('Questionnaire1', views.Questionnaire1, name="Questionnaire1"),
   path('Questionnaire2', views.Questionnaire2, name="Questionnaire2"),
   path('Questionnaire2', views.Questionnaire2, name="Questionnaire2"),
   path('Questionnaire3', views.Questionnaire3, name="Questionnaire3"),
   path('Questionnaire4', views.Questionnaire4, name="Questionnaire4"),
   path('activate/<uidb64>/<token>', views.activate, name="activate"),
 



]
