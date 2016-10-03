# -*- coding: utf-8 -*-
import re
from django.contrib.admin.widgets import AdminDateWidget
from suit.widgets import SuitDateWidget

__author__ = 'pmmr'
# from input_mask.widgets import InputMask
# from input_mask.contrib.localflavor.us.widgets import USDecimalInput
import datetime
from django.utils import timezone
from decimal import Decimal
from dal import autocomplete
from django.core.exceptions import ValidationError, NON_FIELD_ERRORS
from django.utils.translation import ugettext_lazy as _
from django.utils.safestring import mark_safe
from django import forms
# from django.utils import timezone
from compras.models import Proveedor, LineaCreditoProveedor, LineaCreditoProveedorDetalle, ProveedorTelefono, \
    OrdenPago, PagoProveedor, FacturaProveedor, Empresa, OrdenCompra, OrdenCompraDetalle, Compra, \
    CompraDetalle, OrdenPagoDetalle
from stock.models import Producto
# from bar.models import OrdenCompraEstado
from datetimewidget.widgets import DateWidget
from django.core.validators import RegexValidator

numero_factura = RegexValidator(r'^999-999-9999999$', 'Ingrese el Numero de Factura en el formato "999-999-9999999".')
ATTR_NUMERICO = {'style': 'text-align:right;', 'class': 'auto', 'data-a-sep': '.', 'data-a-dec': ',',
                 'type': 'number'}
ATTR_NUMERICO_RO = {'style': 'text-align:right;', 'class': 'auto', 'data-a-sep': '.', 'data-a-dec': ',',
                    'type': 'number', 'readonly': 'readonly'}
ATTR_NUMERICO_RO_RESALTADO = ATTR_NUMERICO_RO.copy()
ATTR_NUMERICO_RO_RESALTADO['style'] += 'font-size: 20px; height: 25px; font-weight: bold; color: indianred;'
ATTR_NUMERICO_RO_RESALTADO_2 = ATTR_NUMERICO_RO.copy()
ATTR_NUMERICO_RO_RESALTADO_2['style'] += 'font-size: 14px; height: 20px; font-weight: bold; color: darkorange;'

# class NumeroFacturaInput(InputMask):
#     mask = {
#         'mask': '999-999-9999999'
#     }


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

    def __init__(self, *args, **kwargs):
        super(ProveedorTelefonoForm, self).__init__(*args, **kwargs)

        self.fields['codigo_pais_telefono'].widget.attrs.update({'style': 'font-size: 15px; height: 30px; width: 300px; font-weight: bold; color: yellowgreen;'})


class LineaCreditoProveedorInlineForm(forms.ModelForm):
    class Meta:
        model = LineaCreditoProveedor
        fields = '__all__'
        # localized_fields = ['linea_credito_proveedor', 'monto_total_facturas_proveedor', 'monto_total_pagos_proveedor',
        #                     'uso_linea_credito_proveedor']


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
        # widgets = {
        #     'monto_pago_proveedor': USDecimalInput,
        # }

    def __init__(self, *args, **kwargs):
        super(PagoProveedorForm, self).__init__(*args, **kwargs)

        pago = self.instance
        if pago and pago.pk:
            for field in self.fields:
                if pago.procesado is True:
                    self.fields['monto_pago_proveedor'].widget = forms.TextInput(attrs=ATTR_NUMERICO_RO)
                    self.fields['fecha_pago_proveedor'].widget = forms.DateInput(format=('%d/%m/%Y'),
                                                                                 attrs={'style': 'text-align:right;',
                                                                                        'readonly': 'readonly'})
                    self.fields['numero_comprobante_pago'].widget = forms.TextInput(attrs=ATTR_NUMERICO_RO)
                    # self.fields['numero_comprobante_pago'].widget = forms.BooleanField()
                    # self.fields[field].widget.attrs['readonly'] = True
                    # self.fields[field].widget.attrs['disabled'] = True


class FacturaProveedorForm(forms.ModelForm):

    estado_factura_compra = forms.CharField(widget=forms.TextInput, label='Estado de la Factura')
    total_pago_factura = forms.CharField(widget=forms.TextInput(attrs=ATTR_NUMERICO_RO), label='Total Pago Factura')
    total_factura_compra = forms.CharField(widget=forms.TextInput(attrs=ATTR_NUMERICO_RO), label='Total Factura Compra')

    class Meta:
        model = FacturaProveedor
        fields = '__all__'
        # error_messages = {
        #     NON_FIELD_ERRORS: {
        #         'unique_together': "%(model_name)s's %(field_labels)s are not unique.",
        #     }
        # }
        # localized_fields = ['total_pago_factura']
        # widgets = {
        #     'total_factura_compra': USDecimalInput,
        # }

    def __init__(self, *args, **kwargs):
        super(FacturaProveedorForm, self).__init__(*args, **kwargs)
        # print self.fields['total_orden_compra'].id_for_label,' pobaasdf'

        # import pdb
        # pdb.set_trace()

        factura = self.instance
        print 'Factura: %s' % factura

        # if self.instance and self.instance.pk:
        if factura and factura.pk:
            # print linea_credito.instance.get_monto_total_facturas_proveedor()
            # self.initial['monto_total_facturas_proveedor'] = linea_credito.get_monto_total_facturas_proveedor()

            # self.instance.save()
            print 'factura.total_pago_factura before save: %s' % factura.total_pago_factura
            print 'factura.estado_factura_compra before save: %s' % factura.estado_factura_compra
            factura.total_pago_factura = factura.get_total_pago_factura()
            factura.estado_factura_compra = factura.get_estado_factura_compra()
            self.initial['total_pago_factura'] = factura.total_pago_factura
            self.initial['estado_factura_compra'] = factura.estado_factura_compra
            factura.save()
            print 'factura.total_pago_factura after save: %s' % factura.total_pago_factura
            print 'factura.estado_factura_compra after save: %s' % factura.estado_factura_compra

            # for field in self.fields:
            #     self.fields[field].widget.attrs['readonly'] = True
            #     self.fields['linea_credito_proveedor'].widget.attrs['readonly'] = False

            # self.fields['estado_linea_credito_proveedor'].widget.attrs['readonly'] = False
            if factura.estado_factura_compra.estado_factura_proveedor == 'PAG':
                self.fields['estado_factura_compra'].widget.attrs.update({'style': 'font-size: 15px; height: 30px; width: 300px; font-weight: bold; color: green;'})
            elif factura.estado_factura_compra.estado_factura_proveedor == 'FPP':
                self.fields['estado_factura_compra'].widget.attrs.update({'style': 'font-size: 15px; height: 30px; width: 300px; font-weight: bold; color: red;'})
            elif factura.estado_factura_compra.estado_factura_proveedor == 'CAN':
                self.fields['estado_factura_compra'].widget.attrs.update({'style': 'font-size: 15px; height: 30px; width: 300px; font-weight: bold; color: orange;'})
            elif factura.estado_factura_compra.estado_factura_proveedor == 'EPP':
                self.fields['estado_factura_compra'].widget.attrs.update({'style': 'font-size: 15px; height: 30px; width: 300px; font-weight: bold; color: yellowgreen;'})
            self.fields['estado_factura_compra'].widget.attrs['readonly'] = True
            self.fields['estado_factura_compra'].widget.attrs['disabled'] = True
            # self.fields['estado_linea_credito_proveedor'].widget.attrs['required'] = False

    def clean(self):
        super(FacturaProveedorForm, self).clean()
        total_factura_compra = self.data.get('total_factura_compra', '') or 0
        total_pago_factura = self.data.get('total_pago_factura', '') or 0

        if Decimal(total_factura_compra) < Decimal(total_pago_factura):
            raise ValidationError('El Monto Total del Pago no debe exceder al Total de la Factura.')


# class AnularOrdenPagoForm(forms.ModelForm):
#
#     class Meta:
#         model = OrdenPago
#         fields = ['motivo_anulacion', 'observaciones_anulacion', 'usuario_anulacion', 'fecha_hora_anulacion']


class OrdenPagoDetalleForm(forms.ModelForm):

    # procesar = forms.BooleanField(label='Procesar?2',
    #                               required=False,
    #                               help_text='Marque esta casilla si la factura sera incluida en la Orden de Pago.2')

    class Meta:
        model = OrdenPagoDetalle
        fields = '__all__'


class OrdenPagoForm(forms.ModelForm):

    total_orden_pago = forms.CharField(widget=forms.TextInput(attrs=ATTR_NUMERICO_RO_RESALTADO),
                                       label=mark_safe('<strong style="font-size: 20px;">Total</strong>'),
                                       required=False, initial=0)

    class Meta:
        model = OrdenPago
        fields = '__all__'


class EmpresaForm(forms.ModelForm):
    class Meta:
        model = Empresa
        fields = '__all__'
        widgets = {
            'pais': autocomplete.ModelSelect2(url='bar:pais-autocomplete'),
            'ciudad': autocomplete.ModelSelect2(url='bar:ciudad-autocomplete', forward=['pais']),
            'fecha_apertura': DateWidget,
        }


# class CancelarOrdenCompraForm(forms.ModelForm):
#
#     class Meta:
#         model = OrdenCompra
#         fields = ['motivo_cancelacion', 'observaciones_cancelacion', 'usuario_cancelacion', 'fecha_hora_cancelacion']


class OrdenCompraForm(forms.ModelForm):

    linea_credito = forms.CharField(widget=forms.TextInput(attrs=ATTR_NUMERICO_RO_RESALTADO_2),
                                    label=mark_safe('<strong style="font-size: 14px;">Disponible Linea de Credito</strong>'),
                                    required=False)  # initial=0
    total_orden_compra = forms.CharField(widget=forms.TextInput(attrs=ATTR_NUMERICO_RO_RESALTADO),
                                         label=mark_safe('<strong style="font-size: 20px;">Total</strong>'),
                                         required=False, initial=0)

    class Meta:
        model = OrdenCompra
        fields = '__all__'
        exclude = ['motivo', 'observaciones']
        # localized_fields = ['total_orden_compra']
        widgets = {
            'proveedor_orden_compra': autocomplete.ModelSelect2(url='compras:proveedor-orden-compra-autocomplete'),
        }

    def __init__(self, *args, **kwargs):
        super(OrdenCompraForm, self).__init__(*args, **kwargs)
        # print self.fields['total_orden_compra'].id_for_label,' pobaasdf'

        if self.instance and self.instance.pk:
            self.initial['linea_credito'] = self.instance.get_linea_credito() or 0

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
                                                   label='Precio Compra del Producto', required=False)
    # unidad_medida_orden_compra = forms.CharField(widget=forms.TextInput(attrs=ATTR_NUMERICO_RO),
    #                                                      label='Un. Med. Compra2', required=False)
    cantidad_producto_orden_compra = forms.CharField(widget=forms.TextInput(attrs=ATTR_NUMERICO),
                                                     label='Cantidad del Producto', required=False)
    total_producto_orden_compra = forms.CharField(widget=forms.TextInput(attrs=ATTR_NUMERICO_RO), initial=0,
                                                  label='Total del Producto', required=False)

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

    nro_orden_compra = forms.ModelChoiceField(queryset=OrdenCompra.objects.all(),
                                              widget=autocomplete.ModelSelect2(url='compras:ordencompra-compra-autocomplete'),
                                              # widget=forms.TextInput(attrs=ATTR_NUMERICO),
                                              label='Ordenes de Compra disponibles',
                                              required=False, initial=0,
                                              help_text='Seleccione el Numero de Orden de Compra para la cual se '
                                                        'confirmara la Compra.')
    # numero_orden_compra = forms.CharField(widget=forms.TextInput,
    #                                       label='Numero Orden de Compra2',
    #                                       required=False, initial=0,
    #                                       help_text='Numero Orden de Compra seleccionada2.')
    disponible_linea_credito_proveedor = forms.CharField(widget=forms.TextInput(attrs=ATTR_NUMERICO_RO_RESALTADO_2),
                                                         label=mark_safe('<strong style="font-size: 14px;">Disponible Linea de Credito</strong>'),
                                                         required=False, initial=0)
    total_compra = forms.CharField(widget=forms.TextInput(attrs=ATTR_NUMERICO_RO_RESALTADO),
                                   label=mark_safe('<strong style="font-size: 20px;">Total</strong>'),
                                   required=False, initial=0)

    class Meta:
        model = Compra
        fields = '__all__'
        # error_messages = {
        #     NON_FIELD_ERRORS: {
        #         'unique_together': "%(model_name)s's %(field_labels)s are not unique.",
        #     }
        # }
        # localized_fields = ['total_compra']
        # widgets = {
        #     # 'proveedor': autocomplete.ModelSelect2(url='compras:proveedor-orden-compra-autocomplete'),
        #     # 'numero_factura_compra': NumeroFacturaInput,
        #     # 'nro_orden_compra': autocomplete.ModelSelect2(url='compras:ordencompra-compra-autocomplete'),
        # }

    #     # print self.fields['total_orden_compra'].id_for_label,' pobaasdf'
    #
    #     # import pdb
    #     # pdb.set_trace()
    #
    #     # if self.instance and self.instance.pk:
    #     #     self.initial['numero_orden_compra'] = self.instance.numero_orden_compra_id or 0
    #
    #     # if self.instance.estado_compra.estado_orden_compra in ('ENT', 'CAN'):
    #     #     if 'nro_orden_compra' in self.fields: del self.fields['nro_orden_compra']

    def __init__(self, *args, **kwargs):
        super(CompraForm, self).__init__(*args, **kwargs)

        # import pdb
        # pdb.set_trace()

        # Recargar los datos de la Orden de Compra por si haya tenido alguna modificacion
        compra = self.instance

        if compra.pk and self.request.method == 'GET' and compra.estado_compra.estado_orden_compra == 'PEN':
            orden_compra = OrdenCompra.objects.get(numero_orden_compra=compra.numero_orden_compra_id)
            print 'compra.total_compra before save: %s' % compra.total_compra
            compra.total_compra = orden_compra.total_orden_compra

            print 'compra.numero_compra: %s - compra_detalle_a_eliminar: %s' % (compra.numero_compra, CompraDetalle.objects.filter(numero_compra_id=compra.numero_compra))
            CompraDetalle.objects.filter(numero_compra_id=compra.numero_compra).delete()
            print 'compra_detalle_a_eliminar: ', CompraDetalle.objects.filter(numero_compra_id=compra.numero_compra)

            for detalle in OrdenCompraDetalle.objects.filter(numero_orden_compra_id=compra.numero_orden_compra_id):
                compra_detalle = CompraDetalle(numero_compra_id=compra.numero_compra,
                                               producto_compra_id=detalle.producto_orden_compra_id,
                                               precio_producto_compra=detalle.precio_producto_orden_compra,
                                               cantidad_producto_compra=detalle.cantidad_producto_orden_compra,
                                               unidad_medida_compra=detalle.unidad_medida_orden_compra,
                                               total_producto_compra=detalle.total_producto_orden_compra)
                compra_detalle.save()
            compra.save()
            self.initial['total_compra'] = compra.total_compra
            print 'compra.total_compra after save: %s' % compra.total_compra

    def clean(self):
        super(CompraForm, self).clean()

        # import pdb
        # pdb.set_trace()

        # 1) Valida que nro_ord_compra contenga un valor valido.
        nro_ord_compra = self.data.get('nro_orden_compra')
        if nro_ord_compra is None:
            ord_compra = self.instance.numero_orden_compra
        else:
            ord_compra = OrdenCompra.objects.get(pk=nro_ord_compra)
        # if not nro_ord_compra:
        #     # pass
        #     raise ValidationError({'nro_orden_compra': 'Debe seleccionar un Numero de Orden de Compra valido.'})

        # 2) Valida que exista una Linea de Credito para el Proveedor.
        linea_credito = self.data.get('disponible_linea_credito_proveedor', '')
        if not linea_credito:
            raise ValidationError('Debe existir una Linea de Credito para el Proveedor.')

        # 3) Valida que el Total de la Compra no sea 0.
        total_compra = self.data.get('total_compra', '')
        if not total_compra:
            raise ValidationError('El Total de la Compra no puede ser 0.')

        # 4) Valida que la fecha_factura_compra no sea menor que la fecha_orden_compra
        # if self.pk is not None:
        #     compra_inicial = Compra.objects.get(pk=self.pk)

        fecha_ord_compra = timezone.localtime(ord_compra.fecha_orden_compra).date()
        fecha_aux = self.data.get('fecha_factura_compra', '')
        if fecha_aux == '':
            fecha_fac_compra = datetime.date.today()
        else:
            fecha_fac_compra = datetime.datetime.strptime(fecha_aux, '%d/%m/%Y').date()

        print 'fecha_fac_compra: %s - ord_compra.fecha_orden_compra: %s' % \
              (fecha_fac_compra, fecha_ord_compra)

        if fecha_fac_compra < fecha_ord_compra:
            raise ValidationError({'fecha_factura_compra': _('La Fecha de la Factura no puede ser menor que la '
                                                             'Fecha de la Orden de Compra. Nro. Orden Compra: %s - '
                                                             'Fecha Orden de Compra: %s' % (ord_compra.pk, datetime.datetime.strftime(fecha_ord_compra, '%d/%m/%Y')))})

        if '_save' in self.request.POST or '_cancel' in self.request.POST:
            # 5) ==> Valida el formato del campo "numero_factura_compra".
            # Mejorar la validacion con RegEx. OK!
            nro_factura = self.data.get('numero_factura_compra', '')
            # if not nro_factura or len(nro_factura) != 15 or '-' not in nro_factura or nro_factura[3] != '-' or nro_factura[7] != '-' :
            if not nro_factura or not re.match(r'^[0-9]{3,}-[0-9]{3,}-[0-9]{7,}$', nro_factura):
                raise ValidationError({'numero_factura_compra': ('Numero de Factura no valido. Ingrese el Numero de '
                                                                 'Factura en el formato "999-999-9999999".')})

            # 6) ==> Validar si ya existe ['proveedor', 'numero_factura_compra', 'fecha_factura_compra'] y emitir un mensaje
            # informando al respecto para evitar un error de integridad al intentar insertar el registro en la DB.
            # No deben existir dos facturas con el mismo numero para el mismo proveedor en la misma fecha.
            proveedor = self.instance.proveedor.pk
            # fecha = self.data.get('fecha_factura_compra', '')
            # fecha = self.instance.fecha_factura_compra
            # fecha_factura = timezone.localtime(fecha)
            # fecha_aux = self.data.get('fecha_factura_compra', '')
            # fecha_fac_compra = datetime.datetime.strptime(fecha_aux, '%d/%m/%Y').date()

            # Dar el formato correcto a la fecha con alguna funcion que convierta una fecha naive a timezone dependiente.
            # No fue necesario. Se trajo el valor del campo de la instancia y no del cleaned_data.
            # if fecha:
            #     aux = fecha.split('/')
            #     fecha = '%s-%s-%s' % (aux[2], aux[1], aux[0])

            print 'Proveedor: %s - fecha_factura_compra: %s - nro_factura: %s' % (proveedor, fecha_fac_compra, nro_factura)

            if FacturaProveedor.objects.filter(numero_factura_compra=nro_factura, proveedor_id=proveedor,
                                               fecha_factura_compra=fecha_fac_compra).exists():
                                     # fecha_factura_compra=datetime.datetime.strftime(fecha, '%d/%m/%Y')).exists():
                print 'EXISTE UNA FACTURA'
                raise ValidationError({'numero_factura_compra': ('Ya existe una factura con el Numero de Factura y Fecha '
                                                                 'de Factura indicados para el Proveedor al cual se desea'
                                                                 'confirmar la compra.')})


# ======================================================================================================================
# class CancelarCompraForm(forms.ModelForm):
#
#     nro_orden_compra = forms.ModelChoiceField(queryset=OrdenCompra.objects.all(),
#                                               widget=autocomplete.ModelSelect2(url='compras:ordencompra-compra-autocomplete'),
#                                               # widget=forms.TextInput(attrs=ATTR_NUMERICO),
#                                               label='Ordenes de Compra disponibles',
#                                               required=False, initial=0,
#                                               help_text='Seleccione el Numero de Orden de Compra para la cual se '
#                                                         'confirmara la Compra.')
#
#     class Meta:
#         model = Compra
#         fields = ['motivo_cancelacion', 'observaciones_cancelacion', 'usuario_cancelacion', 'fecha_hora_cancelacion']


# class CancelarCompraForm(forms.ModelForm):
#
#     nro_orden_compra = forms.ModelChoiceField(queryset=OrdenCompra.objects.all(),
#                                               widget=autocomplete.ModelSelect2(url='compras:ordencompra-compra-autocomplete'),
#                                               # widget=forms.TextInput(attrs=ATTR_NUMERICO),
#                                               label='Ordenes de Compra disponibles',
#                                               required=False, initial=0,
#                                               help_text='Seleccione el Numero de Orden de Compra para la cual se '
#                                                         'confirmara la Compra.')
#
#     class Meta:
#         model = Compra
#         # fields = ['numero_orden_compra', 'proveedor', 'disponible_linea_credito_proveedor', 'numero_factura_compra',
#         #           'tipo_factura_compra', 'estado_compra', 'total_compra', 'fecha_factura_compra', 'motivo_cancelacion',
#         #           'observaciones_cancelacion', 'usuario_cancelacion', 'fecha_hora_cancelacion']
#         fields = '__all__'
#
#     def clean(self):
#         super(CancelarCompraForm, self).clean()
#
#         import pdb
#         pdb.set_trace()
#
#         # 1) Valida que nro_ord_compra contenga un valor valido.
#         nro_ord_compra = self.data.get('nro_orden_compra')
#         if nro_ord_compra is None:
#             ord_compra = self.instance.numero_orden_compra
#         else:
#             ord_compra = OrdenCompra.objects.get(pk=nro_ord_compra)
#         # if not nro_ord_compra:
#         #     # pass
#         #     raise ValidationError({'nro_orden_compra': 'Debe seleccionar un Numero de Orden de Compra valido.'})
#
#         # # 2) Valida que exista una Linea de Credito para el Proveedor.
#         # linea_credito = self.data.get('disponible_linea_credito_proveedor', '')
#         # if not linea_credito:
#         #     raise ValidationError('Debe existir una Linea de Credito para el Proveedor.')
#
#         # # 3) Valida que el Total de la Compra no sea 0.
#         # total_compra = self.data.get('total_compra', '')
#         # if not total_compra:
#         #     raise ValidationError('El Total de la Compra no puede ser 0.')
#
#         # 4) Valida que la fecha_factura_compra no sea menor que la fecha_orden_compra
#         # if self.pk is not None:
#         #     compra_inicial = Compra.objects.get(pk=self.pk)
#
#         fecha_ord_compra = timezone.localtime(ord_compra.fecha_orden_compra).date()
#         fecha_aux = self.data.get('fecha_factura_compra', '')
#         fecha_fac_compra = datetime.datetime.strptime(fecha_aux, '%d/%m/%Y').date()
#
#         print 'fecha_fac_compra: %s - ord_compra.fecha_orden_compra: %s' % \
#               (fecha_fac_compra, fecha_ord_compra)
#
#         if fecha_fac_compra < fecha_ord_compra:
#             raise ValidationError({'fecha_factura_compra': _('La Fecha de la Factura no puede ser menor que la '
#                                                              'Fecha de la Orden de Compra. Nro. Orden Compra: %s - '
#                                                              'Fecha Orden de Compra: %s' % (ord_compra.pk, datetime.datetime.strftime(fecha_ord_compra, '%d/%m/%Y')))})
#
#         # if '_save' in self.request.POST:
#         # 5) ==> Valida el formato del campo "numero_factura_compra".
#         # Mejorar la validacion con RegEx. OK!
#         nro_factura = self.data.get('numero_factura_compra', '')
#         # if not nro_factura or len(nro_factura) != 15 or '-' not in nro_factura or nro_factura[3] != '-' or nro_factura[7] != '-' :
#         if not nro_factura or not re.match(r'^[0-9]{3,}-[0-9]{3,}-[0-9]{7,}$', nro_factura):
#             raise ValidationError({'numero_factura_compra': ('Numero de Factura no valido. Ingrese el Numero de '
#                                                              'Factura en el formato "999-999-9999999".')})
#
#         # 6) ==> Validar si ya existe ['proveedor', 'numero_factura_compra', 'fecha_factura_compra'] y emitir un mensaje
#         # informando al respecto para evitar un error de integridad al intentar insertar el registro en la DB.
#         # No deben existir dos facturas con el mismo numero para el mismo proveedor en la misma fecha.
#         proveedor = self.instance.proveedor.pk
#         # fecha = self.data.get('fecha_factura_compra', '')
#         # fecha = self.instance.fecha_factura_compra
#         # fecha_factura = timezone.localtime(fecha)
#         # fecha_aux = self.data.get('fecha_factura_compra', '')
#         # fecha_fac_compra = datetime.datetime.strptime(fecha_aux, '%d/%m/%Y').date()
#
#         # Dar el formato correcto a la fecha con alguna funcion que convierta una fecha naive a timezone dependiente.
#         # No fue necesario. Se trajo el valor del campo de la instancia y no del cleaned_data.
#         # if fecha:
#         #     aux = fecha.split('/')
#         #     fecha = '%s-%s-%s' % (aux[2], aux[1], aux[0])
#
#         print 'Proveedor: %s - fecha_factura_compra: %s - nro_factura: %s' % (proveedor, fecha_fac_compra, nro_factura)
#
#         if FacturaProveedor.objects.filter(numero_factura_compra=nro_factura, proveedor_id=proveedor,
#                                            fecha_factura_compra=fecha_fac_compra).exists():
#                                  # fecha_factura_compra=datetime.datetime.strftime(fecha, '%d/%m/%Y')).exists():
#             print 'EXISTE UNA FACTURA'
#             raise ValidationError({'numero_factura_compra': ('Ya existe una factura con el Numero de Factura y Fecha '
#                                                              'de Factura indicados para el Proveedor al cual se desea'
#                                                              'confirmar la compra.')})


# class ConfirmarCompraForm(forms.ModelForm):
#
#     nro_orden_compra = forms.ModelChoiceField(queryset=OrdenCompra.objects.all(),
#                                               widget=autocomplete.ModelSelect2(url='compras:ordencompra-compra-autocomplete'),
#                                               # widget=forms.TextInput(attrs=ATTR_NUMERICO),
#                                               label='Ordenes de Compra disponibles',
#                                               required=False, initial=0,
#                                               help_text='Seleccione el Numero de Orden de Compra para la cual se '
#                                                         'confirmara la Compra.')
#     # numero_orden_compra = forms.CharField(widget=forms.TextInput,
#     #                                       label='Numero Orden de Compra2',
#     #                                       required=False, initial=0,
#     #                                       help_text='Numero Orden de Compra seleccionada2.')
#     disponible_linea_credito_proveedor = forms.CharField(widget=forms.TextInput(),  # attrs=ATTR_NUMERICO_RO_RESALTADO_2
#                                                          label=mark_safe('<strong style="font-size: 14px;">Disponible Linea de Credito</strong>'),
#                                                          required=False, initial=0)
#     # fecha_factura_compra = forms.DateField(required=False, input_formats=['%d/%m/%Y'])
#     total_compra = forms.CharField(widget=forms.TextInput(),  # attrs=ATTR_NUMERICO_RO_RESALTADO
#                                    label=mark_safe('<strong style="font-size: 20px;">Total</strong>'),
#                                    required=False, initial=0)
#
#     class Meta:
#         model = Compra
#         fields = '__all__'
#         widgets = {
#             # 'fecha_factura_compra': SuitDateWidget,
#             'fecha_factura_compra': AdminDateWidget,
#         }
#
#     def clean(self):
#         super(ConfirmarCompraForm, self).clean()
#
#         import pdb
#         pdb.set_trace()
#
#         # # 1) ==> Valida que nro_ord_compra contenga un valor valido.
#         # nro_ord_compra = self.data.get('nro_orden_compra', '')
#         # if not nro_ord_compra:
#         #     # pass
#         #     raise ValidationError({'nro_orden_compra': 'Debe seleccionar un Numero de Orden de Compra valido.'})
#
#         # if not self.numero_orden_compra:
#         #     self.numero_orden_compra = self.instance.numero_orden_compra
#
#         # 2) ==> Valida que exista una Linea de Credito para el Proveedor.
#         linea_credito = self.data.get('disponible_linea_credito_proveedor', '')
#         if not linea_credito:
#             raise ValidationError('Debe existir una Linea de Credito para el Proveedor.')
#
#         # 3) ==> Valida que el Total de la Compra no sea 0.
#         total_compra = self.data.get('total_compra', '')
#         if not total_compra:
#             raise ValidationError('El Total de la Compra no puede ser 0.')
#
#         # 4) ==> Valida que la fecha_factura_compra no sea menor que la fecha_orden_compra
#         # if self.pk is not None:
#         #     compra_inicial = Compra.objects.get(pk=self.pk)
#
#         # ord_compra = OrdenCompra.objects.get(pk=nro_ord_compra)
#         # nro_oc = self.data.get('numero_orden_compra', '')
#         ord_compra = self.instance.numero_orden_compra
#         # ord_compra = OrdenCompra.objects.get(pk=nro_oc.pk)
#         fecha_ord_compra = timezone.localtime(ord_compra.fecha_orden_compra).date()
#         fecha_aux = self.data.get('fecha_factura_compra', '')
#         fecha_fac_compra = datetime.datetime.strptime(fecha_aux, '%d/%m/%Y').date()
#
#         print 'fecha_fac_compra: %s - ord_compra.fecha_orden_compra: %s' % \
#               (fecha_fac_compra, fecha_ord_compra)
#
#         if fecha_fac_compra < fecha_ord_compra:
#             raise ValidationError({'fecha_factura_compra': _('La Fecha de la Factura no puede ser menor que la '
#                                                              'Fecha de la Orden de Compra. Nro. Orden Compra: %s - '
#                                                              'Fecha Orden de Compra: %s' % (ord_compra.pk, datetime.datetime.strftime(fecha_ord_compra, '%d/%m/%Y')))})

        # # 5) ==> Valida el formato del campo "numero_factura_compra".
        # # Mejorar la validacion con RegEx. OK!
        # nro_factura = self.data.get('numero_factura_compra', '')
        # # if not nro_factura or len(nro_factura) != 15 or '-' not in nro_factura or nro_factura[3] != '-' or nro_factura[7] != '-' :
        # if not nro_factura or not re.match(r'^[0-9]{3,}-[0-9]{3,}-[0-9]{7,}$', nro_factura):
        #     raise ValidationError({'numero_factura_compra': ('Numero de Factura no valido. Ingrese el Numero de '
        #                                                      'Factura en el formato "999-999-9999999".')})
        #
        # # 6) ==> Validar si ya existe ['proveedor', 'numero_factura_compra', 'fecha_factura_compra'] y emitir un mensaje
        # # informando al respecto para evitar un error de integridad al intentar insertar el registro en la DB.
        # # No deben existir dos facturas con el mismo numero para el mismo proveedor en la misma fecha.
        # proveedor = self.instance.proveedor.pk
        # # fecha = self.data.get('fecha_factura_compra', '')
        # # fecha = self.instance.fecha_factura_compra
        # # fecha_factura = timezone.localtime(fecha)
        # # fecha_aux = self.data.get('fecha_factura_compra', '')
        # # fecha_fac_compra = datetime.datetime.strptime(fecha_aux, '%d/%m/%Y').date()
        #
        # # Dar el formato correcto a la fecha con alguna funcion que convierta una fecha naive a timezone dependiente.
        # # No fue necesario. Se trajo el valor del campo de la instancia y no del cleaned_data.
        # # if fecha:
        # #     aux = fecha.split('/')
        # #     fecha = '%s-%s-%s' % (aux[2], aux[1], aux[0])
        #
        # print 'Proveedor: %s - fecha_factura_compra: %s - nro_factura: %s' % (proveedor, fecha_fac_compra, nro_factura)
        #
        # if FacturaProveedor.objects.filter(numero_factura_compra=nro_factura, proveedor_id=proveedor,
        #                                    fecha_factura_compra=fecha_fac_compra).exists():
        #                          # fecha_factura_compra=datetime.datetime.strftime(fecha, '%d/%m/%Y')).exists():
        #     print 'EXISTE UNA FACTURA'
        #     raise ValidationError({'numero_factura_compra': ('Ya existe una factura con el Numero de Factura y Fecha '
        #                                                      'de Factura indicados para el Proveedor al cual se desea'
        #                                                      'confirmar la compra.')})
# ======================================================================================================================


class CompraDetalleForm(forms.ModelForm):

    # precio_producto_compra = forms.CharField(widget=forms.TextInput(attrs=ATTR_NUMERICO),
    #                                          label='Precio del Producto', required=False)
    # # unidad_medida_compra = forms.CharField(widget=forms.TextInput(attrs=ATTR_NUMERICO_RO),
    # #                                        label='Un. Med. Compra2', required=False)
    # cantidad_producto_compra = forms.CharField(widget=forms.TextInput(attrs=ATTR_NUMERICO),
    #                                            label='Cantidad del Producto', required=False)
    # total_producto_compra = forms.CharField(widget=forms.TextInput(attrs=ATTR_NUMERICO_RO),
    #                                         label='Total del Producto', required=False)

    class Meta:
        model = CompraDetalle
        fields = '__all__'
        # localized_fields = ['precio_producto_compra', 'total_producto_compra']