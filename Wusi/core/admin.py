from django.contrib import admin
from .models import Categoria, Producto, Boleta, Conversacion, Mensaje, Tamano, Unidad_medida, VariantePrecio, Ticket, Reparto, Ciudad, Comuna, Noticia, Region, Calificacion, Subcategoria
# Register your models here.

admin.site.register(Categoria)
admin.site.register(Producto)
admin.site.register(Boleta)
admin.site.register(Conversacion)
admin.site.register(Mensaje)
admin.site.register(Tamano)
admin.site.register(Unidad_medida)
admin.site.register(VariantePrecio)
admin.site.register(Ticket)
admin.site.register(Reparto)
admin.site.register(Region)
admin.site.register(Ciudad)
admin.site.register(Comuna)
admin.site.register(Noticia)
admin.site.register(Calificacion)
admin.site.register(Subcategoria)