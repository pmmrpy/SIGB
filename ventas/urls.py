__author__ = 'pmmr'

from ventas.ajax import get_reserva, get_cliente, get_apertura_caja, get_pedido
from django.conf.urls import url
from .import views
from ventas.autocomplete import ClienteDocumentoAutocomplete

urlpatterns = [
    # # Geraldo reports
    url(r'pedido-report/(?P<pk>\d+)/$', views.pedido_report, name='pedido_report'),
    url(r'venta-report/(?P<pk>\d+)/$', views.venta_report, name='venta_report'),
    url(r'cierre_caja-report/(?P<pk>\d+)/$', views.cierre_caja_report, name='cierre_caja_report'),

    # autocompletes
    url(r'^clientedocumento-autocomplete/$', ClienteDocumentoAutocomplete.as_view(),
        name='clientedocumento-autocomplete'),

    # AJAX
    url(r'^get_reserva/$', get_reserva, name='get_reserva'),
    url(r'^get_cliente/$', get_cliente, name='get_cliente'),
    url(r'^get_apertura_caja/$', get_apertura_caja, name='get_apertura_caja'),
    url(r'^get_pedido/$', get_pedido, name='get_pedido'),
]
