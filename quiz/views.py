from django.shortcuts import render

def index(request):
    return render(request,'QandA_app/index.html')
