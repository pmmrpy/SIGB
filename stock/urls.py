__author__ = 'pmmr'

from stock.ajax import get_producto_detalle, get_producto_venta_detalle, get_insumo_producto_compuesto_detalle, \
    get_cant_existente_producto_por_deposito
from django.conf.urls import url
from .import views
from compras.autocomplete import ProveedorAutocomplete, ProveedorOrdenCompraAutocomplete

urlpatterns = [
    url(r'^get_producto_detalle/$', get_producto_detalle, name='get_producto_detalle'),
    url(r'^get_producto_venta_detalle/$', get_producto_venta_detalle, name='get_producto_venta_detalle'),
    url(r'^get_insumo_producto_compuesto_detalle/$', get_insumo_producto_compuesto_detalle, name='get_insumo_producto_compuesto_detalle'),
    url(r'^get_cant_existente_producto_por_deposito/$', get_cant_existente_producto_por_deposito, name='get_cant_existente_producto_por_deposito'),
]