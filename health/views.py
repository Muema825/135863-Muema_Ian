from bs4 import BeautifulSoup
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate , login , logout
from mental import settings
from django.core.mail import send_mail, EmailMessage
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes, force_str
from .tokens import generate_token
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.urls import reverse
import pandas as pd
from django.http import JsonResponse
import re
from django.contrib.auth.decorators import login_required
import keras
from keras.models import load_model  
import tensorflow as tf
from keras.preprocessing.sequence import pad_sequences
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.ensemble import VotingClassifier
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
ps = PorterStemmer()
from sklearn.ensemble import VotingClassifier
import joblib
import pickle
import json


# Create your views here.
# render index page
def home(request):
    return render(request, "health/index.html")

# render about us page
def about(request):
    return render(request, "health/about.html") 

 # render contacts page
def contact(request):
    return render(request, "health/contact.html")

# render departments page
def departments(request):
    return render(request, "health/departments.html")
# render doctors page
def doctors(request):
    return render(request, "health/doctors.html")
# Load the stop words
stop_words = set(stopwords.words('english'))

# Load the PorterStemmer
ps = PorterStemmer()

# Load the TF-IDF vectorizer
vectorizer = TfidfVectorizer()

# Load the VotingClassifier
VotingClassifiers = joblib.load('C:/Users/muema/Suicide_model.pkl')

    
# Your preprocessing functions
def preprocess(inp):
  inp = inp.lower()  # convert to lower case
  inp = inp.replace(r'[^\w\s]+', '')  # remove punctuations
  inp = [word for word in inp.split() if word not in (stop_words)]  # tokenize the sentence
  inp = ' '.join([ps.stem(i) for i in inp])  # stemming
  inputToModel = vectorizer.transform([inp]).toarray()  # transform to vector form
  return inputToModel
 


def Questionnaire(request):

    if request.method == 'POST':
        
        user_input = request.POST['user_input']
        processed_array = preprocess(user_input)
        predict = VotingClassifiers.predict(processed_array)
        
        feedback = predict[0]

        return render(request, 'health/Questionnaire.html', {'feedback': feedback})
    

    return render(request, 'health/Questionnaire.html')

def signup(request):
    
    if request.method == "POST":
        firstName = request.POST['firstName']
        lastName = request.POST['lastName']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirmPassword = request.POST['confirmPassword']
        

        if User.objects.filter(username=username):
            messages.error(request,"Username already exists")
            return redirect('home')

        if User.objects.filter(email=email):
            messages.error(request,"Email already exists")   
            return redirect('home') 
        
        if len(username)>10:
            messages.error(request, 'Username must be under 10 characters')

        if password != confirmPassword:
            messages.error(request, "Passwords do not match")    


        myuser = User.objects.create_user(username,email,password)
        myuser.first_name = firstName
        myuser.last_name = lastName
        myuser.is_active = False
        myuser.save()

        messages.success(request, "Your Account Has Been Created Successfully \n A confirmation message has been sent to your email, please confirm your email in order to activate your account")

        #Welcome Email Message

        subject = " Welcome to My Mental Health Website"
        message = "Hello" + myuser.first_name + "!!\n" + "Welcome to My Mental Health Website!! \n Thank you for visiting my website \n This is a confirmation email, please confirm your email address in order to activate your account. \n\n  Thank you for your time\n"
        from_email = settings.EMAIL_HOST_USER
        to_list = [myuser.email]
        send_mail(subject, message, from_email, to_list, fail_silently= True)

        # Email Address Confirmation Email

        current_site = get_current_site(request)
        email_subject = "Confirm Email For Mental Health Website"
        message2 = render_to_string('email_confirmation.html',{
            'name': myuser.first_name,
            'domain': current_site.domain,
            'uid': urlsafe_base64_encode(force_bytes(myuser.pk)),
            'token': generate_token.make_token(myuser),

        })

        email = EmailMessage(
            email_subject,
            message2,
            settings.EMAIL_HOST_USER,
            [myuser.email],
        )
        email.fail_silently = True
        email.send()

        return redirect('signin')
    
    return render(request, "health/signup.html")

def signin(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            firstName = user.first_name
            return render(request, "health/index.html",{'firstName': firstName})
        else:
            messages.error(request, "Wrong Credentials")
            return redirect("signin") 
    
    return render(request, "health/signin.html")

def signout(request):
    logout(request)
    messages.success(request,"logged out successfully")
    return redirect('signin')

def activate(request, uidb64, token):
        try:
            uid = force_str(urlsafe_base64_decode(uidb64))
            myuser = User.objects.get(pk=uid)
        except(TypeError, ValueError, OverflowError, User.DoesNotExist):
            myuser = None   

        if myuser is not None and generate_token.check_token(myuser, token):
            myuser.is_active = True
            myuser.save()
            login(request, myuser)
            return redirect('home')
        else:
            return render(request,'activation_failed.html')
        
def predict(request):
    return redirect(request,'health/Questionnaire.html')


def result(request):
    return render(request,'health/request.html')


