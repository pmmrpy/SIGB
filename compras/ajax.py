__author__ = 'pmmr'

import json
import pdb
from django.http.response import HttpResponse
from compras.models import Proveedor, OrdenCompra, OrdenCompraDetalle, CompraDetalle
from bar.models import TipoFacturaCompra
from stock.models import Producto


def get_linea_credito(request):
    if request.method == 'GET':
        id_proveedor = request.GET.get('id_proveedor', False)
        print 'get_linea_credito.id_proveedor: ', id_proveedor
        response_data = {}
        if id_proveedor:
            proveedor = Proveedor.objects.get(pk=id_proveedor)
            print 'Proveedor: ', proveedor
            response_data.update({'linea_credito': proveedor.lineacreditoproveedor and str(proveedor.lineacreditoproveedor.disponible_linea_credito_proveedor) or '0'})
            print response_data

        return HttpResponse(
            json.dumps(response_data),
            content_type="application/json"
        )


def get_orden_compra(request):
    if request.method == 'GET':
        id_orden_compra = request.GET.get('id_orden_compra', False)
        print 'get_orden_compra.id_orden_compra: ', id_orden_compra
        response_data = {}
        if id_orden_compra:
            orden_compra = OrdenCompra.objects.get(pk=id_orden_compra)
            orden_compra_detalle = OrdenCompraDetalle.objects.filter(numero_orden_compra_id=id_orden_compra)

            # for detalle in orden_compra_detalle:
            #     compra_detalle = CompraDetalle(producto_compra_id=detalle.producto_orden_compra_id,  #numero_compra_id=compra_actual.numero_compra,
            #                                    precio_producto_compra=detalle.precio_producto_orden_compra,
            #                                    cantidad_producto_compra=detalle.cantidad_producto_orden_compra,
            #                                    unidad_medida_compra=detalle.unidad_medida_orden_compra,
            #                                    total_producto_compra=detalle.total_producto_orden_compra)

            if orden_compra.forma_pago_orden_compra.forma_pago_compra == 'CO':
                tipo_factura = TipoFacturaCompra.objects.get(tipo_factura_compra='CON')
            else:
                tipo_factura = TipoFacturaCompra.objects.get(tipo_factura_compra='CRE')

            print 'get_orden_compra.orden_compra: ', orden_compra
            print 'get_orden_compra.orden_compra_detalle: ', orden_compra_detalle
            print 'get_orden_compra.tipo_factura: ', tipo_factura

            response_data.update({'proveedor':{'id': str(orden_compra.proveedor_orden_compra.pk),'nombre': str(orden_compra.proveedor_orden_compra)}})
            response_data.update({'linea_credito': orden_compra.proveedor_orden_compra.lineacreditoproveedor and str(orden_compra.proveedor_orden_compra.lineacreditoproveedor.disponible_linea_credito_proveedor) or '0'})
            response_data.update({'tipo_factura': str(tipo_factura)})
            response_data.update({'estado_orden_compra': {'id':str(orden_compra.estado_orden_compra.pk),'nombre':str(orden_compra.estado_orden_compra)}})
            response_data.update({'total_orden_compra': str(orden_compra.total_orden_compra)})
            # response_data.update({'orden_compra_detalle': orden_compra_detalle})

            # response_data.update({'unidad_medida_producto_id': orden_compra_detalle.unidad_medida_compra_id})
            # # response_data.update({'unidad_medida_producto_display': str(producto.unidad_medida_compra.get_unidad_medida_producto_display())})
            # response_data.update({'producto': str(orden_compra_detalle)})
            # response_data.update({'precio_compra': str(orden_compra_detalle.precio_compra)})

            # print response_data

        return HttpResponse(
            json.dumps(response_data),
            content_type="application/json"
        )