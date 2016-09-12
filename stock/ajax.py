import json
from django.http.response import HttpResponse
from stock.models import Producto

__author__ = 'pmmr'


def get_producto_detalle(request):
    if request.method == 'GET':
        id_producto = request.GET.get('id_producto', False)
        response_data = {}
        if id_producto:
            producto = Producto.objects.get(pk=id_producto)
            response_data.update({'unidad_medida_producto_id': producto.unidad_medida_compra_id})
            # response_data.update({'unidad_medida_producto_display': str(producto.unidad_medida_compra.get_unidad_medida_producto_display())})
            response_data.update({'producto': str(producto)})
            response_data.update({'precio_compra': str(producto.precio_compra)})

        return HttpResponse(
            json.dumps(response_data),
            content_type="application/json"
        )
