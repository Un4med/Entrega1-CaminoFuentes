from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from .models import Persona

# Create your views here.
def vista(request):
    return render(request, 'index.html')

def mi_lista(request):
    
    #template= loader.get_template('index.html')
    
    modelo1= Persona(nombre= 'fasolita')
    modelo2= Persona(nombre= 'rupestres')
    modelo3= Persona(nombre= 'rucula')
    modelo1.save()
    modelo2.save()
    modelo3.save()
    
    #render= template.render({'lista_objetos': [modelo1, modelo2, modelo3]})
    return render(request, 'mi_template.html', {'lista_objetos': [modelo1, modelo2, modelo3]})