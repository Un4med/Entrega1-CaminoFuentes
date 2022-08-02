from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.
class Publicaciones(models.Model):
    titulo = models.CharField(max_length=250)
    sub_titulo = models.CharField(max_length=250)
    contenido = RichTextField(null= True)
    autor = models.CharField(max_length=500)
    fecha_creacion= models.DateField(null=True)
    imagenes= models.ImageField(upload_to='imagenes', null=True, blank= True)
    
    
    def __str__(self):
        return f'{self.titulo} {self.titulo} {self. contenido}'
     
