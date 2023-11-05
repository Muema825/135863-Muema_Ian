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

def Questionnaire(request):

    if request.POST.get('action') == 'post':

        Q1A = int(request. POST.get('Q1A'))
        Q2A = int (request.POST.get ('Q2A'))
        Q3A = int (request.POST.get ('Q3A'))
        Q4A = int (request.POST.get ('Q4A'))
        Q5A = int (request.POST.get ('Q5A'))
        Q6A = int (request.POST.get ('Q6A'))
        Q7A = int (request.POST.get ('Q7A'))
        Q8A= int (request.POST.get ('Q8A'))
        Q9A= int (request.POST.get ('Q9A'))
        Q10A= int (request.POST.get ('Q10A'))
        Q11A= int (request.POST.get ('Q11A'))
        Q12A= int (request.POST.get ('Q12A'))
        Q13A= int (request.POST.get ('Q13A'))
        Q14A= int (request.POST.get ('Q14A'))
        Q15A= int (request.POST.get ('Q15A'))
        Q16A= int (request.POST.get ('Q16A'))
        Q17A= int (request.POST.get ('Q17A'))
        Q18A= int (request.POST.get ('Q18A'))
        Q19A= int (request.POST.get ('Q19A'))
        Q20A= int (request.POST.get ('Q20A'))
        Q21A= int (request.POST.get ('Q21A'))
        Q22A= int (request.POST.get ('Q22A'))
        Q23A= int (request.POST.get ('Q23A'))
        Q24A= int (request.POST.get ('Q24A'))
        Q25A= int (request.POST.get ('Q25A'))
        Q26A= int (request.POST.get ('Q26A'))
        Q27A= int (request.POST.get ('Q27A'))
        Q28A= int (request.POST.get ('Q28A'))
        Q29A= int (request.POST.get ('Q29A'))
        Q30A= int (request.POST.get ('Q30A'))
        Q31A= int (request.POST.get ('Q31A'))
        Q32A= int (request.POST.get ('Q32A'))
        Q33A= int (request.POST.get ('Q33A'))
        Q34A= int (request.POST.get ('Q34A'))
        Q35A= int (request.POST.get ('Q35A'))
        Q36A= int (request.POST.get ('Q36A'))
        Q37A= int (request.POST.get ('Q37A'))
        Q38A= int (request.POST.get ('Q38A'))
        Q39A= int (request.POST.get ('Q39A'))
        Q40A= int (request.POST.get ('Q40A'))
        Q41A= int (request.POST.get ('Q41A'))
        Q42A= int (request.POST.get ('Q42A'))

        #Calculate the total score and display it on the page
        score = 0

        for i in range(1, 42):
            question_name = 'Q' + str(i) + 'A'
            answer = int(request.POST.get(question_name))
            score += answer
            
            model = pd.read_pickle("C:\\Users\\muema\\svm_model.pkl")

            result = model.predict([[score]])

            classification = result[0]

            return JsonResponse({'result': classification})

            PredResults.objects.create(classification=classification)

    return render(request, "health/Questionnaire.html")
   


def signup(request):
    
    if request.method == "POST":
        firstName = request.POST['firstName']
        lastName = request.POST['lastName']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirmPassword = request.POST['confirmPassword']
        phoneNumber = request.POST['phoneNumber']
        gender = request.POST['gender']

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


