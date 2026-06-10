from .models import Vino


def datos_vinoteca(request):
    return {
        'nombre_vinoteca': 'La Gran Vinoteca',
        'vinos_destacados': Vino.objects.filter(stock__gt=0).select_related('bodega').order_by('-id')[:3],
        'total_vinos': Vino.objects.count(),
    }
