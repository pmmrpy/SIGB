from django.contrib import admin

# Register your models here.
# from compras.forms import CompraDetalleForm

from .models import Proveedor, TelefonoProveedor, Compra, CompraDetalle, ProductoProveedor


class TelefonoProveedorInline(admin.TabularInline):
    model = TelefonoProveedor
    extra = 1
    verbose_name = 'Telefonos'
    verbose_name_plural = 'Telefonos'


class ProveedorAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Empresa', {'fields': ['proveedor']}),
        ('RUC', {'fields': ['ruc', 'digito_verificador']}),
    ]

    inlines = [TelefonoProveedorInline]

    list_display = ('id', 'proveedor', 'ruc')
    list_filter = ['id', 'proveedor', 'ruc']
    search_fields = ['id', 'proveedor', 'ruc']


class CompraDetalleInline(admin.TabularInline):
    model = CompraDetalle
    extra = 1
#    form = CompraDetalleForm
    verbose_name = 'Detalle de Productos'
    verbose_name_plural = ''


class CompraAdmin(admin.ModelAdmin):

    fieldsets = [
        ('Numero Orden de Compra', {'fields': ['numero_compra']}),
        ('Fecha del Pedido / Fecha de Entrega del Pedido', {'fields': [('fecha_pedido', 'fecha_entrega')]}),
        # ('Fecha de Entrega del Pedido', {'fields': ['fecha_entrega']}),
        ('Datos Proveedor', {'fields': ['proveedor_compra', 'forma_pago']}),
    ]

    inlines = [CompraDetalleInline]

    list_display = ('numero_compra', 'fecha_pedido', 'fecha_entrega', 'proveedor_compra')
    list_filter = ['numero_compra', 'fecha_pedido', 'fecha_entrega', 'proveedor_compra']
    search_fields = ['numero_compra', 'fecha_pedido', 'fecha_entrega', 'proveedor_compra']


class CompraDetalleAdmin(admin.ModelAdmin):
    list_display = ('compra', 'producto', 'cantidad_producto', 'precio_compra_producto')
    list_filter = ['compra', 'producto', 'cantidad_producto', 'precio_compra_producto']
    search_fields = ['compra', 'producto', 'cantidad_producto', 'precio_compra_producto']


class ProductoProveedorAdmin(admin.ModelAdmin):
    list_display = ('id', 'proveedor', 'producto')
    list_filter = ['id', 'proveedor', 'producto']
    search_fields = ['id', 'proveedor', 'producto']


admin.site.register(Proveedor, ProveedorAdmin)
admin.site.register(Compra, CompraAdmin)
admin.site.register(CompraDetalle, CompraDetalleAdmin)
admin.site.register(ProductoProveedor, ProductoProveedorAdmin)