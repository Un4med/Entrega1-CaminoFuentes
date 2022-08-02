from django import forms
from ckeditor.fields import RichTextFormField

class FormPublicacion(forms.Form):
    titulo = forms.CharField(max_length=250)
    sub_titulo = forms.CharField(max_length=250)
    contenido = RichTextFormField()
    autor = forms.CharField(max_length=500)
    fecha_creacion= forms.DateField(required=False)
    imagenes= forms.ImageField(required= False)
    
class BusquedaPublicacion(forms.Form):
    titulo = forms.CharField(max_length=250, required=False)
    

