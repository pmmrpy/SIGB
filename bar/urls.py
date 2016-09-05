__author__ = 'pmmr'

from django.conf.urls import url
from bar.autocomplete import CiudadAutocomplete, PaisAutocomplete, CategoriaProductoAutocomplete, \
    SubCategoriaProductoAutocomplete, CodigoPaisTelefonoAutocomplete, CodigoOperadoraTelefonoAutocomplete
# from bar.views import *


urlpatterns = [
    url(r'^ciudad-autocomplete/$', CiudadAutocomplete.as_view(), name='ciudad-autocomplete'),
    url(r'^pais-autocomplete/$', PaisAutocomplete.as_view(), name='pais-autocomplete'),
    url(r'^categoria_producto-autocomplete/$', CategoriaProductoAutocomplete.as_view(),
        name='categoria_producto-autocomplete'),
    url(r'^subcategoria_producto-autocomplete/$', SubCategoriaProductoAutocomplete.as_view(),
        name='subcategoria_producto-autocomplete'),
    url(r'^codigo_pais_telefono-autocomplete/$', CodigoPaisTelefonoAutocomplete.as_view(),
        name='codigo_pais_telefono-autocomplete'),
    url(r'^codigo_operadora_telefono-autocomplete/$', CodigoOperadoraTelefonoAutocomplete.as_view(),
        name='codigo_operadora_telefono-autocomplete'),
]