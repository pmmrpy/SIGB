__author__ = 'pmmr'

from dal import autocomplete
from django.db.models import Q
from bar.models import Pais, Ciudad


class CiudadAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        if not self.request.user.is_authenticated():
            return Ciudad.objects.none()
        qs = Ciudad.objects.all()
        # pais = self.forwarded.get('pais', None)
        #
        # if pais:
        #     qs = qs.filter(pais__pais=pais)

        if self.q:
            qs = qs.filter(Q(ciudad__icontais=self.q) | Q(ciudad__istartswith=self.q))
        # return qs.order_by('ciudad')
        return qs