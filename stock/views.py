from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.contrib.auth.models import User, Permission
from geraldo.generators import PDFGenerator
from stock.reports import AjusteInventarioReport
from stock.models import AjusteStock


def ajuste_inventario_report(request, pk):
    resp = HttpResponse(content_type='application/pdf')
    ajuste = AjusteStock.objects.filter(pk=pk)
    report = AjusteInventarioReport(queryset=ajuste)
    report.generate_by(PDFGenerator, filename=resp)
    return resp