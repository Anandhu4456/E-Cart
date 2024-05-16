from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from .models import Customer
from django.contrib import messages
# Create your views here.
def signout(request):
    logout(request)
    return redirect("home")

def account(request):
    context={}
    if request.POST and 'register' in request.POST:
        context['register']=True
        try:
            username= request.POST.get('username')
            phone = request.POST.get('phone')
            email= request.POST.get('email')
            password = request.POST.get('password')
            
            #create user account
            user= User.objects.create_user(
                username =username,
                email=email,
                password=password
            )
            
            # with this user object, have to create customer account
            Customer.objects.create(
                user=user,
                phone=phone
            )
            messages.success(request,"User successfully signed-up")
        except Exception as e:
            error_msg = "Duplicate username or invalid credentials"
            messages.error(request,error_msg)
    if request.POST and 'login' in request.POST:
        context['register']=False
        username = request.POST.get("username")
        password = request.POST.get("password")
        
        userExist = authenticate(request,username=username,password=password)
        if userExist:
            login(request,userExist)
            return redirect('home')
        else:
            error_msg = "User not found...Please register first or check credentials"
    return render(request,'account.html',context)