from django.contrib import admin

# Register your models here.
from stock.forms import ProductoForm, ProductoCompuestoForm, SolicitaTransferenciaStockForm  # PrecioVentaProductoForm

from .models import *
from personal.models import Empleado


# class PrecioVentaProductoInline(admin.TabularInline):
#     model = PrecioVentaProducto
#     extra = 0
#     form = PrecioVentaProductoForm
#     readonly_fields = ['fecha_precio_venta_producto']


class ProductoAdmin(admin.ModelAdmin):

    form = ProductoForm

    class Media:
        js = [
            'stock/js/producto.js',
            # 'stock/js/change_form.js'
        ]

    readonly_fields = ['fecha_alta_producto', 'thumb']  # 'compuesto',

    fieldsets = [
        ('Datos del Producto', {'fields': ['producto', 'codigo_barra', 'marca', 'imagen', 'thumb',
                                           'fecha_alta_producto']}),  # 'compuesto'
        ('Contenido del Producto', {'fields': ['tipo_producto', 'categoria', 'subcategoria', 'perecedero',
                                               'unidad_medida_contenido', 'contenido']}),
        ('Datos para la Compra', {'fields': ['unidad_medida_compra', 'precio_compra_sugerido', 'precio_compra']}),
        ('Utilidad', {'fields': ['porcentaje_ganancia', 'precio_venta_sugerido', 'precio_venta']}),
        ('Stock', {'fields': ['stock_minimo']}),
    ]

    # PrecioProducto debe estar disponible como Inline solo para los Productos que tienen Tipo de Producto
    # "VE - Para la Venta", serian los registrados con este Tipo de Producto en la pantalla de Productos mas
    # los Productos Compuestos
    # inlines = [PrecioVentaProductoInline]

    # list_select_related = True
    list_display = ('id', 'producto', 'marca', 'fecha_alta_producto', 'tipo_producto', 'categoria', 'subcategoria',
                    'perecedero', 'unidad_medida_contenido', 'contenido', 'unidad_medida_compra',
                    'precio_compra', 'porcentaje_ganancia', 'precio_venta', 'thumb')  # 'compuesto'
    list_display_links = ['producto']
    list_filter = ['id', 'producto', 'marca', 'fecha_alta_producto', 'tipo_producto', 'categoria', 'subcategoria',
                   'perecedero', 'precio_compra', 'porcentaje_ganancia', 'precio_venta']
    search_fields = ['id', 'producto', 'marca', 'fecha_alta_producto', 'tipo_producto', 'categoria__categoria',
                     'subcategoria__subcategoria', 'perecedero', 'precio_compra', 'porcentaje_ganancia', 'precio_venta']

    def get_queryset(self, request):
        queryset = Producto.objects.filter(compuesto=False)
        return queryset

    # def get_readonly_fields(self, request, obj=None):
    #     if obj and obj.tipo_producto == 'IN':
    #         return ['fecha_alta_producto', 'thumb', 'porcentaje_ganancia', 'precio_venta_sugerido']
    #     else:
    #         return ['fecha_alta_producto', 'thumb']


class ProductoCompuestoDetalleInline(admin.TabularInline):
    model = ProductoCompuestoDetalle
    extra = 0
#    form = RecetaDetalleForm
    raw_id_fields = ['producto']
    verbose_name = 'Detalle de Productos del Producto Compuesto'
    verbose_name_plural = 'Detalles de Productos de los Productos Compuestos'
    fk_name = 'producto_compuesto'


class ProductoCompuestoAdmin(admin.ModelAdmin):

    form = ProductoCompuestoForm

    class Media:
        js = [
            # 'stock/js/producto_compuesto.js',
            'stock/js/change_form.js'
        ]

    readonly_fields = ['compuesto', 'perecedero', 'tipo_producto', 'fecha_alta_producto', 'thumb']  # 'unidad_medida_contenido', 'contenido'

    fieldsets = [
        ('Datos del Producto Compuesto', {'fields': ['producto', 'compuesto', 'perecedero', 'tipo_producto',
                                                     'categoria', 'subcategoria', 'fecha_alta_producto', 'imagen',
                                                     'thumb']}),
        # ('Contenido del Producto', {'fields': ['unidad_medida_contenido', 'contenido']}),
        # ('Contenido del Producto', {'fields': ['perecedero', 'fecha_elaboracion', 'fecha_vencimiento']}),
        ('Elaboracion', {'fields': ['tiempo_elaboracion', 'costo_elaboracion']}),
        ('Utilidad', {'fields': ['porcentaje_ganancia', 'precio_venta_sugerido', 'precio_venta']}),
    ]

    inlines = [ProductoCompuestoDetalleInline]

    list_display = ('id', 'producto', 'compuesto', 'perecedero', 'fecha_alta_producto', 'tipo_producto', 'categoria',
                    'subcategoria', 'costo_elaboracion', 'porcentaje_ganancia', 'precio_venta', 'thumb')
    list_display_links = ['producto']
    list_filter = ['id', 'producto', 'fecha_alta_producto', 'categoria', 'subcategoria', 'costo_elaboracion',
                   'porcentaje_ganancia', 'precio_venta']
    search_fields = ['id', 'producto', 'fecha_alta_producto', 'categoria', 'subcategoria', 'costo_elaboracion',
                     'porcentaje_ganancia', 'precio_venta']

    # def save_model(self, request, obj, form, change):
    #     if not change:
    #         producto = Producto()
    #     else:
    #         producto = Producto.objects.get(obj.pk)
    #     producto.imagen = obj.imagen
    #     producto.producto = obj.producto
    #     producto.tipo_producto = obj.tipo_producto
    #     producto.categoria = obj.categoria
    #     producto.subcategoria = obj.subcategoria
    #     producto.save()
    #
    # def save_formset(self, request, form, formset, change):
    #     obj = form.instance
    #     for f in formset:
    #         detalle = ProductoCompuestoDetalle()
    #         detalle.cantidad_producto = f.cleaned_data['cantidad_producto']
    #         detalle.producto_compuesto_id = f.cleaned_data['cantidad_producto']
    #         detalle.save()
    #
    #     return super(ProductoCompuestoAdmin, self).save_formset(request, form, formset, change)

    def get_queryset(self, request):
        queryset = ProductoCompuesto.objects.filter(compuesto=True)
        return queryset


class ProductoVentaAdmin(admin.ModelAdmin):

    # form = ProductoCompuestoForm

    # class Media:
    #     js = [
    #         # 'stock/js/producto_compuesto.js',
    #         'stock/js/change_form.js'
    #     ]

    # readonly_fields = ['fecha_alta_producto', 'thumb']

    fieldsets = [
        ('Datos del Producto', {'fields': ['producto', 'codigo_barra', 'marca', 'imagen', 'thumb',
                                           'fecha_alta_producto']}),
        ('Contenido del Producto', {'fields': ['tipo_producto', 'categoria', 'subcategoria', 'compuesto', 'perecedero',
                                               'unidad_medida_contenido', 'contenido']}),
        ('Datos para la Compra', {'fields': ['unidad_medida_compra', 'precio_compra']}),
        ('Utilidad', {'fields': ['precio_venta']}),
        ('Elaboracion', {'fields': ['tiempo_elaboracion', 'costo_elaboracion']}),
    ]

    # inlines = [ProductoCompuestoDetalleInline]

    actions = None
    list_display = ('id', 'producto', 'marca', 'categoria', 'subcategoria', 'tiempo_elaboracion',
                    'unidad_medida_contenido', 'contenido', 'precio_venta', 'thumb')
    list_display_links = ['producto']
    list_filter = ['producto', ('categoria', admin.RelatedOnlyFieldListFilter), ('subcategoria', admin.RelatedOnlyFieldListFilter)]
    search_fields = ['producto', 'marca', 'categoria', 'subcategoria']

    def get_queryset(self, request):
        queryset = Producto.objects.filter(tipo_producto='VE')
        return queryset

    def get_readonly_fields(self, request, obj=None):
        if obj is not None:
            return [i.name for i in self.model._meta.fields] + \
                   [i.name for i in self.model._meta.many_to_many] + ['thumb']
        else:
            return super(ProductoVentaAdmin, self).get_readonly_fields(request, obj)

    def changeform_view(self, request, object_id=None, form_url='', extra_context=None):
        extra_context = extra_context or {}

        extra_context['show_button'] = False
        # if object_id is not None:
        #     factura_actual = FacturaProveedor.objects.get(pk=object_id)
        #     print 'factura_actual: %s' % factura_actual
        #     extra_context['show_button'] = factura_actual.estado_factura_compra.estado_factura_proveedor not in ('PAG', 'CAN')

        return super(ProductoVentaAdmin, self).changeform_view(request, object_id, form_url, extra_context)

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    # def has_change_permission(self, request, obj=None):
    #     return False


@admin.register(InventarioProducto)
class InventarioAdmin(admin.ModelAdmin):
    actions = None
    list_display = ['producto', 'stock']
    list_display_links = None
    list_filter = ['producto']
    search_fields = ['producto']

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


# class StockDetalleInline(admin.TabularInline):
#     model = StockDetalle
#     extra = 0
#     readonly_fields = ['tipo_movimiento', 'id_movimiento', 'ubicacion_origen', 'ubicacion_destino', 'cantidad_entrante',
#                        'cantidad_saliente', 'fecha_hora_registro_stock']
#     can_delete = False
#     # form =
#     # raw_id_fields =
#     # verbose_name = ''
#     # verbose_name_plural = ''
#
#     def has_add_permission(self, request):
#         return False


class MovimientoStockAdmin(admin.ModelAdmin):

    # form =

    class Media:
        js = [
            'stock/js/stock.js'
        ]

    readonly_fields = ['id', 'fecha_hora_registro_stock']

    # raw_id_fields = ['producto_stock']

    fieldsets = [
        ('Movimiento', {'fields': ['id', 'fecha_hora_registro_stock']}),
        ('Producto', {'fields': ['producto_stock']}),
        ('Tipo Movimiento', {'fields': ['tipo_movimiento', 'id_movimiento']}),
        ('Ubicaciones', {'fields': ['ubicacion_origen', 'ubicacion_destino']}),
        ('Cantidades', {'fields': ['cantidad_entrante', 'cantidad_saliente']}),
    ]

    # inlines = [StockDetalleInline]

    list_display = ('id', 'producto_stock', 'tipo_movimiento', 'id_movimiento', 'ubicacion_origen', 'ubicacion_destino', 'cantidad_entrante', 'cantidad_saliente', 'fecha_hora_registro_stock')
    list_display_links = ['producto_stock']
    list_filter = ['id', 'producto_stock__producto', 'tipo_movimiento', 'ubicacion_origen', 'ubicacion_destino']
    search_fields = ['id', 'producto_stock__producto', 'tipo_movimiento', 'ubicacion_origen', 'ubicacion_destino']


# ======================================================================================================================
class SolicitaTransferenciaStockAdmin(admin.ModelAdmin):

    form = SolicitaTransferenciaStockForm

    class Media:
        js = [
            'stock/js/solicita_transferencia_stock.js'
        ]

    readonly_fields = ['usuario_solicitante_transferencia', 'usuario_autorizante_transferencia',
                       'estado_transferencia', 'fecha_hora_registro_transferencia',
                       'fecha_hora_autorizacion_transferencia']  # 'cantidad_existente_stock',

    raw_id_fields = ['producto_transferencia']

    fieldsets = [
        ('Datos de la Transferencia', {'fields': ['producto_transferencia', 'deposito_origen_transferencia',
                                                  'cantidad_existente_stock', 'cantidad_producto_transferencia']}),
        ('Solicitante', {'fields': ['deposito_destino_transferencia', 'usuario_solicitante_transferencia']}),
        ('Otros datos de la Transferencia', {'fields': ['estado_transferencia', 'fecha_hora_registro_transferencia',
                                                        'usuario_autorizante_transferencia',
                                                        'fecha_hora_autorizacion_transferencia']}),
    ]

    # inlines =

    list_display = ['producto_transferencia', 'deposito_origen_transferencia', 'cantidad_producto_transferencia',
                    'deposito_destino_transferencia', 'usuario_solicitante_transferencia', 'estado_transferencia',
                    'fecha_hora_registro_transferencia', 'usuario_autorizante_transferencia',
                    'fecha_hora_autorizacion_transferencia']
    list_filter = ['producto_transferencia', 'deposito_origen_transferencia', 'deposito_destino_transferencia',
                   'usuario_solicitante_transferencia', 'estado_transferencia', 'fecha_hora_registro_transferencia',
                   'usuario_autorizante_transferencia', 'fecha_hora_autorizacion_transferencia']
    search_fields = ['producto_transferencia__producto', 'deposito_origen_transferencia__descripcion', 'deposito_destino_transferencia__descripcion',
                   'usuario_solicitante_transferencia__usuario__username', 'estado_transferencia__estado_transferencia_stock', 'fecha_hora_registro_transferencia',
                   'usuario_autorizante_transferencia__usuario__username', 'fecha_hora_autorizacion_transferencia']

    def save_model(self, request, obj, form, change):
        if getattr(obj, 'usuario_solicitante_transferencia', None) is None:
            # empleado = Empleado.objects.filter(usuario=request.user)
            obj.usuario_solicitante_transferencia = Empleado.objects.get(usuario_id=request.user)
        super(SolicitaTransferenciaStockAdmin, self).save_model(request, obj, form, change)


class ConfirmaTransferenciaStockAdmin(admin.ModelAdmin):

    # form =

    class Media:
        js = [
            'stock/js/confirma_transferencia_stock.js'
        ]

    readonly_fields = ['producto_transferencia', 'cantidad_existente_stock', 'deposito_destino_transferencia',
                       'usuario_solicitante_transferencia', 'deposito_origen_transferencia',
                       'usuario_autorizante_transferencia', 'estado_transferencia', 'fecha_hora_registro_transferencia']

    # raw_id_fields = []

    fieldsets = [
        ('Datos del Producto', {'fields': ['producto_transferencia', 'cantidad_existente_stock',
                                           'cantidad_producto_transferencia']}),
        ('Solicitante', {'fields': ['deposito_destino_transferencia', 'usuario_solicitante_transferencia']}),
        ('Proveedor', {'fields': ['deposito_origen_transferencia', 'usuario_autorizante_transferencia']}),
        ('Otros datos de la Transferencia', {'fields': ['estado_transferencia', 'fecha_hora_registro_transferencia']}),
    ]

    # inlines =

    list_display = ['producto_transferencia', 'cantidad_producto_transferencia', 'deposito_destino_transferencia',
                    'usuario_solicitante_transferencia', 'deposito_origen_transferencia',
                    'usuario_autorizante_transferencia', 'estado_transferencia', 'fecha_hora_registro_transferencia']
    list_filter = ['producto_transferencia', 'deposito_destino_transferencia', 'usuario_solicitante_transferencia',
                   'deposito_origen_transferencia', 'usuario_autorizante_transferencia', 'estado_transferencia',
                   'fecha_hora_registro_transferencia']
    search_fields = ['producto_transferencia', 'cantidad_producto_transferencia', 'deposito_destino_transferencia',
                     'usuario_solicitante_transferencia', 'deposito_origen_transferencia',
                     'usuario_autorizante_transferencia', 'estado_transferencia', 'fecha_hora_registro_transferencia']

    def save_model(self, request, obj, form, change):
        if getattr(obj, 'usuario_autorizante_transferencia', None) is None:
            # empleado = Empleado.objects.filter(usuario=request.user)
            obj.usuario_autorizante_transferencia = Empleado.objects.get(usuario_id=request.user)
        super(ConfirmaTransferenciaStockAdmin, self).save_model(request, obj, form, change)
# ======================================================================================================================

admin.site.register(Producto, ProductoAdmin)
# admin.site.register(PrecioVentaProducto, PrecioVentaProductoAdmin)
admin.site.register(ProductoCompuesto, ProductoCompuestoAdmin)
admin.site.register(ProductoVenta, ProductoVentaAdmin)
admin.site.register(MovimientoStock, MovimientoStockAdmin)
# admin.site.register(StockProducto)
# admin.site.register(StockDeposito)
admin.site.register(SolicitaTransferenciaStock, SolicitaTransferenciaStockAdmin)
admin.site.register(ConfirmaTransferenciaStock, ConfirmaTransferenciaStockAdmin)
# admin.site.register(Devolucion)