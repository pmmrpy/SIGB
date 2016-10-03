__author__ = 'pmmr'

import json
from django.http.response import HttpResponse
from clientes.models import Reserva


def get_reserva(request):

    # import pdb
    # pdb.set_trace()

    if request.method == 'GET':
        id_reserva = request.GET.get('id_reserva', False)
        print 'get_reserva.id_reserva: ', id_reserva
        response_data = {}

        try:
            reserva = Reserva.objects.get(pk=id_reserva)
        except Reserva.DoesNotExist:
            reserva = None
        # cliente = Cliente.objects.get(pk=reserva.cliente)

        if id_reserva and reserva is not None:
            response_data.update({'cliente': {'id': str(reserva.cliente.pk), 'nombre_cliente': str(reserva.cliente.nombre_completo)}})
            response_data.update({'monto_entrega': str(reserva.pago) or '0'})
            response_data.update({'mesas': [{'id': m.pk, 'descripcion': str(m)} for m in reserva.mesas.all()]})
        else:
            response_data.update({'cliente': {'id': '', 'nombre_cliente': ''}})
            response_data.update({'monto_entrega': '0'})
            response_data.update({'mesas': ''})

        # print response_data

        return HttpResponse(
            json.dumps(response_data),
            content_type="application/json"
        )