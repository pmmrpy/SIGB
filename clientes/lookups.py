__author__ = 'pmmr'

from ajax_select import register, LookupChannel
from .models import Cliente


@register('clientes')
class ClienteLookup(LookupChannel):

    model = Cliente

    def get_query(self, q, request):
        return self.model.objects.filter(nombres__icontains=q).order_by('nombres')

    def format_item_display(self, item):
        return u"<span class='tag'>%s</span>" % item.name