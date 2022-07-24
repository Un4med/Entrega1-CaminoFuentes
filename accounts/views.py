from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm
from .forms import NuevaCreacionUsuario
from django.contrib.auth import authenticate, login as login1

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