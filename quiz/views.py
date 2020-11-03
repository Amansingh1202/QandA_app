from django.shortcuts import render,redirect
from quiz import models
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required


def index(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        password = request.POST['password']
        try:
            user = User.objects.create_user(name,email,password)
            user.save()
        except:
            context = {}
            context['error'] = "Username already taken!!"
            return render(request,'quiz/index.html',context)
        return redirect('login/')
    else:
        return render(request,'quiz/index.html')

def login(request):
    if request.method == "GET":
        return render(request,'quiz/login.html')
    elif request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username,password=password)
        if user is not None:
            return render(request,'quiz/main.html')
        else:
            context = {}
            context['error'] = "Wrong Username or Password"
            return render(request,'quiz/login.html',context)

@login_required(login_url='login/')
def main(request):
    if request.method == "GET":
        return render(request,"quiz/main.html")

