from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="home"),
    path('detalle/<int:categoria_id>/', views.detalle, name='detalle'),
    path('contacto/', views.contacto, name="contacto"),
    path('checkout/', views.checkout, name="checkout"),
    path('cart/', views.cart, name="cart"),
    path('productos/<int:categoria_id>/', views.productos_por_categoria, name='productos_por_categoria'),
    path('cargar-productos/', views.cargar_productos_desde_excel, name='cargar_productos'),
    path('cargar-categorias/', views.cargar_categorias_desde_excel, name='cargar_categorias'),
    path('cargar-unidades/', views.cargar_unidades_desde_excel, name='cargar_unidades'),
    path('cargar-tamanos/', views.cargar_tamanos_desde_excel, name='cargar_tamanos'),
    path('cargar-regiones/', views.cargar_regiones_desde_excel, name='cargar_regiones'),
    path('cargar-ciudades/', views.cargar_ciudades_desde_excel, name='cargar_ciudades'),
    path('cargar-comunas/', views.cargar_comunas_desde_excel, name='cargar_comunas'),
    path('creararticulo/', views.creararticulo, name="creararticulo"),
    path('crear/', views.crear, name="crear"),
    path('nuevo_producto/', views.nuevo_producto, name="nuevo_producto"),
]