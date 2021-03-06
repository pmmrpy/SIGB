import datetime
from decimal import Decimal
import pdb
from django.conf.urls import patterns
from django.contrib import admin
from django.contrib.admin.options import IS_POPUP_VAR, TO_FIELD_VAR
from django.contrib.admin.templatetags.admin_urls import add_preserved_filters
from django.contrib.messages.context_processors import messages
from django.db.models.expressions import Value, RawSQL
from django.db.models.fields import CharField
from django.db.models.query_utils import Q
from django.forms.models import BaseInlineFormSet
from django.http.response import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template.context import RequestContext
from django.template.response import SimpleTemplateResponse
from django.utils import timezone
from django.core.exceptions import ValidationError
from django.utils.encoding import force_text
from django.utils.html import format_html, escape, escapejs
from django.utils.translation import ugettext_lazy as _
from django.views.generic.dates import timezone_today
from pip._vendor.requests.packages.urllib3 import response
from psycopg2._psycopg import IntegrityError
from compras.forms import ProveedorForm, LineaCreditoProveedorForm, LineaCreditoProveedorDetalleForm, PagoProveedorForm, \
    FacturaProveedorForm, EmpresaForm, OrdenCompraForm, OrdenCompraDetalleForm, CompraForm, CompraDetalleForm, \
    ProveedorTelefonoForm, LineaCreditoProveedorInlineForm, OrdenPagoDetalleForm, OrdenPagoForm
from compras.models import ProveedorTelefono, LineaCreditoProveedor, LineaCreditoProveedorDetalle, Proveedor, PagoProveedor, \
    FacturaProveedor, ProductoProveedor, Empresa, OrdenCompra, OrdenCompraDetalle, Compra, CompraDetalle, \
    OrdenPago, OrdenPagoDetalle  # , ModelA, ModelB, ModelC
from bar.models import CompraEstado, OrdenCompraEstado, TipoMovimientoStock, Deposito, TipoFacturaCompra, \
    FacturaProveedorEstado, OrdenPagoEstado
from stock.models import MovimientoStock, Producto
from personal.models import Empleado
from django.http import HttpResponse
from geraldo.generators import PDFGenerator
from polymorphic.admin import PolymorphicParentModelAdmin, PolymorphicChildModelAdmin, PolymorphicChildModelFilter

# Register your models here.


def calcular_dv(numero, base=11):
    total = 0
    k = 2
    for i in range(len(numero) - 1, - 1, - 1):
        k = 2 if k > base else k
        total += int(numero[i]) * k
        k += 1
    resto = total % 11
    return (11 - resto) if resto > 1 else 0


class ProveedorTelefonoInline(admin.TabularInline):
    model = ProveedorTelefono
    extra = 0
    min_num = 1
    form = ProveedorTelefonoForm
    verbose_name = 'Telefonos'
    verbose_name_plural = 'Telefonos'


class LineaCreditoProveedorInline(admin.TabularInline):
    model = LineaCreditoProveedor
    extra = 1
    min_num = 1
    can_delete = False
    readonly_fields = ['monto_total_facturas_proveedor', 'monto_total_pagos_proveedor', 'uso_linea_credito_proveedor',
                       'disponible_linea_credito_proveedor', 'estado_linea_credito_proveedor']
    # fields = ['tipo_movimiento', 'monto_movimiento', 'numero_comprobante', 'fecha_movimiento']
    form = LineaCreditoProveedorInlineForm
    verbose_name = 'Linea de Credito'
    verbose_name_plural = 'Linea de Credito'


class ProveedorAdmin(admin.ModelAdmin):

    form = ProveedorForm

    class Media:
        js = [
            'compras/js/proveedor.js'
        ]

    readonly_fields = ('digito_verificador', 'fecha_alta_proveedor')

    # list_editable = ('id', 'proveedor', 'ruc', 'digito_verificador', 'direccion', 'pagina_web')

    fieldsets = [
        ('Empresa', {'fields': ['proveedor', 'persona_proveedor']}),
        ('RUC', {'fields': ['ruc', 'digito_verificador']}),
        ('Direccion', {'fields': ['direccion', ('pais', 'ciudad')]}),
        ('Otros datos', {'fields': ['pagina_web', 'fecha_alta_proveedor']}),
    ]

    inlines = [ProveedorTelefonoInline, LineaCreditoProveedorInline]

    list_display = ('id', 'proveedor', 'persona_proveedor', 'ruc', 'digito_verificador', 'direccion', 'pais',
                    'ciudad', 'pagina_web', 'fecha_alta_proveedor')
    list_display_links = ['proveedor']
    list_filter = ['id', 'proveedor', 'ruc', 'fecha_alta_proveedor']
    search_fields = ['id', 'proveedor', 'ruc', 'fecha_alta_proveedor']

    def get_queryset(self, request):
        queryset = Proveedor.objects.filter(empresa_administrada=False)
        return queryset

    def save_model(self, request, obj, form, change):
        if obj.ruc is not None:
            obj.digito_verificador = calcular_dv(obj.ruc, 11)
        else:
            raise ValidationError({'digito_verificador': _('RUC no valido.')})
        super(ProveedorAdmin, self).save_model(request, obj, form, change)

    def save_formset(self, request, form, formset, change):
        # obj = form.instance
        # print obj
        # queryset = self.get_queryset(request).filter()
        # if not change:
            # obj.disponible_linea_credito_proveedor = self.linea_credito_proveedor
        if not change:
            formset.save()
            for inline in formset:
                if isinstance(inline.instance, LineaCreditoProveedor):
                    linea_credito = inline.instance
                    linea_credito.disponible_linea_credito_proveedor = linea_credito.linea_credito_proveedor
                    linea_credito.save()
        # obj.save()

        if change:
            for inline in formset:
                if isinstance(inline.instance, LineaCreditoProveedor):
                    linea_credito = inline.instance
                    print 'Linea de Credito: %s' % linea_credito
                    # if linea_credito and linea_credito.pk:
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
                    # self.initial['estado_linea_credito_proveedor'] = linea_credito.estado_linea_credito_proveedor
                    linea_credito.save()
                    print 'linea_credito.monto_total_facturas_proveedor after save: %s' % linea_credito.monto_total_facturas_proveedor
                    print 'linea_credito.monto_total_pagos_proveedor after save: %s' % linea_credito.monto_total_pagos_proveedor
                    print 'linea_credito.uso_linea_credito_proveedor after save: %s' % linea_credito.uso_linea_credito_proveedor
                    print 'linea_credito.disponible_linea_credito_proveedor after save: %s' % linea_credito.disponible_linea_credito_proveedor
                    print 'linea_credito.estado_linea_credito_proveedor after save: %s' % linea_credito.estado_linea_credito_proveedor

                    # Se intento asignar atributos HTML al campo "estado_linea_credito_proveedor" pero no se como
                    # capturar la propiedad ya que en este punto no esta disponible "self"
                    # if linea_credito.estado_linea_credito_proveedor == 'DEL':
                    #     self.inline.fields['estado_linea_credito_proveedor'].widget.attrs.update({'style': 'font-size: 15px; height: 30px; width: 300px; font-weight: bold; color: green;'})
                    #     # color = 'green'
                    #     # return format_html('<span style="color: %s"><b> %s </b></span>' %
                    #     #                    (color, obj.get_estado_linea_credito_proveedor_display()))
                    # elif linea_credito.estado_linea_credito_proveedor == 'LIM':
                    #     self.inline.fields['estado_linea_credito_proveedor'].widget.attrs.update({'style': 'font-size: 15px; height: 30px; width: 300px; font-weight: bold; color: orange;'})
                    #     # color = 'red'
                    #     # return format_html('<span style="color: %s"><b> %s </b></span>' %
                    #     #                    (color, obj.get_estado_linea_credito_proveedor_display()))
                    # elif linea_credito.estado_linea_credito_proveedor == 'SOB':
                    #     self.inline.fields['estado_linea_credito_proveedor'].widget.attrs.update({'style': 'font-size: 15px; height: 30px; width: 300px; font-weight: bold; color: red;'})
                    # self.inline.fields['estado_linea_credito_proveedor'].widget.attrs['readonly'] = True
                    # # self.fields['estado_linea_credito_proveedor'].widget.attrs['disabled'] = True

        super(ProveedorAdmin, self).save_formset(request, form, formset, change)


class LineaCreditoProveedorDetalleInline(admin.TabularInline):
    model = LineaCreditoProveedorDetalle
    extra = 0
    can_delete = False
    readonly_fields = ['tipo_movimiento', 'monto_movimiento', 'numero_comprobante', 'fecha_movimiento', 'anulado', 'fecha_hora_anulacion']
    # fields = ['tipo_movimiento', 'monto_movimiento', 'numero_comprobante', 'fecha_movimiento']
    form = LineaCreditoProveedorDetalleForm
    # verbose_name = 'Linea de Credito del Proveedor'
    # verbose_name_plural = 'Lineas de Credito del Proveedor'

    def has_add_permission(self, request):
        return False


class LineaCreditoProveedorAdmin(admin.ModelAdmin):

    form = LineaCreditoProveedorForm

    class Media:
        js = [
            ''
        ]

    readonly_fields = ['proveedor', 'fecha_linea_credito_proveedor',
                       'monto_total_facturas_proveedor', 'monto_total_pagos_proveedor', 'uso_linea_credito_proveedor',
                       'disponible_linea_credito_proveedor']
                       # 'estado_linea_credito_proveedor']

    # raw_id_fields =

    fieldsets = [
        ('Proveedor', {'fields': ['proveedor']}),
        ('Linea de Credito', {'fields': ['linea_credito_proveedor', 'fecha_linea_credito_proveedor']}),
        ('Utilizacion Linea de Credito', {'fields': ['monto_total_facturas_proveedor', 'monto_total_pagos_proveedor',
                                                     'uso_linea_credito_proveedor',
                                                     'disponible_linea_credito_proveedor',
                                                     'estado_linea_credito_proveedor']}),
    ]

    inlines = [LineaCreditoProveedorDetalleInline]

    list_display = ['id', 'proveedor', 'linea_credito_proveedor', 'fecha_linea_credito_proveedor',
                    'monto_total_facturas_proveedor', 'monto_total_pagos_proveedor', 'uso_linea_credito_proveedor',
                    'disponible_linea_credito_proveedor', 'colorea_estado_linea_credito_proveedor']
    list_display_links = ['proveedor']
    list_filter = ['proveedor', 'linea_credito_proveedor', 'fecha_linea_credito_proveedor',
                   'estado_linea_credito_proveedor']
    search_fields = ['proveedor__proveedor', 'linea_credito_proveedor', 'fecha_linea_credito_proveedor',
                     'estado_linea_credito_proveedor']

    def colorea_estado_linea_credito_proveedor(self, obj):
        # color = 'black'
        if obj.estado_linea_credito_proveedor == 'DEL':
            color = 'green'
            return format_html('<span style="color: %s"><b> %s </b></span>' %
                               (color, obj.get_estado_linea_credito_proveedor_display()))
        elif obj.estado_linea_credito_proveedor == 'LIM':
            color = 'orange'
            return format_html('<span style="color: %s"><b> %s </b></span>' %
                               (color, obj.get_estado_linea_credito_proveedor_display()))
        elif obj.estado_linea_credito_proveedor == 'SOB':
            color = 'red'
            return format_html('<span style="color: %s"><b> %s </b></span>' %
                               (color, obj.get_estado_linea_credito_proveedor_display()))
        return obj.estado_linea_credito_proveedor
    colorea_estado_linea_credito_proveedor.short_description = 'Estado Linea de Credito'

    # def get_changeform_initial_data(self, request):
    #     return False

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


class PagoProveedorInline(admin.TabularInline):
    model = PagoProveedor
    extra = 0
    can_delete = False
    # readonly_fields = ['procesado']
    form = PagoProveedorForm
    # verbose_name = 'Pago a Proveedores'
    # verbose_name_plural = 'Pagos a Proveedores'

    def get_readonly_fields(self, request, obj=None):
        # print 'Entra a get_readonly_fields: %s - %s - %s' % (self, request, obj)
        # print 'obj.estado_factura_compra: %s' % (obj.estado_factura_compra)
        #
        # # queryset = self.get_queryset(request).filter(estado_factura_compra='EPP')
        # # for factura in queryset:
        #
        # pagos = PagoProveedor.objects.filter(factura_proveedor_id=obj.id)
        # print 'Pagos: %s' % pagos
        #
        # for pago in pagos:
        #     if obj is not None and pago.procesado is True:  # and obj.estado_factura_compra in ('PAG', 'CAN')
        #         return [i.name for i in self.model._meta.fields]
        #     else:
        #         return None
        #         # return super(PagoProveedorInline, self).get_readonly_fields(request, obj)
        if obj is not None:  # and obj.estado_factura_compra in ('PAG', 'CAN'):
            return [i.name for i in self.model._meta.fields]
        else:
            return super(PagoProveedorInline, self).get_readonly_fields(request, obj)

    # def has_add_permission(self, request):
    #     object_id = request.path.split("/")[-2]
    #     if object_id != "add":
    #         factura_actual = FacturaProveedor.objects.get(pk=object_id)
    #         return factura_actual.estado_factura_compra not in ('PAG', 'CAN')
    #     else:
    #         return super(PagoProveedorInline, self).has_add_permission(request)
    #
    # def has_delete_permission(self, request, obj=None):
    #     if obj is not None and obj.estado_factura_compra in ('PAG', 'CAN'):
    #         return False
    #     return super(PagoProveedorInline, self).has_delete_permission(request, obj)

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


class FacturaProveedorAdmin(admin.ModelAdmin):

    form = FacturaProveedorForm

    class Media:
        js = [
            'compras/js/autoNumeric.js', 'compras/js/factura_proveedor.js'
        ]

    readonly_fields = ['proveedor', 'orden_compra', 'numero_factura_compra', 'fecha_factura_compra', 'tipo_factura_compra',
                       'forma_pago_compra', 'plazo_factura_compra']
                       # 'estado_factura_compra']

    # readonly_fields = ['__all__']

    raw_id_fields = ['compra']

    fieldsets = [
        ('Datos de la Factura', {'fields': ['proveedor', 'orden_compra', 'numero_factura_compra', 'fecha_factura_compra',
                                            'tipo_factura_compra', 'forma_pago_compra', 'plazo_factura_compra',
                                            'total_factura_compra', 'total_pago_factura', 'estado_factura_compra']}),
    ]

    inlines = [PagoProveedorInline]

    list_display = ['numero_factura_compra', 'proveedor', 'orden_compra', 'fecha_factura_compra', 'tipo_factura_compra',
                    'forma_pago_compra', 'plazo_factura_compra', 'total_factura_compra', 'total_pago_factura',
                    'colorea_estado_factura_compra']
    list_display_links = ['numero_factura_compra']
    list_filter = ['proveedor', 'orden_compra', 'numero_factura_compra', 'fecha_factura_compra', 'tipo_factura_compra',
                   'forma_pago_compra', 'plazo_factura_compra', 'estado_factura_compra']
    search_fields = ['proveedor__proveedor', 'orden_compra__numero_orden_compra', 'numero_factura_compra',
                     'fecha_factura_compra', 'tipo_factura_compra__tipo_factura_compra',
                     'forma_pago_compra__forma_pago_compra', 'plazo_factura_compra', 'estado_factura_compra__descripcion']

    def colorea_estado_factura_compra(self, obj):
        # color = 'black'
        if obj.estado_factura_compra.estado_factura_proveedor == 'PAG':
            color = 'green'
            return format_html('<span style="color: %s"><b> %s </b></span>' %
                               (color, obj.estado_factura_compra.get_estado_factura_proveedor_display()))
        elif obj.estado_factura_compra.estado_factura_proveedor == 'FPP':
            color = 'red'
            return format_html('<span style="color: %s"><b> %s </b></span>' %
                               (color, obj.estado_factura_compra.get_estado_factura_proveedor_display()))
        elif obj.estado_factura_compra.estado_factura_proveedor == 'CAN':
            color = 'orange'
            return format_html('<span style="color: %s"><b> %s </b></span>' %
                               (color, obj.estado_factura_compra.get_estado_factura_proveedor_display()))
        elif obj.estado_factura_compra.estado_factura_proveedor == 'EPP':
            color = 'yellowgreen'
            return format_html('<span style="color: %s"><b> %s </b></span>' %
                               (color, obj.estado_factura_compra.get_estado_factura_proveedor_display()))
        return obj.estado_factura_compra.estado_factura_proveedor
    colorea_estado_factura_compra.short_description = 'Estado de la Factura'

    def save_formset(self, request, form, formset, change):
        obj = form.instance
        obj.save()
        formset.save(commit=True)
        linea_credito = obj.proveedor.lineacreditoproveedor
        total = 0
        for f in formset:
            pago = f.instance
            total += pago.monto_pago_proveedor
            if not pago.procesado:
                linea_credito_detalle = LineaCreditoProveedorDetalle(linea_credito_proveedor_id=linea_credito.pk,
                                                                     monto_movimiento=pago.monto_pago_proveedor,
                                                                     tipo_movimiento='PAG',
                                                                     numero_comprobante=pago.numero_comprobante_pago,
                                                                     fecha_movimiento=timezone_today())
                linea_credito_detalle.save()
                pago.procesado = True
                pago.save()
        # pdb.set_trace()
        if Decimal(total) == Decimal(obj.total_factura_compra):
            obj.estado_factura_compra.estado_factura_proveedor = 'PAG'
            obj.save()
        elif Decimal(total) > Decimal(obj.total_factura_compra):
            raise ValidationError({'total_pago_factura': _('El Monto Total de los Pagos no puede exceder al Total '
                                                           'de la Factura.')})
            # raise ValidationError({'total_pago_factura': _('La suma de los pagos no debe superar el monto de la '
            #                                                'factura.')})

    def changelist_view(self, request, extra_context=None):
        queryset = self.get_queryset(request).filter(estado_factura_compra__estado_factura_proveedor='EPP')

        for factura in queryset:
            today = datetime.date.today()
            # print factura.estado_factura_compra.estado_factura_proveedor, today

            if factura.tipo_factura_compra.tipo_factura_compra == 'CRE':
                # print ('factura.fecha_factura_compra: %s - factura.plazo_factura_compra: %s') % (factura.fecha_factura_compra, factura.plazo_factura_compra)
                calculo = (factura.fecha_factura_compra + datetime.timedelta(days=factura.plazo_factura_compra))
                # print 'calculo: %s' % calculo
                if calculo < today:
                    # estado = OrdenCompraEstado.objects.get(estado_orden_compra='PEP')
                    factura.estado_factura_compra.estado_factura_proveedor = 'FPP'
                    factura.save()
            elif factura.tipo_factura_compra.tipo_factura_compra == 'CON':
                if factura.fecha_factura_compra < today:
                    factura.estado_factura_compra.estado_factura_proveedor = 'FPP'
                    factura.save()
        return super(FacturaProveedorAdmin, self).changelist_view(request, extra_context=extra_context)

    def changeform_view(self, request, object_id=None, form_url='', extra_context=None):
        extra_context = extra_context or {}

        extra_context['show_button'] = False
        # if object_id is not None:
        #     factura_actual = FacturaProveedor.objects.get(pk=object_id)
        #     print 'factura_actual: %s' % factura_actual
        #     extra_context['show_button'] = factura_actual.estado_factura_compra.estado_factura_proveedor not in ('PAG', 'CAN')

        return super(FacturaProveedorAdmin, self).changeform_view(request, object_id, form_url, extra_context)

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


class OrdenPagoDetalleInline(admin.TabularInline):
    model = OrdenPagoDetalle
    extra = 0
    can_delete = False
    # readonly_fields = ['procesado']
    fields = ['orden_compra', 'proveedor', 'numero_factura_compra', 'fecha_factura_compra',
              'tipo_factura_compra', 'forma_pago_compra', 'plazo_factura_compra', 'total_factura_compra',
              'estado_factura_compra', 'procesado']
    form = OrdenPagoDetalleForm
    ordering = ['fecha_factura_compra']
    # verbose_name = 'Pago a Proveedores'
    # verbose_name_plural = 'Pagos a Proveedores'

    def get_readonly_fields(self, request, obj=None):
        if obj is not None and obj.estado_orden_pago.estado_orden_pago == 'PEN':
            return ['orden_compra', 'proveedor', 'numero_factura_compra', 'fecha_factura_compra', 'tipo_factura_compra',
                    'forma_pago_compra', 'plazo_factura_compra', 'estado_factura_compra']  # 'total_factura_compra',
        elif obj is not None and obj.estado_orden_pago.estado_orden_pago in ('CON', 'ANU', 'CAN'):
            return [i.name for i in self.model._meta.fields]
        else:
            return super(OrdenPagoDetalleInline, self).get_readonly_fields(request, obj)

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    # def get_queryset(self, request):
    #     # empresa = self.get_queryset(request).get(pk=)
    #     queryset = FacturaProveedor.objects.filter(proveedor_id=2)
    #     print queryset
    #     return queryset


class OrdenPagoAdmin(admin.ModelAdmin):

    form = OrdenPagoForm

    class Media:
        js = [
            'compras/js/orden_pago.js'
        ]

    # readonly_fields = ['numero_orden_pago', 'fecha_hora_orden_pago', 'usuario_registro_orden_pago',
    #                    'estado_orden_pago']  # 'total_orden_pago'

    fieldsets = [
        ('Numero Orden de Pago', {'fields': ['numero_orden_pago']}),
        ('Datos del Proveedor', {'fields': ['proveedor_orden_pago']}),
        # ('Fechas', {'fields': ['fecha_hora_orden_pago']}),
        ('Otros datos de la Orden de Pago', {'fields': ['fecha_hora_orden_pago', 'usuario_registro_orden_pago',
                                                        'estado_orden_pago', 'total_orden_pago']}),
    ]

    inlines = [OrdenPagoDetalleInline]

    list_display = ['numero_orden_pago', 'proveedor_orden_pago', 'fecha_hora_orden_pago',
                    'usuario_registro_orden_pago', 'total_orden_pago', 'colorea_estado_orden_pago']
    # list_display_links = []
    list_filter = ['numero_orden_pago', 'proveedor_orden_pago', 'fecha_hora_orden_pago',
                    'usuario_registro_orden_pago', 'estado_orden_pago', 'total_orden_pago']
    search_fields = ['numero_orden_pago', 'proveedor_orden_pago__proveedor', 'fecha_hora_orden_pago',
                    'usuario_registro_orden_pago__usuario__username', 'estado_orden_pago__descripcion', 'total_orden_pago']

    # def get_inline_formsets(self, request, formsets, inline_instances, obj=None):
    #     queryset = FacturaProveedor.objects.filter(proveedor_id=2)
    #     print queryset
    #     return queryset

    def colorea_estado_orden_pago(self, obj):
        # color = 'black'
        if obj.estado_orden_pago.estado_orden_pago == 'CON':
            color = 'green'
            return format_html('<span style="color: %s"><b> %s </b></span>' %
                               (color, obj.estado_orden_pago.get_estado_orden_pago_display()))
        elif obj.estado_orden_pago.estado_orden_pago == 'ANU':
            color = 'red'
            return format_html('<span style="color: %s"><b> %s </b></span>' %
                               (color, obj.estado_orden_pago.get_estado_orden_pago_display()))
        elif obj.estado_orden_pago.estado_orden_pago == 'CAN':
            color = 'orange'
            return format_html('<span style="color: %s"><b> %s </b></span>' %
                               (color, obj.estado_orden_pago.get_estado_orden_pago_display()))
        elif obj.estado_orden_pago.estado_orden_pago == 'PEN':
            color = 'indianred'
            return format_html('<span style="color: %s"><b> %s </b></span>' %
                               (color, obj.estado_orden_pago.get_estado_orden_pago_display()))
        return obj.estado_orden_pago.estado_orden_pago
    colorea_estado_orden_pago.short_description = 'Estado Orden de Pago'

    def save_model(self, request, obj, form, change):

        # import pdb
        # pdb.set_trace()

        orden_pago_actual = obj

        # Si la orden_pago es generada por primera vez se debe guardar el objeto para asignarle un ID y el estado PEN.
        if obj.numero_orden_pago is None:
            obj.usuario_registro_orden_pago = Empleado.objects.get(usuario_id=request.user)
            obj.estado_orden_pago = OrdenPagoEstado.objects.get(estado_orden_pago='PEN')
            obj.total_orden_pago = 1
            super(OrdenPagoAdmin, self).save_model(request, obj, form, change)

        if "_continue" in request.POST and orden_pago_actual.estado_orden_pago.estado_orden_pago == 'PEN':
            orden_pago_actual.estado_orden_pago = OrdenPagoEstado.objects.get(estado_orden_pago='PEN')
            orden_pago_actual.total_orden_pago = 0
            super(OrdenPagoAdmin, self).save_model(request, obj, form, change)

        # Si se CANCELA la Orden de Pago se asigna el estado "CAN" a la Orden de Pago y se marcan como
        # "procesado = False" a los registros del formset
        elif "_cancel" in request.POST:
            orden_pago_actual.estado_orden_pago = OrdenPagoEstado.objects.get(estado_orden_pago='CAN')
            super(OrdenPagoAdmin, self).save_model(request, obj, form, change)

        # Si se ANULA la Orden de Pago se asigna el estado "ANU" a la Orden de Pago, se debe asignar el estado "EPP"
        # o "FPP" a las facturas en el formset y se deben MARCAR como anulados los registros de pagos en PagoProveedor
        # para las facturas afectadas.
        # Se deben MARCAR tambien como anulado el registro correspondiente en la Linea de Credito.
        elif "_anular" in request.POST:
            orden_pago_actual.estado_orden_pago = OrdenPagoEstado.objects.get(estado_orden_pago='ANU')
            orden_pago_actual.motivo_anulacion = request.POST.get('motivo', '')
            orden_pago_actual.observaciones_anulacion = request.POST.get('observaciones', '')
            orden_pago_actual.usuario_anulacion = Empleado.objects.get(usuario_id=request.user)
            orden_pago_actual.fecha_hora_anulacion = timezone.now()
            # return
            super(OrdenPagoAdmin, self).save_model(request, obj, form, change)

        # Si se confirma la Orden de Pago se asigna el estado "CON" a la Orden de Pago, el estado "PAG" a las
        # facturas en el formset y se deben generar registros de pagos en PagoProveedor para las facturas afectadas
        elif "_save" in request.POST:  # and compra_actual.estado_compra.estado_compra == 'CON':
            orden_pago_actual.estado_orden_pago = OrdenPagoEstado.objects.get(estado_orden_pago='CON')
            super(OrdenPagoAdmin, self).save_model(request, obj, form, change)

        if getattr(obj, 'usuario_registro_orden_pago', None) is not None:
            # empleado = Empleado.objects.filter(usuario=request.user)
            obj.usuario_registro_orden_pago = Empleado.objects.get(usuario_id=request.user)
            print 'obj.usuario_registro_orden_pago: ', obj.usuario_registro_orden_pago
        super(OrdenPagoAdmin, self).save_model(request, obj, form, change)

    def save_formset(self, request, form, formset, change):

        # import pdb
        # pdb.set_trace()

        orden_pago_actual = form.instance
        super(OrdenPagoAdmin, self).save_formset(request, form, formset, change)

        print 'obj: %s - orden_pago_actual: %s' % (form.instance, orden_pago_actual)

        if "_continue" in request.POST and orden_pago_actual.estado_orden_pago.estado_orden_pago == 'PEN':
            print 'orden_pago_actual.numero_orden_pago: %s - orden_pago_detalle_a_eliminar: %s' % \
                  (orden_pago_actual.numero_orden_pago, OrdenPagoDetalle.objects.filter(numero_orden_pago_id=orden_pago_actual.numero_orden_pago))

            # if 'procesado' in form.changed_data:
            #     print 'El campo Procesado SI ha cambiado.'
            #     formset.save()
            # else:
            #     print 'El campo Procesado NO ha cambiado.'

            # formset.save()
            OrdenPagoDetalle.objects.filter(numero_orden_pago_id=orden_pago_actual.numero_orden_pago).delete()
            print 'orden_pago_detalle_a_eliminar: ', OrdenPagoDetalle.objects.filter(numero_orden_pago_id=orden_pago_actual.numero_orden_pago)

            # suma_facturas = 0
            for detalle in FacturaProveedor.objects.filter(Q(proveedor_id=orden_pago_actual.proveedor_orden_pago), Q(estado_factura_compra__estado_factura_proveedor='EPP') | Q(estado_factura_compra__estado_factura_proveedor='FPP')):
                orden_pago_detalle = OrdenPagoDetalle(numero_orden_pago_id=orden_pago_actual.numero_orden_pago,
                                                      compra_id=detalle.compra_id,
                                                      orden_compra_id=detalle.orden_compra_id,
                                                      proveedor_id=detalle.proveedor_id,
                                                      numero_factura_compra=detalle.numero_factura_compra,
                                                      fecha_factura_compra=detalle.fecha_factura_compra,
                                                      tipo_factura_compra=detalle.tipo_factura_compra,
                                                      forma_pago_compra=detalle.forma_pago_compra,
                                                      plazo_factura_compra=detalle.plazo_factura_compra,
                                                      total_factura_compra=detalle.total_factura_compra,
                                                      estado_factura_compra=detalle.estado_factura_compra,
                                                      procesado=False)
                # suma_facturas = suma_facturas + detalle.total_factura_compra
                orden_pago_detalle.save()

        # Si se CANCELA la Orden de Pago se asigna el estado "CAN" a la Orden de Pago y se marcan como
        # "procesado = False" a los registros del formset
        elif "_cancel" in request.POST:
            formset.save(commit=False)
            for form in formset:
                factura_orden_pago_detalle = form.instance
                if factura_orden_pago_detalle.procesado is not True:
                    factura_orden_pago_detalle.delete()
                elif factura_orden_pago_detalle.procesado is True:
                    factura_orden_pago_detalle.procesado = False
            super(OrdenPagoAdmin, self).save_formset(request, form, formset, change)

        # Si se ANULA la Orden de Pago se asigna el estado "ANU" a la Orden de Pago, se debe asignar el estado "EPP"
        # o "FPP" a las facturas en el formset y se deben MARCAR como anulados los registros de pagos en PagoProveedor
        # para las facturas afectadas.
        # Se deben MARCAR tambien como anulado el registro correspondiente en la Linea de Credito.
        elif "_anular" in request.POST:
            linea_credito = form.instance.proveedor_orden_pago.lineacreditoproveedor
            for form in formset:
                factura_orden_pago_detalle = form.instance
                factura = FacturaProveedor.objects.get(compra_id=factura_orden_pago_detalle.compra,
                                                       orden_compra_id=factura_orden_pago_detalle.orden_compra,
                                                       proveedor_id=factura_orden_pago_detalle.proveedor,
                                                       numero_factura_compra=factura_orden_pago_detalle.numero_factura_compra,
                                                       fecha_factura_compra=factura_orden_pago_detalle.fecha_factura_compra,
                                                       tipo_factura_compra=factura_orden_pago_detalle.tipo_factura_compra,
                                                       forma_pago_compra=factura_orden_pago_detalle.forma_pago_compra,
                                                       plazo_factura_compra=factura_orden_pago_detalle.plazo_factura_compra,
                                                       total_factura_compra=factura_orden_pago_detalle.total_factura_compra)
                today = datetime.date.today()
                # print factura.estado_factura_compra.estado_factura_proveedor, today

                if factura.tipo_factura_compra.tipo_factura_compra == 'CRE':
                    # print ('factura.fecha_factura_compra: %s - factura.plazo_factura_compra: %s') % (factura.fecha_factura_compra, factura.plazo_factura_compra)
                    calculo = (factura.fecha_factura_compra + datetime.timedelta(days=factura.plazo_factura_compra))
                    # print 'calculo: %s' % calculo
                    if calculo < today:
                        # estado = OrdenCompraEstado.objects.get(estado_orden_compra='PEP')
                        factura.estado_factura_compra.estado_factura_proveedor = 'FPP'
                    else:
                        factura.estado_factura_compra.estado_factura_proveedor = 'EPP'
                    # factura.save()
                elif factura.tipo_factura_compra.tipo_factura_compra == 'CON':
                    if factura.fecha_factura_compra < today:
                        factura.estado_factura_compra.estado_factura_proveedor = 'FPP'
                    else:
                        factura.estado_factura_compra.estado_factura_proveedor = 'EPP'

                factura.total_pago_factura = factura.total_pago_factura - factura_orden_pago_detalle.total_factura_compra
                factura.save()

                pago_proveedor = PagoProveedor.objects.get(factura_proveedor_id=factura.id,
                                                           # factura_proveedor_id=FacturaProveedor.objects.get(compra_id=factura.compra, proveedor_id=factura.proveedor_id, numero_factura_compra=factura.numero_factura_compra).pk,
                                                           monto_pago_proveedor=factura.total_factura_compra,
                                                           fecha_pago_proveedor=timezone.localtime(orden_pago_actual.fecha_hora_orden_pago).date(),
                                                           numero_comprobante_pago=orden_pago_actual.numero_orden_pago,
                                                           procesado=True)
                print 'pago_proveedor: %s' % pago_proveedor
                pago_proveedor.anulado = True
                pago_proveedor.fecha_hora_anulacion = timezone.now()
                pago_proveedor.save()

                linea_credito_detalle = LineaCreditoProveedorDetalle.objects.get(linea_credito_proveedor_id=linea_credito.pk,
                                                                                 monto_movimiento=factura.total_factura_compra,
                                                                                 tipo_movimiento='PAG',
                                                                                 numero_comprobante=orden_pago_actual.numero_orden_pago,
                                                                                 fecha_movimiento=timezone.localtime(orden_pago_actual.fecha_hora_orden_pago).date())
                print 'linea_credito_detalle: %s' % linea_credito_detalle
                linea_credito_detalle.anulado = True
                linea_credito_detalle.fecha_hora_anulacion = timezone.now()
                linea_credito_detalle.save()

            super(OrdenPagoAdmin, self).save_formset(request, form, formset, change)

        # Si se confirma la Orden de Pago se asigna el estado "CON" a la Orden de Pago, el estado "PAG" a las
        # facturas en el formset y se deben generar registros de pagos en PagoProveedor para las facturas afectadas.
        # Generar tambien el registro correspondiente en la Linea de Credito.
        # Solo se debe guardar en el detalle de la Orden de Pago la Factura que fue checkeada en la casilla "Procesar"
        elif "_save" in request.POST:  # and compra_actual.estado_compra.estado_compra == 'CON':
            formset.save(commit=False)
            linea_credito = form.instance.proveedor_orden_pago.lineacreditoproveedor
            for form in formset:
                factura_orden_pago_detalle = form.instance
                if factura_orden_pago_detalle.procesado is True:
                    factura = FacturaProveedor.objects.get(compra_id=factura_orden_pago_detalle.compra,
                                                           orden_compra_id=factura_orden_pago_detalle.orden_compra,
                                                           proveedor_id=factura_orden_pago_detalle.proveedor,
                                                           numero_factura_compra=factura_orden_pago_detalle.numero_factura_compra,
                                                           fecha_factura_compra=factura_orden_pago_detalle.fecha_factura_compra,
                                                           tipo_factura_compra=factura_orden_pago_detalle.tipo_factura_compra,
                                                           forma_pago_compra=factura_orden_pago_detalle.forma_pago_compra,
                                                           plazo_factura_compra=factura_orden_pago_detalle.plazo_factura_compra,
                                                           total_factura_compra=factura_orden_pago_detalle.total_factura_compra)
                    factura.estado_factura_compra = FacturaProveedorEstado.objects.get(estado_factura_proveedor='PAG')
                    factura.save()

                    pago_proveedor = PagoProveedor(factura_proveedor_id=factura.id,
                                                   # factura_proveedor_id=FacturaProveedor.objects.get(compra_id=factura.compra, proveedor_id=factura.proveedor_id, numero_factura_compra=factura.numero_factura_compra).pk,
                                                   monto_pago_proveedor=factura.total_factura_compra,
                                                   fecha_pago_proveedor=timezone_today(),
                                                   numero_comprobante_pago=orden_pago_actual.numero_orden_pago,
                                                   procesado=True,
                                                   anulado=False)
                    pago_proveedor.save()

                    linea_credito_detalle = LineaCreditoProveedorDetalle(linea_credito_proveedor_id=linea_credito.pk,
                                                                         monto_movimiento=factura.total_factura_compra,
                                                                         tipo_movimiento='PAG',
                                                                         numero_comprobante=orden_pago_actual.numero_orden_pago,
                                                                         fecha_movimiento=timezone_today(),
                                                                         anulado=False)
                    linea_credito_detalle.save()

                elif factura_orden_pago_detalle.procesado is not True:
                    factura_orden_pago_detalle.delete()
            super(OrdenPagoAdmin, self).save_formset(request, form, formset, change)

    def get_readonly_fields(self, request, obj=None):
        if obj is not None and obj.estado_orden_pago.estado_orden_pago == 'PEN':
            return ['numero_orden_pago', 'fecha_hora_orden_pago', 'usuario_registro_orden_pago',
                    'estado_orden_pago']
        elif obj is not None and obj.estado_orden_pago.estado_orden_pago in ('CON', 'ANU', 'CAN'):
            return [i.name for i in self.model._meta.fields] + \
                   [i.name for i in self.model._meta.many_to_many]
        elif obj is None:
            return ['numero_orden_pago', 'fecha_hora_orden_pago', 'usuario_registro_orden_pago',
                    'estado_orden_pago']
        else:
            return super(OrdenPagoAdmin, self).get_readonly_fields(request, obj)

    def changeform_view(self, request, object_id=None, form_url='', extra_context=None):
        extra_context = extra_context or {}

        # import pdb
        # pdb.set_trace()

        extra_context['show_button'] = True

        if object_id is not None:
            orden_pago_actual = OrdenPago.objects.get(pk=object_id)
            if orden_pago_actual.estado_orden_pago.estado_orden_pago == 'ANU':
                # extra_context['show_button'] = False
                extra_context['show_save_button'] = False
                extra_context['show_continue_button'] = False
                extra_context['show_cancel_button'] = False
                extra_context['show_anular_button'] = False
                extra_context['show_imprimir_button'] = True
            elif orden_pago_actual.estado_orden_pago.estado_orden_pago == 'CAN':
                extra_context['show_save_button'] = False
                extra_context['show_continue_button'] = False
                extra_context['show_cancel_button'] = False
                extra_context['show_anular_button'] = False
                extra_context['show_imprimir_button'] = False
            elif orden_pago_actual.estado_orden_pago.estado_orden_pago == 'CON':
                extra_context['show_save_button'] = False
                extra_context['show_continue_button'] = False
                extra_context['show_cancel_button'] = False
                extra_context['show_anular_button'] = True
                extra_context['show_imprimir_button'] = True
            elif orden_pago_actual.estado_orden_pago.estado_orden_pago == 'PEN':
                extra_context['show_save_button'] = True
                extra_context['show_continue_button'] = True
                extra_context['show_cancel_button'] = True
                extra_context['show_anular_button'] = False
                extra_context['show_imprimir_button'] = False

        elif object_id is None:
            extra_context['show_save_button'] = True
            extra_context['show_continue_button'] = True
            extra_context['show_cancel_button'] = False
            extra_context['show_anular_button'] = False
            extra_context['show_imprimir_button'] = False

        return super(OrdenPagoAdmin, self).changeform_view(request, object_id, form_url, extra_context)

    def get_form(self, request, obj=None, **kwargs):
        for a in request.POST: print a
        # if '_anular' in request.POST:
        #     form = AnularOrdenPagoForm
        # else:
        form = super(OrdenPagoAdmin, self).get_form(request, obj=obj, **kwargs)
        form.request = request
        return form


# class ProductoProveedorAdmin(admin.ModelAdmin):
#     raw_id_fields = ['producto']
#     list_display = ('id', 'proveedor', 'producto')
#     list_filter = ['id', 'proveedor', 'producto']
#     search_fields = ['id', 'proveedor', 'producto']


class EmpresaAdmin(admin.ModelAdmin):

    form = EmpresaForm

    class Media:
        js = [
            'compras/js/empresa.js'
        ]

    readonly_fields = ('digito_verificador', 'fecha_alta_proveedor', 'thumb')

    # list_editable = ('id', 'proveedor', 'ruc', 'digito_verificador', 'direccion', 'pagina_web')

    fieldsets = [
        ('Empresa', {'fields': ['proveedor', 'persona_proveedor']}),
        ('RUC', {'fields': ['ruc', 'digito_verificador']}),
        ('Logo', {'fields': ['logo_empresa', 'thumb']}),
        ('Direccion', {'fields': ['direccion', ('pais', 'ciudad')]}),
        ('Otros datos', {'fields': ['pagina_web', 'fecha_apertura', 'fecha_alta_proveedor']}),
        # ('Timbrado', {'fields': ['timbrado']}),
        ('Datos Tributarios', {'fields': ['timbrado', 'codigo_establecimiento', 'actividad_economica', 'salario_minimo_vigente']})
    ]

    inlines = [ProveedorTelefonoInline]

    list_display = ['id', 'proveedor', 'persona_proveedor', 'ruc', 'digito_verificador', 'direccion', 'pais',
                    'ciudad', 'pagina_web', 'fecha_apertura', 'fecha_alta_proveedor',
                    'timbrado', 'codigo_establecimiento', 'thumb']
    list_display_links = ['proveedor']
    list_filter = ['id', 'proveedor', 'ruc', 'fecha_alta_proveedor']
    search_fields = ['id', 'proveedor', 'ruc', 'fecha_alta_proveedor']

    def get_queryset(self, request):
        # empresa = self.get_queryset(request).get(pk=)
        queryset = Empresa.objects.filter(proveedor_ptr_id__empresa_administrada=True)
        print queryset
        return queryset

    def save_model(self, request, obj, form, change):
        if obj.ruc is not None:
            obj.digito_verificador = calcular_dv(obj.ruc, 11)
        else:
            raise ValidationError({'digito_verificador': _('RUC no valido.')})
        super(EmpresaAdmin, self).save_model(request, obj, form, change)


# ======================================================================================================================
# # Intento de validacion para controlar que "El Total de la Orden de Compra no debe superar el monto de la
# # Linea de Credito"
# class OrdenCompraDetalleFormset(BaseInlineFormSet):
#    def clean(self):
#       super(OrdenCompraDetalleFormset, self).clean()
#       total = 0
#       for form in self.forms:
#          if not form.is_valid():
#             return
#          if form.cleaned_data and not form.cleaned_data.get('DELETE'):
#             total += Decimal(form.cleaned_data['precio_producto_orden_compra']) * \
#                      Decimal(form.cleaned_data['cantidad_producto_orden_compra'])
#          print self.data
#       raise ValidationError('Total of elements must be 100%%. Current : %(percent).2f%%' % {'percent': total})
# ======================================================================================================================

class OrdenCompraDetalleInline(admin.TabularInline):
    model = OrdenCompraDetalle
    # formset = OrdenCompraDetalleFormset
    extra = 0
    min_num = 1
    fields = ['id', 'producto_orden_compra', 'precio_producto_orden_compra', 'unidad_medida_orden_compra', 'cantidad_producto_orden_compra', 'total_producto_orden_compra']
    readonly_fields = ['id']
    form = OrdenCompraDetalleForm
    raw_id_fields = ['producto_orden_compra']
    verbose_name = 'Orden de Compra - Detalle de Productos'
    verbose_name_plural = 'Orden de Compra - Detalle de Productos'

    def get_readonly_fields(self, request, obj=None):
        if obj is not None and obj.estado_orden_compra.estado_orden_compra in ('ENT', 'CAN'):
            return [i.name for i in self.model._meta.fields]
        else:
            return super(OrdenCompraDetalleInline, self).get_readonly_fields(request, obj)

    def has_add_permission(self, request):
        object_id = request.path.split("/")[-2]
        if object_id != "add":
            orden_compra_actual = OrdenCompra.objects.get(pk=object_id)
            return orden_compra_actual.estado_orden_compra.estado_orden_compra not in ('ENT', 'CAN')
        else:
            return super(OrdenCompraDetalleInline, self).has_add_permission(request)

    def has_delete_permission(self, request, obj=None):
        if obj is not None and obj.estado_orden_compra.estado_orden_compra in ('ENT', 'CAN'):
            return False
        return super(OrdenCompraDetalleInline, self).has_delete_permission(request, obj)


class OrdenCompraAdmin(admin.ModelAdmin):

    form = OrdenCompraForm

    # def formfield_for_dbfield(self, db_field, **kwargs):
    #     # Add some logic here to base your choices on.
    #     if db_field.name == 'estado_orden_compra':
    #         kwargs['widget'].choices = (
    #             ('EPP', 'En Proceso Proveedor'),
    #             # ('ENT', 'Entregada por Proveedor'),
    #             # ('PEP', 'Pendiente Entrega Proveedor'),
    #             ('CAN', 'Cancelada'),
    #         )
    #     return super(OrdenCompraAdmin, self).formfield_for_dbfield(db_field, **kwargs)

    class Media:
        js = [
            'compras/js/autoNumeric.js', 'compras/js/orden_compra.js', 'compras/js/jquery.mask.js'  # 'compras/js/change_form.js',
        ]

    # readonly_fields = ('numero_orden_compra', 'fecha_orden_compra', 'estado_orden_compra')

    # raw_id_fields = ['proveedor_orden_compra']

    fieldsets = [
        ('Numero Orden de Compra', {'fields': ['numero_orden_compra']}),
        ('Datos del Proveedor', {'fields': ['proveedor_orden_compra', 'linea_credito', 'forma_pago_orden_compra']}),
        ('Fechas', {'fields': ['fecha_orden_compra', 'fecha_ultima_modificacion_orden_compra',
                               'fecha_entrega_orden_compra']}),
        # ('Fecha de Entrega del Pedido', {'fields': ['fecha_entrega']}),
        ('Otros datos de la Orden de Compra', {'fields': ['estado_orden_compra', 'total_orden_compra']}),
    ]

    inlines = [OrdenCompraDetalleInline]

    # list_select_related = True
    list_display = ('numero_orden_compra', 'proveedor_orden_compra', 'fecha_orden_compra',
                    'fecha_ultima_modificacion_orden_compra', 'fecha_entrega_orden_compra', 'forma_pago_orden_compra',
                    'colorea_estado_orden_compra', 'total_orden_compra', 'usuario_registro_orden_compra')
    list_filter = ['numero_orden_compra', ('proveedor_orden_compra', admin.RelatedOnlyFieldListFilter),
                   'fecha_orden_compra', 'fecha_ultima_modificacion_orden_compra', 'fecha_entrega_orden_compra',
                   'forma_pago_orden_compra', 'estado_orden_compra', 'usuario_registro_orden_compra']
    search_fields = ['numero_orden_compra', 'proveedor_orden_compra__proveedor', 'fecha_orden_compra',
                     'fecha_ultima_modificacion_orden_compra', 'fecha_entrega_orden_compra',
                     'forma_pago_orden_compra__forma_pago_compra', 'estado_orden_compra__estado_orden_compra',
                     'usuario_registro_orden_compra__usuario__username']

    # def get_readonly_fields(self, request, obj=None):
    #     if obj:  # This is the case when obj is already created i.e. it's an edit
    #         return ['numero_orden_compra', 'fecha_orden_compra', 'estado_orden_compra', 'proveedor_orden_compra']
    #     # elif object.
    #     else:
    #         return ['numero_orden_compra', 'fecha_orden_compra', 'estado_orden_compra']

    # 03/10/2016: Creado para probar el raw SQL para agregar el numero de item a los reportes.
    # def add_view(self, request, form_url='', extra_context=None):
    #     queryset = OrdenCompraDetalle.objects.raw('select  *,Row_Number() Over ( Order By detalle.id ) As fila  from compras_ordencompradetalle detalle')
    #     for obj in queryset:
    #         print obj.producto_orden_compra
    #     # return render_to_response(template_name='holamundo.html',context={})
    #     # return super(OrdenCompraAdmin,self).add_view(request,form_url,extra_context)

    def colorea_estado_orden_compra(self, obj):
        # color = 'black'
        if obj.estado_orden_compra.estado_orden_compra == 'ENT':
            color = 'green'
            return format_html('<span style="color: %s"><b> %s </b></span>' %
                               (color, obj.estado_orden_compra.get_estado_orden_compra_display()))
        elif obj.estado_orden_compra.estado_orden_compra == 'PEP':
            color = 'red'
            return format_html('<span style="color: %s"><b> %s </b></span>' %
                               (color, obj.estado_orden_compra.get_estado_orden_compra_display()))
        elif obj.estado_orden_compra.estado_orden_compra == 'CAN':
            color = 'orange'
            return format_html('<span style="color: %s"><b> %s </b></span>' %
                               (color, obj.estado_orden_compra.get_estado_orden_compra_display()))
        elif obj.estado_orden_compra.estado_orden_compra == 'EPP':
            color = 'yellowgreen'
            return format_html('<span style="color: %s"><b> %s </b></span>' %
                               (color, obj.estado_orden_compra.get_estado_orden_compra_display()))
        elif obj.estado_orden_compra.estado_orden_compra == 'PEN':
            color = 'indianred'
            return format_html('<span style="color: %s"><b> %s </b></span>' %
                               (color, obj.estado_orden_compra.get_estado_orden_compra_display()))
        return obj.estado_orden_compra
    colorea_estado_orden_compra.short_description = 'Estado Orden de Compra'

    def save_model(self, request, obj, form, change):
        # if "_print" in request.POST:
        #     # ordencompra_report(request)
        #     resp = HttpResponse(content_type='application/pdf')
        #     ordenes = OrdenCompra.objects.order_by('fecha_orden_compra')
        #     report = ReportOrdenCompra(queryset=ordenes)
        #     report.generate_by(PDFGenerator, filename=resp)
        #     return resp
        # super(OrdenCompraAdmin, self).save_model(request, obj, form, change)
        # http://localhost:8001/compras/orden-compra-report/

        # import pdb
        # pdb.set_trace()

        # orden_compra = obj

        if '_save' in request.POST or '_continue' in request.POST or '_addanother' in request.POST:
            obj.total_orden_compra = request.POST.get('total_orden_compra', '')

            now = timezone.now()
            if obj.estado_orden_compra.estado_orden_compra == 'EPP' and obj.fecha_entrega_orden_compra < now:
                obj.estado_orden_compra = OrdenCompraEstado.objects.get(estado_orden_compra='PEP')
            elif obj.estado_orden_compra.estado_orden_compra == 'PEP' and obj.fecha_entrega_orden_compra > now:
                obj.estado_orden_compra = OrdenCompraEstado.objects.get(estado_orden_compra='EPP')
            # elif obj.estado_orden_compra.estado_orden_compra == 'PEN' and obj.fecha_entrega_orden_compra > now:
            #     obj.estado_orden_compra = OrdenCompraEstado.objects.get(estado_orden_compra='EPP')
            #     compra_relacionada = Compra.objects.get(numero_orden_compra=obj.numero_orden_compra)
            #     compra_relacionada.estado_compra = OrdenCompraEstado.objects.get(estado_orden_compra='EPP')
            # obj.save()  # No descomentar porque genera un error con el campo usuario_registro_orden_compra debido a
            # que aun no se asigno un valor para este campo en esta instancia, la asignacion del
            # usuario_registro_orden_compra se realiza mas abajo

            # super(OrdenCompraAdmin, self).save_model(request, obj, form, change)

        elif '_cancel' in request.POST:
            obj.estado_orden_compra = OrdenCompraEstado.objects.get(estado_orden_compra='CAN')
            obj.total_orden_compra = request.POST.get('total_orden_compra', '')
            obj.motivo_cancelacion = request.POST.get('motivo', '')
            obj.observaciones_cancelacion = request.POST.get('observaciones', '')
            obj.usuario_cancelacion = Empleado.objects.get(usuario_id=request.user)
            obj.fecha_hora_cancelacion = timezone.now()

            compras_afectadas = Compra.objects.filter(numero_orden_compra=obj.numero_orden_compra)
            if compras_afectadas.exists():
                for compra in compras_afectadas:
                    if compra.estado_compra.estado_orden_compra in ('EPP', 'PEP', 'PEN'):
                        compra.estado_compra = OrdenCompraEstado.objects.get(estado_orden_compra='CAN')
                        compra.motivo_cancelacion = request.POST.get('motivo', '')
                        compra.observaciones_cancelacion = request.POST.get('observaciones', '')
                        compra.usuario_cancelacion = Empleado.objects.get(usuario_id=request.user)
                        compra.fecha_hora_cancelacion = timezone.now()
                    compra.save()
            # super(OrdenCompraAdmin, self).save_model(request, obj, form, change)

        if not change and getattr(obj, 'usuario_registro_orden_compra', None) is None:
            # empleado = Empleado.objects.filter(usuario=request.user)
            obj.usuario_registro_orden_compra = Empleado.objects.get(usuario_id=request.user)
            print 'obj.usuario_registro_orden_compra: ', obj.usuario_registro_orden_compra
        elif change and getattr(obj, 'usuario_registro_orden_compra', None) is not None:
            obj.usuario_modifica_orden_compra = Empleado.objects.get(usuario_id=request.user)
            print 'obj.usuario_modifica_orden_compra: ', obj.usuario_modifica_orden_compra
        super(OrdenCompraAdmin, self).save_model(request, obj, form, change)

    def get_readonly_fields(self, request, obj=None):
        if obj is not None and obj.estado_orden_compra.estado_orden_compra in ('EPP', 'PEP', 'PEN'):
            return ['numero_orden_compra', 'fecha_orden_compra', 'fecha_ultima_modificacion_orden_compra',
                    'estado_orden_compra', 'proveedor_orden_compra', 'usuario_registro_orden_compra']
        elif obj is not None and obj.estado_orden_compra.estado_orden_compra in ('ENT', 'CAN'):
            return [i.name for i in self.model._meta.fields] + \
                   [i.name for i in self.model._meta.many_to_many]
        elif obj is None:
            return ['numero_orden_compra', 'fecha_orden_compra', 'fecha_ultima_modificacion_orden_compra',
                    'estado_orden_compra', 'usuario_registro_orden_compra']
        else:
            return super(OrdenCompraAdmin, self).get_readonly_fields(request, obj)

    def changeform_view(self, request, object_id=None, form_url='', extra_context=None):
        extra_context = extra_context or {}

        extra_context['show_button'] = True
        if object_id is not None:
            orden_compra_actual = OrdenCompra.objects.get(pk=object_id)
            # extra_context['show_button'] = orden_compra_actual.estado_orden_compra.estado_orden_compra \
            #                                not in ('ENT', 'CAN')

            # if orden_compra_actual.estado_orden_compra.estado_orden_compra == 'PEN':
            #     extra_context['show_save_button'] = True
            #     extra_context['show_continue_button'] = True
            #     extra_context['show_addanother_button'] = True
            #     extra_context['show_cancel_button'] = False
            #     extra_context['show_imprimir_button'] = False
            if orden_compra_actual.estado_orden_compra.estado_orden_compra in ('ENT', 'CAN'):
                extra_context['show_save_button'] = False
                extra_context['show_continue_button'] = False
                extra_context['show_addanother_button'] = False
                extra_context['show_cancel_button'] = False
                extra_context['show_imprimir_button'] = True
            elif orden_compra_actual.estado_orden_compra.estado_orden_compra in ('EPP', 'PEP', 'PEN'):
                extra_context['show_save_button'] = True
                extra_context['show_continue_button'] = True
                extra_context['show_addanother_button'] = True
                extra_context['show_cancel_button'] = True
                extra_context['show_imprimir_button'] = True

        elif object_id is None:
            extra_context['show_save_button'] = True
            extra_context['show_continue_button'] = True
            extra_context['show_addanother_button'] = True
            extra_context['show_cancel_button'] = False
            extra_context['show_imprimir_button'] = False

        return super(OrdenCompraAdmin, self).changeform_view(request, object_id, form_url, extra_context)

    def changelist_view(self, request, extra_context=None):
        queryset = self.get_queryset(request).filter(estado_orden_compra__estado_orden_compra='EPP')

        for orden_compra in queryset:
            now = timezone.now()
            print orden_compra.fecha_entrega_orden_compra, now

            if orden_compra.fecha_entrega_orden_compra < now:
            # if timezone.localtime(orden_compra.fecha_entrega_orden_compra) < now:
                estado = OrdenCompraEstado.objects.get(estado_orden_compra='PEP')
                orden_compra.estado_orden_compra = estado
                orden_compra.save()

        return super(OrdenCompraAdmin, self). changelist_view(request, extra_context=extra_context)

    def get_form(self, request, obj=None, **kwargs):
        for a in request.POST: print a
        # if '_cancel' in request.POST:
        #     form = CancelarOrdenCompraForm
        # else:
        form = super(OrdenCompraAdmin, self).get_form(request, obj=obj, **kwargs)
        form.request = request
        return form


# ======================================================================================================================
class CompraDetalleInline(admin.TabularInline):
    model = CompraDetalle
    extra = 0
    can_delete = False
    # read_only_fields = ['producto_compra', 'precio_producto_compra', 'unidad_medida_compra',
    #                     'cantidad_producto_compra', 'total_producto_compra']
    fields = ['producto_compra', 'precio_producto_compra', 'unidad_medida_compra', 'cantidad_producto_compra',
              'total_producto_compra']
    form = CompraDetalleForm
    # raw_id_fields = ['producto_compra']
    verbose_name = 'Detalle de Productos de la Compra'
    verbose_name_plural = 'Detalles de Productos de las Compras'

    def get_readonly_fields(self, request, obj=None):
        # if obj is not None and obj.estado_compra.estado_orden_compra in ('ENT', 'CAN'):
        if obj is not None:
            return [i.name for i in self.model._meta.fields]
        else:
            return super(CompraDetalleInline, self).get_readonly_fields(request, obj)

    # def has_add_permission(self, request):
    #     object_id = request.path.split("/")[-2]
    #     if object_id != "add":
    #         compra_actual = Compra.objects.get(pk=object_id)
    #         return compra_actual.estado_compra.estado_orden_compra not in ('ENT', 'CAN')
    #     else:
    #         return super(CompraDetalleInline, self).has_add_permission(request)
    #
    # def has_delete_permission(self, request, obj=None):
    #     if obj is not None and obj.estado_compra.estado_orden_compra in ('ENT', 'CAN'):
    #         return False
    #     return super(CompraDetalleInline, self).has_delete_permission(request, obj)

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


class CompraAdmin(admin.ModelAdmin):

    form = CompraForm

    # exclude = ['nro_orden_compra']

    class Media:
        js = [
            'compras/js/compra.js', 'compras/js/jquery.mask.js'
        ]

    readonly_fields = ['numero_compra', 'proveedor', 'tipo_factura_compra', 'fecha_compra', 'estado_compra']
                       # 'numero_orden_compra', 'disponible_linea_credito_proveedor', 'total_compra']

    # raw_id_fields = ['numero_orden_compra']

    fieldsets = [
        # ('Compra ID', {'fields': ['numero_compra']}),
        ('Numero Orden de Compra', {'fields': ['nro_orden_compra', 'numero_orden_compra', 'proveedor',
                                               'disponible_linea_credito_proveedor']}),
        # ('Datos de la Orden de Compra', {'fields': ['orden_compra__proveedor_orden_compra',
        #                                             'orden_compra__forma_pago_orden_compra',
        #                                             ('orden_compra__fecha_orden_compra',
        #                                              'orden_compra__fecha_entrega_orden_compra')]}),
        ('Datos de la Factura', {'fields': ['numero_factura_compra', 'tipo_factura_compra', 'fecha_factura_compra']}),
        # ('Datos de la Nota de Credito', {'fields': ['numero_nota_credito_compra']}),
        ('Datos de la Compra', {'fields': ['fecha_compra', 'estado_compra', 'total_compra']}),
    ]

    inlines = [CompraDetalleInline]

    # raw_id_fields = ("numero_orden_compra",)

    list_display = ['numero_orden_compra', 'proveedor', 'fecha_compra', 'numero_factura_compra',
                    'tipo_factura_compra', 'fecha_factura_compra', 'colorea_estado_compra', 'total_compra',
                    'usuario_registro_compra']
    list_display_links = ['numero_orden_compra']
    list_filter = ['numero_compra', ('proveedor', admin.RelatedOnlyFieldListFilter),
                   ('numero_orden_compra', admin.RelatedOnlyFieldListFilter),
                   'fecha_compra', 'numero_factura_compra', 'tipo_factura_compra', 'fecha_factura_compra',
                   'estado_compra__estado_orden_compra', 'total_compra',
                   ('usuario_registro_compra', admin.RelatedOnlyFieldListFilter)]
    search_fields = ['numero_compra', 'proveedor__proveedor', 'numero_orden_compra__numero_orden_compra',
                     'fecha_compra', 'numero_factura_compra', 'tipo_factura_compra__tipo_factura_compra',
                     'fecha_factura_compra', 'estado_compra__estado_orden_compra', 'total_compra',
                     'usuario_registro_compra__usuario__username']

    def colorea_estado_compra(self, obj):
        # color = 'black'
        if obj.estado_compra.estado_orden_compra == 'ENT':
            color = 'green'
            # print 'Entra en colorea_estado_compra:', obj.estado_compra.estado_compra, color
            return format_html('<span style="color: %s"><b> %s </b></span>' %
                               (color, obj.estado_compra.get_estado_orden_compra_display()))
        elif obj.estado_compra.estado_orden_compra == 'PEP':
            color = 'red'
            return format_html('<span style="color: %s"><b> %s </b></span>' %
                               (color, obj.estado_compra.get_estado_orden_compra_display()))
        elif obj.estado_compra.estado_orden_compra == 'CAN':
            color = 'orange'
            return format_html('<span style="color: %s"><b> %s </b></span>' %
                               (color, obj.estado_compra.get_estado_orden_compra_display()))
        elif obj.estado_compra.estado_orden_compra == 'EPP':
            color = 'yellowgreen'
            return format_html('<span style="color: %s"><b> %s </b></span>' %
                               (color, obj.estado_compra.get_estado_orden_compra_display()))
        elif obj.estado_compra.estado_orden_compra == 'PEN':
            color = 'orangered'
            return format_html('<span style="color: %s"><b> %s </b></span>' %
                               (color, obj.estado_compra.get_estado_orden_compra_display()))
        return obj.estado_compra
    colorea_estado_compra.short_description = 'Estado Compra'

    def save_model(self, request, obj, form, change):

        # import pdb
        # pdb.set_trace()

        compra_actual = obj
        compra_anterior = None
        nro_orden_compra_form = form.cleaned_data['nro_orden_compra']
        # tot_compra = 0

        print 'obj: %s - compra_actual: %s - compra_anterior: %s - nro_orden_compra_form: %s' % \
              (obj, compra_actual, compra_anterior, nro_orden_compra_form)

        # Recupera la compra_anterior
        if obj.numero_compra is not None:
            compra_anterior = Compra.objects.get(pk=obj.numero_compra)
            if nro_orden_compra_form is not None:
                compra_actual.numero_orden_compra = nro_orden_compra_form
        else:
            obj.numero_orden_compra = nro_orden_compra_form
            obj.proveedor = Proveedor.objects.get(pk=9)
            # obj.numero_factura_compra = 1
            obj.tipo_factura_compra = TipoFacturaCompra.objects.get(tipo_factura_compra='CON')
            obj.estado_compra = OrdenCompraEstado.objects.get(estado_orden_compra='PEN')
            super(CompraAdmin, self).save_model(request, obj, form, change)

        if "_continue" in request.POST and compra_actual.estado_compra.estado_orden_compra == 'PEN':
            if compra_anterior is None \
                    or compra_anterior.numero_orden_compra_id != compra_actual.numero_orden_compra_id:

                # compra_actual.numero_orden_compra = nro_orden_compra_form
                compra_actual.proveedor = compra_actual.numero_orden_compra.proveedor_orden_compra

                print 'compra_actual.numero_compra: %s - compra_detalle_a_eliminar: %s' % \
                      (compra_actual.numero_compra, CompraDetalle.objects.filter(numero_compra_id=compra_actual.numero_compra))
                CompraDetalle.objects.filter(numero_compra_id=compra_actual.numero_compra).delete()
                print 'compra_detalle_a_eliminar: ', CompraDetalle.objects.filter(numero_compra_id=compra_actual.numero_compra)

                for detalle in OrdenCompraDetalle.objects.filter(numero_orden_compra_id=compra_actual.numero_orden_compra_id):
                    compra_detalle = CompraDetalle(numero_compra_id=compra_actual.numero_compra,
                                                   producto_compra_id=detalle.producto_orden_compra_id,
                                                   precio_producto_compra=detalle.precio_producto_orden_compra,
                                                   cantidad_producto_compra=detalle.cantidad_producto_orden_compra,
                                                   unidad_medida_compra=detalle.unidad_medida_orden_compra,
                                                   total_producto_compra=detalle.total_producto_orden_compra)
                    # tot_compra = tot_compra + detalle.total_producto_orden_compra
                    compra_detalle.save()

                orden = compra_actual.numero_orden_compra
                if orden.forma_pago_orden_compra.forma_pago_compra == 'CO':
                    compra_actual.tipo_factura_compra = TipoFacturaCompra.objects.get(tipo_factura_compra='CON')
                else:
                    compra_actual.tipo_factura_compra = TipoFacturaCompra.objects.get(tipo_factura_compra='CRE')

                # import pdb
                # pdb.set_trace()

                # compra_actual.total_compra = tot_compra
                compra_actual.disponible_linea_credito_proveedor = compra_actual.numero_orden_compra.proveedor_orden_compra.lineacreditoproveedor.disponible_linea_credito_proveedor
                compra_actual.estado_compra = OrdenCompraEstado.objects.get(estado_orden_compra='PEN')
                orden.estado_orden_compra = OrdenCompraEstado.objects.get(estado_orden_compra='PEN')
                compra_actual.total_compra = compra_actual.numero_orden_compra.total_orden_compra
                orden.save()

            if compra_anterior is not None:
                orden_anterior = compra_anterior.numero_orden_compra
                now = timezone.now()

                print 'orden_anterior.fecha_entrega_orden_compra: %s - now: %s' % \
                      (orden_anterior.fecha_entrega_orden_compra, now)

                if orden_anterior.fecha_entrega_orden_compra < now:
                # if timezone.localtime(orden_compra.fecha_entrega_orden_compra) < now:
                    orden_anterior.estado_orden_compra = OrdenCompraEstado.objects.get(estado_orden_compra='PEP')
                elif orden_anterior.fecha_entrega_orden_compra > now:
                    orden_anterior.estado_orden_compra = OrdenCompraEstado.objects.get(estado_orden_compra='EPP')
                orden_anterior.save()

            # ==> Descomentar por si se desee permitir la edicion del detalle de la Compra
            # else:
            #     compra_actual.estado_compra = OrdenCompraEstado.objects.get(estado_orden_compra='BOR')

            super(CompraAdmin, self).save_model(request, obj, form, change)

        # Si se cancela la Compra se asigna el estado "CAN" a la Compra
        elif "_cancel" in request.POST:
            orden = compra_actual.numero_orden_compra
            orden.estado_orden_compra = OrdenCompraEstado.objects.get(estado_orden_compra='CAN')
            orden.motivo_cancelacion = request.POST.get('motivo', '')
            orden.observaciones_cancelacion = request.POST.get('observaciones', '')
            orden.usuario_cancelacion = Empleado.objects.get(usuario_id=request.user)
            orden.fecha_hora_cancelacion = timezone.now()
            orden.save()

            compra_actual.estado_compra = OrdenCompraEstado.objects.get(estado_orden_compra='CAN')
            compra_actual.motivo_cancelacion = request.POST.get('motivo', '')
            compra_actual.observaciones_cancelacion = request.POST.get('observaciones', '')
            compra_actual.usuario_cancelacion = Empleado.objects.get(usuario_id=request.user)
            compra_actual.fecha_hora_cancelacion = timezone.now()

            # return
            super(CompraAdmin, self).save_model(request, obj, form, change)

        # Si se confirma la Compra se asigna el estado "ENT" a la Orden de Compra
        # Capturar el evento de clic en el boton "Confirmar Compra" para asignar el estado de CON a la Compra y el
        # estado de ENT a la Orden de Compra
        elif "_save" in request.POST:  # and compra_actual.estado_compra.estado_compra == 'CON':
            compra_actual.estado_compra = OrdenCompraEstado.objects.get(estado_orden_compra='ENT')
            orden = compra_actual.numero_orden_compra
            orden.estado_orden_compra = OrdenCompraEstado.objects.get(estado_orden_compra='ENT')
        # 3) Al confirmar la Compra se debe generar un registro en FacturaProveedor con los datos de la factura a pagar.
            factura_proveedor = FacturaProveedor(compra_id=compra_actual.numero_compra,
                                                 orden_compra_id=compra_actual.numero_orden_compra.pk,
                                                 proveedor_id=compra_actual.numero_orden_compra.proveedor_orden_compra_id,
                                                 # Incluir orden_pago
                                                 numero_factura_compra=compra_actual.numero_factura_compra,
                                                 fecha_factura_compra=compra_actual.fecha_factura_compra,
                                                 tipo_factura_compra_id=compra_actual.tipo_factura_compra_id,
                                                 forma_pago_compra_id=orden.forma_pago_orden_compra_id,
                                                 plazo_factura_compra=orden.forma_pago_orden_compra.plazo_compra,
                                                 total_factura_compra=compra_actual.total_compra,
                                                 total_pago_factura=0,
                                                 estado_factura_compra=FacturaProveedorEstado.objects.get(estado_factura_proveedor="EPP"))
        # Al confirmar la Compra se debe generar un registro en LineaCreditoProveedorDetalle con los datos de la factura
        # de la Compra.
            proveedor = orden.proveedor_orden_compra
            # Validar que exista una Linea de Credito para el Proveedor, de lo contrario sugerir la creacion de la misma
            linea_credito_proveedor_actual = LineaCreditoProveedor.objects.filter(proveedor_id=proveedor.id)
            if not linea_credito_proveedor_actual.exists():
                linea_credito_proveedor_cabecera = LineaCreditoProveedor(proveedor_id=compra_actual.numero_orden_compra.proveedor_orden_compra_id,
                                                                         linea_credito_proveedor=5000000,
                                                                         fecha_linea_credito_proveedor=timezone.now(),
                                                                         monto_total_facturas_proveedor=compra_actual.total_compra,
                                                                         monto_total_pagos_proveedor=0,
                                                                         uso_linea_credito_proveedor=compra_actual.total_compra,
                                                                         disponible_linea_credito_proveedor=5000000,
                                                                         estado_linea_credito_proveedor="DEL")
                linea_credito_proveedor_cabecera.save()
                linea_credito_proveedor_detalle = LineaCreditoProveedorDetalle(linea_credito_proveedor_id=linea_credito_proveedor_cabecera.id,
                                                                               monto_movimiento=compra_actual.total_compra,
                                                                               tipo_movimiento='FAC',
                                                                               numero_comprobante=compra_actual.numero_factura_compra,
                                                                               fecha_movimiento=compra_actual.fecha_factura_compra)
                linea_credito_proveedor_detalle.save()
            else:
                # Asignar el valor de estado_linea_credito_proveedor evaluando una condicion
                print 'Imprime =====>', linea_credito_proveedor_actual
                print 'Imprime =====>', proveedor
                print 'Imprime =====>', linea_credito_proveedor_actual.first().linea_credito_proveedor
                estado_linea_credito_proveedor = "DEL"
                if linea_credito_proveedor_actual.first().uso_linea_credito_proveedor + compra_actual.total_compra > linea_credito_proveedor_actual.first().linea_credito_proveedor:
                    estado_linea_credito_proveedor = "SOB"
                elif linea_credito_proveedor_actual.first().uso_linea_credito_proveedor + compra_actual.total_compra == linea_credito_proveedor_actual.first().linea_credito_proveedor:
                    estado_linea_credito_proveedor = "LIM"
                elif linea_credito_proveedor_actual.first().uso_linea_credito_proveedor + compra_actual.total_compra < linea_credito_proveedor_actual.first().linea_credito_proveedor:
                    estado_linea_credito_proveedor = "DEL"
                linea_credito_proveedor_cabecera = LineaCreditoProveedor(id=linea_credito_proveedor_actual.first().id,
                                                                         proveedor_id=compra_actual.numero_orden_compra.proveedor_orden_compra_id,
                                                                         linea_credito_proveedor=linea_credito_proveedor_actual.first().linea_credito_proveedor,
                                                                         fecha_linea_credito_proveedor=linea_credito_proveedor_actual.first().fecha_linea_credito_proveedor,
                                                                         monto_total_facturas_proveedor=linea_credito_proveedor_actual.first().monto_total_facturas_proveedor + compra_actual.total_compra,
                                                                         monto_total_pagos_proveedor=linea_credito_proveedor_actual.first().monto_total_pagos_proveedor,
                                                                         uso_linea_credito_proveedor=linea_credito_proveedor_actual.first().uso_linea_credito_proveedor + compra_actual.total_compra,
                                                                         disponible_linea_credito_proveedor=linea_credito_proveedor_actual.first().disponible_linea_credito_proveedor - compra_actual.total_compra,
                                                                         estado_linea_credito_proveedor=estado_linea_credito_proveedor)

                linea_credito_proveedor_cabecera.save()
                linea_credito_proveedor_detalle = LineaCreditoProveedorDetalle(linea_credito_proveedor_id=linea_credito_proveedor_actual.first().id,
                                                                               monto_movimiento=compra_actual.total_compra,
                                                                               tipo_movimiento='FAC',
                                                                               numero_comprobante=compra_actual.numero_factura_compra,
                                                                               fecha_movimiento=compra_actual.fecha_factura_compra)
                linea_credito_proveedor_detalle.save()

            super(CompraAdmin, self).save_model(request, obj, form, change)
            orden.save()

            # try:
            #     factura_proveedor.save()
            # except IntegrityError as ex:
            #     message = 'Ya existe una factura con el Numero de Factura y Fecha de Factura indicados.'
            #     self.message_user(request,message,messages.ERROR)
            #     xx = ex
            #     if xx.pgcode == '23505':
            #         message = 'Ya existe una factura con el Numero de Factura y Fecha de Factura indicados.'
            #         self.message_user(request,message,messages.ERROR)
            #         print 'Error'
            #         raise ValidationError({'numero_factura_compra': _ ()})
            #     else:
            #         raise ValidationError('El registro no puede ser guardado en la Base de Datos.')
            # except:
            #     raise ValidationError({'numero_factura_compra': _('El registro no puede ser guardado en la Base '
            #                                                       'de Datos.')})

            factura_proveedor.save()
            linea_credito_proveedor_detalle.save()

        # import pdb
        # pdb.set_trace()
        # print 'Usuarios: ', request.user, obj, obj.usuario_registro_compra

        # Tratar la condicion "is not None"
        if getattr(obj, 'usuario_registro_compra', None):
            # empleado = Empleado.objects.filter(usuario=request.user)
            obj.usuario_registro_compra = Empleado.objects.get(usuario_id=request.user)
            print 'Usuarios: ', request.user, obj.usuario_registro_compra
            super(CompraAdmin, self).save_model(request, obj, form, change)

    # Alternativa programada con JuanBer para el caso de que no se borraban los registros de CompraDetalle en la DB,
    # el problema se daba con los formfields definidos en el Form, al parecer el framework valida los datos cargdos
    # en los formfields y como son los mismos registrados en la DB no los elimina.
    # Con esta alternativa se realiza el borrado de los registros una vez que finaliza la ejecucion del save_model
    # def response_change(self, request, obj):
    #     """
    #     Determines the HttpResponse for the change_view stage.
    #     """
    #     if "_continue" in request.POST:
    #         boton = request.POST.get('_continue','')
    #         numero_orden_compra = request.POST.get('numero_orden_compra','')
    #
    #         if numero_orden_compra:
    #             obj.numero_orden_compra_id = numero_orden_compra
    #             obj.save()
    #
    #         if boton == 'cambio_nro_orden':
    #             detalles = CompraDetalle.objects.filter(numero_compra_id=obj.pk)
    #             detalles.delete()
    #             for detalle in OrdenCompraDetalle.objects.filter(numero_orden_compra_id=obj.numero_orden_compra_id):
    #                 compra_detalle = CompraDetalle(numero_compra_id=obj.numero_compra,
    #                                                producto_compra_id=detalle.producto_orden_compra_id,
    #                                                precio_producto_compra=detalle.precio_producto_orden_compra,
    #                                                cantidad_producto_compra=detalle.cantidad_producto_orden_compra,
    #                                                unidad_medida_compra=detalle.unidad_medida_orden_compra,
    #                                                total_producto_compra=detalle.total_producto_orden_compra)
    #                 compra_detalle.save()
    #             return HttpResponseRedirect('/admin/compras/compra/%s/'%obj.pk)
    #     return super(CompraAdmin, self).response_change(request, obj)

    def save_formset(self, request, form, formset, change):

        # import pdb
        # pdb.set_trace()

        # si orden cambio entonces no hacer nada
        compra_actual = form.instance
        super(CompraAdmin, self).save_formset(request, form, formset, change)

        # ==> Descomentar por si se desee permitir la edicion del detalle de la Compra
        # if "_continue" in request.POST and compra_actual.estado_compra.estado_orden_compra == 'PEN':
        #     formset.save(commit=False)
        #     for form in formset:
        #         form.instance.delete()
        # elif "_continue" in request.POST and compra_actual.estado_compra.estado_orden_compra == 'BOR':
        #     formset.save(commit=False)
        #     for form in formset:
        #         form.instance.save()
        #     compra_actual.estado_compra = OrdenCompraEstado.objects.get(estado_orden_compra='PEN')
        #     compra_actual.save()

        # Si la Compra se confirma se suman los Productos al Stock.
        if compra_actual.estado_compra.estado_orden_compra == 'ENT':
            for form in formset:
                detalle = form.instance
                # # Validar que exista un registro de Stock para el Producto, si no existe entonces se debe crear el
                # # registro cabecera en la tabla Stock y luego el detalle en Stock_Detalle
                # # stock_actual = Stock.objects.get(producto_stock_id=detalle.producto_compra_id)
                # stock_actual = MovimientoStock.objects.filter(producto_stock_id=detalle.producto_compra_id)
                # if not stock_actual.exists():
                #     stock = MovimientoStock(producto_stock_id=detalle.producto_compra_id,
                #                   stock_minimo=0,
                #                   cantidad_existente=detalle.cantidad_producto_compra)
                #     stock.save()
                #     stock_detalle = MovimientoStock(stock_id=stock.id,
                #                                  tipo_movimiento=TipoMovimientoStock.objects.get(tipo_movimiento_stock='CO'),
                #                                  id_movimiento=compra_actual.numero_compra,
                #                                  ubicacion_origen=Deposito.objects.get(deposito='PRO'),
                #                                  ubicacion_destino=Deposito.objects.get(deposito='DCE'),
                #                                  cantidad_entrante=detalle.cantidad_producto_compra,
                #                                  cantidad_saliente=0,
                #                                  fecha_hora_registro_stock=timezone.now())
                #     stock_detalle.save()
                # else:
                #     stock = MovimientoStock(id=stock_actual.first().id,
                #                   producto_stock_id=detalle.producto_compra_id,
                #                   stock_minimo=stock_actual.first().stock_minimo,
                #                   cantidad_existente=stock_actual.first().cantidad_existente + detalle.cantidad_producto_compra)
                #     stock.save()
                #     stock_detalle = MovimientoStock(stock_id=stock_actual.first().id,
                #                                  tipo_movimiento=TipoMovimientoStock.objects.get(tipo_movimiento_stock='CO'),
                #                                  id_movimiento=compra_actual.numero_compra,
                #                                  ubicacion_origen=Deposito.objects.get(deposito='PRO'),
                #                                  ubicacion_destino=Deposito.objects.get(deposito='DCE'),
                #                                  cantidad_entrante=detalle.cantidad_producto_compra,
                #                                  cantidad_saliente=0,
                #                                  fecha_hora_registro_stock=timezone.now())
                #     stock_detalle.save()

                # Si el Producto es un Insumo se debe multiplicar su contenido por las unidades compradas.
                # import pdb
                # pdb.set_trace()

                cantidad = detalle.cantidad_producto_compra
                if detalle.producto_compra.tipo_producto == 'IN':
                    cantidad = detalle.cantidad_producto_compra * detalle.producto_compra.contenido
                elif detalle.producto_compra.tipo_producto == 'VE':
                    cantidad = detalle.cantidad_producto_compra

                stock = MovimientoStock(producto_stock_id=detalle.producto_compra_id,
                                        tipo_movimiento='CO',
                                        id_movimiento=compra_actual.numero_compra,
                                        ubicacion_origen=Deposito.objects.get(deposito='PRO'),
                                        ubicacion_destino=Deposito.objects.get(deposito='DCE'),
                                        cantidad_entrante=cantidad,
                                        cantidad_saliente=0,
                                        fecha_hora_registro_stock=timezone.now())
                stock.save()

                # Asigna precio_compra y precio_venta de acuerdo a las Compras realizadas.
                producto = Producto.objects.get(id=detalle.producto_compra_id)
                compras = CompraDetalle.objects.filter(producto_compra_id=producto.id,
                                                       numero_compra__estado_compra__estado_orden_compra='ENT')
                fecha = timezone.now() - datetime.timedelta(days=30)
                compras = compras.filter(numero_compra__fecha_compra__gte=fecha)
                total = 0
                cantidad = 0
                # precio_compra_sugerido = 0

                if compras.exists():
                    for producto_compra in compras:
                        total += producto_compra.precio_producto_compra
                        # cantidad += detalle.cantidad_producto_compra
                        cantidad += 1
                    print total, cantidad
                    producto.precio_compra = total / (cantidad if cantidad else 1)
                else:
                    producto.precio_compra = detalle.precio_producto_compra

                if producto.tipo_producto == 'VE':
                    producto.precio_venta = (((producto.precio_compra * producto.porcentaje_ganancia) / 100) + producto.precio_compra)

                producto.save()

    def get_readonly_fields(self, request, obj=None):
        if obj is not None and obj.estado_compra.estado_orden_compra in ('PEN', 'EPP', 'PEP'):
            return ['numero_compra', 'proveedor', 'tipo_factura_compra', 'fecha_compra', 'estado_compra']
                    # 'numero_orden_compra', 'total_compra']
        elif obj is not None and obj.estado_compra.estado_orden_compra in ('ENT', 'CAN'):
            return [i.name for i in self.model._meta.fields] + \
                   [i.name for i in self.model._meta.many_to_many]
        # elif obj is None:
        #     return ['numero_compra', 'proveedor', 'tipo_factura_compra', 'fecha_compra', 'estado_compra']
        #             # 'total_compra']
        else:
            return super(CompraAdmin, self).get_readonly_fields(request, obj)

    def changeform_view(self, request, object_id=None, form_url='', extra_context=None):
        extra_context = extra_context or {}

        extra_context['show_button'] = True
        if object_id is not None:
            compra_actual = Compra.objects.get(pk=object_id)
            # extra_context['show_button'] = compra_actual.estado_compra.estado_orden_compra not in ('ENT', 'CAN')

            if compra_actual.estado_compra.estado_orden_compra in ('EPP', 'PEP', 'PEN'):
                extra_context['show_save_button'] = True
                extra_context['show_continue_button'] = True
                extra_context['show_cancel_button'] = True
                extra_context['show_imprimir_button'] = False
            elif compra_actual.estado_compra.estado_orden_compra in ('ENT', 'CAN'):
                extra_context['show_save_button'] = False
                extra_context['show_continue_button'] = False
                extra_context['show_cancel_button'] = False
                extra_context['show_imprimir_button'] = True

        elif object_id is None:
            extra_context['show_save_button'] = True
            extra_context['show_continue_button'] = True
            extra_context['show_cancel_button'] = False
            extra_context['show_imprimir_button'] = False

        return super(CompraAdmin, self).changeform_view(request, object_id, form_url, extra_context)

    # def get_form(self, request, obj=None, **kwargs):
    #
    #     import pdb
    #     pdb.set_trace()
    #
    #     compra = obj
    #     if compra.estado_compra.estado_orden_compra in ('ENT', 'CAN'):
    #         self.exclude = ("nro_orden_compra", )
    #         # kwargs['exclude'] = ['fecha_compra', 'nro_orden_compra']
    #     form = super(CompraAdmin, self).get_form(request, obj, **kwargs)
    #       print form.errors
    #     return form

    def get_new_fieldsets(self):
        return [
            # ('Compra ID', {'fields': ['numero_compra']}),
            ('Numero Orden de Compra', {'fields': ['numero_orden_compra', 'proveedor',
                                                   'disponible_linea_credito_proveedor']}),
            ('Datos de la Factura', {'fields': ['numero_factura_compra', 'tipo_factura_compra',
                                                'fecha_factura_compra']}),
            ('Datos de la Compra', {'fields': ['fecha_compra', 'estado_compra', 'total_compra']}),
        ]

    # def get_urls(self):
    #     urls = super(OrdenCompraAdmin, self).get_urls()
    #     my_urls = patterns('',
    #         (r'\d+/cancelar/$', self.admin_site.admin_view(self.review)),
    #     )
    #     return my_urls + urls
    #
    # def review(self, request, id):
    #     orden_compra = OrdenCompra.objects.get(pk=id)
    #
    #     return render_to_response(self.review_template, {
    #         'title': 'Review entry: %s' % entry.title,
    #         'entry': entry,
    #         'opts': self.model._meta,
    #         'root_path': self.admin_site.root_path,
    #     }, context_instance=RequestContext(request))

    def get_fieldsets(self, request, obj=None):
        if obj is not None:
            if obj.estado_compra.estado_orden_compra in ['ENT', 'CAN']:
                return self.get_new_fieldsets()
        return super(CompraAdmin, self).get_fieldsets(request, obj)

    def get_form(self, request, obj=None, **kwargs):
        # if obj is not None:
        #     if '_save' in request.POST:  # or obj.estado_compra.estado_orden_compra in ['ENT', 'CAN']:
        #         # self.fieldsets = self.get_new_fieldsets()
        #         return ConfirmarCompraForm
        # return super(CompraAdmin, self).get_form(request, obj, **kwargs)

        # ModelForm = super(CompraAdmin, self).get_form(request, obj=None, **kwargs)
        #
        # def form_wrapper(*args, **kwargs):
        #     a = ModelForm(*args, **kwargs)
        #     a.request = request
        #     return a
        # return form_wrapper
        
        for a in request.POST: print a
        # if '_cancel' in request.POST:
        #     form = CancelarCompraForm
        # else:
        form = super(CompraAdmin, self).get_form(request, obj=obj, **kwargs)
        form.request = request
        return form

    # def has_add_permission(self, request):
    #     return False

    def has_delete_permission(self, request, obj=None):
        return False


# ======================================================================================================================
# class OrdenCompraChildAdmin(PolymorphicChildModelAdmin):
#     base_model = OrdenCompra
#     # base_form =
#     # base_fieldsets =
#
#
# class OrdenCompraDetalleChildAdmin(PolymorphicChildModelAdmin):
#     base_model = OrdenCompraDetalle
#
#
# class CompraAdmin(OrdenCompraChildAdmin):
#     base_model = Compra
#
#
# class CompraDetalleAdmin(OrdenCompraDetalleChildAdmin):
#     base_model = CompraDetalle
#
#
# class OrdenCompraParentAdmin(PolymorphicParentModelAdmin):
#     base_model = OrdenCompra
#     child_models = (Compra,)
#     list_filter = (PolymorphicChildModelFilter,)
#
#
# class OrdenCompraDetalleParentAdmin(PolymorphicParentModelAdmin):
#     base_model = OrdenCompraDetalle
#     child_models = (CompraDetalle,)
#     list_filter = (PolymorphicChildModelFilter,)

# ======================================================================================================================
# class ModelAChildAdmin(PolymorphicChildModelAdmin):
#     """ Base admin class for all child models """
#     base_model = ModelA
#
#     # By using these `base_...` attributes instead of the regular ModelAdmin `form` and `fieldsets`,
#     # the additional fields of the child models are automatically added to the admin form.
#     # base_form = ...
#     # base_fieldsets = (
#     #     ...
#     # )
#
#
# class ModelBAdmin(ModelAChildAdmin):
#     base_model = ModelB
#     # define custom features here
#
#
# class ModelCAdmin(ModelBAdmin):
#     base_model = ModelC
#     show_in_index = True  # makes child model admin visible in main admin site
#     # define custom features here
#
#
# class ModelAParentAdmin(PolymorphicParentModelAdmin):
#     """ The parent model admin """
#     base_model = ModelA
#     child_models = (ModelB, ModelC)
#     list_filter = (PolymorphicChildModelFilter,)  # This is optional.
# ======================================================================================================================

# admin.site.site_header = 'Prueba de Cabecera del Sitio'
# admin.site.site_title = 'Hola Mundo2!'
# admin.site.index_title = 'Hola Mundo!'

admin.site.register(Proveedor, ProveedorAdmin)
admin.site.register(LineaCreditoProveedor, LineaCreditoProveedorAdmin)
admin.site.register(FacturaProveedor, FacturaProveedorAdmin)
admin.site.register(OrdenPago, OrdenPagoAdmin)
# admin.site.register(ProductoProveedor, ProductoProveedorAdmin)
admin.site.register(Empresa, EmpresaAdmin)
admin.site.register(OrdenCompra, OrdenCompraAdmin)
admin.site.register(Compra, CompraAdmin)

# Only the parent needs to be registered:
# admin.site.register(OrdenCompra, OrdenCompraParentAdmin)
# admin.site.register(OrdenCompraDetalle, OrdenCompraDetalleParentAdmin)
# admin.site.register(Compra, CompraAdmin)
# admin.site.register(CompraDetalle, CompraDetalleAdmin)
# admin.site.register(ModelA, ModelAParentAdmin)
# admin.site.register(ModelB, ModelBAdmin)
# admin.site.register(ModelC, ModelCAdmin)