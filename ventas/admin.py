from django.contrib import admin

# Register your models here.

from .models import Pedido, PedidoDetalle


class PedidoDetalleInline(admin.TabularInline):
    model = PedidoDetalle
    extra = 1


class PedidoAdmin(admin.ModelAdmin):
    inlines = [PedidoDetalleInline]

    list_display = ('id', 'fecha_pedido')
    list_filter = ['id', 'fecha_pedido']
    search_fields = ['id', 'fecha_pedido']


class PedidoDetalleAdmin(admin.ModelAdmin):
    list_display = ('id', 'pedido', 'producto_pedido', 'cantidad_producto_pedido')
    list_filter = ['id', 'pedido', 'producto_pedido', 'cantidad_producto_pedido']
    search_fields = ['id', 'pedido', 'producto_pedido', 'cantidad_producto_pedido']


admin.site.register(Pedido, PedidoAdmin)
# admin.site.register(PedidoDetalle, PedidoDetalleAdmin)
