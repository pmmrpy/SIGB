__author__ = 'pmmr'

from ventas.ajax import get_reserva
from django.conf.urls import url
from .import views
from compras.autocomplete import ProveedorAutocomplete, ProveedorOrdenCompraAutocomplete, OrdenCompraCompraAutocomplete

urlpatterns = [
    # # Geraldo reports
    url(r'pedido-report/(?P<pk>\d+)/$', views.pedido_report, name='pedido_report'),
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
