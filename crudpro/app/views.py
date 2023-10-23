from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
from django.contrib.auth.hashers import make_password,check_password


def index(request):
    return render(request,'index.html')

def registration(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        password = make_password(request.POST['password'])
        if User.objects.filter(email=email).exists():
            return HttpResponse('email already exist')
        elif User.objects.filter(phone=phone).exists():
            return HttpResponse('phone already exist')
        else:
            User.objects.create(name=name,email=email,phone=phone,password=password)
            return HttpResponse('user created successfully')
        

def table(request):
    data = User.objects.all() 
    return render(request,'table.html',{'data':data})

def delete(request,pk):
    User.objects.filter(pk=pk).delete()
    return redirect('/table/')
    

def update(request,uid):
    res = User.objects.get(id=uid)
    return render(request,'update.html',{'res':res})


def update_view(request):
    if request.method == 'POST':
        uid = request.POST['uid']
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        User.objects.filter(id=uid).update(name=name, email=email, phone=phone)
        return redirect('/table/')
    
def login(request):
    return render(request,'login.html')

def login_view(request):
    if request.method == 'POST':
        email = request.POST['email']
        user_password = request.POST['password']
        if User.objects.filter(email=email).exists():
            obj=User.objects.get(email=email)
            password=obj.password
            if check_password(user_password,password):
                return redirect('/table/')
            else:
                return HttpResponse('password incorrect')
        else:
            return HttpResponse('email does not register')
        