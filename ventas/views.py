# Create your views here.
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.contrib.auth.models import User, Permission
from geraldo.generators import PDFGenerator
from ventas.reports import PedidoReport, VentaReport, CierreCajaReport
from ventas.models import Pedido, Venta, CierreCaja


def pedido_report(request, pk):
    resp = HttpResponse(content_type='application/pdf')
    pedido = Pedido.objects.filter(numero_pedido=pk)  # 62: CANCELADA - 70: CONFIRMADA - 46: PEP
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