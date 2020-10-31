from django.shortcuts import render,redirect
from quiz import models

def index(request):
    return render(request,'quiz/index.html')

def save(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        password = request.POST['password']
    user = models.User.objects.filter(email=email).all()
    if not user:
        newUser = models.User(full_name=name,email=email,password=password)
        newUser.save()
        return redirect('login/')
    else:
        args = {}
        args['error'] = "Email already exists!!"
        return render(request,'quiz/index.html',args)

def login(request):
    return render(request,'quiz/login.html')