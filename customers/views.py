from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from .models import Customer
from django.contrib import messages
# Create your views here.
def account(request):
    if request.POST and 'register' in request.POST:
        try:
            username= request.POST.get('username')
            phone = request.POST.get('phone')
            email= request.POST.get('email')
            password = request.POST.get('password')
            
            #create user account
            user= User.objects.create(
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
    return render(request,'account.html')