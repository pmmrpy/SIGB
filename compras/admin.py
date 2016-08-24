from django.contrib import admin

# from polymorphic.admin import PolymorphicParentModelAdmin, PolymorphicChildModelAdmin, PolymorphicChildModelFilter
from django.utils import timezone
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
from .forms import LineaCreditoProveedorForm, LineaCreditoProveedorDetalleForm, PagoProveedorForm, \
    FacturaProveedorForm, EmpresaForm, OrdenCompraForm, OrdenCompraDetalleForm, CompraForm, CompraDetalleForm
from .models import ProveedorTelefono, LineaCreditoProveedor, LineaCreditoProveedorDetalle, Proveedor, PagoProveedor, \
    FacturaProveedor, ProductoProveedor, Empresa, OrdenCompra, OrdenCompraDetalle, Compra, CompraDetalle \
    # , ModelA, ModelB, ModelC
from bar.models import CompraEstado, OrdenCompraEstado, TipoMovimientoStock, Deposito, TipoFacturaCompra
from stock.models import Stock, StockDetalle
from personal.models import Empleado

from django.http import HttpResponse
from reports import ReportOrdenCompra, GraphicsReport, MasterReport
from geraldo.generators import PDFGenerator

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
    verbose_name = 'Telefonos'
    verbose_name_plural = 'Telefonos'


class ProveedorAdmin(admin.ModelAdmin):

    class Media:
        js = [
            'compras/js/proveedor.js'
        ]

    readonly_fields = ('digito_verificador', 'fecha_alta_proveedor')

    # list_editable = ('id', 'proveedor', 'ruc', 'digito_verificador', 'direccion', 'pagina_web')

    fieldsets = [
        ('Empresa', {'fields': ['proveedor', 'persona_proveedor']}),
        ('RUC', {'fields': ['ruc', 'digito_verificador']}),
        ('Direccion', {'fields': ['direccion', ('pais_proveedor', 'ciudad_proveedor')]}),
        ('Otros datos', {'fields': ['pagina_web', 'fecha_alta_proveedor']}),
    ]

    inlines = [ProveedorTelefonoInline]

    list_display = ('id', 'proveedor', 'persona_proveedor', 'ruc', 'digito_verificador', 'direccion', 'pais_proveedor',
                    'ciudad_proveedor', 'pagina_web', 'fecha_alta_proveedor')
    list_display_links = ['proveedor']
    list_filter = ['id', 'proveedor', 'ruc', 'fecha_alta_proveedor']
    search_fields = ['id', 'proveedor', 'ruc', 'fecha_alta_proveedor']

    def save_model(self, request, obj, form, change):
        if obj.ruc is not None:
            obj.digito_verificador = calcular_dv(obj.ruc, 11)
        else:
            raise ValidationError({'digito_verificador': _('RUC no valido.')})
        super(ProveedorAdmin, self).save_model(request, obj, form, change)


class LineaCreditoProveedorDetalleInline(admin.TabularInline):
    model = LineaCreditoProveedorDetalle
    extra = 0
    readonly_fields = ['monto_movimiento', 'tipo_movimiento', 'numero_comprobante', 'fecha_movimiento']
    fields = ['tipo_movimiento', 'monto_movimiento', 'numero_comprobante', 'fecha_movimiento']
    form = LineaCreditoProveedorDetalleForm
    # verbose_name = 'Linea de Credito del Proveedor'
    # verbose_name_plural = 'Lineas de Credito del Proveedor'


class LineaCreditoProveedorAdmin(admin.ModelAdmin):

    form = LineaCreditoProveedorForm

    class Media:
        js = [
            ''
        ]

    readonly_fields = ['proveedor', 'fecha_linea_credito_proveedor', 'monto_total_facturas_proveedor',
                       'monto_total_pagos_proveedor', 'uso_linea_credito_proveedor', 'estado_linea_credito_proveedor']

    # raw_id_fields =

    fieldsets = [
        ('Proveedor', {'fields': ['proveedor']}),
        ('Linea de Credito', {'fields': ['linea_credito_proveedor', 'fecha_linea_credito_proveedor']}),
        ('Utilizacion Linea de Credito', {'fields': ['monto_total_facturas_proveedor', 'monto_total_pagos_proveedor',
                                                     'uso_linea_credito_proveedor', 'estado_linea_credito_proveedor']}),
    ]

    inlines = [LineaCreditoProveedorDetalleInline]

    list_display = ['proveedor', 'linea_credito_proveedor', 'fecha_linea_credito_proveedor',
                    'monto_total_facturas_proveedor', 'monto_total_pagos_proveedor', 'uso_linea_credito_proveedor',
                    'estado_linea_credito_proveedor']
    list_filter = ['proveedor', 'linea_credito_proveedor', 'fecha_linea_credito_proveedor',
                   'estado_linea_credito_proveedor']
    search_fields = ['proveedor', 'linea_credito_proveedor', 'fecha_linea_credito_proveedor',
                     'estado_linea_credito_proveedor']


class PagoProveedorInline(admin.TabularInline):
    model = PagoProveedor
    extra = 0
    form = PagoProveedorForm
    # verbose_name = 'Pago a Proveedores'
    # verbose_name_plural = 'Pagos a Proveedores'


class FacturaProveedorAdmin(admin.ModelAdmin):

    form = FacturaProveedorForm

    class Media:
        js = [
            ''
        ]

    readonly_fields = ['proveedor', 'compra', 'numero_factura_compra', 'fecha_factura_compra', 'tipo_factura_compra',
                       'forma_pago_compra', 'plazo_factura_compra', 'total_factura_compra', 'total_pago_factura',
                       'estado_factura_compra']

    # readonly_fields = ['__all__']

    raw_id_fields = ['compra']

    fieldsets = [
        ('Datos de la Factura', {'fields': ['proveedor', 'compra', 'numero_factura_compra', 'fecha_factura_compra',
                                            'tipo_factura_compra', 'forma_pago_compra', 'plazo_factura_compra',
                                            'total_factura_compra', 'total_pago_factura', 'estado_factura_compra']}),
    ]

    inlines = [PagoProveedorInline]

    list_display = ['id', 'proveedor', 'compra', 'numero_factura_compra', 'fecha_factura_compra', 'tipo_factura_compra',
                    'forma_pago_compra', 'plazo_factura_compra', 'total_factura_compra', 'total_pago_factura',
                    'estado_factura_compra']
    list_display_links = ['proveedor']
    list_filter = ['id', 'proveedor', 'compra', 'numero_factura_compra', 'fecha_factura_compra', 'tipo_factura_compra',
                   'forma_pago_compra', 'plazo_factura_compra', 'estado_factura_compra']
    search_fields = ['id', 'proveedor', 'compra', 'numero_factura_compra', 'fecha_factura_compra',
                     'tipo_factura_compra', 'forma_pago_compra', 'plazo_factura_compra', 'estado_factura_compra']


# class ProductoProveedorAdmin(admin.ModelAdmin):
#     raw_id_fields = ['producto']
#     list_display = ('id', 'proveedor', 'producto')
#     list_filter = ['id', 'proveedor', 'producto']
#     search_fields = ['id', 'proveedor', 'producto']


class EmpresaAdmin(admin.ModelAdmin):

    form = EmpresaForm

    readonly_fields = ('digito_verificador', 'fecha_alta_proveedor', 'thumb')

    # list_editable = ('id', 'proveedor', 'ruc', 'digito_verificador', 'direccion', 'pagina_web')

    fieldsets = [
        ('Empresa', {'fields': ['proveedor', 'persona_proveedor']}),
        ('RUC', {'fields': ['ruc', 'digito_verificador']}),
        ('Logo', {'fields': ['logo_empresa', 'thumb']}),
        ('Direccion', {'fields': ['direccion', ('pais_proveedor', 'ciudad_proveedor')]}),
        ('Otros datos', {'fields': ['pagina_web', 'fecha_apertura', 'fecha_alta_proveedor']}),
        # ('Timbrado', {'fields': ['timbrado']}),
        ('Datos Tributarios', {'fields': ['codigo_establecimiento', 'actividad_economica', 'salario_minimo_vigente']})
    ]

    list_display = ('id', 'proveedor', 'persona_proveedor', 'ruc', 'digito_verificador', 'direccion', 'pais_proveedor',
                    'ciudad_proveedor', 'pagina_web', 'fecha_apertura', 'fecha_alta_proveedor',
                    'codigo_establecimiento', 'thumb')
    list_filter = ['id', 'proveedor', 'ruc', 'fecha_alta_proveedor']
    search_fields = ['id', 'proveedor', 'ruc', 'fecha_alta_proveedor']


# ======================================================================================================================
class OrdenCompraDetalleInline(admin.TabularInline):
    model = OrdenCompraDetalle
    extra = 0
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
            'compras/js/autoNumeric.js', 'compras/js/orden_compra.js'  # 'compras/js/change_form.js',
        ]

    # readonly_fields = ('numero_orden_compra', 'fecha_orden_compra', 'estado_orden_compra')

    raw_id_fields = ['proveedor_orden_compra']

    fieldsets = [
        ('Numero Orden de Compra', {'fields': ['numero_orden_compra']}),
        ('Datos del Proveedor', {'fields': ['proveedor_orden_compra', 'forma_pago_orden_compra']}),
        ('Fechas', {'fields': ['fecha_orden_compra', 'fecha_ultima_modificacion_orden_compra',
                               'fecha_entrega_orden_compra']}),
        # ('Fecha de Entrega del Pedido', {'fields': ['fecha_entrega']}),
        ('Otros datos de la Orden de Compra', {'fields': ['estado_orden_compra', 'total_orden_compra']}),
    ]

    inlines = [OrdenCompraDetalleInline]

    # list_select_related = True
    list_display = ('numero_orden_compra', 'proveedor_orden_compra', 'fecha_orden_compra',
                    'fecha_ultima_modificacion_orden_compra', 'fecha_entrega_orden_compra', 'forma_pago_orden_compra',
                    'estado_orden_compra', 'total_orden_compra', 'usuario_registro_orden_compra')
    list_filter = ['numero_orden_compra', ('proveedor_orden_compra', admin.RelatedOnlyFieldListFilter),
                   'fecha_orden_compra', 'fecha_ultima_modificacion_orden_compra', 'fecha_entrega_orden_compra',
                   'forma_pago_orden_compra', 'estado_orden_compra', 'usuario_registro_orden_compra']
    search_fields = ['numero_orden_compra', 'proveedor_orden_compra', 'fecha_orden_compra',
                     'fecha_ultima_modificacion_orden_compra', 'fecha_entrega_orden_compra', 'forma_pago_orden_compra',
                     'estado_orden_compra', 'usuario_registro_orden_compra']

    # def get_readonly_fields(self, request, obj=None):
    #     if obj:  # This is the case when obj is already created i.e. it's an edit
    #         return ['numero_orden_compra', 'fecha_orden_compra', 'estado_orden_compra', 'proveedor_orden_compra']
    #     # elif object.
    #     else:
    #         return ['numero_orden_compra', 'fecha_orden_compra', 'estado_orden_compra']

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

        if getattr(obj, 'usuario_registro_orden_compra', None) is None:
            # empleado = Empleado.objects.filter(usuario=request.user)
            obj.usuario_registro_orden_compra = Empleado.objects.get(usuario_id=request.user)
        super(OrdenCompraAdmin, self).save_model(request, obj, form, change)

    def get_readonly_fields(self, request, obj=None):
        if obj is not None and obj.estado_orden_compra.estado_orden_compra in ('EPP', 'PEP'):
            return ['numero_orden_compra', 'fecha_orden_compra', 'fecha_ultima_modificacion_orden_compra',
                    'estado_orden_compra', 'proveedor_orden_compra']
        elif obj is not None and obj.estado_orden_compra.estado_orden_compra in ('ENT', 'CAN'):
            return [i.name for i in self.model._meta.fields] + \
                   [i.name for i in self.model._meta.many_to_many]
        elif obj is None:
            return ['numero_orden_compra', 'fecha_orden_compra', 'fecha_ultima_modificacion_orden_compra',
                    'estado_orden_compra']
        else:
            return super(OrdenCompraAdmin, self).get_readonly_fields(request, obj)

    def changeform_view(self, request, object_id=None, form_url='', extra_context=None):
        extra_context = extra_context or {}

        extra_context['show_button'] = True
        if object_id is not None:
            orden_compra_actual = OrdenCompra.objects.get(pk=object_id)
            extra_context['show_button'] = orden_compra_actual.estado_orden_compra.estado_orden_compra \
                                           not in ('ENT', 'CAN')

        return super(OrdenCompraAdmin, self).changeform_view(request, object_id, form_url, extra_context)


# ======================================================================================================================
class CompraDetalleInline(admin.TabularInline):
    model = CompraDetalle
    extra = 0
    form = CompraDetalleForm
    raw_id_fields = ['producto_compra']
    verbose_name = 'Detalle de Productos de la Compra'
    verbose_name_plural = 'Detalles de Productos de las Compras'

    def get_readonly_fields(self, request, obj=None):
        if obj is not None and obj.estado_compra.estado_compra in ('CON', 'CAN'):
            return [i.name for i in self.model._meta.fields]
        else:
            return super(CompraDetalleInline, self).get_readonly_fields(request, obj)

    def has_add_permission(self, request):
        object_id = request.path.split("/")[-2]
        if object_id != "add":
            compra_actual = Compra.objects.get(pk=object_id)
            return compra_actual.estado_compra.estado_compra not in ('CON', 'CAN')
        else:
            return super(CompraDetalleInline, self).has_add_permission(request)

    def has_delete_permission(self, request, obj=None):
        if obj is not None and obj.estado_compra.estado_compra in ('CON', 'CAN'):
            return False
        return super(CompraDetalleInline, self).has_delete_permission(request, obj)


class CompraAdmin(admin.ModelAdmin):

    form = CompraForm

    class Media:
        js = [
            'compras/js/compra.js'
        ]

    readonly_fields = ['numero_compra', 'proveedor', 'tipo_factura_compra', 'fecha_compra', 'estado_compra',
                       'total_compra']

    # raw_id_fields = ['numero_orden_compra']

    fieldsets = [
        ('Compra ID', {'fields': ['numero_compra']}),
        ('Numero Orden de Compra', {'fields': ['numero_orden_compra', 'proveedor']}),
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

    list_display = ('numero_compra', 'proveedor', 'numero_orden_compra', 'fecha_compra', 'numero_factura_compra',
                    'tipo_factura_compra', 'fecha_factura_compra', 'estado_compra', 'total_compra',
                    'usuario_registro_compra')
    list_filter = ['numero_compra', 'proveedor', ('numero_orden_compra', admin.RelatedOnlyFieldListFilter),
                   'fecha_compra', 'numero_factura_compra', 'tipo_factura_compra', 'fecha_factura_compra',
                   'estado_compra', 'total_compra', 'usuario_registro_compra']
    search_fields = ['numero_compra', 'proveedor__proveedor', 'numero_orden_compra__numero_orden_compra',
                     'fecha_compra', 'numero_factura_compra', 'tipo_factura_compra__tipo_factura_compra',
                     'fecha_factura_compra', 'estado_compra__estado_compra', 'total_compra', 'usuario_registro_compra']

    def save_model(self, request, obj, form, change):
        compra_actual = obj
        compra_anterior = None
        tot_compra = 0
        # Recupera la compra_anterior
        if obj.numero_compra is not None:
            compra_anterior = Compra.objects.get(pk=obj.numero_compra)
        else:
            super(CompraAdmin, self).save_model(request, obj, form, change)

        if "_continue" in request.POST and compra_actual.estado_compra.estado_compra == 'PEN':
            if compra_anterior is None \
                    or compra_anterior.numero_orden_compra_id != compra_actual.numero_orden_compra_id:
                compra_actual.proveedor = compra_actual.numero_orden_compra.proveedor_orden_compra
                CompraDetalle.objects.filter(numero_compra_id=compra_actual.numero_compra).delete()
                for detalle in OrdenCompraDetalle.objects.filter(numero_orden_compra_id=compra_actual.numero_orden_compra_id):
                    compra_detalle = CompraDetalle(numero_compra_id=compra_actual.numero_compra,
                                                   producto_compra_id=detalle.producto_orden_compra_id,
                                                   precio_producto_compra=detalle.precio_producto_orden_compra,
                                                   cantidad_producto_compra=detalle.cantidad_producto_orden_compra,
                                                   # unidad_medida_compra=detalle.unidad_medida_orden_compra,
                                                   total_producto_compra=detalle.total_producto_orden_compra)
                    tot_compra = tot_compra + detalle.total_producto_orden_compra
                    compra_detalle.save()
                orden = compra_actual.numero_orden_compra
                if orden.forma_pago_orden_compra.forma_pago_compra == 'CO':
                    compra_actual.tipo_factura_compra = TipoFacturaCompra.objects.get(tipo_factura_compra='CON')
                else:
                    compra_actual.tipo_factura_compra = TipoFacturaCompra.objects.get(tipo_factura_compra='CRE')
            compra_actual.total_compra = tot_compra
            compra_actual.estado_compra = CompraEstado.objects.get(estado_compra='PEN')
            super(CompraAdmin, self).save_model(request, obj, form, change)

        # Si se cancela la Compra se asigna el estado "CAN" a la Compra
        elif "_cancel" in request.POST:
            compra_actual.estado_compra = CompraEstado.objects.get(estado_compra='CAN')
            orden = compra_actual.numero_orden_compra
            orden.estado_orden_compra = OrdenCompraEstado.objects.get(estado_orden_compra='CAN')
            super(CompraAdmin, self).save_model(request, obj, form, change)

        # Si se confirma la Compra se asigna el estado "ENT" a la Orden de Compra
        # Capturar el evento de clic en el boton "Confirmar Compra" para asignar el estado de CON a la Compra y el
        # estado de ENT a la Orden de Compra
        elif "_save" in request.POST:  # and compra_actual.estado_compra.estado_compra == 'CON':
            compra_actual.estado_compra = CompraEstado.objects.get(estado_compra='CON')
            orden = compra_actual.numero_orden_compra
            orden.estado_orden_compra = OrdenCompraEstado.objects.get(estado_orden_compra='ENT')
        # 3) Al confirmar la Compra se debe generar un registro en FacturaProveedor con los datos de la factura a pagar.
            factura_proveedor = FacturaProveedor(compra_id=compra_actual.numero_compra,
                                                 proveedor_id=compra_actual.numero_orden_compra.proveedor_orden_compra_id,
                                                 numero_factura_compra=compra_actual.numero_factura_compra,
                                                 fecha_factura_compra=compra_actual.fecha_factura_compra,
                                                 tipo_factura_compra_id=compra_actual.tipo_factura_compra_id,
                                                 forma_pago_compra_id=orden.forma_pago_orden_compra_id,
                                                 plazo_factura_compra=orden.forma_pago_orden_compra.plazo_compra,
                                                 total_factura_compra=compra_actual.total_compra,
                                                 total_pago_factura=0,
                                                 estado_factura_compra="PEN")
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
                                                                         estado_linea_credito_proveedor="DEL")
                linea_credito_proveedor_cabecera.save()
                linea_credito_proveedor_detalle = LineaCreditoProveedorDetalle(linea_credito_proveedor_id=linea_credito_proveedor_cabecera.id,
                                                                               monto_movimiento=compra_actual.total_compra,
                                                                               tipo_movimiento='FAC',
                                                                               numero_comprobante=compra_actual.numero_factura_compra,
                                                                               fecha_movimiento=compra_actual.fecha_factura_compra)
                linea_credito_proveedor_detalle.save()
            else:
                linea_credito_proveedor_cabecera = LineaCreditoProveedor(id=linea_credito_proveedor_actual.first().id,
                                                                         proveedor_id=compra_actual.numero_orden_compra.proveedor_orden_compra_id,
                                                                         linea_credito_proveedor=linea_credito_proveedor_actual.first().linea_credito_proveedor,
                                                                         fecha_linea_credito_proveedor=linea_credito_proveedor_actual.first().fecha_linea_credito_proveedor,
                                                                         monto_total_facturas_proveedor=linea_credito_proveedor_actual.first().monto_total_facturas_proveedor + compra_actual.total_compra,
                                                                         monto_total_pagos_proveedor=linea_credito_proveedor_actual.first().monto_total_pagos_proveedor,
                                                                         uso_linea_credito_proveedor=linea_credito_proveedor_actual.first().uso_linea_credito_proveedor + compra_actual.total_compra,
                                                                         estado_linea_credito_proveedor="DEL")
                                                                         # Asignar el valor de estado_linea_credito_proveedor evaluando una condicion
                                                                         # if linea_credito_proveedor_actual.uso_linea_credito_proveedor + compra_actual.total_compra > linea_credito_proveedor_actual.linea_credito_proveedor:
                                                                         #     estado_linea_credito_proveedor="SOB"
                                                                         # else:
                                                                         #     estado_linea_credito_proveedor="DEL")
                linea_credito_proveedor_cabecera.save()
                linea_credito_proveedor_detalle = LineaCreditoProveedorDetalle(linea_credito_proveedor_id=linea_credito_proveedor_actual.first().id,
                                                                               monto_movimiento=compra_actual.total_compra,
                                                                               tipo_movimiento='FAC',
                                                                               numero_comprobante=compra_actual.numero_factura_compra,
                                                                               fecha_movimiento=compra_actual.fecha_factura_compra)
                linea_credito_proveedor_detalle.save()

            super(CompraAdmin, self).save_model(request, obj, form, change)
            orden.save()
            factura_proveedor.save()
            linea_credito_proveedor_detalle.save()

        if getattr(obj, 'usuario_registro_compra', None) is None:
            # empleado = Empleado.objects.filter(usuario=request.user)
            obj.usuario_registro_compra = Empleado.objects.get(usuario_id=request.user)
        super(CompraAdmin, self).save_model(request, obj, form, change)

    def save_formset(self, request, form, formset, change):
        # si orden cambio entonces no hacer nada
        compra_actual = form.instance
        super(CompraAdmin, self).save_formset(request, form, formset, change)

        # Si la Compra se confirma se suman los Productos al Stock.
        if compra_actual.estado_compra.estado_compra == 'CON':
            for form in formset:
                detalle = form.instance
                # Validar que exista un registro de Stock para el Producto, si no existe entonces se debe crear el
                # registro cabecera en la tabla Stock y luego el detalle en Stock_Detalle
                # import pdb;
                # pdb.set_trace()
                # stock_actual = Stock.objects.get(producto_stock_id=detalle.producto_compra_id)
                stock_actual = Stock.objects.filter(producto_stock_id=detalle.producto_compra_id)
                if not stock_actual.exists():
                    stock = Stock(producto_stock_id=detalle.producto_compra_id,
                                  stock_minimo=0,
                                  cantidad_existente=detalle.cantidad_producto_compra)
                    stock.save()
                    stock_detalle = StockDetalle(stock_id=stock.id,
                                                 tipo_movimiento=TipoMovimientoStock.objects.get(tipo_movimiento_stock='CO'),
                                                 id_movimiento=compra_actual.numero_compra,
                                                 ubicacion_origen=Deposito.objects.get(deposito='PRO'),
                                                 ubicacion_destino=Deposito.objects.get(deposito='DCE'),
                                                 cantidad_entrante=detalle.cantidad_producto_compra,
                                                 cantidad_saliente=0,
                                                 fecha_hora_registro_stock=timezone.now())
                    stock_detalle.save()
                else:
                    stock = Stock(id=stock_actual.first().id,
                                  producto_stock_id=detalle.producto_compra_id,
                                  stock_minimo=stock_actual.first().stock_minimo,
                                  cantidad_existente=stock_actual.first().cantidad_existente + detalle.cantidad_producto_compra)
                    stock.save()
                    stock_detalle = StockDetalle(stock_id=stock_actual.first().id,
                                                 tipo_movimiento=TipoMovimientoStock.objects.get(tipo_movimiento_stock='CO'),
                                                 id_movimiento=compra_actual.numero_compra,
                                                 ubicacion_origen=Deposito.objects.get(deposito='PRO'),
                                                 ubicacion_destino=Deposito.objects.get(deposito='DCE'),
                                                 cantidad_entrante=detalle.cantidad_producto_compra,
                                                 cantidad_saliente=0,
                                                 fecha_hora_registro_stock=timezone.now())
                    stock_detalle.save()

    def get_readonly_fields(self, request, obj=None):
        if obj is not None and obj.estado_compra.estado_compra in ('CON', 'CAN'):
            return [i.name for i in self.model._meta.fields] + \
                   [i.name for i in self.model._meta.many_to_many]
        else:
            return super(CompraAdmin, self).get_readonly_fields(request, obj)

    def changeform_view(self, request, object_id=None, form_url='', extra_context=None):
        extra_context = extra_context or {}

        extra_context['show_button'] = True
        if object_id is not None:
            compra_actual = Compra.objects.get(pk=object_id)
            extra_context['show_button'] = compra_actual.estado_compra.estado_compra not in ('CON', 'CAN')

        return super(CompraAdmin, self).changeform_view(request, object_id, form_url, extra_context)


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