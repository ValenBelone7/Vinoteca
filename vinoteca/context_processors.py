from .models import Vino, Compra


def calcular_total_compra(compra):
    total = 0
    for item in compra.items.all():
        total += item.cantidad * item.precio_unitario
    return total


def datos_vinoteca(request):
    # Si el usuario está autenticado, mostrar sus compras recientes
    if request.user.is_authenticated:
        compras_recientes = Compra.objects.filter(usuario=request.user).select_related('usuario').order_by('-fecha')[:5]
        # Agregar el total a cada compra
        for compra in compras_recientes:
            compra.total = calcular_total_compra(compra)
    else:
        compras_recientes = []
    
    return {
        'nombre_vinoteca': 'La Gran Vinoteca',
        'vinos_destacados': Vino.objects.filter(stock__gt=0).select_related('bodega').order_by('-id')[:3],
        'total_vinos': Vino.objects.count(),
        'compras_recientes': compras_recientes,
    }
