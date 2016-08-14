__author__ = 'pmmr'

from controlcenter import Dashboard, widgets
from clientes.models import Cliente


class ClienteItemList(widgets.ItemList):
    model = Cliente
    list_display = ['id', 'nombres', 'apellidos', 'direccion', 'pais', 'ciudad', 'email']


class MyDashboard(Dashboard):
    widgets = (
        ClienteItemList,
    )