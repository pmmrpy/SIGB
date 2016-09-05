# -*- coding: utf-8 -*-

__author__ = 'pmmr'

from decimal import Decimal
from dal import autocomplete
from django.core.exceptions import ValidationError
from django.utils.safestring import mark_safe
from django import forms
# from django.utils import timezone
from .models import Proveedor, LineaCreditoProveedor, LineaCreditoProveedorDetalle, PagoProveedor, FacturaProveedor, \
    Empresa, OrdenCompra, OrdenCompraDetalle, Compra, CompraDetalle, ProveedorTelefono
# from bar.models import OrdenCompraEstado
from datetimewidget.widgets import DateWidget

ATTR_NUMERICO = {'style': 'text-align:right;', 'class': 'auto', 'data-a-sep': '.', 'data-a-dec': ',',
                 'type': 'number'}
ATTR_NUMERICO_RO = {'style': 'text-align:right;', 'class': 'auto', 'data-a-sep': '.', 'data-a-dec': ',',
                    'type': 'number', 'readonly': 'readonly'}
ATTR_NUMERICO_RO_RESALTADO = ATTR_NUMERICO_RO.copy()
ATTR_NUMERICO_RO_RESALTADO['style'] += 'font-size: 20px; height: 25px; font-weight: bold; color: indianred;'


class ProveedorForm(forms.ModelForm):
    class Meta:
        model = Proveedor
        fields = '__all__'
        widgets = {
            'pais': autocomplete.ModelSelect2(url='bar:pais-autocomplete'),
            'ciudad': autocomplete.ModelSelect2(url='bar:ciudad-autocomplete', forward=['pais']),
        }


class ProveedorTelefonoForm(forms.ModelForm):
    class Meta:
        model = ProveedorTelefono
        fields = '__all__'
        widgets = {
            'codigo_pais_telefono': autocomplete.ModelSelect2(url='bar:codigo_pais_telefono-autocomplete'),
            'codigo_operadora_telefono': autocomplete.ModelSelect2(url='bar:codigo_operadora_telefono-autocomplete',
                                                                   forward=['codigo_pais_telefono']),
        }


class LineaCreditoProveedorForm(forms.ModelForm):
    class Meta:
        model = LineaCreditoProveedor
        fields = '__all__'
        # localized_fields = ['linea_credito_proveedor', 'monto_total_facturas_proveedor', 'monto_total_pagos_proveedor',
        #                     'uso_linea_credito_proveedor']

    def __init__(self, *args, **kwargs):
        super(LineaCreditoProveedorForm, self).__init__(*args, **kwargs)
        # print self.fields['total_orden_compra'].id_for_label,' pobaasdf'

        linea_credito = self.instance
        print 'Linea de Credito: %s' % linea_credito

        # if self.instance and self.instance.pk:
        if linea_credito and linea_credito.pk:
            # print linea_credito.instance.get_monto_total_facturas_proveedor()
            # self.initial['monto_total_facturas_proveedor'] = linea_credito.get_monto_total_facturas_proveedor()

            # self.instance.save()
            print 'linea_credito.monto_total_facturas_proveedor before save: %s' % linea_credito.monto_total_facturas_proveedor
            print 'linea_credito.monto_total_pagos_proveedor before save: %s' % linea_credito.monto_total_pagos_proveedor
            print 'linea_credito.uso_linea_credito_proveedor before save: %s' % linea_credito.uso_linea_credito_proveedor
            print 'linea_credito.disponible_linea_credito_proveedor before save: %s' % linea_credito.disponible_linea_credito_proveedor
            print 'linea_credito.estado_linea_credito_proveedor before save: %s' % linea_credito.estado_linea_credito_proveedor
            linea_credito.monto_total_facturas_proveedor = linea_credito.get_monto_total_facturas_proveedor()
            linea_credito.monto_total_pagos_proveedor = linea_credito.get_monto_total_pagos_proveedor()
            linea_credito.uso_linea_credito_proveedor = linea_credito.get_uso_linea_credito_proveedor()
            linea_credito.disponible_linea_credito_proveedor = linea_credito.get_disponible_linea_credito_proveedor()
            linea_credito.estado_linea_credito_proveedor = linea_credito.get_estado_linea_credito_proveedor()
            self.initial['estado_linea_credito_proveedor'] = linea_credito.estado_linea_credito_proveedor
            linea_credito.save()
            print 'linea_credito.monto_total_facturas_proveedor after save: %s' % linea_credito.monto_total_facturas_proveedor
            print 'linea_credito.monto_total_pagos_proveedor after save: %s' % linea_credito.monto_total_pagos_proveedor
            print 'linea_credito.uso_linea_credito_proveedor after save: %s' % linea_credito.uso_linea_credito_proveedor
            print 'linea_credito.disponible_linea_credito_proveedor after save: %s' % linea_credito.disponible_linea_credito_proveedor
            print 'linea_credito.estado_linea_credito_proveedor after save: %s' % linea_credito.estado_linea_credito_proveedor

            # for field in self.fields:
            #     self.fields[field].widget.attrs['readonly'] = True
            #     self.fields['linea_credito_proveedor'].widget.attrs['readonly'] = False

            # self.fields['estado_linea_credito_proveedor'].widget.attrs['readonly'] = False
            if linea_credito.estado_linea_credito_proveedor == 'DEL':
                self.fields['estado_linea_credito_proveedor'].widget.attrs.update({'style': 'font-size: 15px; height: 30px; width: 300px; font-weight: bold; color: green;'})
                # color = 'green'
                # return format_html('<span style="color: %s"><b> %s </b></span>' %
                #                    (color, obj.get_estado_linea_credito_proveedor_display()))
            elif linea_credito.estado_linea_credito_proveedor == 'LIM':
                self.fields['estado_linea_credito_proveedor'].widget.attrs.update({'style': 'font-size: 15px; height: 30px; width: 300px; font-weight: bold; color: orange;'})
                # color = 'red'
                # return format_html('<span style="color: %s"><b> %s </b></span>' %
                #                    (color, obj.get_estado_linea_credito_proveedor_display()))
            elif linea_credito.estado_linea_credito_proveedor == 'SOB':
                self.fields['estado_linea_credito_proveedor'].widget.attrs.update({'style': 'font-size: 15px; height: 30px; width: 300px; font-weight: bold; color: red;'})
            self.fields['estado_linea_credito_proveedor'].widget.attrs['readonly'] = True
            self.fields['estado_linea_credito_proveedor'].widget.attrs['disabled'] = True
            # self.fields['estado_linea_credito_proveedor'].widget.attrs['required'] = False


class LineaCreditoProveedorDetalleForm(forms.ModelForm):
    class Meta:
        model = LineaCreditoProveedorDetalle
        fields = '__all__'
        # localized_fields = ['monto_movimiento']


class PagoProveedorForm(forms.ModelForm):
    class Meta:
        model = PagoProveedor
        fields = '__all__'
        # localized_fields = ['monto_pago_proveedor']

    def __init__(self, *args, **kwargs):
        super(PagoProveedorForm, self).__init__(*args, **kwargs)
        if self.instance and self.instance.pk:
            for field in self.fields:
                self.fields[field].widget.attrs['readonly'] = True


class EmpresaForm(forms.ModelForm):
    class Meta:
        model = Empresa
        fields = '__all__'
        widgets = {
            'pais': autocomplete.ModelSelect2(url='bar:pais-autocomplete'),
            'ciudad': autocomplete.ModelSelect2(url='bar:ciudad-autocomplete', forward=['pais']),
            'fecha_apertura': DateWidget,
        }


class FacturaProveedorForm(forms.ModelForm):

    total_pago_factura = forms.CharField(widget=forms.TextInput(attrs=ATTR_NUMERICO_RO), label='Total Pago Factura')
    total_factura_compra = forms.CharField(widget=forms.TextInput(attrs=ATTR_NUMERICO_RO), label='Total Factura Compra')

    class Media:
        js = ('compras/js/autoNumeric.js', 'compras/js/factura_proveedor.js')

    class Meta:
        model = FacturaProveedor
        fields = '__all__'
        # localized_fields = ['total_pago_factura']

    def clean(self):
        super(FacturaProveedorForm, self).clean()
        total_factura_compra = self.data.get('total_factura_compra', '') or 0
        total_pago_factura = self.data.get('total_pago_factura', '') or 0

        if Decimal(total_factura_compra) < Decimal(total_pago_factura):
            raise ValidationError('El total del pago no debe exceder el monto de la factura ')


class OrdenCompraForm(forms.ModelForm):

    linea_credito = forms.CharField(widget=forms.TextInput(attrs=ATTR_NUMERICO_RO),
                                    label='Disponible Linea de Crédito', required=False)
    total_orden_compra = forms.CharField(widget=forms.TextInput(attrs=ATTR_NUMERICO_RO_RESALTADO),
                                         label=mark_safe('<strong style="font-size: 20px;">Total</strong>'),
                                         required=False)

    class Meta:
        model = OrdenCompra
        fields = '__all__'
        # localized_fields = ['total_orden_compra']
        widgets = {
            'proveedor_orden_compra': autocomplete.ModelSelect2(url='compras:proveedor-orden-compra-autocomplete'),
        }

    def __init__(self, *args, **kwargs):
        super(OrdenCompraForm, self).__init__(*args, **kwargs)
        # print self.fields['total_orden_compra'].id_for_label,' pobaasdf'

        if self.instance and self.instance.pk:
            self.initial['linea_credito'] = self.instance.get_linea_credito()

    def clean(self):
        super(OrdenCompraForm, self).clean()
        linea_credito = self.data.get('linea_credito', '')
        if not linea_credito:
            raise ValidationError('Debe existir una Linea de Credito para el Proveedor.')
        total_orden_compra = self.data.get('total_orden_compra', '')
        if not total_orden_compra:
            raise ValidationError('El Total de la Orden de Compra no puede ser 0.')
        if Decimal(linea_credito) < Decimal(total_orden_compra):
            raise ValidationError('El Total de la Orden de Compra no debe superar el monto de la Linea de Credito. '
                                  'Linea de Credito Disponible: %s Gs.' % linea_credito)


class OrdenCompraDetalleForm(forms.ModelForm):

    precio_producto_orden_compra = forms.CharField(widget=forms.TextInput(attrs=ATTR_NUMERICO),
                                                   label='Precio del Producto', required=False)
    # unidad_medida_orden_compra = forms.CharField(widget=forms.TextInput(attrs=ATTR_NUMERICO_RO),
    #                                                      label='Un. Med. Compra2', required=False)
    cantidad_producto_orden_compra = forms.CharField(widget=forms.TextInput(attrs=ATTR_NUMERICO),
                                                     label='Cantidad del Producto', required=False)
    total_producto_orden_compra = forms.CharField(widget=forms.TextInput(attrs=ATTR_NUMERICO_RO),
                                                  label='Total del Producto', required=False)

    class Media:
        js = ('compras/js/autoNumeric.js', 'compras/js/orden_compra.js')

    class Meta:
        model = OrdenCompraDetalle
        fields = '__all__'
        # localized_fields = ['precio_producto_orden_compra', 'total_producto_orden_compra']
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
        # localized_fields = ['total_compra']


class CompraDetalleForm(forms.ModelForm):
    class Meta:
        model = CompraDetalle
        fields = '__all__'
        # localized_fields = ['precio_producto_compra', 'total_producto_compra']