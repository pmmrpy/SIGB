__author__ = 'pmmr'

from dal import autocomplete
from django.db.models import Q
from clientes.models import ClienteDocumento


class ClienteDocumentoAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):

        import pdb
        pdb.set_trace()

        if not self.request.user.is_authenticated():
            return ClienteDocumento.objects.none()
        qs = ClienteDocumento.objects.all()
        cliente_id = self.forwarded.get('cliente_factura', None)
        # print pais_id

        if cliente_id:
            qs = qs.filter(cliente_id=cliente_id)

        # if self.q:
        #     qs = qs.filter(Q(ciudad__icontains=self.q) | Q(ciudad__istartswith=self.q))

            return qs.order_by('tipo_documento_id')
        else:
            return ClienteDocumento.objects.none()
        # return qs