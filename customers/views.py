from django.shortcuts import render

# Create your views here.
def account(request):
    if request.POST and 'register' in request.POST:
        user= request.POST.get('username')
        phone = request.POST.get('phone')
        email= request.POST.get('email')
        password = request.POST.get('password')
    return render(request,'account.html')