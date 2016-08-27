from django import forms
from .models import Producto, ProductoCompuesto, Stock  # PrecioVentaProducto
from dal import autocomplete

# Restringir la carga de un mismo producto varias veces
# Producto.precio_venta = Debe ser el ultimo precio definido en PrecioProducto, se debe validar por la fecha.as


# class PrecioVentaProductoForm(forms.ModelForm):
#     class Meta:
#         model = PrecioVentaProducto
#         fields = '__all__'
#         localized_fields = ('precio_venta',)

class ProductoForm(forms.ModelForm):

    class Meta:
        model = Producto
        fields = '__all__'
        widgets = {
            'categoria': autocomplete.ModelSelect2(url='bar:categoria_producto-autocomplete'),
            'subcategoria': autocomplete.ModelSelect2(url='bar:subcategoria_producto-autocomplete',
                                                      forward=['categoria']),
        }


class ProductoCompuestoForm(forms.ModelForm):

    class Meta:
        model = ProductoCompuesto
        fields = '__all__'
        widgets = {
            'categoria': autocomplete.ModelSelect2(url='bar:categoria_producto-autocomplete'),
            'subcategoria': autocomplete.ModelSelect2(url='bar:subcategoria_producto-autocomplete',
                                                      forward=['categoria']),
        }