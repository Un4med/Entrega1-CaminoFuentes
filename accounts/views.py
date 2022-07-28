from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm

from accounts.models import ImagenUsuario
from .forms import NuevaCreacionUsuario, MiEditarPerfil
from django.contrib.auth import authenticate, login as login1
from django.contrib.auth.decorators import login_required

# Create your views here.
def login(request):
    if request.method =='POST':
        form= AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            usuario=form.cleaned_data.get('username')
            contraseña=form.cleaned_data.get('password')
            usuario1= authenticate(username=usuario, password=contraseña)
            
            if usuario1 is not None:
                login1(request, usuario1)
                return render(request, 'index.html', {})
            else:
                return render(request,'accounts/login.html', {'form':form})
        else:
           return render(request,'accounts/login.html', {'form':form}) 
    
    form= AuthenticationForm()
    return render(request,'accounts/login.html', {'form':form})

def registrar(request):
    if request.method == 'POST':
        form = NuevaCreacionUsuario(request.POST)
        if form.is_valid():
            form.save()
            return render(request,'index.html', {})
        else:
            return render(request, 'accounts/registrar.html', {'form':form})
    
    form= NuevaCreacionUsuario()
    return render(request, 'accounts/registrar.html', {'form':form})

@login_required
def perfil(request):
    return render(request, 'accounts/perfil.html/')

@login_required
def editar_perfil(request):
    
    user= request.user
    mi_editar_perfil, _ = ImagenUsuario.objects.get_or_create(user=user)
    if request.method == 'POST':
        form=  MiEditarPerfil(request.POST,request.FILES)
        if form.is_valid():
            data= form.cleaned_data
            user.first_name = data.get('first_name') if data.get('first_name') else user.first_name
            user.last_name = data.get('last_name') if data.get('last_name') else user.last_name
            user.email = data.get('email') if data.get('email') else user.email
            mi_editar_perfil.avatar = data.get('avatar') if data.get('avatar') else mi_editar_perfil.avatar
            
            if data.get('password1') and data.get('password1') == data.get('password2'):
                user.set_password (data.get('password1'))
            
            mi_editar_perfil.save()
            user.save()
            
            return redirect('perfil') 
   #       
        else:
            return render(request, 'accounts/editar_.html', {'form': form})
    
    form= MiEditarPerfil(
            initial= {
            'email': user.email, 'first_name': user.email, 
            'last_name': user.last_name, 'avatar': mi_editar_perfil.avatar}
             )
    
    return render(request, 'accounts/editar_perfil.html/', {'form': form})