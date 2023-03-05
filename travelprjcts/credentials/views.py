from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.
def register(request):
    if request.method=='POST':
        user=request.POST['name']
        fname=request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        pwd = request.POST['pwd']
        cpwd = request.POST['cpwd']
        if pwd==cpwd:
            if User.objects.filter(username=user).exists():
                messages.info(request,"Username already exist")
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, "email already exist")
                return redirect('register')
            else:
                user=User.objects.create_user(username=user,first_name=fname,last_name=lname,email=email,password=pwd)
                user.save();
                return redirect('login')

        else:
            messages.info(request, "password incorrect")
            return redirect('register')
        return redirect('/')
    return render(request,'register.html')
def login(request):
    if request.method=='POST':
        usern=request.POST['name']
        pwd=request.POST['pwd']
        user=auth.authenticate(username=usern,password=pwd)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,'invalid credentials')
            return redirect('login')
    return render(request,'login.html')
def logout(request):
    auth.logout(request)
    return redirect('/')