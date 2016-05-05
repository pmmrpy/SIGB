from django.contrib import admin

# Register your models here.
# from bar.forms import PaisForm
from .models import ReservaEstado, Mesa, MesaEstado, MesaUbicacion, Caja, CajaEstado, CajaUbicacion, Documento, \
    FormaPagoVenta, FormaPagoCompra, TipoDeposito, CategoriaProducto, TipoProducto, Moneda, Cotizacion, CodigoPaisTelefono, \
    CodigoCiudadOperadoraTelefono, Pais, Ciudad


# class MyAdminSite(admin.AdminSite):
#     site_header = 'SIGB Admin'
#     site_title ='SIGB Admin'


class ReservaEstadoAdmin(admin.ModelAdmin):
    list_display = ('id', 'reserva_estado', 'descripcion')
    list_filter = ['id', 'reserva_estado', 'descripcion']
    search_fields = ['id', 'reserva_estado', 'descripcion']


class MesaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'ubicacion', 'estado')
    list_filter = ['id', 'nombre', 'ubicacion', 'estado']
    search_fields = ['id', 'nombre', 'ubicacion', 'estado']


class MesaEstadoAdmin(admin.ModelAdmin):
    list_display = ('id', 'mesa_estado', 'descripcion')
    list_filter = ['id', 'mesa_estado', 'descripcion']
    search_fields = ['id', 'mesa_estado', 'descripcion']


class MesaUbicacionAdmin(admin.ModelAdmin):
    list_display = ('id', 'ubicacion', 'descripcion')
    list_filter = ['id', 'ubicacion', 'descripcion']
    search_fields = ['id', 'ubicacion', 'descripcion']


class CajaAdmin(admin.ModelAdmin):
    list_display = ('id', 'numero', 'ubicacion', 'estado')
    list_filter = ['id', 'numero', 'ubicacion', 'estado']
    search_fields = ['id', 'numero', 'ubicacion', 'estado']


class CajaEstadoAdmin(admin.ModelAdmin):
    list_display = ('id', 'caja_estado', 'descripcion')
    list_filter = ['id', 'caja_estado', 'descripcion']
    search_fields = ['id', 'caja_estado', 'descripcion']


class CajaUbicacionAdmin(admin.ModelAdmin):
    list_display = ('id', 'ubicacion', 'descripcion')
    list_filter = ['id', 'ubicacion', 'descripcion']
    search_fields = ['id', 'ubicacion', 'descripcion']


class DocumentoAdmin(admin.ModelAdmin):
    list_display = ('id', 'documento', 'descripcion')
    list_filter = ['id', 'documento', 'descripcion']
    search_fields = ['id', 'documento', 'descripcion']


class FormaPagoVentaAdmin(admin.ModelAdmin):
    list_display = ('id', 'forma_pago_venta')
    list_filter = ['id', 'forma_pago_venta']
    search_fields = ['id', 'forma_pago_venta']


class FormaPagoCompraAdmin(admin.ModelAdmin):
    list_display = ('id', 'forma_pago_compra', 'plazo_compra')
    list_filter = ['id', 'forma_pago_compra', 'plazo_compra']
    search_fields = ['id', 'forma_pago_compra', 'plazo_compra']


class TipoDepositoAdmin(admin.ModelAdmin):
    list_display = ('tipo_deposito', 'descripcion')
    list_filter = ['tipo_deposito', 'descripcion']
    search_fields = ['tipo_deposito', 'descripcion']


class CategoriaProductoAdmin(admin.ModelAdmin):
    list_display = ('id', 'categoria', 'descripcion')
    list_filter = ['id', 'categoria', 'descripcion']
    search_fields = ['id', 'categoria', 'descripcion']


class TipoProductoAdmin(admin.ModelAdmin):
    list_display = ('id', 'tipo_producto', 'descripcion')
    list_filter = ['id', 'tipo_producto', 'descripcion']
    search_fields = ['id', 'tipo_producto', 'descripcion']


class MonedaAdmin(admin.ModelAdmin):
    list_display = ('id', 'codigo_moneda', 'moneda', 'abreviacion_moneda')
    list_filter = ['id', 'codigo_moneda', 'moneda', 'abreviacion_moneda']
    search_fields = ['id', 'codigo_moneda', 'moneda', 'abreviacion_moneda']


class CotizacionAdmin(admin.ModelAdmin):
    list_display = ('id', 'moneda', 'fecha_cotizacion', 'cotizacion')
    list_filter = ['id', 'moneda', 'fecha_cotizacion', 'cotizacion']
    search_fields = ['id', 'moneda', 'fecha_cotizacion', 'cotizacion']


class CodigoPaisTelefonoAdmin(admin.ModelAdmin):
    list_display = ('id', 'codigo_pais_telefono', 'pais')
    list_filter = ['id', 'codigo_pais_telefono', 'pais']
    search_fields = ['id', 'codigo_pais_telefono', 'pais']


class CodigoCiudadOperadoraTelefonoAdmin(admin.ModelAdmin):
    list_display = ('id', 'codigo_pais_telefono', 'codigo_ciudad_operadora_telefono', 'ciudad_operadora')
    list_filter = ['id', 'codigo_pais_telefono', 'codigo_ciudad_operadora_telefono', 'ciudad_operadora']
    search_fields = ['id', 'codigo_pais_telefono', 'codigo_ciudad_operadora_telefono', 'ciudad_operadora']


class PaisAdmin(admin.ModelAdmin):

    # form = PaisForm

    list_display = ('id', 'pais')
    list_filter = ['id', 'pais']
    search_fields = ['id', 'pais']


class CiudadAdmin(admin.ModelAdmin):
    list_display = ('id', 'pais', 'ciudad')
    list_filter = ['id', 'pais', 'ciudad']
    search_fields = ['id', 'pais', 'ciudad']


# admin_site = MyAdminSite(name='myadmin')
admin.site.register(ReservaEstado, ReservaEstadoAdmin)
admin.site.register(Mesa, MesaAdmin)
admin.site.register(MesaEstado, MesaEstadoAdmin)
admin.site.register(MesaUbicacion, MesaUbicacionAdmin)
admin.site.register(Caja, CajaAdmin)
admin.site.register(CajaEstado, CajaEstadoAdmin)
admin.site.register(CajaUbicacion, CajaUbicacionAdmin)
admin.site.register(Documento, DocumentoAdmin)
admin.site.register(FormaPagoVenta, FormaPagoVentaAdmin)
admin.site.register(FormaPagoCompra, FormaPagoCompraAdmin)
admin.site.register(TipoDeposito, TipoDepositoAdmin)
admin.site.register(CategoriaProducto, CategoriaProductoAdmin)
admin.site.register(TipoProducto, TipoProductoAdmin)
admin.site.register(Moneda, MonedaAdmin)
admin.site.register(Cotizacion, CotizacionAdmin)
admin.site.register(CodigoPaisTelefono, CodigoPaisTelefonoAdmin)
admin.site.register(CodigoCiudadOperadoraTelefono, CodigoCiudadOperadoraTelefonoAdmin)
admin.site.register(Pais, PaisAdmin)
admin.site.register(Ciudad, CiudadAdmin)