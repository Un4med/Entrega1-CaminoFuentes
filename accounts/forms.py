import email
from socket import fromshare
from django import forms
from django.contrib.auth.forms import  UserCreationForm
from django.contrib.auth.models import User

class NuevaCreacionUsuario(UserCreationForm):
    
    username= forms.CharField(label='usuario', max_length=30)
    email= forms.EmailField()
    password1= forms.CharField(label= 'contraseña', widget=forms.PasswordInput)
    password2= forms.CharField(label= 'repetir contraseña', widget=forms.PasswordInput)
    
    

    class Meta:
        model = User
        fields = ['username','email', 'password1', 'password2']
        help_texts = {  key: '' for key in fields}
        
        
class MiEditarPerfil(forms.Form):
    
    email= forms.EmailField()
    first_name= forms.CharField(label='nombre', max_length=30, required= False)
    last_name= forms.CharField(label='apellido', max_length=30, required= False)
    password1= forms.CharField(label= 'contraseña', widget=forms.PasswordInput, required= False)
    password2= forms.CharField(label= 'repetir contraseña', widget=forms.PasswordInput, required= False)
    avatar= forms.ImageField(required= False)