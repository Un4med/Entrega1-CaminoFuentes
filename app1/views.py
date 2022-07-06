from socketserver import _RequestType
from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

from .forms import FormPersona
from .models import Persona
from datetime import datetime

# Create your views here.
def vista(request):
    return render(request, 'index.html')

def crear_persona(request):

    if request.method =="POST":
        form= FormPersona(request.POST)
        if form.is_valid():
            data= form.cleaned_data 
            fecha= data.get('fecha_creacion')
            
            persona1= Persona(
                nombre=data.get('nombre'), 
                edad=data.get('edad'), 
                fecha_creacion= fecha if fecha else datetime.now() )
            persona1.save()
            
            return render(request, 'listado_personas.html', {})
        
    else:
         return render(request, 'crear_persona.html', {form})   
        
    form_persona= FormPersona()
    
    return render(request, 'crear_persona.html', {'form': form_persona})


