from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout,get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.mail import send_mail
from .models import CustomUser
import random
from django.contrib.auth.hashers import make_password
from django_password_history.models import UserPasswordHistory




# Create your views here.
User = get_user_model()

@login_required
def HomePage(request):
    messages.success(request, "You login successfully!!")
    return render (request, 'home.html')

def SignupPage(request):
    if request.method == 'POST':
        uname = request.POST.get('username')
        email = request.POST.get('email')
        pass1 = request.POST.get('password1')
        pass2 = request.POST.get('password2')
        security = request.POST.get('food')




        if len(pass1)<8:
        #    messages.error(request, 'Password is shorter than 8 Character')
           return redirect('hirad:signup')
           
        
        if not any(char.isupper() for char in pass1):
            # messages.error(request, "Password should contain at least one uppercase")
            return redirect('hirad:signup')
        
        if not any(char.islower() for char in pass1):
            # messages.error(request, "Password should contain at least one lowercase")
            return redirect('hirad:signup')
        
        if not any(char.isdigit() for char in pass1):
            # messages.error(request, "Password should contain at least one digit")
            return redirect('hirad:signup')


        if pass1 != pass2:
            return render (request, 'password.html')
        else:
            CustomUser=get_user_model()
            hashedpassword=make_password(pass1)

            my_user = CustomUser.objects.create(username=uname,email=email,password=hashedpassword,security=security)
            my_user.password_history.create(password=hashedpassword)
            return redirect('hirad:login')
    else:
        return render(request, 'signup.html')







def sendmail(mail,mailto):
    subject='otp password'
    messages=str(mail)
    from_email="bayathirad7@gmail.com"
    recipient_list=[mailto]

    send_mail(
        subject,
        messages,
        from_email,
        recipient_list,
        fail_silently=False

    )

def LoginPage(request):
    

    if request.method == 'POST':
        username = request.POST.get('username')
        pass1 = request.POST.get('pass')

        if username and pass1 is not None:
                
            user = authenticate(request, username = username, password = pass1)
            # user=User.objects.get(username=username)
          

            if user is not None:
                email=user.email
                Sentcode=verification_code()
                request.session['verificationcode']=Sentcode
                print(Sentcode)

                subject='2fa'
                messages=Sentcode
                from_email="bayathirad7@gmail.com"
                recipient_list=[email]

                send_mail(
                    subject,
                    messages,
                    from_email,
                    [email],
                    fail_silently=False

                )
                login(request, user)
                
                return redirect('hirad:verify',username=username)

            else:
                return render (request, 'login.html')
        else:
            return render (request, 'login.html')
            
    return render (request, 'login.html')




@login_required
def verify(request,username):
    user = request.user
    SecurityQuestion=user.security
    
    if user.is_authenticated:
        if request.method == 'POST':
            SecurityAnswer=request.POST.get('food')
            code=request.POST.get('code')
            storedcode=request.session.get('verificationcode')
            if code==storedcode and SecurityQuestion==SecurityAnswer:
                return redirect('hirad:home')
            else:
                return render (request, 'incorrectCode.html')
        else:
            return render(request,'verifycode.html')
    else:
        return redirect('hirad:login')


    
    
def verification_code():
    return str(random.randint(10000,999999))



def LogoutPage(request):
    logout(request)
    return redirect('hirad:login')