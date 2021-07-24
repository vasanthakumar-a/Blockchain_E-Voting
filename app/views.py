from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request,'index.html')

def userLogin(request):
    return render(request,'userLogin.html')

def userRegister(request):
    return render(request,'userRegister.html')

def adminLogin(request):
    return render(request, 'adminLogin.html')