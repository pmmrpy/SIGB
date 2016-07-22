from django.contrib import admin

# Register your models here.
from stock.forms import PrecioProductoForm

from .models import Producto, PrecioProducto, Stock  # Receta, RecetaDetalle,


class PrecioProductoInline(admin.TabularInline):
    model = PrecioProducto
    extra = 0
    form = PrecioProductoForm


class ProductoAdmin(admin.ModelAdmin):
    # form =

    class Media:
        js = [
            'stock/js/producto.js'
        ]

    readonly_fields = ['fecha_alta_producto', 'thumb']

    fieldsets = [
        ('Datos del Producto', {'fields': ['producto', 'codigo_barra', 'marca', 'fecha_alta_producto',
                                           'unidad_medida_compra', 'imagen', 'thumb']}),
        ('Contenido del Producto', {'fields': ['tipo_producto', 'categoria', 'subcategoria', 'unidad_medida_contenido',
                                               'contenido']}),
    ]

    # PrecioProducto debe estar disponible como Inline solo para los Productos que tienen Tipo de Producto
    # "VE - Para la Venta", serian los registrados con este Tipo de Producto en la pantalla de Productos mas
    # los Productos Compuestos
    # inlines = [PrecioProductoInline]

    # list_select_related = True
    list_display = ('id', 'producto', 'marca', 'fecha_alta_producto', 'unidad_medida_compra', 'tipo_producto',
                    'categoria', 'subcategoria', 'unidad_medida_contenido', 'contenido', 'thumb')
    list_filter = ['id', 'producto', 'marca', 'fecha_alta_producto', 'tipo_producto', 'categoria', 'subcategoria']
    search_fields = ['id', 'producto', 'marca', 'fecha_alta_producto', 'tipo_producto', 'categoria', 'subcategoria']


# class PrecioProductoAdmin(admin.ModelAdmin):
#     list_display = ('producto', 'fecha_precio_producto', 'precio_venta', 'activo')
#     list_filter = ['producto', 'fecha_precio_producto', 'precio_venta', 'activo']
#     search_fields = ['producto', 'fecha_precio_producto', 'precio_venta', 'activo']


# class RecetaDetalleInline(admin.TabularInline):
#     model = RecetaDetalle
#     extra = 1
# #    form = RecetaDetalleForm
#
#
# class RecetaAdmin(admin.ModelAdmin):
#
#     inlines = [RecetaDetalleInline]
#
#     list_display = ('id', 'receta', 'estado')
#     list_filter = ['id', 'receta', 'estado']
#     search_fields = ['id', 'receta', 'estado']
#
#
# class RecetaDetalleAdmin(admin.ModelAdmin):
#     list_display = ('id', 'receta', 'producto', 'cantidad_producto')
#     list_filter = ['id', 'receta', 'producto', 'cantidad_producto']
#     search_fields = ['id', 'receta', 'producto', 'cantidad_producto']


class StockAdmin(admin.ModelAdmin):
    list_display = ('id', 'producto_stock', 'ubicacion', 'fecha_hora_registro_stock', 'stock_minimo',
                    'cantidad_existente', 'cantidad_entrante', 'cantidad_saliente')
    list_filter = ['id', 'producto_stock', 'ubicacion', 'fecha_hora_registro_stock', 'stock_minimo',
                   'cantidad_existente', 'cantidad_entrante', 'cantidad_saliente']
    search_fields = ['id', 'producto_stock', 'ubicacion', 'fecha_hora_registro_stock', 'stock_minimo',
                     'cantidad_existente', 'cantidad_entrante', 'cantidad_saliente']

admin.site.register(Producto, ProductoAdmin)
# admin.site.register(PrecioProducto, PrecioProductoAdmin)
# admin.site.register(Receta, RecetaAdmin)
# admin.site.register(RecetaDetalle, RecetaDetalleAdmin)
# admin.site.register(Deposito, DepositoAdmin)
admin.site.register(Stock, StockAdmin)