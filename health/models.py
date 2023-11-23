from django.db import models
from django.contrib.auth.models import  User, AbstractBaseUser, BaseUserManager , PermissionsMixin , AbstractUser



GENDER_CHOICES = [
    ('male', 'Male'),
    ('female', 'Female'),
    # You can add more options here 
    ]


class MentalHealthAssessment(models.Model):

    Username = models.CharField(max_length=150)
    gender = models.CharField(max_length=6, choices= GENDER_CHOICES, default='', blank=True)
   # Verdict = models.CharField(max_length=150)
   
    

    def __str__(self):
        return self.Username






