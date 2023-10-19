from django.contrib import admin
from django.urls import path , include
from .import views
urlpatterns = [
   path('',views.home, name="home" ),
   path('signup', views.signup, name="signup"),
   path('signin', views.signin, name="signin"),
   path('signout', views.signout, name="signout"),
   path('about', views.about, name="about" ),
   path('contact', views.contact, name="contact"),
   path('departments', views.departments, name="departments"),
   path('doctors', views.doctors, name="doctors"),
   path('activate/<uidb64>/<token>', views.activate, name="activate"), 
   

]
