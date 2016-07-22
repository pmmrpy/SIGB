from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

from reports import ReportOrdenCompra, GraphicsReport, MasterReport
from geraldo.generators import PDFGenerator
from models import OrdenCompra, OrdenCompraDetalle, Proveedor
from django.contrib.auth.models import User, Permission


def ordencompra_report(request):
    resp = HttpResponse(content_type='application/pdf')

    ordenes = OrdenCompra.objects.order_by('fecha_orden_compra')
    report = ReportOrdenCompra(queryset=ordenes)
    report.generate_by(PDFGenerator, filename=resp)

    return resp


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