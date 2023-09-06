from django import forms
from django.forms import ModelForm
from .models import Producto, Reparto, Noticia, Promocion
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = [
            'codigo_barras', 'nombre', 'descripcion', 'precio', 'precio_oferta', 'stock',
            'categoria', 'subcategoria', 'imagen', 'unidad_medida', 'tamano', 'oferta', 'descuento'
            
        ]