__author__ = 'pmmr'

from django.conf.urls import url
from bar.autocomplete import CiudadAutocomplete
from bar.views import *


urlpatterns = [
    url(r'^ciudad-autocomplete/$', CiudadAutocomplete.as_view(), name='ciudad-autocomplete'),
]