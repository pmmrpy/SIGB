__author__ = 'pmmr'

from ventas.ajax import get_reserva
from django.conf.urls import url
from .import views
from compras.autocomplete import ProveedorAutocomplete, ProveedorOrdenCompraAutocomplete, OrdenCompraCompraAutocomplete

urlpatterns = [
    # # Geraldo reports
    # url(r'orden-compra-report/$', views.orden_compra_report, name='orden_compra_report'),
    # url(r'compra-report/$', views.compra_report, name='compra_report'),
    # url(r'orden-pago-report/$', views.orden_pago_report, name='orden_pago_report'),
    # url(r'listado-ordenes-compra-report/$', views.listado_ordenes_compra_report, name='listado_ordenes_compra_report'),
    #
    # url(r'graphic-report/$', views.graphic_report, name='graphic_report'),
    # url(r'master-report/$', views.master_report, name='master_report'),
    #
    # # autocompletes
    # url(r'^proveedor-autocomplete/$', ProveedorAutocomplete.as_view(), name='proveedor-autocomplete'),
    # url(r'^proveedor-orden-compra-autocomplete/$', ProveedorOrdenCompraAutocomplete.as_view(),
    #     name='proveedor-orden-compra-autocomplete'),
    # url(r'^ordencompra-compra-autocomplete/$', OrdenCompraCompraAutocomplete.as_view(),
    #     name='ordencompra-compra-autocomplete'),

    # AJAX
    url(r'^get_reserva/$', get_reserva, name='get_reserva'),
]
