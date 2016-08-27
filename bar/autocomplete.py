__author__ = 'pmmr'

from dal import autocomplete
from django.db.models import Q
from bar.models import Pais, Ciudad, CategoriaProducto, SubCategoriaProducto


class PaisAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        if not self.request.user.is_authenticated():
            return Pais.objects.none()
        qs = Pais.objects.all()

        if self.q:
            qs = qs.filter(Q(pais__icontains=self.q) | Q(pais__istartswith=self.q))
        return qs.order_by('pais')


class CiudadAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        if not self.request.user.is_authenticated():
            return Ciudad.objects.none()
        qs = Ciudad.objects.all()
        pais_id = self.forwarded.get('pais', None)
        print self.forwarded

        if pais_id:
            qs = qs.filter(pais__pk=pais_id)

        if self.q:
            qs = qs.filter(Q(ciudad__icontains=self.q) | Q(ciudad__istartswith=self.q))
        return qs.order_by('ciudad')
        # return qs


class CategoriaProductoAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        if not self.request.user.is_authenticated():
            return CategoriaProducto.objects.none()
        qs = CategoriaProducto.objects.all()

        if self.q:
            qs = qs.filter(Q(descripcion__icontains=self.q) | Q(descripcion__istartswith=self.q))
        return qs.order_by('categoria')


class SubCategoriaProductoAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        if not self.request.user.is_authenticated():
            return SubCategoriaProducto.objects.none()
        qs = SubCategoriaProducto.objects.all()
        categoria_id = self.forwarded.get('categoria', None)
        print self.forwarded

        if categoria_id:
            qs = qs.filter(categoria__pk=categoria_id)

        if self.q:
            qs = qs.filter(Q(descripcion__icontains=self.q) | Q(descripcion__istartswith=self.q))
        return qs.order_by('subcategoria')