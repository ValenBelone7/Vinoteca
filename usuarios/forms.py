from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import CustomUser

INPUT_CLASS = 'w-full border border-gray-300 rounded px-3 py-2 focus:outline-none focus:ring-2 focus:ring-red-500'


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'telefono', 'direccion', 'foto')
        widgets = {
            'username': forms.TextInput(attrs={'class': INPUT_CLASS}),
            'email': forms.EmailInput(attrs={'class': INPUT_CLASS}),
            'telefono': forms.TextInput(attrs={'class': INPUT_CLASS}),
            'direccion': forms.TextInput(attrs={'class': INPUT_CLASS}),
            'foto': forms.FileInput(attrs={'class': INPUT_CLASS}),
        }
