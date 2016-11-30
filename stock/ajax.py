import json
from django.http.response import HttpResponse
from bar.models import UnidadMedidaProducto
from stock.models import Producto, ProductoVenta, Insumo, InventarioDeposito

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


def get_producto_venta_detalle(request):
    if request.method == 'GET':
        id_producto = request.GET.get('id_producto', False)
        response_data = {}
        if id_producto:
            producto = ProductoVenta.objects.get(pk=id_producto)
            # response_data.update({'unidad_medida_producto_id': producto.unidad_medida_compra_id})
            # response_data.update({'unidad_medida_producto_display': str(producto.unidad_medida_compra.get_unidad_medida_producto_display())})
            response_data.update({'producto': str(producto)})
            response_data.update({'precio_venta': str(producto.precio_venta)})

        return HttpResponse(
            json.dumps(response_data),
            content_type="application/json"
        )


def get_insumo_producto_compuesto_detalle(request):

    # import pdb
    # pdb.set_trace()

    if request.method == 'GET':
        id_insumo = request.GET.get('id_insumo', False)
        response_data = {}

        if id_insumo is not False:
            try:
                insumo = Insumo.objects.get(pk=id_insumo)
            except Insumo.DoesNotExist:
                insumo = None

            if insumo is not None:
                response_data.update({'insumo': str(insumo)})
                response_data.update({'unidad_medida': insumo.unidad_medida_id})
                response_data.update({'costo_promedio_insumo': str(insumo.get_costo_promedio_por_unidad())})

        else:
                response_data.update({'insumo': ''})
                response_data.update({'unidad_medida': ''})
                response_data.update({'costo_promedio_insumo': '0'})

        return HttpResponse(
            json.dumps(response_data),
            content_type="application/json"
        )


def get_cant_existente_producto_por_deposito(request):

    # import pdb
    # pdb.set_trace()

    if request.method == 'GET':
        id_producto = request.GET.get('id_producto', False)
        response_data = {}

        if id_producto is not False:
            try:
                producto = Producto.objects.get(pk=id_producto)
                stock = InventarioDeposito.objects.get(pk=id_producto)
            except Producto.DoesNotExist:
                producto = None
                stock = None
            except InventarioDeposito.DoesNotExist:
                producto = Producto.objects.get(pk=id_producto)
                stock = None

            if producto is not None and stock is not None:
                response_data.update({'producto': unicode(producto.producto)})

                unidad_medida = UnidadMedidaProducto.objects.get(unidad_medida_producto='UN')
                if producto.tipo_producto == 'VE':
                    unidad_medida = producto.unidad_medida_compra_id
                elif producto.tipo_producto == 'IN':
                    unidad_medida = producto.unidad_medida_contenido_id

                response_data.update({'unidad_medida_id': unidad_medida})
                response_data.update({'cant_exist_dce': str(stock.cant_exist_dce)})
                response_data.update({'cant_exist_dbp': str(stock.cant_exist_dbp)})
                response_data.update({'cant_exist_dba': str(stock.cant_exist_dba)})
                response_data.update({'cant_exist_dco': str(stock.cant_exist_dco)})
                response_data.update({'cant_exist_dbi': str(stock.cant_exist_dbi)})
                response_data.update({'cant_existente': str(stock.cant_existente)})
            elif producto is not None and stock is None:
                response_data.update({'producto': unicode(producto.producto)})
                response_data.update({'unidad_medida_id': ''})
                response_data.update({'cant_exist_dce': '0'})
                response_data.update({'cant_exist_dbp': '0'})
                response_data.update({'cant_exist_dba': '0'})
                response_data.update({'cant_exist_dco': '0'})
                response_data.update({'cant_exist_dbi': '0'})
                response_data.update({'cant_existente': '0'})
            else:
                response_data.update({'producto': ''})
                response_data.update({'unidad_medida_id': ''})
                response_data.update({'cant_exist_dce': '0'})
                response_data.update({'cant_exist_dbp': '0'})
                response_data.update({'cant_exist_dba': '0'})
                response_data.update({'cant_exist_dco': '0'})
                response_data.update({'cant_exist_dbi': '0'})
                response_data.update({'cant_existente': '0'})

        else:
            response_data.update({'producto': ''})
            response_data.update({'unidad_medida_id': ''})
            response_data.update({'cant_exist_dce': '0'})
            response_data.update({'cant_exist_dbp': '0'})
            response_data.update({'cant_exist_dba': '0'})
            response_data.update({'cant_exist_dco': '0'})
            response_data.update({'cant_exist_dbi': '0'})
            response_data.update({'cant_existente': '0'})

        return HttpResponse(
            json.dumps(response_data),
            content_type="application/json"
        )