from django.contrib import admin

# Register your models here.
# from bar.forms import PaisForm
from django.utils.html import format_html
from bar.forms import TimbradoForm
from bar.models import NumeroFacturaVenta
from .models import ReservaEstado, Mesa, MesaEstado, MesaUbicacion, Caja, Sector, Documento, \
    Persona, FormaPagoCompra, TipoDeposito, Deposito, CategoriaProducto, SubCategoriaProducto, \
    TipoProducto, UnidadMedidaProducto, Moneda, Cotizacion, CodigoPaisTelefono, CodigoOperadoraTelefono, Pais, \
    Ciudad, CompraEstado, OrdenCompraEstado, PedidoEstado, VentaEstado, Timbrado, FacturaVenta, TipoMovimientoStock, \
    TransferenciaStockEstado, TipoFacturaCompra


# class MyAdminSite(admin.AdminSite):
#     site_header = 'SIGB Admin'
#     site_title ='SIGB Admin'


class ReservaEstadoAdmin(admin.ModelAdmin):
    list_display = ('id', 'reserva_estado', 'descripcion')
    list_filter = ['id', 'reserva_estado', 'descripcion']
    search_fields = ['id', 'reserva_estado', 'descripcion']


class MesaAdmin(admin.ModelAdmin):
    ordering = ['numero_mesa']
    list_display = ('nombre_mesa', 'numero_mesa', 'sector', 'ubicacion', 'colorea_estado_mesa', 'utilizada_por_numero_pedido')
    list_display_links = ['nombre_mesa']
    list_filter = ['numero_mesa', 'nombre_mesa', 'sector', 'ubicacion', 'estado']
    search_fields = ['numero_mesa', 'nombre_mesa', 'sector__sector', 'ubicacion__mesa_ubicacion', 'estado__mesa_estado']

    def colorea_estado_mesa(self, obj):
        # color = 'black'
        if obj.estado.mesa_estado == 'DI':
            color = 'green'
            return format_html('<span style="color: %s"><b> %s </b></span>' %
                               (color, obj.estado.get_mesa_estado_display()))
        elif obj.estado.mesa_estado == 'OC':
            color = 'red'
            return format_html('<span style="color: %s"><b> %s </b></span>' %
                               (color, obj.estado.get_mesa_estado_display()))
        elif obj.estado.mesa_estado == 'IN':
            color = 'orange'
            return format_html('<span style="color: %s"><b> %s </b></span>' %
                               (color, obj.estado.get_mesa_estado_display()))
        return obj.estado.mesa_estado
    colorea_estado_mesa.short_description = 'Estado Mesa'


class MesaEstadoAdmin(admin.ModelAdmin):
    list_display = ('id', 'mesa_estado', 'descripcion')
    list_filter = ['id', 'mesa_estado', 'descripcion']
    search_fields = ['id', 'mesa_estado', 'descripcion']


class MesaUbicacionAdmin(admin.ModelAdmin):
    list_display = ('id', 'mesa_ubicacion', 'descripcion')
    list_filter = ['id', 'mesa_ubicacion', 'descripcion']
    search_fields = ['id', 'mesa_ubicacion', 'descripcion']


class CajaAdmin(admin.ModelAdmin):

    fieldsets = [
        ('Datos Caja', {'fields': ['numero_caja', 'sector', 'estado_caja']}),
        ('Datos Tributarios', {'fields': ['punto_expedicion', 'marca', 'modelo_fabricacion', 'numero_serie']}),
    ]

    ordering = ['numero_caja']
    list_display = ['numero_caja', 'sector', 'punto_expedicion', 'marca', 'modelo_fabricacion', 'numero_serie',
                    'colorea_estado_caja']
    list_display_links = ['numero_caja']
    list_filter = ['numero_caja', 'sector', 'punto_expedicion', 'marca', 'modelo_fabricacion', 'numero_serie',
                   'estado_caja']
    search_fields = ['numero_caja', 'sector__sector', 'punto_expedicion', 'marca', 'modelo_fabricacion', 'numero_serie',
                     'estado_caja']

    def colorea_estado_caja(self, obj):
        # color = 'black'
        if obj.estado_caja == 'ABI':
            color = 'orange'
            return format_html('<span style="color: %s"><b> %s </b></span>' %
                               (color, obj.get_estado_caja_display()))
        elif obj.estado_caja == 'CER':
            color = 'green'
            return format_html('<span style="color: %s"><b> %s </b></span>' %
                               (color, obj.get_estado_caja_display()))
        elif obj.estado_caja == 'CLA':
            color = 'red'
            return format_html('<span style="color: %s"><b> %s </b></span>' %
                               (color, obj.get_estado_caja_display()))
        return obj.estado_caja
    colorea_estado_caja.short_description = 'Estado Caja'


# class CajaEstadoAdmin(admin.ModelAdmin):
#     list_display = ('id', 'caja_estado', 'descripcion')
#     list_filter = ['id', 'caja_estado', 'descripcion']
#     search_fields = ['id', 'caja_estado', 'descripcion']


# class CajaUbicacionAdmin(admin.ModelAdmin):
#     list_display = ('id', 'caja_ubicacion', 'descripcion')
#     list_filter = ['id', 'caja_ubicacion', 'descripcion']
#     search_fields = ['id', 'caja_ubicacion', 'descripcion']


class SectorAdmin(admin.ModelAdmin):
    ordering = ['id']
    list_display = ('id', 'sector', 'descripcion', 'operativo', 'deposito')
    list_filter = ['id', 'sector', 'descripcion', 'deposito__deposito']
    search_fields = ['id', 'sector', 'descripcion', 'operativo', 'deposito__deposito']


class DocumentoAdmin(admin.ModelAdmin):
    list_display = ('id', 'documento', 'descripcion')
    list_filter = ['id', 'documento', 'descripcion']
    search_fields = ['id', 'documento', 'descripcion']


class PersonaAdmin(admin.ModelAdmin):
    list_display = ('id', 'persona')
    list_filter = ['id', 'persona']
    search_fields = ['id', 'persona']


# class FormaPagoVentaAdmin(admin.ModelAdmin):
#     list_display = ['id', 'forma_pago_venta']
#     list_display_links = ['forma_pago_venta']
#     list_filter = ['id', 'forma_pago_venta']
#     search_fields = ['id', 'forma_pago_venta']


class FormaPagoCompraAdmin(admin.ModelAdmin):
    list_display = ('id', 'forma_pago_compra', 'plazo_compra')
    list_filter = ['id', 'forma_pago_compra', 'plazo_compra']
    search_fields = ['id', 'forma_pago_compra', 'plazo_compra']


class TipoDepositoAdmin(admin.ModelAdmin):
    ordering = ['id']
    list_display = ['id', 'tipo_deposito', 'descripcion']
    list_display_links = ['tipo_deposito']
    list_filter = ['tipo_deposito', 'descripcion']
    search_fields = ['tipo_deposito', 'descripcion']


class DepositoAdmin(admin.ModelAdmin):
    ordering = ['id']
    list_display = ('id', 'deposito', 'descripcion', 'tipo_deposito')
    list_display_links = ['deposito']
    list_filter = ['deposito', 'descripcion', 'tipo_deposito']
    search_fields = ['deposito', 'descripcion', 'tipo_deposito']


class CategoriaProductoAdmin(admin.ModelAdmin):
    list_display = ('id', 'categoria', 'descripcion')
    list_filter = ['id', 'categoria', 'descripcion']
    search_fields = ['id', 'categoria', 'descripcion']


class SubCategoriaProductoAdmin(admin.ModelAdmin):
    list_display = ('id', 'categoria', 'subcategoria', 'descripcion')
    list_filter = ['id', 'categoria', 'subcategoria', 'descripcion']
    search_fields = ['id', 'categoria', 'subcategoria', 'descripcion']


class TipoProductoAdmin(admin.ModelAdmin):
    list_display = ('id', 'tipo_producto', 'descripcion')
    list_filter = ['id', 'tipo_producto', 'descripcion']
    search_fields = ['id', 'tipo_producto', 'descripcion']


class UnidadMedidaProductoAdmin(admin.ModelAdmin):
    list_display = ('id', 'unidad_medida_producto', 'descripcion')
    list_filter = ['id', 'unidad_medida_producto', 'descripcion']
    search_fields = ['id', 'unidad_medida_producto', 'descripcion']


class MonedaAdmin(admin.ModelAdmin):
    list_display = ('id', 'codigo_moneda', 'moneda', 'abreviacion_moneda')
    list_filter = ['id', 'codigo_moneda', 'moneda', 'abreviacion_moneda']
    search_fields = ['id', 'codigo_moneda', 'moneda', 'abreviacion_moneda']


class CotizacionAdmin(admin.ModelAdmin):

    readonly_fields = ['fecha_cotizacion']

    list_display = ('id', 'moneda', 'fecha_cotizacion', 'cotizacion')
    list_filter = ['id', 'moneda', 'fecha_cotizacion', 'cotizacion']
    search_fields = ['id', 'moneda', 'fecha_cotizacion', 'cotizacion']


class CodigoPaisTelefonoAdmin(admin.ModelAdmin):
    fields = ('pais', 'codigo_pais_telefono')
    list_display = ('id', 'pais', 'codigo_pais_telefono')
    list_filter = ['id', 'pais', 'codigo_pais_telefono']
    search_fields = ['id', 'pais', 'codigo_pais_telefono']


class CodigoOperadoraTelefonoAdmin(admin.ModelAdmin):
    list_display = ('id', 'codigo_pais_telefono', 'codigo_operadora_telefono', 'tipo_operadora')
    list_filter = ['id', 'codigo_pais_telefono', 'codigo_operadora_telefono', 'tipo_operadora']
    search_fields = ['id', 'codigo_pais_telefono', 'codigo_operadora_telefono', 'tipo_operadora']


class PaisAdmin(admin.ModelAdmin):

    # form = PaisForm

    list_display = ('id', 'pais')
    list_filter = ['id', 'pais']
    search_fields = ['id', 'pais']


class CiudadAdmin(admin.ModelAdmin):
    list_display = ('id', 'pais', 'ciudad')
    list_filter = ['id', 'pais__pais', 'ciudad']
    search_fields = ['id', 'pais__pais', 'ciudad']


class CompraEstadoAdmin(admin.ModelAdmin):
    list_display = ('id', 'estado_compra', 'descripcion')
    list_filter = ['id', 'estado_compra', 'descripcion']
    search_fields = ['id', 'estado_compra', 'descripcion']


class OrdenCompraEstadoAdmin(admin.ModelAdmin):
    list_display = ('id', 'estado_orden_compra', 'descripcion')
    list_filter = ['id', 'estado_orden_compra', 'descripcion']
    search_fields = ['id', 'estado_orden_compra', 'descripcion']


class PedidoEstadoAdmin(admin.ModelAdmin):
    list_display = ('id', 'pedido_estado', 'descripcion')
    list_filter = ['id', 'pedido_estado', 'descripcion']
    search_fields = ['id', 'pedido_estado', 'descripcion']


class VentaEstadoAdmin(admin.ModelAdmin):
    list_display = ('id', 'venta_estado', 'descripcion')
    list_filter = ['id', 'venta_estado', 'descripcion']
    search_fields = ['id', 'venta_estado', 'descripcion']


class TimbradoAdmin(admin.ModelAdmin):
    form = TimbradoForm

    readonly_fields = []

    fieldsets = [
        # ('Empresa', {'fields': ['empresa']}),
        ('Timbrado', {'fields': ['timbrado', 'descripcion_timbrado', 'estado_timbrado']}),
        ('Fechas', {'fields': ['fecha_autorizacion_timbrado', 'fecha_limite_vigencia_timbrado']}),
    ]

    list_display = ['id', 'timbrado', 'descripcion_timbrado', 'estado_timbrado',
                    'fecha_autorizacion_timbrado', 'fecha_limite_vigencia_timbrado']
    list_display_links = ['timbrado']
    list_filter = ['id', 'timbrado', 'descripcion_timbrado', 'estado_timbrado',
                   'fecha_autorizacion_timbrado', 'fecha_limite_vigencia_timbrado']
    search_fields = ['id', 'timbrado', 'descripcion_timbrado', 'estado_timbrado',
                     'fecha_autorizacion_timbrado', 'fecha_limite_vigencia_timbrado']


# class FacturaAdmin(admin.ModelAdmin):
#     list_display = ()
#     list_filter = []
#     search_fields = []


class FacturaVentaAdmin(admin.ModelAdmin):
    list_display = ['id', 'numero_serie', 'caja', 'estado', 'numero_factura_inicial', 'numero_factura_final']
    list_filter = ['numero_serie', 'caja', 'estado']
    search_fields = ['numero_serie', 'caja', 'estado']


class NumeroFacturaVentaAdmin(admin.ModelAdmin):
    list_display = ['id', 'serie', 'numero_factura', 'venta_asociada', 'fecha_hora_uso']
    list_filter = ['serie', 'numero_factura', 'venta_asociada', 'fecha_hora_uso']
    search_fields = ['serie__numero_serie', 'numero_factura', 'venta_asociada', 'fecha_hora_uso']


class TipoMovimientoStockAdmin(admin.ModelAdmin):
    list_display = ('id', 'tipo_movimiento_stock', 'descripcion')
    list_filter = ['id', 'tipo_movimiento_stock', 'descripcion']
    search_fields = ['id', 'tipo_movimiento_stock', 'descripcion']


class TransferenciaStockEstadoAdmin(admin.ModelAdmin):
    list_display = ('id', 'estado_transferencia_stock', 'descripcion')
    list_filter = ['id', 'estado_transferencia_stock', 'descripcion']
    search_fields = ['id', 'estado_transferencia_stock', 'descripcion']

# admin_site = MyAdminSite(name='myadmin')
admin.site.register(ReservaEstado, ReservaEstadoAdmin)
admin.site.register(Mesa, MesaAdmin)
admin.site.register(MesaEstado, MesaEstadoAdmin)
admin.site.register(MesaUbicacion, MesaUbicacionAdmin)
admin.site.register(Caja, CajaAdmin)
# admin.site.register(CajaEstado, CajaEstadoAdmin)
# admin.site.register(CajaUbicacion, CajaUbicacionAdmin)
admin.site.register(Sector, SectorAdmin)
admin.site.register(Documento, DocumentoAdmin)
admin.site.register(Persona, PersonaAdmin)
# admin.site.register(FormaPagoVenta, FormaPagoVentaAdmin)
admin.site.register(FormaPagoCompra, FormaPagoCompraAdmin)
admin.site.register(TipoDeposito, TipoDepositoAdmin)
admin.site.register(Deposito, DepositoAdmin)
admin.site.register(CategoriaProducto, CategoriaProductoAdmin)
admin.site.register(SubCategoriaProducto, SubCategoriaProductoAdmin)
admin.site.register(TipoProducto, TipoProductoAdmin)
admin.site.register(UnidadMedidaProducto, UnidadMedidaProductoAdmin)
admin.site.register(Moneda, MonedaAdmin)
admin.site.register(Cotizacion, CotizacionAdmin)
admin.site.register(CodigoPaisTelefono, CodigoPaisTelefonoAdmin)
admin.site.register(CodigoOperadoraTelefono, CodigoOperadoraTelefonoAdmin)
admin.site.register(Pais, PaisAdmin)
admin.site.register(Ciudad, CiudadAdmin)
admin.site.register(CompraEstado, CompraEstadoAdmin)
admin.site.register(OrdenCompraEstado, OrdenCompraEstadoAdmin)
admin.site.register(PedidoEstado, PedidoEstadoAdmin)
admin.site.register(VentaEstado, VentaEstadoAdmin)
admin.site.register(Timbrado, TimbradoAdmin)
admin.site.register(FacturaVenta, FacturaVentaAdmin)
admin.site.register(NumeroFacturaVenta, NumeroFacturaVentaAdmin)
admin.site.register(TipoMovimientoStock, TipoMovimientoStockAdmin)
admin.site.register(TransferenciaStockEstado, TransferenciaStockEstadoAdmin)
admin.site.register(TipoFacturaCompra)