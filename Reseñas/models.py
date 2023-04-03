from django.db import models
import uuid
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth.models import User

# Create your models here.
class Review(models.Model):
    titulo= models.CharField(max_length=70)
    subtitulo= models.CharField(max_length=70)
    cuerpo= RichTextUploadingField(null=True, blank=True)
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    imagen_portada = models.ImageField(null= True, blank=True, default ="defaultimage.jpg")
    creado_at= models.DateTimeField(auto_now_add=True)
    id= models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.titulo
    