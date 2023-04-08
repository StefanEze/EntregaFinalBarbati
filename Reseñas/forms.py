from django import forms
from django.forms import ModelForm
from .models import Review
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields ='__all__'
    
    def __init__(self,*args,**kwargs):
        super(ReviewForm,self).__init__(*args,**kwargs)
        self.fields['titulo'].widget.attrs.update({'class':'form-control'})
        self.fields['subtitulo'].widget.attrs.update({'class':'form-control'})
        self.fields['cuerpo'].widget.attrs.update({'class':'form-control'})
        self.fields['imagen_portada'].widget.attrs.update({'class':'form-control'})

