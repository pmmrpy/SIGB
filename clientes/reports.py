# coding=utf-8
import locale

from django.utils import timezone
from clientes.models import ClienteTelefono


locale.setlocale(locale.LC_ALL, '')

__author__ = 'pmmr'

import os
cur_dir = os.path.dirname(os.path.abspath(__file__))
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# from models import OrdenCompra, OrdenCompraDetalle, Proveedor

from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm
from reportlab.lib.colors import red, darkgreen
from reportlab.lib.enums import TA_RIGHT, TA_CENTER, TA_LEFT

from geraldo import Report, landscape, ReportBand, ObjectValue, SystemField, BAND_WIDTH, Label, SubReport, Image, \
    FIELD_ACTION_SUM, Line


class ReservaReport(Report):
    title = u'Confirmación de Reserva'
    author = 'Pedro Molas'

    page_size = landscape(A4)
    margin_left = 4*cm
    margin_top = 3*cm
    margin_right = 3*cm
    margin_bottom = 2*cm

    class band_detail(ReportBand):
        height = 11*cm
        margin_top=0.5*cm
        # margin_bottom=0.5*cm
        # queryset_string = '%(object)s.ordencompradetalle_set.all()',

        elements = [
            SystemField(expression=u'Asunción, %(now:%d de %B de %Y)s.', top=0.3*cm, width=BAND_WIDTH, style={'fontSize': 12, 'alignment': TA_CENTER}),
            Label(text=u"Nro. de Reserva:", top=-1*cm, left=17.5*cm, width=5*cm,
                  style={'fontName': 'Helvetica-Bold', 'fontSize': 12, 'wordWrap': True, 'borderWidth': 1,
                         'borderColor': red, 'borderPadding': 5, 'borderRadius': 5, 'alignment': TA_LEFT}),
            ObjectValue(attribute_name='id', top=-1*cm, left=-0.4*cm, width=BAND_WIDTH,
                        style={'fontName': 'Helvetica-Bold', 'fontSize': 12, 'alignment': TA_RIGHT}),

            Label(text=u'Datos del Cliente', top=1*cm, left=0.3*cm, style={'fontName': 'Helvetica-Bold', 'fontSize': 14, 'alignment': TA_LEFT}),
            Line(left=0.3*cm, top=1.6*cm, right=10*cm, bottom=1.6*cm),
            Label(text=u'RECIBIMOS DE:', top=2*cm, left=0.3*cm, style={'fontName': 'Helvetica-Bold'}),
            ObjectValue(attribute_name='cliente.nombre_completo', top=2*cm, left=3.5*cm, width=BAND_WIDTH),

            Label(text=u'CON DOCUMENTO:', top=2.7*cm, left=0.3*cm, style={'fontName': 'Helvetica-Bold'}),
            ObjectValue(attribute_name='cliente_documento_reserva', top=2.7*cm, left=4*cm, width=BAND_WIDTH),

            Label(text=u'DIRECCIÓN:', top=3.4*cm, left=0.3*cm, style={'fontName': 'Helvetica-Bold'}),
            ObjectValue(attribute_name='cliente.direccion', top=3.4*cm, left=3*cm, width=BAND_WIDTH),

            Label(text=u'CIUDAD:', top=4.1*cm, left=0.3*cm, style={'fontName': 'Helvetica-Bold'}),
            ObjectValue(attribute_name='cliente.ciudad', top=4.1*cm, left=2.3*cm, width=BAND_WIDTH),

            Label(text=u'PAÍS:', top=4.1*cm, left=6*cm, style={'fontName': 'Helvetica-Bold'}),
            ObjectValue(attribute_name='cliente.pais', top=4.1*cm, left=7.5*cm, width=BAND_WIDTH),

            Label(text=u'TELÉFONO:', top=4.8*cm, left=0.3*cm, style={'fontName': 'Helvetica-Bold'}),
            ObjectValue(attribute_name='cliente', top=4.8*cm, left=3*cm, width=BAND_WIDTH,
                        get_value=lambda instance: " - ".join(['%s%s%s' % (t.codigo_pais_telefono.codigo_pais_telefono, t.codigo_operadora_telefono.codigo_operadora_telefono, t.telefono) for t in ClienteTelefono.objects.filter(cliente_id=instance.cliente.pk)]) if instance.cliente is not None else 'N/A'),

            Label(text=u'MAIL:', top=5.5*cm, left=0.3*cm, style={'fontName': 'Helvetica-Bold'}),
            ObjectValue(attribute_name='cliente.email', top=5.5*cm, left=2*cm, width=BAND_WIDTH),

            Label(text=u'Datos de la Reserva', top=6.5*cm, left=0.3*cm, style={'fontName': 'Helvetica-Bold', 'fontSize': 14, 'alignment': TA_LEFT}),
            Line(left=0.3*cm, top=7.1*cm, right=10*cm, bottom=7.1*cm),

            Label(text=u'Estado Reserva:', top=7.5*cm, left=15*cm, width=6*cm,
                  style={'fontName': 'Helvetica-Bold', 'fontSize': 12, 'wordWrap': True, 'borderWidth': 1,
                         'borderColor': red, 'borderPadding': 4, 'borderRadius': 5, 'alignment': TA_LEFT}),
            ObjectValue(attribute_name='estado', top=7.55*cm, left=18.5*cm, width=BAND_WIDTH),

            Label(text=u'FECHA:', top=7.5*cm, left=0.3*cm, style={'fontName': 'Helvetica-Bold'}),
            ObjectValue(attribute_name='fecha_hora_reserva', top=7.5*cm, left=2*cm, width=BAND_WIDTH,
                        get_value=lambda instance: timezone.localtime(instance.fecha_hora_reserva).date().strftime('%d/%m/%Y')),

            Label(text=u'HORA:', top=7.5*cm, left=5*cm, style={'fontName': 'Helvetica-Bold'}),
            ObjectValue(attribute_name='fecha_hora_reserva', top=7.5*cm, left=6.5*cm, width=BAND_WIDTH,
                        get_value=lambda instance: timezone.localtime(instance.fecha_hora_reserva).time().strftime('%H:%M')),

            Label(text=u'MONTO ENTREGA:', top=8.2*cm, left=0.3*cm, style={'fontName': 'Helvetica-Bold'}),
            ObjectValue(attribute_name='pago', top=8.2*cm, left=4*cm, width=BAND_WIDTH,
                        get_value=lambda instance: '%s Gs.' % '{0:n}'.format(instance.pago)),

            Label(text=u'CANTIDAD DE PERSONAS:', top=8.9*cm, left=0.3*cm, style={'fontName': 'Helvetica-Bold'}),
            ObjectValue(attribute_name='cantidad_personas', top=8.9*cm, left=5.5*cm, width=BAND_WIDTH),

            Label(text=u'UBICACIÓN:', top=9.6*cm, left=0.3*cm, style={'fontName': 'Helvetica-Bold'}),
            ObjectValue(attribute_name='mesas', top=9.6*cm, left=3*cm, width=BAND_WIDTH,
                        get_value=lambda instance: " - ".join([str(m.nombre_mesa) for m in instance.mesas.all()])),

            Label(text=u'RECIBIDO POR:', top=10.3*cm, left=0.3*cm, style={'fontName': 'Helvetica-Bold'}),
            ObjectValue(attribute_name='usuario_registro', top=10.3*cm, left=3.5*cm, width=BAND_WIDTH,
                        get_value=lambda instance: instance.usuario_registro.usuario.empleado.nombre_completo if instance.usuario_registro is not None else 'N/A'),

            # Label(text=u'Motivo Cancelación:', top=11*cm, left=0.3*cm, style={'fontName': 'Helvetica-Bold'}),
            # ObjectValue(attribute_name='motivo_cancelacion', top=11*cm, left=3.9*cm, width=BAND_WIDTH,
            #             get_value=lambda instance: instance.motivo_cancelacion if instance.motivo_cancelacion is not None else 'N/A'),
            #
            # Label(text=u'Cancelado por:', top=11*cm, left=15.5*cm, style={'fontName': 'Helvetica-Bold'}),
            # ObjectValue(attribute_name='usuario_cancelacion', top=11*cm, left=18.1*cm, width=BAND_WIDTH,
            #             get_value=lambda instance: instance.usuario_cancelacion if instance.usuario_cancelacion is not None else 'N/A'),
            #
            # Label(text=u'Observ. Canc.:', top=11.7*cm, left=0.3*cm, style={'fontName': 'Helvetica-Bold'}),
            # ObjectValue(attribute_name='observaciones_cancelacion', top=11.7*cm, left=3*cm, width=BAND_WIDTH,
            #             get_value=lambda instance: instance.observaciones_cancelacion if instance.observaciones_cancelacion is not None else 'N/A'),
            #
            # Label(text=u'Fecha/hora Canc.:', top=11.7*cm, left=15*cm, style={'fontName': 'Helvetica-Bold'}),
            # ObjectValue(attribute_name='fecha_hora_cancelacion', top=11.7*cm, left=18.1*cm,
            #             get_value=lambda instance: timezone.localtime(instance.fecha_hora_cancelacion).strftime('%d/%m/%Y %H:%M') if instance.fecha_hora_cancelacion is not None else 'N/A'),

            Label(text=u'* OBS: Documento válido como Recibo de Dinero.', top=11.2*cm, left=0.3*cm, width=BAND_WIDTH, style={'fontSize': 8, 'alignment': TA_LEFT}),
        ]

        borders={'top': True, 'bottom': True, 'left': True, 'right': True, 'borderWidth': 5, 'borderColor': darkgreen, 'borderPadding': 5, 'borderRadius': 5}

    class band_page_header(ReportBand):
        height = 2*cm
        elements = [
            SystemField(expression='%(report_title)s', top=0.5*cm, left=0, width=BAND_WIDTH,
                        style={'fontName': 'Helvetica-Bold', 'fontSize': 18, 'alignment': TA_CENTER}),
            Image(left=0.1*cm, top=0.1*cm, width=5*cm, height=3*cm,
                  filename=os.path.join(BASE_DIR, "static/compras/empresa/logo_Kilk.JPG")),
        ]
        borders = {'bottom': True}

    class band_page_footer(ReportBand):
        height = 1*cm
        elements = [
                Label(text='SIGB Reportes', top=0.3*cm, left=0.3*cm),
                SystemField(expression=u'Pagina %(page_number)d de %(page_count)d', top=0.1*cm, width=BAND_WIDTH,
                            style={'alignment': TA_CENTER}),
                SystemField(expression=u'Impreso el %(now:%d de %B de %Y)s a las %(now:%H:%M)s', top=0.3*cm, left=-0.2*cm,
                    width=BAND_WIDTH, style={'alignment': TA_RIGHT}),
                ]
        borders = {'top': True}