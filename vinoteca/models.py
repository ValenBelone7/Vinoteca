from django.db import models
from django.conf import settings


class Bodega(models.Model):
    nombre = models.CharField(max_length=100)
    pais = models.CharField(max_length=50)
    region = models.CharField(max_length=100, blank=True)
    descripcion = models.TextField(blank=True)
    logo = models.ImageField(upload_to='bodegas/', blank=True, null=True)

    class Meta:
        ordering = ['nombre']
        verbose_name_plural = 'bodegas'

    def __str__(self):
        return self.nombre


class Varietal(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField(blank=True)

    class Meta:
        ordering = ['nombre']

    def __str__(self):
        return self.nombre


class Categoria(models.Model):
    nombre = models.CharField(max_length=50)  # Tinto, Blanco, Rosado, Espumante

    class Meta:
        ordering = ['nombre']

    def __str__(self):
        return self.nombre


class Proveedor(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField(blank=True)
    telefono = models.CharField(max_length=20, blank=True)
    bodegas = models.ManyToManyField(Bodega, blank=True, related_name='proveedores')

    class Meta:
        ordering = ['nombre']

    def __str__(self):
        return self.nombre


class Vino(models.Model):
    nombre = models.CharField(max_length=100)
    bodega = models.ForeignKey(Bodega, on_delete=models.CASCADE, related_name='vinos')
    varietal = models.ForeignKey(Varietal, on_delete=models.SET_NULL, null=True, related_name='vinos')
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True, related_name='vinos')
    anio = models.PositiveIntegerField(verbose_name='Año')
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField(default=0)
    foto = models.ImageField(upload_to='vinos/', blank=True, null=True)
    descripcion = models.TextField(blank=True)

    class Meta:
        ordering = ['nombre']

    def __str__(self):
        return f'{self.nombre} ({self.anio})'


class Compra(models.Model):
    ESTADO_CHOICES = [
        ('pendiente', 'Pendiente'),
        ('completada', 'Completada'),
        ('cancelada', 'Cancelada'),
    ]
    usuario = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='compras'
    )
    fecha = models.DateTimeField(auto_now_add=True)
    estado = models.CharField(max_length=20, choices=ESTADO_CHOICES, default='pendiente')

    class Meta:
        ordering = ['-fecha']

    def __str__(self):
        return f'Compra #{self.pk} — {self.usuario} ({self.estado})'


class ItemCompra(models.Model):
    compra = models.ForeignKey(Compra, on_delete=models.CASCADE, related_name='items')
    vino = models.ForeignKey(Vino, on_delete=models.CASCADE, related_name='items')
    cantidad = models.PositiveIntegerField()
    precio_unitario = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f'{self.cantidad}x {self.vino} en Compra #{self.compra.pk}'