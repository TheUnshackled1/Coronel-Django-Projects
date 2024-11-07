from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.models import User
from django.contrib import messages,auth
def register(request):
    if request.user.is_authenticated:
        return redirect('index')
    if request.method == "POST":  
        username = request.POST['username']
        password = request.POST['password']
        password2 = request.POST['password2']
        if password == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,"Username already taken")
                return redirect('register')
            else:
                user = User.objects.create_user(username=username,password=password)               
                user.save()
                messages.success(request, "User registered successfully")
                return redirect('login')
        else:
            messages.info(request, "Password not the same")
            return redirect('register')
    return render(request, 'register.html')
def login(request):
    if request.user.is_authenticated:
        return redirect('index')
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        if username and password:
            user = auth.authenticate(username=username, password=password)
            if user is not None:
                auth.login(request, user)
                return redirect('index')  
            else:
                messages.info(request, "Invalid username or password!")
                return redirect('login')  
        else:
            messages.info(request, "Username and Password are required!")
            return redirect('login')  
    return render(request, 'login.html')
def logout(request):
    auth.logout(request)
    return redirect('index')

def index(request):
    return render(request, 'index.html')
def about(request):
    return render(request,'about.html')
def menu(request):
    return render(request, 'menu.html')
def contact(request):
    return render(request, 'contact.html')
def news(request):
    return render(request, 'news.html')
def story(request):
    return render(request,'story.html')
def calcu(request):
    return render(request, 'calcu.html')