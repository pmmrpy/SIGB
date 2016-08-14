__author__ = 'pmmr'

from django.conf.urls import url
from .import views

urlpatterns = [
    url(r'orden-compra-report/$', views.ordencompra_report, name='ordenescompras_report'),
    url(r'graphic-report/$', views.graphic_report, name='graphic_report'),
    url(r'master-report/$', views.master_report, name='master_report'),
]