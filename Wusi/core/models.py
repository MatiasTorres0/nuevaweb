import uuid
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.core.validators import MinValueValidator, MaxValueValidator

class Categoria(models.Model):
    nombre = models.CharField(max_length=100)
    imagen = models.FileField(upload_to='categoria/', blank=True, null=True, verbose_name="Imagen o Video")
    cantidad_productos = models.PositiveIntegerField(default=0, editable=False)  # Inicialmente, la cantidad es 0
    def __str__(self):
        return self.nombre
    

class Subcategoria(models.Model):
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100)
    def __str__(self):
        return f'{self.categoria.nombre} - {self.nombre}'

class Unidad_medida(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Tamano(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre



class Producto(models.Model):
    codigo_barras = models.CharField(max_length=200, null=True)
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2, null=True, validators=[MinValueValidator(0)])
    precio_oferta = models.DecimalField(max_digits=10, decimal_places=2, null=True, validators=[MinValueValidator(0)])
    stock = models.IntegerField( null=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    subcategoria = models.ForeignKey(Subcategoria, on_delete=models.CASCADE, null=True)
    imagen = models.FileField(upload_to='productos/', blank=True, null=True, verbose_name="Imagen o Video")
    unidad_medida = models.ForeignKey(Unidad_medida, on_delete=models.CASCADE, default=None, blank=True, null=True)
    tamano = models.ForeignKey(Tamano, on_delete=models.CASCADE, default=None, blank=True, null=True)
    oferta = models.CharField(max_length=100, null=True)
    descuento = models.PositiveIntegerField(default=0, validators=[MaxValueValidator(100)])
    calificacion_promedio = models.DecimalField(max_digits=3, decimal_places=2, null=True, blank=True,validators=[MinValueValidator(0), MaxValueValidator(5)])
    def precio_con_descuento(self):
        if self.descuento > 0:
            descuento_decimal = self.descuento / 100
            precio_con_descuento = self.precio - (self.precio * descuento_decimal)
            return round(precio_con_descuento, 2)
        return self.precio
    def save(self, *args, **kwargs):
        if not self.pk:  # Si es un producto nuevo
            self.categoria.cantidad_productos += 1
            self.categoria.save()
        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        self.categoria.cantidad_productos -= 1
        self.categoria.save()
        super().delete(*args, **kwargs)
    
    def calificacion_promedio(self):
        calificaciones = Calificacion.objects.filter(producto=self)
        if calificaciones.exists():
            total_calificaciones = sum(calificacion.valor for calificacion in calificaciones)
            promedio = total_calificaciones / calificaciones.count()
            return round(promedio, 1)
        return None
    
    def __str__(self):
        return self.nombre
class Calificacion(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    valor = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])

    def __str__(self):
        return f"Calificación de {self.valor} para {self.producto.nombre}"
    

class Boleta(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)  # Relación con el usuario que generó la boleta
    nro_boleta = models.CharField(max_length=20, unique=True)  # Número de la boleta
    fecha_generacion = models.DateTimeField(auto_now_add=True)
    total_a_pagar = models.DecimalField(max_digits=10, decimal_places=2)
    archivo_pdf = models.FileField(upload_to='boletas/')

    def __str__(self):
        return f"Boleta #{self.nro_boleta} - Usuario: {self.usuario.username} - Total: ${self.total_a_pagar}"
    

    
class Conversacion(models.Model):
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    usuario_creador = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return f'Conversación {self.id}'

class Mensaje(models.Model):
    conversacion = models.ForeignKey(Conversacion, on_delete=models.CASCADE)
    contenido = models.TextField()
    fecha_envio = models.DateTimeField(auto_now_add=True)
    remitente = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'Mensaje de {self.remitente} en Conversación {self.conversacion.id}'
    

class VariantePrecio(models.Model):
    codigo_barras = models.CharField(max_length=200, null=True)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    precio = models.IntegerField()  # Precio en pesos chilenos
    peso_kilo = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    unidad = models.CharField(max_length=10, null=True, blank=True)



class Ticket(models.Model):
    STATUS_CHOICES = (
        ('Open', 'Abierto'),
        ('In Progress', 'En Progreso'),
        ('Closed', 'Cerrado'),
    )

    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    message = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Open')
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)
    respuesta = models.TextField(blank=True, null=True)  # Campo para almacenar la respuesta

    def __str__(self):
        return self.name
    





class Noticia(models.Model):
    titulo = models.CharField(max_length=200, null=True)
    contenido = models.TextField()
    imagen = models.ImageField(upload_to='noticias', blank=True, null=True)
    fecha_publicacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo
    

class Region(models.Model):
    nombre = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.nombre if self.nombre else "Nombre no disponible"


class Ciudad(models.Model):
    nombre = models.CharField(max_length=100, null=True)
    region = models.ForeignKey(Region, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.nombre

class Comuna(models.Model):
    nombre = models.CharField(max_length=100, null=True)
    ciudad = models.ForeignKey(Ciudad, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.nombre
    
class Reparto(models.Model):
    fecha = models.DateTimeField(default=timezone.now)
    region = models.ForeignKey(Region, on_delete=models.CASCADE, null=True)
    ciudad = models.ForeignKey(Ciudad, on_delete=models.CASCADE, null=True)
    comuna = models.ForeignKey(Comuna, on_delete=models.CASCADE, null=True)
    direccion = models.CharField(max_length=200, null=True)
    persona_recibe = models.CharField(max_length=200, null=True)
    numero_contacto = models.CharField(max_length=20, null=True)

    def __str__(self):
        return f"Reparto en {self.comuna.nombre}, {self.ciudad.nombre}, {self.region.nombre} - {self.fecha}"
    

class Promocion(models.Model):
    nombre = models.CharField(max_length=100)
    producto = models.ForeignKey('Producto', on_delete=models.CASCADE)
    descuento = models.DecimalField(max_digits=5, decimal_places=2)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()

    def __str__(self):
        return self.nombre