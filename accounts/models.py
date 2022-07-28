from pyexpat import model
from django.db import models
from django.contrib.auth.models import User


class ImagenUsuario(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar= models.ImageField(upload_to='avatares', null=True, blank= True)
