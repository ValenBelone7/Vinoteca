from django import forms

from .models import Vino

INPUT_CLASS = 'w-full border border-gray-300 rounded px-3 py-2 focus:outline-none focus:ring-2 focus:ring-red-500'


class VinoForm(forms.ModelForm):
    class Meta:
        model = Vino
        fields = [
            'nombre', 'bodega', 'varietal', 'categoria',
            'anio', 'precio', 'stock', 'foto', 'descripcion',
        ]
        widgets = {
            'nombre': forms.TextInput(attrs={'class': INPUT_CLASS}),
            'bodega': forms.Select(attrs={'class': INPUT_CLASS}),
            'varietal': forms.Select(attrs={'class': INPUT_CLASS}),
            'categoria': forms.Select(attrs={'class': INPUT_CLASS}),
            'anio': forms.NumberInput(attrs={'class': INPUT_CLASS}),
            'precio': forms.NumberInput(attrs={'class': INPUT_CLASS, 'step': '0.01'}),
            'stock': forms.NumberInput(attrs={'class': INPUT_CLASS}),
            'foto': forms.FileInput(attrs={'class': INPUT_CLASS}),
            'descripcion': forms.Textarea(attrs={'class': INPUT_CLASS, 'rows': 4}),
        }
