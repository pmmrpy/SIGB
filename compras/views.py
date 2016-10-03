from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.contrib.auth.models import User, Permission
from geraldo.generators import PDFGenerator
from compras.reports import ListadoOrdenesCompraReport, GraphicsReport, MasterReport, OrdenCompraReport, OrdenPagoReport, \
    CompraReport
from compras.models import OrdenCompra, OrdenCompraDetalle, Proveedor, OrdenPago, Compra


def orden_compra_report(request, pk):

    # import pdb
    # pdb.set_trace()
    # id_orden_compra = 62

    resp = HttpResponse(content_type='application/pdf')
    # nro_orden_compra = request.path.split("/")[-2]
    # id_orden_compra = request.GET.get('id_orden_compra', False)
    orden_compra = OrdenCompra.objects.filter(numero_orden_compra=pk)  # 62: CANCELADA - 70: CONFIRMADA - 46: PEP
    # orden_compra_detalle = OrdenCompraDetalle.objects.filter(numero_orden_compra=18)
    # subqueryset = OrdenCompraDetalle.objects.raw('select *, Row_Number() Over (Order By detalle.id) As fila from compras_ordencompradetalle detalle where detalle.numero_orden_compra_id = %s' % pk)
    # report = OrdenCompraReport(queryset=orden_compra, subqueryset=subqueryset)
    report = OrdenCompraReport(queryset=orden_compra)

    report.generate_by(PDFGenerator, filename=resp)

    return resp


def compra_report(request, pk):
    resp = HttpResponse(content_type='application/pdf')

    compra = Compra.objects.filter(numero_compra=pk)  # 107: ENTREGADA - 111: CANCELADA - 56: PENDIENTE
    report = CompraReport(queryset=compra)

    report.generate_by(PDFGenerator, filename=resp)

    return resp


def orden_pago_report(request, pk):
    resp = HttpResponse(content_type='application/pdf')

    orden_pago = OrdenPago.objects.filter(numero_orden_pago=pk)  # 15: CONFIRMADA - 17: CANCELADA - 21: PENDIENTE - 13: ANULADA
    report = OrdenPagoReport(queryset=orden_pago)

    report.generate_by(PDFGenerator, filename=resp)

    return resp


def listado_ordenes_compra_report(request):
    resp = HttpResponse(content_type='application/pdf')

    ordenes = OrdenCompra.objects.order_by('fecha_orden_compra')
    report = ListadoOrdenesCompraReport(queryset=ordenes)

    report.generate_by(PDFGenerator, filename=resp)

    return resp


# ======================================================================================================================
def graphic_report(request):
    resp = HttpResponse(content_type='application/pdf')

    report = GraphicsReport()
    report.generate_by(PDFGenerator, filename=resp)

    return resp


def master_report(request):
    resp = HttpResponse(content_type='application/pdf')

    queryset = User.objects.order_by('username')
    report = MasterReport(queryset=queryset)
    report.generate_by(PDFGenerator, filename=resp)

    return resp