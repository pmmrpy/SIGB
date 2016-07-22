from django.contrib import admin

# from polymorphic.admin import PolymorphicParentModelAdmin, PolymorphicChildModelAdmin, PolymorphicChildModelFilter
from bar.models import CompraEstado, OrdenCompraEstado
from stock.models import Stock
from .forms import LineaCreditoProveedorForm, OrdenCompraForm, OrdenCompraDetalleForm, CompraForm
from .models import ProveedorTelefono, LineaCreditoProveedor, Proveedor, OrdenCompra, OrdenCompraDetalle, \
    ProductoProveedor, Compra, CompraDetalle, Empresa  # , ModelA, ModelB, ModelC  # , PagoProveedor

# Register your models here.


class ProveedorTelefonoInline(admin.TabularInline):
    model = ProveedorTelefono
    extra = 0
    min_num = 1
    verbose_name = 'Telefonos'
    verbose_name_plural = 'Telefonos'


class LineaCreditoProveedorInline(admin.TabularInline):
    model = LineaCreditoProveedor
    extra = 0
    form = LineaCreditoProveedorForm
    verbose_name = 'Linea de Credito del Proveedor'
    verbose_name_plural = 'Lineas de Credito del Proveedor'


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

    inlines = [ProveedorTelefonoInline, LineaCreditoProveedorInline]

    list_display = ('id', 'proveedor', 'persona_proveedor', 'ruc', 'digito_verificador', 'direccion', 'pais_proveedor',
                    'ciudad_proveedor', 'pagina_web', 'fecha_alta_proveedor')
    list_filter = ['id', 'proveedor', 'ruc', 'fecha_alta_proveedor']
    search_fields = ['id', 'proveedor', 'ruc', 'fecha_alta_proveedor']


# class PagoProveedorAdmin(admin.ModelAdmin):
#
#     class Media:
#         js = [
#             ''
#         ]
#
#     # readonly_fields = ('')
#
#     list_display = ['id', 'monto_pago_proveedor', 'fecha_pago_proveedor']
#     list_filter = ['id', 'monto_pago_proveedor', 'fecha_pago_proveedor']
#     search_fields = ['id', 'monto_pago_proveedor', 'fecha_pago_proveedor']


class ProductoProveedorAdmin(admin.ModelAdmin):
    list_display = ('id', 'proveedor', 'producto')
    list_filter = ['id', 'proveedor', 'producto']
    search_fields = ['id', 'proveedor', 'producto']


class EmpresaAdmin(admin.ModelAdmin):
    model = Empresa


# ======================================================================================================================
class OrdenCompraDetalleInline(admin.TabularInline):
    model = OrdenCompraDetalle
    extra = 0
    form = OrdenCompraDetalleForm
    raw_id_fields = ['producto_orden_compra']
    verbose_name = 'Orden de Compra - Detalle de Productos'
    verbose_name_plural = 'Orden de Compra - Detalle de Productos'


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
            'compras/js/orden_compra.js'
        ]

    # readonly_fields = ('numero_orden_compra', 'fecha_orden_compra', 'estado_orden_compra')

    fieldsets = [
        ('Numero Orden de Compra', {'fields': ['numero_orden_compra']}),
        ('Datos del Proveedor', {'fields': ['proveedor_orden_compra', 'forma_pago_orden_compra']}),
        ('Fechas', {'fields': ['fecha_orden_compra', 'fecha_entrega_orden_compra']}),
        # ('Fecha de Entrega del Pedido', {'fields': ['fecha_entrega']}),
        ('Otros datos de la Orden de Compra', {'fields': ['estado_orden_compra', 'total_orden_compra', 'prueba2']}),
    ]

    inlines = [OrdenCompraDetalleInline]

    # list_select_related = True
    list_display = ('numero_orden_compra', 'proveedor_orden_compra', 'fecha_orden_compra',
                    'fecha_entrega_orden_compra', 'forma_pago_orden_compra', 'estado_orden_compra',
                    'total_orden_compra')
    list_filter = ['numero_orden_compra', ('proveedor_orden_compra', admin.RelatedOnlyFieldListFilter),
                   'fecha_orden_compra', 'fecha_entrega_orden_compra', 'forma_pago_orden_compra', 'estado_orden_compra']
    search_fields = ['numero_orden_compra', 'proveedor_orden_compra', 'fecha_orden_compra',
                     'fecha_entrega_orden_compra', 'forma_pago_orden_compra', 'estado_orden_compra']

    def get_readonly_fields(self, request, obj=None):
        if obj:  # This is the case when obj is already created i.e. it's an edit
            return ['numero_orden_compra', 'fecha_orden_compra', 'estado_orden_compra', 'proveedor_orden_compra']
        # elif object.
        else:
            return ['numero_orden_compra', 'fecha_orden_compra', 'estado_orden_compra']


# ======================================================================================================================
class CompraDetalleInline(admin.TabularInline):
    model = CompraDetalle
    extra = 0
    # form = CompraDetalleForm
    raw_id_fields = ['producto_compra']
    verbose_name = 'Detalle de Productos de la Compra'
    verbose_name_plural = ''

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

    readonly_fields = ['numero_compra', 'fecha_compra', 'total_compra', 'estado_compra']

    fieldsets = [
        ('Compra ID', {'fields': ['numero_compra']}),
        ('Numero Orden de Compra', {'fields': ['numero_orden_compra']}),
        # ('Datos de la Orden de Compra', {'fields': ['orden_compra__proveedor_orden_compra',
        #                                             'orden_compra__forma_pago_orden_compra',
        #                                             ('orden_compra__fecha_orden_compra',
        #                                              'orden_compra__fecha_entrega_orden_compra')]}),
        ('Datos de la Factura', {'fields': ['numero_factura_compra', 'fecha_factura_compra']}),
        ('Datos de la Nota de Credito', {'fields': ['numero_nota_credito_compra']}),
        ('Datos de la Compra', {'fields': ['fecha_compra', 'estado_compra', 'total_compra']}),
    ]

    inlines = [CompraDetalleInline]

    # raw_id_fields = ("numero_orden_compra",)

    # list_display = ('compra_id', 'fecha_compra')
    list_display = ('numero_compra', 'numero_orden_compra', 'fecha_compra', 'numero_factura_compra',
                    'fecha_factura_compra', 'numero_nota_credito_compra', 'estado_compra', 'total_compra')
    list_filter = ['numero_compra', ('numero_orden_compra', admin.RelatedOnlyFieldListFilter), 'fecha_compra',
                   'numero_factura_compra', 'fecha_factura_compra', 'numero_nota_credito_compra', 'estado_compra',
                   'total_compra']
    search_fields = ['numero_compra', 'numero_orden_compra', 'fecha_compra', 'numero_factura_compra',
                     'fecha_factura_compra', 'numero_nota_credito_compra', 'estado_compra', 'total_compra']

    def save_model(self, request, obj, form, change):
        compra_actual = obj
        compra_anterior = None
        if obj.numero_compra is not None:
            compra_anterior = Compra.objects.get(pk=obj.numero_compra)
        else:
            super(CompraAdmin, self).save_model(request, obj, form, change)

        if "_continue" in request.POST and compra_actual.estado_compra.estado_compra == 'PEN':
            if compra_anterior is None \
                    or compra_anterior.numero_orden_compra_id != compra_actual.numero_orden_compra_id:
                CompraDetalle.objects.filter(numero_compra=compra_actual.numero_compra).delete()
                for detalle in OrdenCompraDetalle.objects.filter(numero_orden_compra_id=compra_actual.numero_orden_compra_id):
                    compra_detalle = CompraDetalle(numero_compra=compra_actual.numero_compra,
                                                   producto_compra_id=detalle.producto_orden_compra_id,
                                                   precio_producto_compra=detalle.precio_producto_orden_compra,
                                                   cantidad_producto_compra=detalle.cantidad_producto_orden_compra,
                                                   unidad_medida_compra=detalle.unidad_medida_orden_compra,
                                                   total_producto_compra=detalle.total_producto_orden_compra)
                    compra_detalle.save()
        elif "_cancel" in request.POST:
            compra_actual.estado_compra = CompraEstado.objects.get(estado_compra='CAN')
            super(CompraAdmin, self).save_model(request, obj, form, change)
        elif compra_actual.estado_compra.estado_compra == 'CON':
            orden = compra_actual.numero_orden_compra
            orden.estado_orden_compra = OrdenCompraEstado.objects.get(estado_orden_compra='ENT')
            super(CompraAdmin, self).save_model(request, obj, form, change)
            orden.save()

    def save_formset(self, request, form, formset, change):
        # si orden cambio entonces no hacer nada
        compra_actual = form.instance
        super(CompraAdmin, self).save_formset(request, form, formset, change)

        if compra_actual.estado_compra.estado_compra == 'CON':
            for form in formset:
                detalle = form.instance
                # stock = Stock(numero_orden_compra_id=compra_actual.numero_orden_compra_id,
                #              producto_compra_id=detalle.producto_orden_compra_id,
                #              entrada=detalle.cantidad_producto_compra, salida=0)
                # stock.save()

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


# class CompraDetalleAdmin(admin.ModelAdmin):
#     list_display = ('compra', 'producto', 'cantidad_producto', 'precio_compra_producto', 'total_compra_producto')
#     list_filter = ['compra', 'producto', 'cantidad_producto', 'precio_compra_producto']
#     search_fields = ['compra', 'producto', 'cantidad_producto', 'precio_compra_producto']


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
# admin.site.register(Empresa, EmpresaAdmin)
admin.site.register(ProductoProveedor, ProductoProveedorAdmin)
# admin.site.register(PagoProveedor, PagoProveedorAdmin)
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