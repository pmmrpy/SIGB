from django.contrib import admin

# Register your models here.

from .models import Pedido, PedidoDetalle


class PedidoDetalleInline(admin.TabularInline):
    model = PedidoDetalle
    extra = 1


class PedidoAdmin(admin.ModelAdmin):
    inlines = [PedidoDetalleInline]

    list_display = ('id', 'fecha')
    list_filter = ['id', 'fecha']
    search_fields = ['id', 'fecha']


class PedidoDetalleAdmin(admin.ModelAdmin):
    list_display = ('id', 'pedido', 'producto', 'cantidad_producto')
    list_filter = ['id', 'pedido', 'producto', 'cantidad_producto']
    search_fields = ['id', 'pedido', 'producto', 'cantidad_producto']


admin.site.register(Pedido, PedidoAdmin)
admin.site.register(PedidoDetalle, PedidoDetalleAdmin)
