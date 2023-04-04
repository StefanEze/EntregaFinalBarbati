from django.shortcuts import render, redirect
from Reseñas.models import *
from Reseñas.forms import *
from .forms import RegisterForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required


#-----------------Crear una reseña-----------------#
@login_required(login_url="/login")
def reviews(request):
    form=ReviewForm()
    if request.method =="POST":
        form = ReviewForm(request.POST, request.FILES)
        if form.is_valid():
            review = form.save(commit=False)
            review.autor = request.user
            form.save()
            form.autor = request.user
            return redirect('List')
    else:
        form = ReviewForm()

    context={'form':form}
    return render(request,'Reseñas/Reseñas/reseñas.html', context)
#-----------------Lista de reseñas-----------------#
@login_required(login_url="/login")
def list(request):
    reviews = Review.objects.all()
    context ={'reviews':reviews}
    return render(request,'Reseñas/Reseñas/list.html',context)
#-----------------Ver una reseña-----------------#
@login_required(login_url="/login")
def detalle(request,pk):
    review = Review.objects.get(id=pk)
    context = {'review':review}
    return render(request,"Reseñas/Reseñas/detalle.html", context)
#-----------------Editar una reseña-----------------#
@login_required(login_url="/login")
def updateReview(request, pk):
    review = Review.objects.get(id=pk)
    form = ReviewForm(instance=review)
    update = 1

    if request.method == "POST":
        form=ReviewForm(request.POST, request.FILES, instance=review)
        review.autor = request.user
        form.save()
        return redirect('List')

    context={"form":form,"update":update}
    return render(request,"Reseñas/Reseñas/reseñas.html", context)
#-----------------Eliminar una reseña-----------------#
@login_required(login_url="/login")
def deleteReview(request, pk):
    review = Review.objects.get(id=pk)
    if request.method =="POST":
        review.delete()
        return redirect('List')
    
    context={'review':review}

    return render(request,"Reseñas/Reseñas/confirm_delete.html", context)

@login_required(login_url="/login")
def inicio(request):
    return render(request,"Reseñas/inicio.html")

@login_required(login_url="/login")
def biografia(request):
    return render(request,"Reseñas/acercademi.html")

def sign_up(request):
    if request.method =="POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('Inicio')
    else:
        form= RegisterForm()
    
    return render(request,'registration/sign_up.html', {"form":form})