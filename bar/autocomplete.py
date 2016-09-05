__author__ = 'pmmr'

from dal import autocomplete
from django.db.models import Q
from bar.models import Pais, Ciudad, CategoriaProducto, SubCategoriaProducto, CodigoPaisTelefono, CodigoOperadoraTelefono


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
        # print pais_id

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


class CodigoPaisTelefonoAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        if not self.request.user.is_authenticated():
            return CodigoPaisTelefono.objects.none()
        qs = CodigoPaisTelefono.objects.all()

        if self.q:
            qs = qs.filter(Q(codigo_pais_telefono__icontains=self.q) | Q(codigo_pais_telefono__istartswith=self.q) |
                           Q(pais__pais__icontains=self.q) | Q(pais__pais__istartswith=self.q))
        return qs.order_by('codigo_pais_telefono', 'pais__pais')


class CodigoOperadoraTelefonoAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        if not self.request.user.is_authenticated():
            return CodigoOperadoraTelefono.objects.none()
        qs = CodigoOperadoraTelefono.objects.all()
        codigo_pais_telefono_id = self.forwarded.get('codigo_pais_telefono', None)
        print self.forwarded

        if codigo_pais_telefono_id:
            qs = qs.filter(codigo_pais_telefono=codigo_pais_telefono_id)

        if self.q:
            qs = qs.filter(Q(codigo_operadora_telefono__icontains=self.q) | Q(codigo_operadora_telefono__istartswith=self.q))
        return qs.order_by('codigo_operadora_telefono')