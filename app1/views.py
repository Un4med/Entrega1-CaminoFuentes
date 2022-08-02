from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required

from .forms import FormPublicacion, BusquedaPublicacion
from .models import Publicaciones
from datetime import datetime


# Create your views here.
def vista(request):
    return render(request, 'index.html')

@login_required
def crear_publicaciones(request):
    
    if request.method =="POST":
        form= FormPublicacion(request.POST)
        if form.is_valid():
            data= form.cleaned_data 
            fecha= data.get('fecha_creacion')
            
            publicacion= Publicaciones(
                titulo=data.get('titulo'), 
                sub_titulo=data.get('sub_titulo'),
                contenido=data.get('contenido'),
                autor=data.get('autor'),
                imagenes=data.get('imagenes'),
                fecha_creacion= fecha if fecha else datetime.now() )
            publicacion.save()
            return redirect('listado_publicaciones')
        
        else:
            return render(request, 'persona/crear_publicacion.html', {'form':form})   
        
    form_publicacion= FormPublicacion()
    
    return render(request, 'persona/crear_publicacion.html', {'form': form_publicacion})


def listado_publicaciones(request):
    
    titulo_de_busqueda = request.GET.get('titulo')

    if titulo_de_busqueda:
        listado_publicaciones = Publicaciones.objects.filter(titulo__icontains=titulo_de_busqueda) 
    else:
        listado_publicaciones = Publicaciones.objects.all()

    form = BusquedaPublicacion()
    return render(request, 'persona/listado_publicaciones.html', {'listado_publicaciones': listado_publicaciones, 'form': form})

@login_required
def editar_publicaciones(request, id):
    publicaciones= Publicaciones.objects.get(id=id)
    
    if request.method == 'POST':
        form= FormPublicacion(request.POST, request.FILES)
        if form.is_valid():
            publicaciones.titulo = form.cleaned_data.get('titulo')
            publicaciones.sub_titulo = form.cleaned_data.get('sub_titulo')
            publicaciones.contenido = form.cleaned_data.get('contenido')
            publicaciones.autor = form.cleaned_data.get('autor')
            publicaciones.fecha_creacion = form.cleaned_data.get('fecha_creacion')
            publicaciones.imagenes= form.cleaned_data.get('imagenes')
            publicaciones.save()
            
            return redirect('listado_publicaciones') 
          
        else:
            return render(request, 'persona/editar_publicaciones.html', {'form': form, 'publicaciones': publicaciones})
    
    form_publicacion= FormPublicacion(initial={'titulo': publicaciones.titulo, 
                                       'sub_titulo': publicaciones.sub_titulo,
                                       'contenido': publicaciones.contenido,
                                       'autor': publicaciones.autor, 
                                       'fecha_creacion': publicaciones.fecha_creacion,
                                       'imagenes':publicaciones.imagenes})
    
    return render(request, 'persona/editar_publicaciones.html', {'form': form_publicacion,'publicaciones': publicaciones })


@login_required
def eliminar_publicaciones(request, id):
    publicacion1= Publicaciones.objects.get(id=id)
    publicacion1.delete() 

    return redirect('listado_publicaciones')


def mostrar_publicaciones(request,id): 
    publicacion1= Publicaciones.objects.get(id=id)
    return render(request, 'persona/mostrar_publicaciones.html', {'publicaciones': publicacion1}) 


def nosotros(request):
    return render(request, 'nosotros.html', {})