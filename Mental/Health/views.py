from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User,auth
from django.contrib import messages
from .utils import send_otp
from datetime import datetime
import pyotp
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
    return render(request,"home.html")

def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST ['confirm_password']
        if password==confirm_password:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username exists')
                return redirect(register)
            if User.objects.filter(email=email).exists():
                messages.info(request, 'Email exists')
                return redirect(register)
            
            else:
                user = User.objects.create_user(username=username, password=password, email=email, first_name=first_name, last_name=last_name)
                user.set_password(password)
                user.save()
                print('success in registration')
                return redirect('login_user')
        else:
            messages.info(request,"Passwords are not matching")
            return redirect(register)
    else:
        print("No Post Method")    
        return render(request,'register.html')
    
def login_user(request):
    error_message = None
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            
            request.session['username'] = username
            return redirect('otp')
           # auth.login(request,user)
           # return redirect('home')
        else:
            messages.info(request,'Invalid Username or Password')
            return redirect('login_user')
    else:
         return render(request,'login.html')
    



def otp_view(request):
    error_message = None
    if request.method == 'POST':
        otp = request.POST['otp']
        username = request.session['username']

        otp_secret_key = request.session['otp_secret_key']
        otp_valid_until = request.session['otp_valid_date']

        if otp_secret_key and otp_valid_until is not None:
            valid_until = datetime.fromisoformat(otp_valid_until)

            if valid_until > datetime.now():
                totp = pyotp.TOTP(otp_secret_key, interval=60)
                if totp.verify(otp):
                    user= get_object_or_404(User, username=username)
                    login_user(request,user)

                    del request.session['otp_secret_key']
                    del request.session['otp_valid_date']

                    return redirect('home')
                else:
                    error_message='Invalid one time password'

            else:
               error_message='Invalid one time has expired' 

        else:
            error_message='Oops something went wrong:('          

    return render(request, 'otp.html', {'error_message':error_message})    

@login_required
def home(request):
    return render(request, 'home.html', {})




def logout_user(request):
    auth.logout(request)
    return redirect('home')

