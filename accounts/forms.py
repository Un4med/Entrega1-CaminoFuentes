from django import forms
from django.contrib.auth.forms import  UserCreationForm
from django.contrib.auth.models import User

class NuevaCreacionUsuario(UserCreationForm):
    
    usuario= forms.CharField(label='usuario', max_length=30)
    email= forms.EmailField()
    contrasenia1= forms.CharField(label= 'contraseña', widget=forms.PasswordInput)
    contrasenia2= forms.CharField(label= 'repetir contraseña', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['usuario','email', 'contrasenia1', 'contrasenia2']
        help_texts = {  key: '' for key in fields}