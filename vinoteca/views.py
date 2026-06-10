from django.shortcuts import get_object_or_404, redirect, render

from .forms import BodegaForm, VinoForm
from .models import Bodega, Vino


def home(request):
    return render(request, 'vinoteca/home.html')


def lista_vinos(request):
    vinos = Vino.objects.select_related('bodega', 'varietal', 'categoria')
    return render(request, 'vinoteca/lista_vinos.html', {'vinos': vinos})


def detalle_vino(request, pk):
    vino = get_object_or_404(
        Vino.objects.select_related('bodega', 'varietal', 'categoria'),
        pk=pk,
    )
    return render(request, 'vinoteca/detalle_vino.html', {'vino': vino})


def crear_vino(request):
    if request.method == 'POST':
        form = VinoForm(request.POST, request.FILES)
        if form.is_valid():
            vino = form.save()
            return redirect('detalle_vino', pk=vino.pk)
    else:
        form = VinoForm()
    return render(request, 'vinoteca/crear_vino.html', {'form': form})


def editar_vino(request, pk):
    vino = get_object_or_404(Vino, pk=pk)
    if request.method == 'POST':
        form = VinoForm(request.POST, request.FILES, instance=vino)
        if form.is_valid():
            form.save()
            return redirect('detalle_vino', pk=pk)
    else:
        form = VinoForm(instance=vino)
    return render(request, 'vinoteca/editar_vino.html', {'form': form, 'vino': vino})


def eliminar_vino(request, pk):
    vino = get_object_or_404(Vino, pk=pk)
    if request.method == 'POST':
        vino.delete()
        return redirect('lista_vinos')
    return render(request, 'vinoteca/eliminar_vino.html', {'vino': vino})


def lista_bodegas(request):
    bodegas = Bodega.objects.all()
    return render(request, 'vinoteca/lista_bodegas.html', {'bodegas': bodegas})


def detalle_bodega(request, pk):
    bodega = get_object_or_404(Bodega, pk=pk)
    return render(request, 'vinoteca/detalle_bodega.html', {'bodega': bodega})


def crear_bodega(request):
    if request.method == 'POST':
        form = BodegaForm(request.POST, request.FILES)
        if form.is_valid():
            bodega = form.save()
            return redirect('detalle_bodega', pk=bodega.pk)
    else:
        form = BodegaForm()
    return render(request, 'vinoteca/crear_bodega.html', {'form': form})


def editar_bodega(request, pk):
    bodega = get_object_or_404(Bodega, pk=pk)
    if request.method == 'POST':
        form = BodegaForm(request.POST, request.FILES, instance=bodega)
        if form.is_valid():
            form.save()
            return redirect('detalle_bodega', pk=pk)
    else:
        form = BodegaForm(instance=bodega)
    return render(request, 'vinoteca/editar_bodega.html', {'form': form, 'bodega': bodega})


def eliminar_bodega(request, pk):
    bodega = get_object_or_404(Bodega, pk=pk)
    if request.method == 'POST':
        bodega.delete()
        return redirect('lista_bodegas')
    return render(request, 'vinoteca/eliminar_bodega.html', {'bodega': bodega})
