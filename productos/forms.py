from django import forms
from .models import categoria, productos, clientes


class CategoriaForm(forms.ModelForm):
    class Meta:
        model = categoria
        fields = '__all__'


class ProductoForm(forms.ModelForm):
    class Meta:
        model = productos
        fields = '__all__'


class ClienteForm(forms.ModelForm):
    class Meta:
        model = clientes
        fields = '__all__'