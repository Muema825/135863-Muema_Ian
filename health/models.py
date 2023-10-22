from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager , PermissionsMixin

class CustomUserManager(BaseUserManager):

    def create_superuser(self, email, username, firstName, lastName, gender, phoneNumber, password, **other_fields):

    
        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_active', True)
        
        
       
        return self.create_user(email,username,firstName,lastName,gender,phoneNumber,password, **other_fields)
    
    def create_user(self, email, username, firstName, lastName, gender, phoneNumber, password, **other_fields):
        if not email:
            raise ValueError('Users must have an email address')
        if not username:
            raise ValueError('Users must have a username')
        if not firstName:
            raise ValueError('Users must have a first name')
        if not lastName:
            raise ValueError('Users must have a last name')
        if not gender:
            raise ValueError('Users must have a gender')
        if not phoneNumber:
            raise ValueError('Users must have a phone number')

        
        user = self.model(
            email=self.normalize_email(email),
            username=username,
            firstName=firstName,
            lastName=lastName,
            gender=gender,
            phoneNumber=phoneNumber,
            **other_fields
        )

        
        user.set_password(password)
        user.save()
        return user

    

class CustomUser(AbstractBaseUser,PermissionsMixin):
    email = models.EmailField(verbose_name='email address', max_length=255, unique=True)
    username = models.CharField(max_length=150, unique=True)
    firstName = models.CharField(max_length=150)
    lastName = models.CharField(max_length=150)
    gender = models.CharField(max_length=10)
    phoneNumber = models.CharField(max_length=20)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    
    

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username','firstName', 'lastName', 'gender', 'phoneNumber']

    def __str__(self):
        return self.username
    


    

class MentalHealthAssessment(models.Model):
    DateOfAssessment = models.DateField()
    Scores = models.IntegerField()
    Username = models.CharField(max_length=150)
    Gender = models.CharField(max_length=10)

    def __str__(self):
        return self.Username

class MentalHealthDiagnosis(models.Model):
    
    Username = models.CharField(max_length=150)
    Gender = models.CharField(max_length=10)
    Diagnosis = models.CharField(max_length=150)
    Severity = models.IntegerField()

    def __str__(self):
        return self.Username



    

