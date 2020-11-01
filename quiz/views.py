from django.shortcuts import render,redirect
from quiz import models
from django.contrib import messages
from django.contrib.auth.hashers import check_password,make_password

def index(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        password = request.POST['password']
        user = models.User.objects.filter(email=email).all()
        if not user:
            newUser = models.User(full_name=name,email=email,   password=password)
            newUser.save()
            return redirect('login/')
        else:
            context = {}
            context['error'] = "Email already exists!!"
            return render(request,'quiz/index.html',context)
    elif request.method == "GET":
        return render(request,'quiz/index.html')

def login(request):
    if request.method == "GET":
        return render(request,'quiz/login.html')
    elif request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']
        user = models.User.objects.filter(email=email).first()
        if not user:
            context = {}
            context['error'] = "Wrong Email"
            return render(request,'quiz/login.html',context)
        else:
            password1 = user.password
            is_correct = (password1 == password)
            print(is_correct)
            if is_correct:
                return render(request,'quiz/main.html')
            else:
                context = {}
                context['error'] = "Wrong Password"
                return render(request,'quiz/login.html',context)


def main(request):
    if request.method == "GET":
        return render(request,"quiz/main.html")

