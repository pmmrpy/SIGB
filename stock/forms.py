import pdb
from django import forms
from django.core.validators import RegexValidator
from django.utils.safestring import mark_safe
from .models import Producto, ProductoCompuesto, MovimientoStock  # PrecioVentaProducto
from dal import autocomplete
from stock.models import SolicitaTransferenciaStock

numero_factura = RegexValidator(r'^999-999-9999999$', 'Ingrese el Numero de Factura en el formato "999-999-9999999".')
ATTR_NUMERICO = {'style': 'text-align:right;', 'class': 'auto', 'data-a-sep': '.', 'data-a-dec': ',',
                 'type': 'number'}
ATTR_NUMERICO_RO = {'style': 'text-align:right;', 'class': 'auto', 'data-a-sep': '.', 'data-a-dec': ',',
                    'type': 'number', 'readonly': 'readonly'}
ATTR_NUMERICO_RO_RESALTADO = ATTR_NUMERICO_RO.copy()
ATTR_NUMERICO_RO_RESALTADO['style'] += 'font-size: 20px; height: 25px; font-weight: bold; color: indianred;'
ATTR_NUMERICO_RO_RESALTADO_2 = ATTR_NUMERICO_RO.copy()
ATTR_NUMERICO_RO_RESALTADO_2['style'] += 'font-size: 14px; height: 20px; font-weight: bold; color: darkorange;'

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
                                                      'registrado por primera vez se calcula el Precio de Compra por '
                                                      'el Porcentaje de Ganancia ingresados.')

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

    precio_venta_sugerido = forms.CharField(widget=forms.TextInput(attrs=ATTR_NUMERICO_RO),
                                            label='Precio Venta Sugerido', required=False,
                                            help_text='Precio de Venta sugerido calculado a partir del Costo de '
                                                      'Elaboracion por el Porcentaje de Ganancia.')

    class Meta:
        model = ProductoCompuesto
        fields = '__all__'
        widgets = {
            'categoria': autocomplete.ModelSelect2(url='bar:categoria_producto-autocomplete'),
            'subcategoria': autocomplete.ModelSelect2(url='bar:subcategoria_producto-autocomplete',
                                                      forward=['categoria']),
        }
        

class SolicitaTransferenciaStockForm(forms.ModelForm):
    
    cantidad_existente_stock = forms.CharField(widget=forms.TextInput(attrs=ATTR_NUMERICO_RO_RESALTADO_2),
                                               label=mark_safe('<strong style="font-size: 14px;">Cantidad Existente Producto</strong>'),
                                               required=False)  # initial=0
    
    class Meta:
        model = SolicitaTransferenciaStock
        fields = '__all__'
        # widgets = {
        #
        # }
        
    # def __init__(self, *args, **kwargs):
    #     super(SolicitaTransferenciaStockForm, self).__init__(*args, **kwargs)
    #
    #     if self.instance and self.instance.pk:
    #         self.initial['cantidad_existente_stock'] = self.instance.get_linea_credito() or 0