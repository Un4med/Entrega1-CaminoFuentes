from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required

from .forms import BusquedaPersona, FormPersona
from .models import Persona
from datetime import datetime


# Create your views here.
def vista(request):
    return render(request, 'index.html')


def crear_persona(request):
    
    
    print(request.POST)
    
    if request.method =="POST":
        form= FormPersona(request.POST)
        if form.is_valid():
            data= form.cleaned_data 
            fecha= data.get('fecha_creacion')
            
            persona= Persona(
                nombre=data.get('nombre'), 
                edad=data.get('edad'), 
                fecha_creacion= fecha if fecha else datetime.now() )
            persona.save()
            
            listado_personas = Persona.objects.all()
            return redirect('listado_personas')
        
        else:
            return render(request, 'persona/crear_persona.html', {'form':form})   
        
    form_persona= FormPersona()
    
    return render(request, 'persona/crear_persona.html', {'form': form_persona})


def listado_persona(request):
    nombre_de_persona= request.GET.get('nombre')
    
    if nombre_de_persona: 
        listado_personas= Persona.objects.filter(nombre__icontains= nombre_de_persona)
    else:
        listado_personas= Persona.objects.all()
    
    form= BusquedaPersona()
    return render(request, 'persona/listado_personas.html', {'listado_personas': listado_personas,'form': form})


@login_required
def editar_persona(request, id):
    persona1= Persona.objects.get(id=id)
    
    if request.method == 'POST':
        form= FormPersona(request.POST)
        if form.is_valid():
            persona1.nombre = form.cleaned_data.get('nombre')
            persona1.edad = form.cleaned_data.get('edad')
            persona1.fecha_creacion = form.cleaned_data.get('fecha_creacion')
            persona1.save()
            
            return redirect('listado_personas') 
          
        else:
            return render(request, 'persona/editar_persona.html', {'form': form, 'persona': persona1})
    
    form_persona= FormPersona(initial={'nombre': persona1.nombre , 
                                       'edad': persona1.edad , 
                                       'fecha_creacion': persona1.fecha_creacion }) 
    
    return render(request, 'persona/editar_persona.html', {'form': form_persona,'persona': persona1 })


@login_required
def eliminar_persona(request, id):
    persona1= Persona.objects.get(id=id)
    persona1.delete() 

    return redirect('listado_personas')


def mostrar_persona(request, id):
    persona1= Persona.objects.get(id=id)
    
    return render(request, 'persona/mostrar_persona.html', {'persona':persona1}) 