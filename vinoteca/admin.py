from django.contrib import admin

from .models import Bodega, Categoria, Compra, ItemCompra, Proveedor, Varietal, Vino


@admin.register(Bodega)
class BodegaAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'pais', 'region']
    search_fields = ['nombre', 'pais']


@admin.register(Varietal)
class VarietalAdmin(admin.ModelAdmin):
    list_display = ['nombre']
    search_fields = ['nombre']


@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ['nombre']
    search_fields = ['nombre']


@admin.register(Vino)
class VinoAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'bodega', 'varietal', 'precio', 'stock']
    list_filter = ['categoria', 'varietal', 'bodega']
    search_fields = ['nombre']


@admin.register(Proveedor)
class ProveedorAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'email', 'telefono']
    search_fields = ['nombre', 'email']
    filter_horizontal = ['bodegas']


@admin.register(Compra)
class CompraAdmin(admin.ModelAdmin):
    list_display = ['usuario', 'fecha', 'estado']
    list_filter = ['estado']
    search_fields = ['usuario__username']


@admin.register(ItemCompra)
class ItemCompraAdmin(admin.ModelAdmin):
    list_display = ['compra', 'vino', 'cantidad', 'precio_unitario']
    search_fields = ['vino__nombre', 'compra__usuario__username']
