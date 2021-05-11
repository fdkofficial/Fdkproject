from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
#from shop.models import Post
def homepage(req):
    return render(req,"shop/hp.html")
def signup(req):
    if req.method == 'POST':
        FName=req.POST['FName']
        Email=req.POST['Email']
        Password=req.POST['Password']
        username=req.POST['Username']
        myuser=User.objects.create_user(username,Email,Password)
        myuser.first_name=FName
        myuser.save()
        messages.success(req,"You are a member")
        return redirect('/')
    return render(req,"shop/login.html")
def signin(req):
    if req.method == 'POST':
        Login_username=req.POST['loginUsername']
        Login_password=req.POST['LoginPassword']
        user = authenticate(username=Login_username,password=Login_password)
        if user is not None:
            login(req,user)
            messages.error(req,"You are logged in")
            return redirect('/')
        else:
            messages.error(req,'Incorrect Username/Password')
    return render(req,'shop/login.html')
def logout1(req):
    logout(req)
    messages.success(req,"You are logged out")
    return redirect('/')