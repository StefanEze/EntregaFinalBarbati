from django.urls import path
from Registro import views

urlpatterns = [
    path('sign_up', views.sign_up, name="sign_up"),
]