__author__ = 'pmmr'

from compras.ajax import get_linea_credito, get_orden_compra
from django.conf.urls import url
from .import views
from compras.autocomplete import ProveedorAutocomplete, ProveedorOrdenCompraAutocomplete, OrdenCompraCompraAutocomplete

urlpatterns = [
    url(r'orden-compra-report/$', views.ordencompra_report, name='ordenescompras_report'),
    url(r'graphic-report/$', views.graphic_report, name='graphic_report'),
    url(r'master-report/$', views.master_report, name='master_report'),
    url(r'^proveedor-autocomplete/$', ProveedorAutocomplete.as_view(), name='proveedor-autocomplete'),
    url(r'^proveedor-orden-compra-autocomplete/$', ProveedorOrdenCompraAutocomplete.as_view(),
        name='proveedor-orden-compra-autocomplete'),
    url(r'^ordencompra-compra-autocomplete/$', OrdenCompraCompraAutocomplete.as_view(),
        name='ordencompra-compra-autocomplete'),
    url(r'^get_linea_credito/$', get_linea_credito, name='get_linea_credito'),
    url(r'^get_orden_compra/$', get_orden_compra, name='get_orden_compra'),
]