from django.shortcuts import render,redirect
from quiz import models
from django.contrib import messages
from django.contrib.auth.hashers import make_password

def index(request):
    return render(request,'quiz/index.html')

def save(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        password = request.POST['password']
    user = models.User.objects.filter(email=email).all()
    if not user:
        password = make_password(password)
        newUser = models.User(full_name=name,email=email,password=password)
        newUser.save()
        return redirect('login/')
    else:
        messages.success(request, "Email already exists!!")
        return redirect ("/")

def login(request):
    return render(request,'quiz/login.html')