from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.contrib.auth.models import User, Permission
from geraldo.generators import PDFGenerator
from ventas.reports import PedidoReport, VentaReport, CierreCajaReport
from ventas.models import Pedido, Venta, CierreCaja


def pedido_report(request, pk):

    # import pdb
    # pdb.set_trace()
    # id_orden_compra = 62

    resp = HttpResponse(content_type='application/pdf')
    # nro_orden_compra = request.path.split("/")[-2]
    # id_orden_compra = request.GET.get('id_orden_compra', False)
    pedido = Pedido.objects.filter(numero_pedido=pk)  # 62: CANCELADA - 70: CONFIRMADA - 46: PEP
    # orden_compra_detalle = OrdenCompraDetalle.objects.filter(numero_orden_compra=18)
    # subqueryset = OrdenCompraDetalle.objects.raw('select *, Row_Number() Over (Order By detalle.id) As fila from compras_ordencompradetalle detalle where detalle.numero_orden_compra_id = %s' % pk)
    # report = OrdenCompraReport(queryset=orden_compra, subqueryset=subqueryset)
    report = PedidoReport(queryset=pedido)

    report.generate_by(PDFGenerator, filename=resp)

    return resp


def venta_report(request, pk):
    resp = HttpResponse(content_type='application/pdf')
    venta = Venta.objects.filter(id=pk)  # 62: CANCELADA - 70: CONFIRMADA - 46: PEP
    report = VentaReport(queryset=venta)
    report.generate_by(PDFGenerator, filename=resp)
    return resp


def cierre_caja_report(request, pk):

    # import pdb
    # pdb.set_trace()

    resp = HttpResponse(content_type='application/pdf')
    cierre = CierreCaja.objects.filter(id=pk)  # 62: CANCELADA - 70: CONFIRMADA - 46: PEP
    report = CierreCajaReport(queryset=cierre)
    report.generate_by(PDFGenerator, filename=resp)
    return resp