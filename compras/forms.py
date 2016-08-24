__author__ = 'pmmr'

from django import forms
# from django.utils import timezone
from .models import LineaCreditoProveedor, LineaCreditoProveedorDetalle, PagoProveedor, FacturaProveedor, Empresa, \
    OrdenCompra, OrdenCompraDetalle, Compra, CompraDetalle
# from bar.models import OrdenCompraEstado
from datetimewidget.widgets import DateWidget

# def get_my_choices():
#     # you place some logic here
#     choices_list = (
#         ('EPP', 'En Proceso Proveedor'),
#         # ('ENT', 'Entregada por Proveedor'),
#         # ('PEP', 'Pendiente Entrega Proveedor'),
#         ('CAN', 'Cancelada'),
#     )
#     return choices_list

ATTR_NUMERICO = {'style': 'text-align:right', 'class': 'auto', 'data-a-sep': '.', 'data-a-dec': ','}
ATTR_NUMERICO_RO = ATTR_NUMERICO.copy()


class LineaCreditoProveedorForm(forms.ModelForm):
    class Meta:
        model = LineaCreditoProveedor
        fields = '__all__'
        localized_fields = ['linea_credito_proveedor', 'monto_total_facturas_proveedor', 'monto_total_pagos_proveedor',
        'uso_linea_credito_proveedor']


class LineaCreditoProveedorDetalleForm(forms.ModelForm):
    class Meta:
        model = LineaCreditoProveedorDetalle
        fields = '__all__'
        localized_fields = ['monto_movimiento']


class PagoProveedorForm(forms.ModelForm):
    class Meta:
        model = PagoProveedor
        fields = '__all__'
        localized_fields = ['monto_pago_proveedor']


class EmpresaForm(forms.ModelForm):
    class Meta:
        model = Empresa
        fields = '__all__'
        widgets = {
            'fecha_apertura': DateWidget,
        }


class FacturaProveedorForm(forms.ModelForm):
    class Meta:
        model = FacturaProveedor
        fields = '__all__'
        localized_fields = ['total_pago_factura']


class OrdenCompraForm(forms.ModelForm):

    # prueba2 = forms.CharField(max_length=100)
    # prueba2 = Cliente.objects.filter(pk=4)

    class Meta:
        model = OrdenCompra
        fields = '__all__'
        localized_fields = ['total_orden_compra']
        # widgets = {
        #     # 'estado_orden_compra': forms.Select(),
        # }

    # def __init__(self, *args, **kwargs):
    #     super(OrdenCompraForm, self).__init__(*args, **kwargs)
    #     self.fields['estado_orden_compra'] = forms.ChoiceField(choices=get_my_choices())


class OrdenCompraDetalleForm(forms.ModelForm):

    precio_producto_orden_compra = forms.CharField(widget=forms.TextInput,  # (attrs=ATTR_NUMERICO),
                                                   label='Precio del Producto2', required=False)
    cantidad_producto_orden_compra = forms.CharField(widget=forms.TextInput(attrs=ATTR_NUMERICO),
                                                     label='Cantidad del Producto2', required=False)
    total_producto_orden_compra = forms.CharField(widget=forms.TextInput(attrs=ATTR_NUMERICO),
                                                  label='Total del Producto2', required=False)

    class Meta:
        model = OrdenCompraDetalle
        fields = '__all__'
        localized_fields = ['precio_producto_orden_compra', 'total_producto_orden_compra']
        # widgets = {
        #     'precio_producto_orden_compra': forms.CharField(widget=forms.TextInput(attrs=ATTR_NUMERICO),
        #                                                     label='Precio del Producto2', required=False),
        #     'cantidad_producto_orden_compra': forms.CharField(widget=forms.TextInput(attrs=ATTR_NUMERICO),
        #                                                       label='Cantidad del Producto2', required=False),
        #     'total_producto_orden_compra': forms.CharField(widget=forms.TextInput(attrs=ATTR_NUMERICO),
        #                                                    label='Total del Producto2', required=False),
        # }


class CompraForm(forms.ModelForm):
    class Meta:
        model = Compra
        fields = '__all__'
        localized_fields = ['total_compra']


class CompraDetalleForm(forms.ModelForm):
    class Meta:
        model = CompraDetalle
        fields = '__all__'
        localized_fields = ['precio_producto_compra', 'total_producto_compra']