__author__ = 'pmmr'

from stock.ajax import get_producto_detalle, get_producto_venta_detalle
from django.conf.urls import url
from .import views
from compras.autocomplete import ProveedorAutocomplete, ProveedorOrdenCompraAutocomplete

urlpatterns = [
    url(r'^get_producto_detalle/$', get_producto_detalle, name='get_producto_detalle'),
    url(r'^get_producto_venta_detalle/$', get_producto_venta_detalle, name='get_producto_venta_detalle'),
]