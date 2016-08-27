from django.contrib import admin

# Register your models here.
from stock.forms import ProductoForm, ProductoCompuestoForm  # PrecioVentaProductoForm

from .models import Producto, ProductoCompuesto, ProductoCompuestoDetalle, Stock, StockDetalle, StockProducto, \
    StockDeposito, Devolucion, SolicitaTransferenciaStock, ConfirmaTransferenciaStock  # PrecioVentaProducto
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
            'stock/js/producto.js'
        ]

    readonly_fields = ['fecha_alta_producto', 'thumb']  # 'compuesto',

    fieldsets = [
        ('Datos del Producto', {'fields': ['producto', 'codigo_barra', 'marca', 'unidad_medida_compra', 'contenido',
                                           'imagen', 'thumb', 'fecha_alta_producto']}),  # 'compuesto'
        ('Contenido del Producto', {'fields': ['tipo_producto', 'categoria', 'subcategoria', 'perecedero']}),  # 'unidad_medida_contenido',
        ('Utilidad', {'fields': ['porcentaje_ganancia', 'precio_venta_sugerido']}),
    ]

    # PrecioProducto debe estar disponible como Inline solo para los Productos que tienen Tipo de Producto
    # "VE - Para la Venta", serian los registrados con este Tipo de Producto en la pantalla de Productos mas
    # los Productos Compuestos
    # inlines = [PrecioVentaProductoInline]

    # list_select_related = True
    list_display = ('id', 'producto', 'marca', 'fecha_alta_producto', 'unidad_medida_compra', 'contenido',
                    'tipo_producto', 'categoria', 'subcategoria', 'perecedero', 'porcentaje_ganancia', 'thumb')  # 'compuesto', 'unidad_medida_contenido',
    list_display_links = ['producto']
    list_filter = ['id', 'producto', 'marca', 'fecha_alta_producto', 'tipo_producto', 'categoria', 'subcategoria',
                   'perecedero']
    search_fields = ['id', 'producto', 'marca', 'fecha_alta_producto', 'tipo_producto__tipo_producto',
                     'categoria__categoria', 'subcategoria__subcategoria', 'perecedero']

    def get_queryset(self, request):
        queryset = Producto.objects.filter(compuesto=False)
        return queryset


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
            'stock/js/producto_compuesto.js'
        ]

    readonly_fields = ['compuesto', 'perecedero', 'tipo_producto', 'fecha_alta_producto', 'thumb']  # 'unidad_medida_contenido', 'contenido'

    fieldsets = [
        ('Datos del Producto Compuesto', {'fields': ['producto', 'compuesto', 'perecedero', 'tipo_producto',
                                                     'categoria', 'subcategoria', 'fecha_alta_producto', 'imagen',
                                                     'thumb']}),
        # ('Contenido del Producto', {'fields': ['unidad_medida_contenido', 'contenido']}),
        # ('Contenido del Producto', {'fields': ['perecedero', 'fecha_elaboracion', 'fecha_vencimiento']}),
        ('Elaboracion', {'fields': ['costo_elaboracion']}),
        ('Utilidad', {'fields': ['porcentaje_ganancia', 'precio_venta_sugerido']}),
    ]

    inlines = [ProductoCompuestoDetalleInline]

    list_display = ('id', 'producto', 'compuesto', 'perecedero', 'fecha_alta_producto', 'tipo_producto', 'categoria',
                    'subcategoria', 'porcentaje_ganancia', 'thumb')  # 'unidad_medida_contenido', 'contenido',
    list_display_links = ['producto']
    list_filter = ['id', 'producto', 'categoria', 'subcategoria', 'porcentaje_ganancia', 'fecha_alta_producto']
    search_fields = ['id', 'producto', 'categoria', 'subcategoria', 'porcentaje_ganancia', 'fecha_alta_producto']

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


class StockDetalleInline(admin.TabularInline):
    model = StockDetalle
    extra = 0
    readonly_fields = ['tipo_movimiento', 'id_movimiento', 'ubicacion_origen', 'ubicacion_destino', 'cantidad_entrante',
                       'cantidad_saliente', 'fecha_hora_registro_stock']
    # form =
    # raw_id_fields =
    # verbose_name = ''
    # verbose_name_plural = ''


class StockAdmin(admin.ModelAdmin):

    # form =

    class Media:
        js = [
            'stock/js/stock.js'
        ]

    readonly_fields = ['producto_stock', 'cantidad_existente']

    # raw_id_fields = ['producto_stock']

    fieldsets = [
        ('Producto/Ubicacion', {'fields': ['producto_stock']}),
        ('Cantidades', {'fields': ['stock_minimo', 'cantidad_existente']}),
    ]

    inlines = [StockDetalleInline]

    list_display = ('id', 'producto_stock', 'stock_minimo', 'cantidad_existente')
    list_display_links = ['producto_stock']
    list_filter = ['id', 'producto_stock__producto', 'stock_minimo', 'cantidad_existente']
    search_fields = ['id', 'producto_stock__producto', 'stock_minimo', 'cantidad_existente']


# ======================================================================================================================
class SolicitaTransferenciaStockAdmin(admin.ModelAdmin):

    # form =

    class Media:
        js = [
            'stock/js/solicita_transferencia_stock.js'
        ]

    readonly_fields = ['usuario_solicitante_transferencia', 'usuario_autorizante_transferencia',
                       'estado_transferencia', 'fecha_hora_registro_transferencia']  # 'cantidad_existente_stock',

    raw_id_fields = ['producto_transferencia']

    fieldsets = [
        ('Datos del Producto', {'fields': ['producto_transferencia', 'cantidad_existente_stock',
                                           'cantidad_producto_transferencia']}),
        ('Solicitante', {'fields': ['deposito_solicitante_transferencia', 'usuario_solicitante_transferencia']}),
        ('Proveedor', {'fields': ['deposito_proveedor_transferencia', 'usuario_autorizante_transferencia']}),
        ('Otros datos de la Transferencia', {'fields': ['estado_transferencia', 'fecha_hora_registro_transferencia']}),
    ]

    # inlines =

    list_display = ['producto_transferencia', 'cantidad_producto_transferencia', 'deposito_solicitante_transferencia',
                    'usuario_solicitante_transferencia', 'deposito_proveedor_transferencia',
                    'usuario_autorizante_transferencia', 'estado_transferencia', 'fecha_hora_registro_transferencia']
    list_filter = ['producto_transferencia', 'deposito_solicitante_transferencia', 'usuario_solicitante_transferencia',
                   'deposito_proveedor_transferencia', 'usuario_autorizante_transferencia', 'estado_transferencia',
                   'fecha_hora_registro_transferencia']
    search_fields = ['producto_transferencia', 'cantidad_producto_transferencia', 'deposito_solicitante_transferencia',
                     'usuario_solicitante_transferencia', 'deposito_proveedor_transferencia',
                     'usuario_autorizante_transferencia', 'estado_transferencia', 'fecha_hora_registro_transferencia']

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

    readonly_fields = ['producto_transferencia', 'cantidad_existente_stock', 'deposito_solicitante_transferencia',
                       'usuario_solicitante_transferencia', 'deposito_proveedor_transferencia',
                       'usuario_autorizante_transferencia', 'estado_transferencia', 'fecha_hora_registro_transferencia']

    # raw_id_fields = []

    fieldsets = [
        ('Datos del Producto', {'fields': ['producto_transferencia', 'cantidad_existente_stock',
                                           'cantidad_producto_transferencia']}),
        ('Solicitante', {'fields': ['deposito_solicitante_transferencia', 'usuario_solicitante_transferencia']}),
        ('Proveedor', {'fields': ['deposito_proveedor_transferencia', 'usuario_autorizante_transferencia']}),
        ('Otros datos de la Transferencia', {'fields': ['estado_transferencia', 'fecha_hora_registro_transferencia']}),
    ]

    # inlines =

    list_display = ['producto_transferencia', 'cantidad_producto_transferencia', 'deposito_solicitante_transferencia',
                    'usuario_solicitante_transferencia', 'deposito_proveedor_transferencia',
                    'usuario_autorizante_transferencia', 'estado_transferencia', 'fecha_hora_registro_transferencia']
    list_filter = ['producto_transferencia', 'deposito_solicitante_transferencia', 'usuario_solicitante_transferencia',
                   'deposito_proveedor_transferencia', 'usuario_autorizante_transferencia', 'estado_transferencia',
                   'fecha_hora_registro_transferencia']
    search_fields = ['producto_transferencia', 'cantidad_producto_transferencia', 'deposito_solicitante_transferencia',
                     'usuario_solicitante_transferencia', 'deposito_proveedor_transferencia',
                     'usuario_autorizante_transferencia', 'estado_transferencia', 'fecha_hora_registro_transferencia']
# ======================================================================================================================

admin.site.register(Producto, ProductoAdmin)
# admin.site.register(PrecioVentaProducto, PrecioVentaProductoAdmin)
admin.site.register(ProductoCompuesto, ProductoCompuestoAdmin)
admin.site.register(Stock, StockAdmin)
admin.site.register(StockProducto)
admin.site.register(StockDeposito)
admin.site.register(SolicitaTransferenciaStock, SolicitaTransferenciaStockAdmin)
admin.site.register(ConfirmaTransferenciaStock, ConfirmaTransferenciaStockAdmin)
admin.site.register(Devolucion)