__author__ = 'pmmr'

from django import forms
from ventas.models import Pedido, PedidoDetalle


#class PedidoDetalleForm(forms.ModelForm):
    # Validar que el Producto seleccionado perteneza a la categoria de "VE - Para la venta".