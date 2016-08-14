__author__ = 'pmmr'

from django import forms
from .models import LineaCreditoProveedor, LineaCreditoProveedorDetalle, PagoProveedor, FacturaProveedor, OrdenCompra, \
    OrdenCompraDetalle, Compra, CompraDetalle


# def get_my_choices():
#     # you place some logic here
#     choices_list = (
#         ('EPP', 'En Proceso Proveedor'),
#         # ('ENT', 'Entregada por Proveedor'),
#         # ('PEP', 'Pendiente Entrega Proveedor'),
#         ('CAN', 'Cancelada'),
#     )
#     return choices_list

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
    #     # widgets = {
    #     #     'estado_orden_compra': forms.Select(),
    #     # }

    # def __init__(self, *args, **kwargs):
    #     super(OrdenCompraForm, self).__init__(*args, **kwargs)
    #     self.fields['estado_orden_compra'] = forms.ChoiceField(choices=get_my_choices())

    # def clean_estado_orden_compra(self):
    #     self.


class OrdenCompraDetalleForm(forms.ModelForm):
    class Meta:
        model = OrdenCompraDetalle
        fields = '__all__'
        localized_fields = ['precio_producto_orden_compra', 'total_producto_orden_compra']


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