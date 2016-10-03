__author__ = 'pmmr'

from compras.ajax import get_linea_credito, get_orden_compra
from django.conf.urls import url
from .import views
from compras.autocomplete import ProveedorAutocomplete, ProveedorOrdenCompraAutocomplete, OrdenCompraCompraAutocomplete

urlpatterns = [
    # Geraldo reports
    url(r'orden-compra-report/(?P<pk>\d+)/$', views.orden_compra_report, name='orden_compra_report'),
    url(r'compra-report/(?P<pk>\d+)/$', views.compra_report, name='compra_report'),
    url(r'orden-pago-report/(?P<pk>\d+)/$', views.orden_pago_report, name='orden_pago_report'),
    url(r'listado-ordenes-compra-report/$', views.listado_ordenes_compra_report, name='listado_ordenes_compra_report'),

    url(r'graphic-report/$', views.graphic_report, name='graphic_report'),
    url(r'master-report/$', views.master_report, name='master_report'),

    # autocompletes
    url(r'^proveedor-autocomplete/$', ProveedorAutocomplete.as_view(), name='proveedor-autocomplete'),
    url(r'^proveedor-orden-compra-autocomplete/$', ProveedorOrdenCompraAutocomplete.as_view(),
        name='proveedor-orden-compra-autocomplete'),
    url(r'^ordencompra-compra-autocomplete/$', OrdenCompraCompraAutocomplete.as_view(),
        name='ordencompra-compra-autocomplete'),

    # AJAX
    url(r'^get_linea_credito/$', get_linea_credito, name='get_linea_credito'),
    url(r'^get_orden_compra/$', get_orden_compra, name='get_orden_compra'),
]
