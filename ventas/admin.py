from django.contrib import admin

# Register your models here.

from .models import Pedido, PedidoDetalle, Venta, VentaDetalle, Cocina, AperturaCaja


# class PedidoDetalleAdmin(admin.ModelAdmin):
#     list_display = ('id', 'pedido', 'producto_pedido', 'cantidad_producto_pedido')
#     list_filter = ['id', 'pedido', 'producto_pedido', 'cantidad_producto_pedido']
#     search_fields = ['id', 'pedido', 'producto_pedido', 'cantidad_producto_pedido']


class PedidoDetalleInline(admin.TabularInline):
    model = PedidoDetalle
    extra = 0
    # form =
    readonly_fields = ['fecha_pedido_detalle']
    raw_id_fields = ['producto_pedido']
    # verbose_name =
    # verbose_name_plural =


class PedidoAdmin(admin.ModelAdmin):
    # form =

    class Media:
        js = [
            'ventas/js/pedido.js'
        ]

    readonly_fields = ['estado_pedido', 'fecha_pedido']  # Agregar 'total_pedido'

    raw_id_fields = ['reserva']

    fieldsets = [
        ('Datos de la Reserva', {'fields': ['reserva', 'monto_entrega_reserva']}),
        ('Datos del Pedido', {'fields': ['mesa_pedido', 'mozo_pedido', 'estado_pedido', 'fecha_pedido']}),
        ('Total', {'fields': ['total_pedido']}),
    ]

    inlines = [PedidoDetalleInline]

    list_display = ('id', 'reserva', 'monto_entrega_reserva', 'mozo_pedido', 'estado_pedido', 'fecha_pedido', 'total_pedido')
    list_filter = ['id', 'mesa_pedido', 'mozo_pedido', 'estado_pedido', 'fecha_pedido']
    search_fields = ['id', 'mesa_pedido', 'mozo_pedido', 'estado_pedido', 'fecha_pedido']


class VentaDetalleInline(admin.TabularInline):
    model = VentaDetalle
    extra = 0
    # form =
    raw_id_fields = ['producto_venta']
    # verbose_name =
    # verbose_name_plural =


class VentaAdmin(admin.ModelAdmin):
    # form =

    class Media:
        js = [
            'ventas/js/venta.js'
        ]

    readonly_fields = ['fecha_venta']

    # raw_id_fields = []

    fieldsets = [
        ('', {'fields': ['empresa', 'numero_factura_venta', 'fecha_venta', 'caja', 'numero_pedido', 'reserva',
                         'cliente', 'forma_pago', 'total_venta', 'estado_venta']})
    ]

    inlines = [VentaDetalleInline]

    list_display = ('numero_factura_venta', 'numero_factura_venta', 'caja', 'numero_pedido', 'reserva',
                         'reserva', 'forma_pago', 'total_venta', 'estado_venta')
    list_filter = []
    search_fields = []


class AperturaCajaAdmin(admin.ModelAdmin):
    fieldsets = [

    ]
    list_display = ()
    list_filter = []
    search_fields = []

admin.site.register(Pedido, PedidoAdmin)
admin.site.register(Venta, VentaAdmin)
admin.site.register(AperturaCaja)
admin.site.register(Cocina)