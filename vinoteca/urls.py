from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('vinos/', views.lista_vinos, name='lista_vinos'),
    path('vinos/crear/', views.crear_vino, name='crear_vino'),
    path('vinos/<int:pk>/', views.detalle_vino, name='detalle_vino'),
    path('vinos/editar/<int:pk>/', views.editar_vino, name='editar_vino'),
    path('vinos/eliminar/<int:pk>/', views.eliminar_vino, name='eliminar_vino'),
    path('bodegas/', views.lista_bodegas, name='lista_bodegas'),
    path('bodegas/crear/', views.crear_bodega, name='crear_bodega'),
    path('bodegas/<int:pk>/', views.detalle_bodega, name='detalle_bodega'),
    path('bodegas/editar/<int:pk>/', views.editar_bodega, name='editar_bodega'),
    path('bodegas/eliminar/<int:pk>/', views.eliminar_bodega, name='eliminar_bodega'),
    path('compras/crear/', views.crear_compra, name='crear_compra'),
    path('mis-compras/', views.mis_compras, name='mis_compras'),
    path('varietales/crear/', views.crear_varietal, name='crear_varietal'),
    path('categorias/crear/', views.crear_categoria, name='crear_categoria'),
]
