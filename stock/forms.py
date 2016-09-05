import pdb
from django import forms
from .models import Producto, ProductoCompuesto, Stock  # PrecioVentaProducto
from dal import autocomplete

ATTR_NUMERICO = {'style': 'text-align:right', 'class': 'auto', 'data-a-sep': '.', 'data-a-dec': ','}
ATTR_NUMERICO_RO = {'style': 'text-align:right', 'class': 'auto', 'data-a-sep': '.', 'data-a-dec': ',', 'readonly': 'readonly'}

# Restringir la carga de un mismo producto varias veces
# Producto.precio_venta = Debe ser el ultimo precio definido en PrecioProducto, se debe validar por la fecha.as


# class PrecioVentaProductoForm(forms.ModelForm):
#     class Meta:
#         model = PrecioVentaProducto
#         fields = '__all__'
#         localized_fields = ('precio_venta',)

class ProductoForm(forms.ModelForm):

    precio_compra_sugerido = forms.CharField(widget=forms.TextInput(attrs=ATTR_NUMERICO_RO),
                                             label='Precio Compra Sugerido', required=False,
                                             help_text='Este valor se calcula promediando el Costo de Compra del '
                                                       'Producto en los ultimos 30 dias.')
    precio_venta_sugerido = forms.CharField(widget=forms.TextInput(attrs=ATTR_NUMERICO_RO),
                                            label='Precio Venta Sugerido', required=False,
                                            help_text='Precio de Venta sugerido calculado a partir del Precio Compra '
                                                      'Sugerido por el Porcentaje de Ganancia. Cuando el Producto es '
                                                      'registrado se calcula el Precio de Compra por el Porcentaje '
                                                      'de Ganancia ingresados.')

    class Meta:
        model = Producto
        fields = '__all__'
        widgets = {
            'categoria': autocomplete.ModelSelect2(url='bar:categoria_producto-autocomplete'),
            'subcategoria': autocomplete.ModelSelect2(url='bar:subcategoria_producto-autocomplete',
                                                      forward=['categoria']),
        }

    def __init__(self, *args, **kwargs):
        super(ProductoForm, self).__init__(*args, **kwargs)

        # instance = getattr(self, 'instance', None)

        if self.instance:  # and self.instance.pk:
            self.initial['precio_compra_sugerido'] = self.instance.get_precio_compra_sugerido()
            # self.initial['precio_venta_sugerido'] = self.instance.get_precio_venta_sugerido()
            # self.instance.save()
            # if self.fields['tipo_producto'] == 'IN':
            #     self.fields['porcentaje_ganancia'].widgets.attrs['readonly'] = True
            #     self.fields['precio_venta_sugerido'].widgets.attrs['readonly'] = True
            # elif self.fields['tipo_producto'] == 'VE':
            #     self.fields['porcentaje_ganancia'].widgets.attrs['readonly'] = False
            #     self.fields['precio_venta_sugerido'].widgets.attrs['readonly'] = False


class ProductoCompuestoForm(forms.ModelForm):

    class Meta:
        model = ProductoCompuesto
        fields = '__all__'
        widgets = {
            'categoria': autocomplete.ModelSelect2(url='bar:categoria_producto-autocomplete'),
            'subcategoria': autocomplete.ModelSelect2(url='bar:subcategoria_producto-autocomplete',
                                                      forward=['categoria']),
        }