from django.contrib import admin

# Register your models here.
# from stock.forms import RecetaDetalleForm

from .models import Producto, PrecioProducto, UnidadMedida, Receta, RecetaDetalle, Deposito


class PrecioProductoInline(admin.TabularInline):
    model = PrecioProducto
    extra = 0


class ProductoAdmin(admin.ModelAdmin):
    inlines = [PrecioProductoInline]

    list_display = ('id', 'producto', 'marca', 'tipo_producto', 'categoria', 'unidad_medida', 'contenido', 'imagen')
    list_filter = ['id', 'producto', 'marca', 'tipo_producto', 'categoria']
    search_fields = ['id', 'producto', 'marca', 'tipo_producto', 'categoria']


class PrecioProductoAdmin(admin.ModelAdmin):
    list_display = ('producto', 'fecha', 'precio_venta')
    list_filter = ['producto', 'fecha', 'precio_venta']
    search_fields = ['producto', 'fecha', 'precio_venta']


class UnidadMedidaAdmin(admin.ModelAdmin):
    list_display = ('id', 'unidad_medida', 'descripcion')
    list_filter = ['id', 'unidad_medida', 'descripcion']
    search_fields = ['id', 'unidad_medida', 'descripcion']


class RecetaDetalleInline(admin.TabularInline):
    model = RecetaDetalle
    extra = 1
#    form = RecetaDetalleForm


class RecetaAdmin(admin.ModelAdmin):

    inlines = [RecetaDetalleInline]

    list_display = ('id', 'receta', 'estado')
    list_filter = ['id', 'receta', 'estado']
    search_fields = ['id', 'receta', 'estado']


class RecetaDetalleAdmin(admin.ModelAdmin):
    list_display = ('id', 'receta', 'producto', 'cantidad_producto')
    list_filter = ['id', 'receta', 'producto', 'cantidad_producto']
    search_fields = ['id', 'receta', 'producto', 'cantidad_producto']


class DepositoAdmin(admin.ModelAdmin):
    list_display = ('id', 'deposito', 'descripcion', 'tipo_deposito')
    list_filter = ['id', 'deposito', 'descripcion', 'tipo_deposito']
    search_fields = ['id', 'deposito', 'descripcion', 'tipo_deposito']


admin.site.register(Producto, ProductoAdmin)
admin.site.register(PrecioProducto, PrecioProductoAdmin)
admin.site.register(UnidadMedida, UnidadMedidaAdmin)
admin.site.register(Receta, RecetaAdmin)
admin.site.register(RecetaDetalle, RecetaDetalleAdmin)
admin.site.register(Deposito, DepositoAdmin)