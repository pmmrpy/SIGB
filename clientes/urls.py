from django.conf.urls import url
from .import views
# from views import ClienteAutocomplete

urlpatterns = [
    # url(r'^cliente-autocomplete/$', ClienteAutocomplete.as_view(), name='cliente-autocomplete'),
    url(regex=r'^$', view=views.index, name='index'),
    url(r'^cliente/(?P<cliente_id>\d+)/edit/$', views.cliente_edit, name='cliente_edit'),
    url(r'^cliente/(?P<cliente_id>\d+)/$', views.cliente_detalle, name='cliente_detalle'),
    url(r'^cliente/new/$', views.cliente_nuevo, name='cliente_nuevo'),

    # Geraldo reports
    url(r'reserva-report/(?P<pk>\d+)/$', views.reserva_report, name='reserva_report'),
]