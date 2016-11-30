# -*- coding: utf-8 -*-
from django.contrib import admin

# Register your models here.
from django.forms.models import BaseInlineFormSet
from django.utils.html import format_html
from bar.models import AjusteStockEstado, CategoriaProducto, SubCategoriaProducto
from stock.forms import ProductoForm, ProductoCompuestoForm, ProductoCompuestoDetalleInlineForm, \
    InsumoForm, TransferenciaStockForm, TransferenciaStockDetalleInlineForm, \
    TransferenciaStockDetalleFormSet, AjusteStockDetalleInlineForm, AjusteStockDetalleFormSet, \
    AjusteStockForm  # PrecioVentaProductoForm

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
                    'precio_compra', 'porcentaje_ganancia', 'precio_venta', 'thumb')  # 'compuesto', 'get_cantidad_existente_producto',
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
                    'subcategoria', 'costo_elaboracion', 'porcentaje_ganancia', 'precio_venta',
                    'get_insumos_disponibles_producto_compuesto', 'thumb')
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
    ordering = ['producto']
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

    ordering = ['insumo']

    inlines = [ProductoInsumoInlineAdmin]

    list_display = ['id', 'insumo', 'unidad_medida', 'get_costo_promedio_por_unidad',
                    'get_cantidad_existente_insumo_dce', 'get_cantidad_existente_insumo_dbp', 'get_cantidad_existente_insumo_dba', 'get_cantidad_existente_insumo_dco', 'get_cantidad_existente_insumo_dbi',
                    'get_cantidad_existente_insumo']
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

    ordering = ['producto']


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
                    'unidad_medida_contenido', 'contenido', 'precio_venta', 'get_unidad_medida_producto_existente',
                    'get_cantidad_existente_producto_dce', 'get_cantidad_existente_producto_dbp', 'get_cantidad_existente_producto_dba', 'get_cantidad_existente_producto_dbi',
                    'get_cantidad_existente_producto', 'thumb')
    list_display_links = ['producto']
    list_filter = ['id', 'producto', 'marca', ('categoria', admin.RelatedOnlyFieldListFilter), ('subcategoria', admin.RelatedOnlyFieldListFilter)]
    search_fields = ['id', 'producto', 'marca', 'categoria__categoria', 'subcategoria__subcategoria']

    # def get_producto_nombre(self,obj):
    #     if obj.compuesto:
    #         link = '/admin/stock/productocompuesto/%s'%obj.pk
    #     else:
    #         link = '/admin/stock/producto/%s'%obj.pk
    #     tag = '<a href="%s">%s</a>'%(link,str(obj))
    #
    #     return mark_safe(tag)

    def get_queryset(self, request):

        # import pdb
        # pdb.set_trace()

        # Filtra los Productos para la Venta que poseen disponibilidad en Stock.
        # queryset = Producto.objects.filter(Q(tipo_producto='VE', id__in=InventarioDeposito.objects.filter(cant_existente__gt=0))
        #                                    | Q(tipo_producto='VE', compuesto=True))  # , get_insumos_disponibles_producto_compuesto=True

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


class ProductoExistenteAdmin(admin.ModelAdmin):

    # form = ProductoCompuestoForm

    # class Media:
    #     js = [
    #         # 'stock/js/producto_compuesto.js',
    #     ]

    # readonly_fields = ['fecha_alta_producto', 'thumb']

    ordering = ['producto']

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
    list_display = ('id', 'producto', 'marca', 'categoria', 'subcategoria', 'get_unidad_medida_producto_existente',
                    'get_cantidad_existente_producto', 'thumb')
    list_display_links = ['producto']
    list_filter = ['producto', 'marca', ('categoria', admin.RelatedOnlyFieldListFilter), ('subcategoria', admin.RelatedOnlyFieldListFilter)]
    search_fields = ['id', 'producto', 'marca', 'categoria__categoria', 'subcategoria__subcategoria']

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


# ======================================================================================================================
class CategoriaProductoListFilter(admin.SimpleListFilter):

    """
    This filter will always return a subset of the instances in a Model, either filtering by the
    user choice or by a default value.
    """
    # Human-readable title which will be displayed in the
    # right admin sidebar just above the filter options.
    title = 'categoria'

    # Parameter for the filter that will be used in the URL query.
    parameter_name = 'categoria'

    default_value = None

    def lookups(self, request, model_admin):
        """
        Returns a list of tuples. The first element in each
        tuple is the coded value for the option that will
        appear in the URL query. The second element is the
        human-readable name for the option that will appear
        in the right sidebar.
        """
        list_of_categories = []
        queryset = CategoriaProducto.objects.all()
        for categoria in queryset:
            list_of_categories.append(
                (str(categoria.id), categoria.get_categoria_display())
            )
        return sorted(list_of_categories, key=lambda tp: tp[1])

    def queryset(self, request, queryset):
        """
        Returns the filtered queryset based on the value
        provided in the query string and retrievable via
        `self.value()`.
        """
        # Compare the requested value to decide how to filter the queryset.
        if self.value():
            productos_por_categoria = Producto.objects.filter(categoria_id=self.value())
            return queryset.filter(id__in=productos_por_categoria)
        return queryset

    # def value(self):
    #     """
    #     Overriding this method will allow us to always have a default value.
    #     """
    #     value = super(CategoriaProductoListFilter, self).value()
    #     if value is None:
    #         if self.default_value is None:
    #             # If there is at least one Species, return the first by name. Otherwise, None.
    #             first_categories = CategoriaProducto.objects.order_by('categoria').first()
    #             value = None if first_categories is None else first_categories.id
    #             self.default_value = value
    #         else:
    #             value = self.default_value
    #     return str(value)


class SubCategoriaProductoListFilter(admin.SimpleListFilter):

    """
    This filter will always return a subset of the instances in a Model, either filtering by the
    user choice or by a default value.
    """
    # Human-readable title which will be displayed in the
    # right admin sidebar just above the filter options.
    title = 'subcategoria'

    # Parameter for the filter that will be used in the URL query.
    parameter_name = 'subcategoria'

    default_value = None

    # Custom attributes
    related_filter_parameter = 'subcategoria__categoria__id__exact'

    def lookups(self, request, model_admin):
        """
        Returns a list of tuples. The first element in each
        tuple is the coded value for the option that will
        appear in the URL query. The second element is the
        human-readable name for the option that will appear
        in the right sidebar.
        """
        list_of_subcategories = []
        queryset = SubCategoriaProducto.objects.order_by('categoria_id')
        if self.related_filter_parameter in request.GET:
            queryset = queryset.filter(categoria_id=request.GET[self.related_filter_parameter])
        for subcategoria in queryset:
            list_of_subcategories.append(
                (str(subcategoria.id), subcategoria.descripcion)
            )
        return sorted(list_of_subcategories, key=lambda tp: tp[1])

    def queryset(self, request, queryset):
        """
        Returns the filtered queryset based on the value
        provided in the query string and retrievable via
        `self.value()`.
        """
        # Compare the requested value to decide how to filter the queryset.
        if self.value():
            productos_por_subcategoria = Producto.objects.filter(subcategoria_id=self.value())
            return queryset.filter(id__in=productos_por_subcategoria)
        return queryset
    

@admin.register(InventarioProducto)
class InventarioProductoAdmin(admin.ModelAdmin):
    actions = None
    ordering = ['producto']
    list_display = ['id', 'producto', 'get_unidad_medida_inventario_producto', 'total_compras', 'total_ventas']  # 'cantidad_existente'
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
    list_display = ['id', 'producto', 'get_categoria_inventario_deposito', 'get_subcategoria_inventario_deposito',
                    'get_marca_inventario_deposito', 'get_unidad_medida_inventario_deposito',
                    'cant_exist_dce', 'cant_exist_dbp', 'cant_exist_dba', 'cant_exist_dco', 'cant_exist_dbi', 'cant_existente']
    list_display_links = None
    list_filter = ['id', 'producto', CategoriaProductoListFilter, SubCategoriaProductoListFilter]
    search_fields = ['id', 'producto']

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


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
    #         'stock/js/transferencia_stock.js'
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
    #         'stock/js/transferencia_stock.js'
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

        # import pdb
        # pdb.set_trace()

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
class AjusteStockDetalleInline(admin.TabularInline):
    model = AjusteStockDetalle
    extra = 1
    can_delete = False
    readonly_fields = ['producto_ajuste', 'unidad_medida', 'cantidad_existente_producto']
    fields = ['producto_ajuste', 'unidad_medida', 'cantidad_existente_producto', 'ajustar', 'cantidad_ajustar_producto',
              'motivo_ajuste']
    form = AjusteStockDetalleInlineForm
    formset = AjusteStockDetalleFormSet
    ordering = ['producto_ajuste__producto']
    # verbose_name = 'Pago a Proveedores'
    # verbose_name_plural = 'Pagos a Proveedores'

    def get_readonly_fields(self, request, obj=None):
        if obj is not None and obj.estado_ajuste.estado_ajuste_stock == 'PEN':
            return self.readonly_fields
        elif obj is not None and obj.estado_ajuste.estado_ajuste_stock in ('PRO', 'CAN'):
            return [i.name for i in self.model._meta.fields] + \
                   [i.name for i in self.model._meta.many_to_many]
        else:
            return super(AjusteStockDetalleInline, self).get_readonly_fields(request, obj)

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


class AjusteStockAdmin(admin.ModelAdmin):
    form = AjusteStockForm

    class Media:
        js = [
            'stock/js/ajuste_stock.js'
        ]

    readonly_fields = ['estado_ajuste', 'usuario_registra_ajuste', 'fecha_hora_registro_ajuste']

    # raw_id_fields = ['producto_transferencia']

    fieldsets = [
        ('Deposito', {'fields': ['deposito']}),
        ('Otros datos del Ajuste de Inventario', {'fields': ['estado_ajuste', 'usuario_registra_ajuste', 'fecha_hora_registro_ajuste']}),
    ]

    inlines = [AjusteStockDetalleInline]

    list_display = ['id', 'deposito', 'fecha_hora_registro_ajuste', 'usuario_registra_ajuste', 'colorea_estado_ajuste']
    list_filter = ['id', 'deposito', 'fecha_hora_registro_ajuste', 'usuario_registra_ajuste', 'estado_ajuste']
    search_fields = ['id', 'deposito__descripcion', 'fecha_hora_registro_ajuste', 'usuario_registra_ajuste__usuario__username',
                     'estado_ajuste__estado_ajuste_stock']

    def colorea_estado_ajuste(self, obj):
        # color = 'black'
        if obj.estado_ajuste.estado_ajuste_stock == 'PRO':
            color = 'green'
            return format_html('<span style="color: %s"><b> %s </b></span>' %
                               (color, obj.estado_ajuste.get_estado_ajuste_stock_display()))
        elif obj.estado_ajuste.estado_ajuste_stock == 'CAN':
            color = 'orange'
            return format_html('<span style="color: %s"><b> %s </b></span>' %
                               (color, obj.estado_ajuste.get_estado_ajuste_stock_display()))
        elif obj.estado_ajuste.estado_ajuste_stock == 'PEN':
            color = 'red'
            return format_html('<span style="color: %s"><b> %s </b></span>' %
                               (color, obj.estado_ajuste.get_estado_ajuste_stock_display()))
        return obj.estado_ajuste
    colorea_estado_ajuste.short_description = 'Estado Ajuste de Inventario'

    def save_model(self, request, obj, form, change):

        import pdb
        pdb.set_trace()

        ajuste_stock_actual = obj

        if "_continue" in request.POST:
            ajuste_stock_actual.estado_ajuste = AjusteStockEstado.objects.get(estado_ajuste_stock='PEN')
            ajuste_stock_actual.usuario_registra_ajuste = Empleado.objects.get(usuario_id=request.user)
            # ajuste_stock_actual.fecha_hora_registro_ajuste = timezone.now()

        elif "_cancel" in request.POST:
            ajuste_stock_actual.estado_ajuste = AjusteStockEstado.objects.get(estado_ajuste_stock='CAN')
            ajuste_stock_actual.motivo_cancelacion = request.POST.get('motivo', '')
            ajuste_stock_actual.observaciones_cancelacion = request.POST.get('observaciones', '')
            ajuste_stock_actual.usuario_cancelacion = Empleado.objects.get(usuario_id=request.user)
            ajuste_stock_actual.fecha_hora_cancelacion = timezone.now()

        elif "_save" in request.POST:
            ajuste_stock_actual.estado_ajuste = AjusteStockEstado.objects.get(estado_ajuste_stock='PRO')
            ajuste_stock_actual.usuario_registra_ajuste = Empleado.objects.get(usuario_id=request.user)

        super(AjusteStockAdmin, self).save_model(request, obj, form, change)

    def save_formset(self, request, form, formset, change):

        import pdb
        pdb.set_trace()

        ajuste_stock_actual = form.instance

        if "_continue" in request.POST:

            if not change:
                AjusteStockDetalle.objects.filter(ajuste_stock_id=ajuste_stock_actual.id).delete()
                print 'ajuste_stock_detalle_a_eliminar: ', AjusteStockDetalle.objects.filter(ajuste_stock_id=ajuste_stock_actual.id)

                for stock_deposito in StockDepositoAjusteInventario.objects.filter(deposito_id=ajuste_stock_actual.deposito.id):
                    unidad_medida_producto_id = 0
                    producto = Producto.objects.get(pk=stock_deposito.id)
                    if producto.tipo_producto == 'VE':
                        unidad_medida_producto_id = producto.unidad_medida_compra.id
                    elif producto.tipo_producto == 'IN':
                        unidad_medida_producto_id = producto.unidad_medida_contenido.id
                    ajuste_stock_detalle = AjusteStockDetalle(ajuste_stock_id=ajuste_stock_actual.id,
                                                              producto_ajuste_id=stock_deposito.id,
                                                              unidad_medida_id=unidad_medida_producto_id,
                                                              cantidad_existente_producto=stock_deposito.cantidad_existente,
                                                              ajustar=False,
                                                              cantidad_ajustar_producto=None,
                                                              motivo_ajuste=None)
                    ajuste_stock_detalle.save()
            super(AjusteStockAdmin, self).save_formset(request, form, formset, change)

        # Si se CANCELA la Orden de Pago se asigna el estado "CAN" a la Orden de Pago y se marcan como
        # "procesado = False" a los registros del formset
        elif "_cancel" in request.POST:
            # formset.save(commit=False)
            # for form in formset:
            #     factura_orden_pago_detalle = form.instance
            #     if factura_orden_pago_detalle.procesado is not True:
            #         factura_orden_pago_detalle.delete()
            #     elif factura_orden_pago_detalle.procesado is True:
            #         factura_orden_pago_detalle.procesado = False
            super(AjusteStockAdmin, self).save_formset(request, form, formset, change)

        # Si se confirma la Orden de Pago se asigna el estado "CON" a la Orden de Pago, el estado "PAG" a las
        # facturas en el formset y se deben generar registros de pagos en PagoProveedor para las facturas afectadas.
        # Generar tambien el registro correspondiente en la Linea de Credito.
        # Solo se debe guardar en el detalle de la Orden de Pago la Factura que fue checkeada en la casilla "Procesar"
        elif "_save" in request.POST:  # and compra_actual.estado_compra.estado_compra == 'CON':
            formset.save(commit=False)
            for form in formset:
                ajuste_stock_actual_detalle = form.instance
                if ajuste_stock_actual_detalle.ajustar is True:
                    cant_saliente = 0
                    cant_entrante = 0
                    if ajuste_stock_actual_detalle.cantidad_existente_producto > ajuste_stock_actual_detalle.cantidad_ajustar_producto:
                        cant_saliente = ajuste_stock_actual_detalle.cantidad_existente_producto - ajuste_stock_actual_detalle.cantidad_ajustar_producto
                    elif ajuste_stock_actual_detalle.cantidad_existente_producto < ajuste_stock_actual_detalle.cantidad_ajustar_producto:
                        cant_entrante = ajuste_stock_actual_detalle.cantidad_ajustar_producto - ajuste_stock_actual_detalle.cantidad_existente_producto
                    stock = MovimientoStock(producto_stock_id=ajuste_stock_actual_detalle.producto_ajuste.id,
                                            tipo_movimiento='AI',
                                            id_movimiento=ajuste_stock_actual.id,
                                            ubicacion_origen=ajuste_stock_actual.deposito,
                                            ubicacion_destino=ajuste_stock_actual.deposito,
                                            cantidad_entrante=cant_entrante,
                                            cantidad_saliente=cant_saliente,
                                            fecha_hora_registro_stock=timezone.now())
                    stock.save()
            super(AjusteStockAdmin, self).save_formset(request, form, formset, change)

    def get_readonly_fields(self, request, obj=None):

        # import pdb
        # pdb.set_trace()

        # if obj is not None and obj.estado_transferencia.estado_transferencia_stock == 'PEN':
        #     return self.readonly_fields
        if obj is not None and obj.estado_ajuste.estado_ajuste_stock in ('PRO', 'CAN', 'PEN'):
            return [i.name for i in self.model._meta.fields] + \
                   [i.name for i in self.model._meta.many_to_many]
        else:
            return super(AjusteStockAdmin, self).get_readonly_fields(request, obj)

    def changeform_view(self, request, object_id=None, form_url='', extra_context=None):
        extra_context = extra_context or {}

        extra_context['show_button'] = True
        if object_id is not None:
            ajuste = AjusteStock.objects.get(pk=object_id)

            if ajuste.estado_ajuste.estado_ajuste_stock == 'PEN':
                extra_context['show_save_button'] = True
                extra_context['show_continue_button'] = True
                # extra_context['show_change_button'] = False
                extra_context['show_cancel_button'] = True
                extra_context['show_imprimir_button'] = False
            elif ajuste.estado_ajuste.estado_ajuste_stock == 'CAN':
                extra_context['show_save_button'] = False
                extra_context['show_continue_button'] = False
                # extra_context['show_change_button'] = False
                extra_context['show_cancel_button'] = False
                extra_context['show_imprimir_button'] = False
            elif ajuste.estado_ajuste.estado_ajuste_stock == 'PRO':
                extra_context['show_save_button'] = False
                extra_context['show_continue_button'] = False
                # extra_context['show_change_button'] = False
                extra_context['show_cancel_button'] = False
                extra_context['show_imprimir_button'] = True

        elif object_id is None:
            extra_context['show_save_button'] = True
            extra_context['show_continue_button'] = True
            # extra_context['show_change_button'] = False
            extra_context['show_cancel_button'] = False
            extra_context['show_imprimir_button'] = False

        return super(AjusteStockAdmin, self).changeform_view(request, object_id, form_url, extra_context)

    def get_form(self, request, obj=None, **kwargs):
        form = super(AjusteStockAdmin, self).get_form(request, obj=obj, **kwargs)

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
        formsets, inline_instances = super(AjusteStockAdmin, self)._create_formsets(request, obj, change)
        for formset in formsets:
            formset.request = request
        return formsets, inline_instances

    # def has_add_permission(self, request):
    #     return False

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
admin.site.register(AjusteStock, AjusteStockAdmin)
# admin.site.register(Devolucion)