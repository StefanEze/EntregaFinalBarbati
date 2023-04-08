from django.shortcuts import render,redirect
from Registro.forms import RegisterForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
# Create your views here.

def sign_up(request):
    if request.method =="POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('../Reseñas/')
    else:
        form= RegisterForm()
    
    return render(request,'registration/sign_up.html', {"form":form})