__author__ = 'pmmr'

import json
import pdb
from django.http.response import HttpResponse
from compras.models import Proveedor
from stock.models import Producto


def get_linea_credito(request):
    if request.method == 'GET':
        id_proveedor = request.GET.get('id_proveedor', False)
        print id_proveedor, 'hola'
        response_data = {}
        if id_proveedor:
            proveedor = Proveedor.objects.get(pk=id_proveedor)
            print proveedor, 'proveedor'
            response_data.update({'linea_credito': proveedor.lineacreditoproveedor and str(proveedor.lineacreditoproveedor.disponible_linea_credito_proveedor) or '0'})
            print response_data

        return HttpResponse(
            json.dumps(response_data),
            content_type="application/json"
        )
