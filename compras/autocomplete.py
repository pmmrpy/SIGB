from compras.models import LineaCreditoProveedor

__author__ = 'pmmr'

from dal import autocomplete
from django.db.models import Q
from .models import Proveedor


class ProveedorAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        if not self.request.user.is_authenticated():
            return Proveedor.objects.none()
        qs = Proveedor.objects.all()

        if self.q:
            qs = qs.filter(Q(proveedor__icontains=self.q) | Q(proveedor__istartswith=self.q))
        return qs.order_by('proveedor')


class ProveedorOrdenCompraAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        if not self.request.user.is_authenticated():
            return Proveedor.objects.none()
        qs = Proveedor.objects.all()

        lineas_queryset = LineaCreditoProveedor.objects.filter(estado_linea_credito_proveedor='DEL')
        proveedores_id = [l.proveedor.pk for l in lineas_queryset]
        qs = qs.filter(pk__in=proveedores_id)

        if self.q:
            qs = qs.filter(Q(proveedor__icontains=self.q) | Q(proveedor__istartswith=self.q))
        return qs.order_by('proveedor')