from django import forms
from .models import Producto, PrecioProducto, Stock

# Restringir la carga de un mismo producto varias veces
# Producto.precio_venta = Debe ser el ultimo precio definido en PrecioProducto, se debe validar por la fecha.as


class PrecioProductoForm(forms.ModelForm):
    class Meta:
        model = PrecioProducto
        fields = '__all__'
        localized_fields = ('precio_venta',)