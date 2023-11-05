from django.db import models
from django.contrib.auth.models import  User, AbstractBaseUser, BaseUserManager , PermissionsMixin

'''
class Account(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    birthday = models.DateField() 
    gender = models.CharField(
        max_length=6,
        choices=[('MALE','MALE'),('FEMALE','FEMALE')]
    )
    phoneNumber = models.CharField(max_length=11)

    def __str__(self):
        return self.user.username
'''
    

class MentalHealthAssessment(models.Model):
    DateOfAssessment = models.DateField()
    Scores = models.IntegerField()
    Diagnosis = models.CharField(max_length=150)
    Username = models.CharField(max_length=150)
    Gender = models.CharField(max_length=10)

    def __str__(self):
        return self.Username

class MentalHealthDiagnosis(models.Model):
    
    Username = models.CharField(max_length=150)
    Gender = models.CharField(max_length=10)
    Diagnosis = models.CharField(max_length=150)
    Severity = models.IntegerField()
    Scores = models.IntegerField()

    def __str__(self):
        return self.Username






