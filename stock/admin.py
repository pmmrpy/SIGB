from django.contrib import admin

# Register your models here.
from django.forms.models import BaseInlineFormSet
from django.utils.html import format_html
from stock.forms import ProductoForm, ProductoCompuestoForm, ProductoCompuestoDetalleInlineForm, \
    InsumoForm, TransferenciaStockForm, TransferenciaStockDetalleInlineForm, \
    TransferenciaStockDetalleFormSet  # PrecioVentaProductoForm

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
        ]

    readonly_fields = ['fecha_alta_producto', 'thumb']  # 'compuesto',

    raw_id_fields = ['insumo']

    fieldsets = [
        ('Datos del Producto', {'fields': ['producto', 'codigo_barra', 'marca', 'imagen', 'thumb',
                                           'fecha_alta_producto']}),  # 'compuesto'
        ('Contenido del Producto', {'fields': ['tipo_producto', 'insumo', 'categoria', 'subcategoria', 'perecedero',
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
    list_display = ('id', 'producto', 'marca', 'fecha_alta_producto', 'tipo_producto', 'insumo', 'categoria', 'subcategoria',
                    'perecedero', 'unidad_medida_contenido', 'contenido', 'unidad_medida_compra',
                    'precio_compra', 'porcentaje_ganancia', 'precio_venta', 'cantidad_existente_producto', 'thumb')  # 'compuesto'
    list_display_links = ['producto']
    list_filter = ['id', 'producto', 'marca', 'fecha_alta_producto', 'tipo_producto', 'categoria', 'subcategoria',
                   'perecedero', 'precio_compra', 'porcentaje_ganancia', 'precio_venta']
    search_fields = ['id', 'producto', 'marca', 'fecha_alta_producto', 'tipo_producto', 'categoria__categoria',
                     'subcategoria__subcategoria', 'perecedero', 'precio_compra', 'porcentaje_ganancia', 'precio_venta']

    def get_queryset(self, request):
        queryset = Producto.objects.filter(compuesto=False)
        return queryset

    def has_delete_permission(self, request, obj=None):
        return False

    # def get_readonly_fields(self, request, obj=None):
    #     if obj and obj.tipo_producto == 'IN':
    #         return ['fecha_alta_producto', 'thumb', 'porcentaje_ganancia', 'precio_venta_sugerido']
    #     else:
    #         return ['fecha_alta_producto', 'thumb']


class ProductoCompuestoDetalleInline(admin.TabularInline):
    model = ProductoCompuestoDetalle
    extra = 0
    form = ProductoCompuestoDetalleInlineForm
    raw_id_fields = ['insumo']
    # verbose_name = 'Detalle de Insumos del Producto Compuesto'
    # verbose_name_plural = 'Detalles de Productos Componentes'
    fk_name = 'producto_compuesto'


class ProductoCompuestoAdmin(admin.ModelAdmin):

    form = ProductoCompuestoForm

    class Media:
        js = [
            'stock/js/producto_compuesto.js',
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

    def get_form(self, request, obj=None, **kwargs):
        form = super(ProductoCompuestoAdmin, self).get_form(request, obj=obj, **kwargs)

        # if obj is None:
        #     # usuario = Empleado.objects.get(usuario=request.user)
        #     # form.base_fields['cajero'].initial = usuario
        #     # form.base_fields['horario'].initial = usuario.horario
        #     form.base_fields['mozo_pedido'].widget.attrs['readonly'] = True
        #     form.base_fields['jornada'].widget.attrs['readonly'] = True
        #     form.base_fields['jornada'].widget.attrs['style'] = 'width: 300px;'
        form.request = request
        return form

    def get_queryset(self, request):
        queryset = ProductoCompuesto.objects.filter(compuesto=True)
        return queryset

    def has_delete_permission(self, request, obj=None):
        return False


# class MyInlineFormSet(BaseInlineFormSet):
#
#     @property
#     def deleted_forms(self):
#         deleted_forms = super(MyInlineFormSet, self).deleted_forms
#
#         for i, form in enumerate(deleted_forms):
#             # Use form.instance to access object instance if needed
#             if some_criteria_to_prevent_deletion:
#                 deleted_forms.pop(i)
#
#         return deleted_forms


class ProductoInsumoInlineAdmin(admin.TabularInline):
    model = Producto
    extra = 0
    can_delete = False
    fields = ['id', 'producto', 'codigo_barra', 'marca', 'unidad_medida_contenido', 'contenido', 'unidad_medida_compra', 'precio_compra', 'fecha_alta_producto']
    readonly_fields = ['id', 'fecha_alta_producto']
    # form = ProductoCompuestoDetalleInlineForm
    # raw_id_fields = ['producto']
    verbose_name = 'Producto'
    verbose_name_plural = 'Productos'
    # fk_name = 'producto_compuesto'

    def get_readonly_fields(self, request, obj=None):
        if obj is not None:  # and obj.estado_factura_compra in ('PAG', 'CAN'):
            return [i.name for i in self.model._meta.fields]
        else:
            return super(ProductoInsumoInlineAdmin, self).get_readonly_fields(request, obj)

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


class InsumoAdmin(admin.ModelAdmin):
    form = InsumoForm

    readonly_fields = ['fecha_alta_insumo', 'fecha_modificacion_insumo']

    inlines = [ProductoInsumoInlineAdmin]

    list_display = ['insumo', 'unidad_medida', 'get_costo_promedio_por_unidad']
    list_filter = ['insumo', 'unidad_medida']
    search_fields = ['insumo', 'unidad_medida__descripcion']

    def get_form(self, request, obj=None, **kwargs):
        form = super(InsumoAdmin, self).get_form(request, obj=obj, **kwargs)

        # import pdb
        # pdb.set_trace()

        # insumo = obj

        # if obj is not None:
        # #     # usuario = Empleado.objects.get(usuario=request.user)
        # #     # form.base_fields['cajero'].initial = usuario
        # #     # form.base_fields['horario'].initial = usuario.horario
        # #     form.base_fields['mozo_pedido'].widget.attrs['readonly'] = True
        # #     form.base_fields['jornada'].widget.attrs['readonly'] = True
        # #     form.base_fields['jornada'].widget.attrs['style'] = 'width: 300px;'
        #     form.base_fields['costo_promedio'].initial = insumo.get_costo_promedio_por_unidad()
        # form.base_fields['costo_promedio'].widget.attrs['readonly'] = True
        form.request = request
        return form

    def has_delete_permission(self, request, obj=None):
        return False


class ProductoVentaAdmin(admin.ModelAdmin):

    # form = ProductoCompuestoForm

    # class Media:
    #     js = [
    #         # 'stock/js/producto_compuesto.js',
    #     ]

    # readonly_fields = ['fecha_alta_producto', 'thumb']

    fieldsets = [
        ('Datos del Producto', {'fields': ['producto', 'codigo_barra', 'marca', 'imagen', 'thumb',
                                           'fecha_alta_producto', 'fecha_modificacion_producto']}),
        ('Contenido del Producto', {'fields': ['tipo_producto', 'categoria', 'subcategoria', 'compuesto', 'perecedero',
                                               'unidad_medida_contenido', 'contenido']}),
        ('Datos para la Compra', {'fields': ['unidad_medida_compra', 'precio_compra']}),
        ('Utilidad', {'fields': ['precio_venta']}),
        ('Elaboracion', {'fields': ['tiempo_elaboracion', 'costo_elaboracion']}),
    ]

    # inlines = [ProductoCompuestoDetalleInline]

    actions = None
    list_display = ('id', 'producto', 'marca', 'categoria', 'subcategoria', 'tiempo_elaboracion',
                    'unidad_medida_contenido', 'contenido', 'precio_venta', 'cantidad_existente_producto', 'thumb')
    list_display_links = ['producto']
    list_filter = ['producto', ('categoria', admin.RelatedOnlyFieldListFilter), ('subcategoria', admin.RelatedOnlyFieldListFilter)]
    search_fields = ['producto', 'marca', 'categoria__categoria', 'subcategoria__subcategoria']

    def get_queryset(self, request):
        queryset = Producto.objects.filter(tipo_producto='VE', id__in=InventarioDeposito.objects.filter(cant_existente__gt=0))
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


class ProductoExistenteAdmin(admin.ModelAdmin):

    # form = ProductoCompuestoForm

    # class Media:
    #     js = [
    #         # 'stock/js/producto_compuesto.js',
    #     ]

    # readonly_fields = ['fecha_alta_producto', 'thumb']

    fieldsets = [
        ('Datos del Producto', {'fields': ['producto', 'codigo_barra', 'marca', 'imagen', 'thumb',
                                           'fecha_alta_producto', 'fecha_modificacion_producto']}),
        ('Contenido del Producto', {'fields': ['tipo_producto', 'categoria', 'subcategoria', 'compuesto', 'perecedero',
                                               'unidad_medida_contenido', 'contenido']}),
        ('Datos para la Compra', {'fields': ['unidad_medida_compra', 'precio_compra']}),
        ('Utilidad', {'fields': ['precio_venta']}),
        ('Elaboracion', {'fields': ['tiempo_elaboracion', 'costo_elaboracion']}),
    ]

    # inlines = [ProductoCompuestoDetalleInline]

    actions = None
    list_display = ('id', 'producto', 'marca', 'categoria', 'subcategoria', 'tiempo_elaboracion',
                    'unidad_medida_contenido', 'contenido', 'precio_venta', 'cantidad_existente_producto', 'thumb')
    list_display_links = ['producto']
    list_filter = ['producto', ('categoria', admin.RelatedOnlyFieldListFilter), ('subcategoria', admin.RelatedOnlyFieldListFilter)]
    search_fields = ['producto', 'marca', 'categoria__categoria', 'subcategoria__subcategoria']

    def get_queryset(self, request):
        queryset = Producto.objects.filter(id__in=InventarioDeposito.objects.filter(cant_existente__gt=0))
        return queryset

    def get_readonly_fields(self, request, obj=None):
        if obj is not None:
            return [i.name for i in self.model._meta.fields] + \
                   [i.name for i in self.model._meta.many_to_many] + ['thumb']
        else:
            return super(ProductoExistenteAdmin, self).get_readonly_fields(request, obj)

    def changeform_view(self, request, object_id=None, form_url='', extra_context=None):
        extra_context = extra_context or {}

        extra_context['show_button'] = False
        # if object_id is not None:
        #     factura_actual = FacturaProveedor.objects.get(pk=object_id)
        #     print 'factura_actual: %s' % factura_actual
        #     extra_context['show_button'] = factura_actual.estado_factura_compra.estado_factura_proveedor not in ('PAG', 'CAN')

        return super(ProductoExistenteAdmin, self).changeform_view(request, object_id, form_url, extra_context)

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    # def has_change_permission(self, request, obj=None):
    #     return False


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

    list_display = ('id', 'producto_stock', 'tipo_movimiento', 'id_movimiento', 'ubicacion_origen', 'ubicacion_destino',
                    'cantidad_entrante', 'cantidad_saliente', 'fecha_hora_registro_stock')
    list_display_links = ['producto_stock']
    list_filter = ['id', 'producto_stock__producto', 'tipo_movimiento', 'id_movimiento', 'ubicacion_origen', 'ubicacion_destino']
    search_fields = ['id', 'producto_stock__producto', 'tipo_movimiento', 'id_movimiento', 'ubicacion_origen__descripcion', 'ubicacion_destino__descripcion']

    def get_readonly_fields(self, request, obj=None):
        if obj is not None:
            return [i.name for i in self.model._meta.fields] + \
                   [i.name for i in self.model._meta.many_to_many] + ['thumb']
        else:
            return super(MovimientoStockAdmin, self).get_readonly_fields(request, obj)

    def changeform_view(self, request, object_id=None, form_url='', extra_context=None):
        extra_context = extra_context or {}

        extra_context['show_button'] = False
        # if object_id is not None:
        #     factura_actual = FacturaProveedor.objects.get(pk=object_id)
        #     print 'factura_actual: %s' % factura_actual
        #     extra_context['show_button'] = factura_actual.estado_factura_compra.estado_factura_proveedor not in ('PAG', 'CAN')

        return super(MovimientoStockAdmin, self).changeform_view(request, object_id, form_url, extra_context)

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(InventarioProducto)
class InventarioProductoAdmin(admin.ModelAdmin):
    actions = None
    ordering = ['producto']
    list_display = ['id', 'producto', 'total_compras', 'total_ventas', 'cantidad_existente']
    list_display_links = None
    list_filter = ['id', 'producto']
    search_fields = ['id', 'producto']

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(InventarioDeposito)
class InventarioDepositoAdmin(admin.ModelAdmin):
    actions = None
    ordering = ['producto']
    list_display = ['id', 'producto', 'cant_exist_dce', 'cant_exist_dbp', 'cant_exist_dba', 'cant_exist_dco',
                    'cant_exist_dbi', 'cant_existente']
    list_display_links = None
    list_filter = ['id', 'producto']
    search_fields = ['id', 'producto']

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


class StockAjusteAdmin(admin.ModelAdmin):
    # form =

    list_display = []
    list_filter = []
    search_fields = []


# ======================================================================================================================
class TransferenciaStockDetalleInline(admin.TabularInline):
    model = TransferenciaStockDetalle
    extra = 0
    min_num = 1
    # can_delete = False

    class Media:
        js = [
            'stock/js/transferencia_stock.js'
        ]

    fields = ['producto_transferencia', 'unidad_medida',
              ('cant_exist_dce', 'cant_exist_dbp', 'cant_exist_dba', 'cant_exist_dco', 'cant_exist_dbi', 'cant_total_existente'),
              'cantidad_producto_transferencia']

    # readonly_fields = ['id', 'fecha_alta_producto']
    form = TransferenciaStockDetalleInlineForm
    formset = TransferenciaStockDetalleFormSet
    raw_id_fields = ['producto_transferencia']
    verbose_name = 'Detalle de Producto a Transferir'
    verbose_name_plural = 'Detalles de Productos a Transferir'
    # fk_name = 'producto_compuesto'

    def get_readonly_fields(self, request, obj=None):
        if obj is not None and obj.estado_transferencia.estado_transferencia_stock == 'PEN':
            return self.readonly_fields
        elif obj is not None and obj.estado_transferencia.estado_transferencia_stock in ('PRO', 'CAN'):
            return [i.name for i in self.model._meta.fields] + \
                   [i.name for i in self.model._meta.many_to_many]
        elif obj is None:
            return super(TransferenciaStockDetalleInline, self).get_readonly_fields(request, obj)

    # def has_add_permission(self, request):
    #
    #     # import pdb
    #     # pdb.set_trace()
    #
    #     # Deshabilitar el link para agregar registros en el Inline solo para la pantalla de Confirmaciones de Transferencias
    #     return False

    # def has_delete_permission(self, request, obj=None):
    #     return False

    def has_add_permission(self, request):
        object_id = request.path.split("/")[-2]
        if object_id != "add":
            transferencia_actual = TransferenciaStock.objects.get(pk=object_id)
            return transferencia_actual.estado_transferencia.estado_transferencia_stock not in ('PRO', 'CAN')
        else:
            return super(TransferenciaStockDetalleInline, self).has_add_permission(request)

    def has_delete_permission(self, request, obj=None):
        if obj is not None and obj.estado_transferencia.estado_transferencia_stock in ('PRO', 'CAN'):
            return False
        return super(TransferenciaStockDetalleInline, self).has_delete_permission(request, obj)


class SolicitaTransferenciaStockAdmin(admin.ModelAdmin):

    form = TransferenciaStockForm

    # class Media:
    #     js = [
    #         'stock/js/solicita_transferencia_stock.js'
    #     ]

    readonly_fields = ['usuario_solicitante_transferencia', 'estado_transferencia', 'fecha_hora_registro_transferencia']  # 'cantidad_existente_stock', 'usuario_autorizante_transferencia', 'fecha_hora_autorizacion_transferencia'

    # raw_id_fields = ['producto_transferencia']

    fieldsets = [
        # ('Datos de la Transferencia', {'fields': ['producto_transferencia', ('cant_exist_dce', 'cant_exist_dbp', 'cant_exist_dba', 'cant_exist_dco', 'cant_exist_dbi', 'cant_total_existente'),
        #                                           'deposito_origen_transferencia', 'cantidad_producto_transferencia']}),
        ('Deposito Solicitante', {'fields': ['deposito_destino_transferencia', 'usuario_solicitante_transferencia']}),
        ('Deposito Proveedor', {'fields': ['deposito_origen_transferencia']}),
        ('Otros datos de la Transferencia', {'fields': ['estado_transferencia', 'fecha_hora_registro_transferencia']}),  # 'usuario_autorizante_transferencia', 'fecha_hora_autorizacion_transferencia'
    ]

    inlines = [TransferenciaStockDetalleInline]

    list_display = ['id', 'deposito_destino_transferencia',
                    'usuario_solicitante_transferencia', 'fecha_hora_registro_transferencia', 'colorea_estado_transferencia',
                    'deposito_origen_transferencia']  # 'producto_transferencia', 'cantidad_producto_transferencia',
    list_filter = ['id', 'deposito_destino_transferencia',
                    'usuario_solicitante_transferencia', 'fecha_hora_registro_transferencia', 'estado_transferencia',
                    'deposito_origen_transferencia']  # 'producto_transferencia',
    search_fields = ['id', 'deposito_destino_transferencia__descripcion',
                    'usuario_solicitante_transferencia__usuario__username', 'fecha_hora_registro_transferencia', 'estado_transferencia__estado_transferencia_stock',
                    'deposito_origen_transferencia__descripcion']  # 'producto_transferencia__producto', 'cantidad_producto_transferencia',

    def colorea_estado_transferencia(self, obj):
        # color = 'black'
        if obj.estado_transferencia.estado_transferencia_stock == 'PRO':
            color = 'green'
            return format_html('<span style="color: %s"><b> %s </b></span>' %
                               (color, obj.estado_transferencia.get_estado_transferencia_stock_display()))
        elif obj.estado_transferencia.estado_transferencia_stock == 'CAN':
            color = 'orange'
            return format_html('<span style="color: %s"><b> %s </b></span>' %
                               (color, obj.estado_transferencia.get_estado_transferencia_stock_display()))
        elif obj.estado_transferencia.estado_transferencia_stock == 'PEN':
            color = 'red'
            return format_html('<span style="color: %s"><b> %s </b></span>' %
                               (color, obj.estado_transferencia.get_estado_transferencia_stock_display()))
        return obj.estado_transferencia
    colorea_estado_transferencia.short_description = 'Estado Transferencia'

    def save_model(self, request, obj, form, change):

        transferencia = obj

        if '_save' in request.POST or '_continue' in request.POST:
            transferencia.estado_transferencia = TransferenciaStockEstado.objects.get(estado_transferencia_stock='PEN')
            if getattr(transferencia, 'usuario_solicitante_transferencia', None) is None:
                transferencia.usuario_solicitante_transferencia = Empleado.objects.get(usuario_id=request.user)
            # 1) Al confirmarse la Transferencia se deben generar dos registros en StockDetalle, uno que reste la
            # "cantidad_producto_transferencia" del "deposito_proveedor_transferencia" y otro que sume
            # "cantidad_producto_transferencia" al "deposito_solicitante_transferencia".

        # elif '_continue' in request.POST:
        #     transferencia.estado_transferencia = TransferenciaStockEstado.objects.get(estado_transferencia_stock='PEN')

        elif '_cancel' in request.POST:
            transferencia.estado_transferencia = TransferenciaStockEstado.objects.get(estado_transferencia_stock='CAN')
            transferencia.motivo_cancelacion = request.POST.get('motivo', '')
            transferencia.observaciones_cancelacion = request.POST.get('observaciones', '')
            transferencia.usuario_cancelacion = Empleado.objects.get(usuario_id=request.user)
            transferencia.fecha_hora_cancelacion = timezone.now()

        super(SolicitaTransferenciaStockAdmin, self).save_model(request, obj, form, change)

    def get_readonly_fields(self, request, obj=None):

        # import pdb
        # pdb.set_trace()

        if obj is not None and obj.estado_transferencia.estado_transferencia_stock == 'PEN':
            return self.readonly_fields
        elif obj is not None and obj.estado_transferencia.estado_transferencia_stock in ('PRO', 'CAN'):
            return [i.name for i in self.model._meta.fields] + \
                   [i.name for i in self.model._meta.many_to_many]
        else:
            return super(SolicitaTransferenciaStockAdmin, self).get_readonly_fields(request, obj)

    def changeform_view(self, request, object_id=None, form_url='', extra_context=None):
        extra_context = extra_context or {}

        extra_context['show_button'] = True
        if object_id is not None:
            transferencia = TransferenciaStock.objects.get(pk=object_id)

            if transferencia.estado_transferencia.estado_transferencia_stock == 'PEN':
                extra_context['show_save_button'] = True
                extra_context['show_continue_button'] = True
                # extra_context['show_change_button'] = False
                extra_context['show_cancel_button'] = True
                # extra_context['show_imprimir_button'] = True
            elif transferencia.estado_transferencia.estado_transferencia_stock in ('PRO', 'CAN'):
                extra_context['show_save_button'] = False
                extra_context['show_continue_button'] = False
                # extra_context['show_change_button'] = False
                extra_context['show_cancel_button'] = False
                # extra_context['show_imprimir_button'] = True

        elif object_id is None:
            extra_context['show_save_button'] = True
            extra_context['show_continue_button'] = True
            # extra_context['show_change_button'] = False
            extra_context['show_cancel_button'] = False
            # extra_context['show_imprimir_button'] = False

        return super(SolicitaTransferenciaStockAdmin, self).changeform_view(request, object_id, form_url, extra_context)

    def get_form(self, request, obj=None, **kwargs):
        form = super(SolicitaTransferenciaStockAdmin, self).get_form(request, obj=obj, **kwargs)

        # if obj is None:
        #     # usuario = Empleado.objects.get(usuario=request.user)
        #     # form.base_fields['cajero'].initial = usuario
        #     # form.base_fields['horario'].initial = usuario.horario
        #     form.base_fields['mozo_pedido'].widget.attrs['readonly'] = True
        #     form.base_fields['jornada'].widget.attrs['readonly'] = True
        #     form.base_fields['jornada'].widget.attrs['style'] = 'width: 300px;'

        form.request = request
        return form

    def _create_formsets(self, request, obj, change):
        formsets, inline_instances = super(SolicitaTransferenciaStockAdmin, self)._create_formsets(request, obj, change)
        for formset in formsets:
            formset.request = request
        return formsets, inline_instances


class ConfirmaTransferenciaStockAdmin(admin.ModelAdmin):

    form = TransferenciaStockForm

    # class Media:
    #     js = [
    #         'stock/js/confirma_transferencia_stock.js'
    #     ]

    readonly_fields = ['deposito_origen_transferencia', 'deposito_destino_transferencia',
                       'usuario_solicitante_transferencia', 'estado_transferencia', 'fecha_hora_registro_transferencia',
                       'usuario_autorizante_transferencia', 'fecha_hora_autorizacion_transferencia']  # 'producto_transferencia',

    # raw_id_fields = []

    fieldsets = [
        # ('Datos de la Transferencia', {'fields': ['producto_transferencia', ('cant_exist_dce', 'cant_exist_dbp', 'cant_exist_dba', 'cant_exist_dco', 'cant_exist_dbi', 'cant_total_existente'),
        #                                           'deposito_origen_transferencia', 'cantidad_producto_transferencia']}),
        ('Deposito Solicitante', {'fields': ['deposito_destino_transferencia', 'usuario_solicitante_transferencia']}),
        ('Deposito Proveedor', {'fields': ['deposito_origen_transferencia']}),
        ('Otros datos de la Transferencia', {'fields': ['estado_transferencia', 'fecha_hora_registro_transferencia',
                                                        'usuario_autorizante_transferencia', 'fecha_hora_autorizacion_transferencia']}),
    ]

    inlines = [TransferenciaStockDetalleInline]

    list_display = ['id', 'deposito_destino_transferencia',
                    'usuario_solicitante_transferencia', 'fecha_hora_registro_transferencia', 'colorea_estado_transferencia',
                    'deposito_origen_transferencia', 'usuario_autorizante_transferencia', 'fecha_hora_autorizacion_transferencia']  # 'producto_transferencia', 'cantidad_producto_transferencia',
    list_filter = ['id', 'deposito_destino_transferencia',
                    'usuario_solicitante_transferencia', 'fecha_hora_registro_transferencia', 'estado_transferencia',
                    'deposito_origen_transferencia', 'usuario_autorizante_transferencia', 'fecha_hora_autorizacion_transferencia']  # 'producto_transferencia',
    search_fields = ['id', 'deposito_destino_transferencia__descripcion',
                    'usuario_solicitante_transferencia__usuario__username', 'fecha_hora_registro_transferencia', 'estado_transferencia__estado_transferencia_stock',
                    'deposito_origen_transferencia__descripcion', 'usuario_autorizante_transferencia__usuario__username', 'fecha_hora_autorizacion_transferencia']  # 'producto_transferencia__producto', 'cantidad_producto_transferencia',

    def colorea_estado_transferencia(self, obj):
        # color = 'black'
        if obj.estado_transferencia.estado_transferencia_stock == 'PRO':
            color = 'green'
            return format_html('<span style="color: %s"><b> %s </b></span>' %
                               (color, obj.estado_transferencia.get_estado_transferencia_stock_display()))
        elif obj.estado_transferencia.estado_transferencia_stock == 'CAN':
            color = 'orange'
            return format_html('<span style="color: %s"><b> %s </b></span>' %
                               (color, obj.estado_transferencia.get_estado_transferencia_stock_display()))
        elif obj.estado_transferencia.estado_transferencia_stock == 'PEN':
            color = 'red'
            return format_html('<span style="color: %s"><b> %s </b></span>' %
                               (color, obj.estado_transferencia.get_estado_transferencia_stock_display()))
        return obj.estado_transferencia
    colorea_estado_transferencia.short_description = 'Estado Transferencia'

    def save_model(self, request, obj, form, change):

        transferencia = obj

        if '_save' in request.POST:
            transferencia.estado_transferencia = TransferenciaStockEstado.objects.get(estado_transferencia_stock='PRO')
            transferencia.fecha_hora_autorizacion_transferencia = timezone.now()
            if getattr(transferencia, 'usuario_autorizante_transferencia', None) is None:
                transferencia.usuario_autorizante_transferencia = Empleado.objects.get(usuario_id=request.user)

        elif '_continue' in request.POST:
            pass

        elif '_cancel' in request.POST:
            transferencia.estado_transferencia = TransferenciaStockEstado.objects.get(estado_transferencia_stock='CAN')
            transferencia.motivo_cancelacion = request.POST.get('motivo', '')
            transferencia.observaciones_cancelacion = request.POST.get('observaciones', '')
            transferencia.usuario_cancelacion = Empleado.objects.get(usuario_id=request.user)
            transferencia.fecha_hora_cancelacion = timezone.now()

        super(ConfirmaTransferenciaStockAdmin, self).save_model(request, obj, form, change)

    def save_formset(self, request, form, formset, change):

        import pdb
        pdb.set_trace()

        transferencia = form.instance

        if "_save" in request.POST:
            for form in formset:
                transferencia_detalle = form.instance

                # 1) Al confirmarse la Transferencia se deben generar dos registros en MovimientoStock, uno que reste la
                # "cantidad_producto_transferencia" del "deposito_origen_transferencia" y otro que sume
                # "cantidad_producto_transferencia" al "deposito_destino_transferencia".

                stock = MovimientoStock(producto_stock_id=transferencia_detalle.producto_transferencia.id,
                                        tipo_movimiento='TR',
                                        id_movimiento=transferencia.id,
                                        ubicacion_origen=transferencia.deposito_origen_transferencia,
                                        ubicacion_destino=transferencia.deposito_destino_transferencia,
                                        cantidad_entrante=transferencia_detalle.cantidad_producto_transferencia,
                                        cantidad_saliente=transferencia_detalle.cantidad_producto_transferencia,
                                        fecha_hora_registro_stock=timezone.now())
                stock.save()

        super(ConfirmaTransferenciaStockAdmin, self).save_formset(request, form, formset, change)

    def get_readonly_fields(self, request, obj=None):

        # import pdb
        # pdb.set_trace()

        # if obj is not None and obj.estado_transferencia.estado_transferencia_stock == 'PEN':
        #     return self.readonly_fields
        if obj is not None and obj.estado_transferencia.estado_transferencia_stock in ('PRO', 'CAN', 'PEN'):
            return [i.name for i in self.model._meta.fields] + \
                   [i.name for i in self.model._meta.many_to_many]
        else:
            return super(ConfirmaTransferenciaStockAdmin, self).get_readonly_fields(request, obj)

    def changeform_view(self, request, object_id=None, form_url='', extra_context=None):
        extra_context = extra_context or {}

        extra_context['show_button'] = True
        if object_id is not None:
            transferencia = TransferenciaStock.objects.get(pk=object_id)

            if transferencia.estado_transferencia.estado_transferencia_stock == 'PEN':
                extra_context['show_save_button'] = True
                extra_context['show_continue_button'] = True
                # extra_context['show_change_button'] = False
                extra_context['show_cancel_button'] = True
                # extra_context['show_imprimir_button'] = True
            elif transferencia.estado_transferencia.estado_transferencia_stock in ('PRO', 'CAN'):
                extra_context['show_save_button'] = False
                extra_context['show_continue_button'] = False
                # extra_context['show_change_button'] = False
                extra_context['show_cancel_button'] = False
                # extra_context['show_imprimir_button'] = True

        elif object_id is None:
            extra_context['show_save_button'] = True
            extra_context['show_continue_button'] = True
            # extra_context['show_change_button'] = False
            extra_context['show_cancel_button'] = False
            # extra_context['show_imprimir_button'] = False

        return super(ConfirmaTransferenciaStockAdmin, self).changeform_view(request, object_id, form_url, extra_context)

    def get_form(self, request, obj=None, **kwargs):
        form = super(ConfirmaTransferenciaStockAdmin, self).get_form(request, obj=obj, **kwargs)

        # if obj is None:
        #     # usuario = Empleado.objects.get(usuario=request.user)
        #     # form.base_fields['cajero'].initial = usuario
        #     # form.base_fields['horario'].initial = usuario.horario
        #     form.base_fields['mozo_pedido'].widget.attrs['readonly'] = True
        #     form.base_fields['jornada'].widget.attrs['readonly'] = True
        #     form.base_fields['jornada'].widget.attrs['style'] = 'width: 300px;'

        form.request = request
        return form

    def _create_formsets(self, request, obj, change):
        formsets, inline_instances = super(ConfirmaTransferenciaStockAdmin, self)._create_formsets(request, obj, change)
        for formset in formsets:
            formset.request = request
        return formsets, inline_instances

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

# ======================================================================================================================

admin.site.register(Producto, ProductoAdmin)
# admin.site.register(PrecioVentaProducto, PrecioVentaProductoAdmin)
admin.site.register(ProductoCompuesto, ProductoCompuestoAdmin)
admin.site.register(ProductoVenta, ProductoVentaAdmin)
admin.site.register(ProductoExistente, ProductoExistenteAdmin)
admin.site.register(Insumo, InsumoAdmin)
admin.site.register(MovimientoStock, MovimientoStockAdmin)
# admin.site.register(StockProducto)
# admin.site.register(StockDeposito)
admin.site.register(SolicitaTransferenciaStock, SolicitaTransferenciaStockAdmin)
admin.site.register(ConfirmaTransferenciaStock, ConfirmaTransferenciaStockAdmin)
admin.site.register(StockAjuste, StockAjusteAdmin)
# admin.site.register(Devolucion)