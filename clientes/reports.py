# coding=utf-8
import locale

from django.utils import timezone


locale.setlocale(locale.LC_ALL, '')

__author__ = 'pmmr'

import os
cur_dir = os.path.dirname(os.path.abspath(__file__))
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# from models import OrdenCompra, OrdenCompraDetalle, Proveedor

from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm
from reportlab.lib.colors import red
from reportlab.lib.enums import TA_RIGHT, TA_CENTER, TA_LEFT

from geraldo import Report, landscape, ReportBand, ObjectValue, SystemField, BAND_WIDTH, Label, SubReport, Image, \
    FIELD_ACTION_SUM


# class SubReporte(SubReport):
#     def __init__(self):
#         super(SubReporte, self).__init__()
#         self.get_queryset = lambda self, parent_object:


class ReservaReport(Report):
    title = 'Confirmacion de Reserva'
    author = 'Pedro Molas'

    page_size = landscape(A4)
    margin_left = 1.5*cm
    margin_top = 0.5*cm
    margin_right = 1.5*cm
    margin_bottom = 0.5*cm

    class band_detail(ReportBand):
        height = 4.5*cm
        margin_top=0.5*cm
        # margin_bottom=0.5*cm
        # queryset_string = '%(object)s.ordencompradetalle_set.all()',

        # elements = [
        #     # Ocultar el Nro. Compra, visualizar solo el Nro. Orden Compra
        #     # Label(text="Nro. Compra:", top=0.3*cm, left=20*cm, width=6.5*cm,
        #     #       style={'fontName': 'Helvetica-Bold', 'fontSize': 12, 'wordWrap': True, 'borderWidth': 1,
        #     #              'borderColor': red, 'borderPadding': 5, 'borderRadius': 5, 'alignment': TA_LEFT}),
        #     # ObjectValue(attribute_name='numero_compra', top=0.3*cm, left=-0.2*cm, width=BAND_WIDTH,
        #     #             style={'fontName': 'Helvetica-Bold', 'fontSize': 12, 'alignment': TA_RIGHT}),
        #     Label(text="Nro. Orden Compra:", top=0.3*cm, left=20*cm, width=6.5*cm,
        #           style={'fontName': 'Helvetica-Bold', 'fontSize': 12, 'wordWrap': True, 'borderWidth': 1,
        #                  'borderColor': red, 'borderPadding': 5, 'borderRadius': 5, 'alignment': TA_LEFT}),
        #     ObjectValue(attribute_name='numero_orden_compra', top=0.3*cm, left=-0.2*cm, width=BAND_WIDTH,
        #                 style={'fontName': 'Helvetica-Bold', 'fontSize': 12, 'alignment': TA_RIGHT}),
        #
        #     Label(text='Proveedor:', top=0.3*cm, left=0.3*cm, style={'fontName': 'Helvetica-Bold'}),
        #     ObjectValue(attribute_name='proveedor', top=0.3*cm, left=2.3*cm, width=BAND_WIDTH),
        #
        #     Label(text='RUC:', top=0.3*cm, left=10*cm, style={'fontName': 'Helvetica-Bold'}),
        #     ObjectValue(attribute_name='proveedor.ruc', top=0.3*cm, left=11*cm),
        #     Label(text='-', top=0.3*cm, left=12.7*cm),
        #     ObjectValue(attribute_name='proveedor.digito_verificador', top=0.3*cm, left=12.9*cm),
        #
        #     Label(text='Direccion:', top=1.0*cm, left=0.3*cm, style={'fontName': 'Helvetica-Bold'}),
        #     ObjectValue(attribute_name='proveedor.direccion', top=1.0*cm, left=2.1*cm, width=11*cm),  # width=BAND_WIDTH
        #
        #     Label(text='Pais:', top=1.0*cm, left=13*cm, style={'fontName': 'Helvetica-Bold'}),
        #     ObjectValue(attribute_name='proveedor.pais', top=1.0*cm, left=14*cm, width=BAND_WIDTH),
        #
        #     Label(text='Ciudad:', top=1.0*cm, left=16*cm, style={'fontName': 'Helvetica-Bold'}),
        #     ObjectValue(attribute_name='proveedor.ciudad', top=1.0*cm, left=17.4*cm, width=BAND_WIDTH),
        #
        #     Label(text='Fecha/hora Compra:', top=1.7*cm, left=0.3*cm, style={'fontName': 'Helvetica-Bold'}),
        #     ObjectValue(attribute_name='fecha_compra', top=1.7*cm, left=3.9*cm,
        #                 get_value=lambda instance: timezone.localtime(instance.fecha_compra).strftime('%d/%m/%Y %H:%M')),
        #
        #     # Label(text='Fecha/hora Entrega:', top=1.7*cm, left=9*cm, style={'fontName': 'Helvetica-Bold'}),
        #     # ObjectValue(attribute_name='fecha_entrega_orden_compra', top=1.7*cm, left=12.5*cm,
        #     #             get_value=lambda instance: timezone.localtime(instance.fecha_entrega_orden_compra).strftime('%d/%m/%Y %H:%M')),
        #
        #     Label(text='Forma de Pago:', top=1.7*cm, left=10*cm, style={'fontName': 'Helvetica-Bold'}),
        #     ObjectValue(attribute_name='numero_orden_compra.forma_pago_orden_compra', top=1.7*cm, left=12.8*cm, width=BAND_WIDTH),
        #
        #     Label(text='Numero de Factura:', top=2.4*cm, left=0.3*cm, style={'fontName': 'Helvetica-Bold'}),
        #     ObjectValue(attribute_name='numero_factura_compra', top=2.4*cm, left=3.7*cm, width=BAND_WIDTH),
        #
        #     Label(text='Tipo Factura:', top=2.4*cm, left=8*cm, style={'fontName': 'Helvetica-Bold'}),
        #     ObjectValue(attribute_name='tipo_factura_compra', top=2.4*cm, left=10.3*cm, width=BAND_WIDTH),
        #
        #     Label(text='Fecha Factura:', top=2.4*cm, left=15*cm, style={'fontName': 'Helvetica-Bold'}),
        #     ObjectValue(attribute_name='fecha_factura_compra', top=2.4*cm, left=17.6*cm),
        #                 # get_value=lambda instance: instance.fecha_factura_compra.strftime('%d/%m/%Y')),
        #
        #     Label(text='Elaborado por:', top=2.4*cm, left=21.5*cm, style={'fontName': 'Helvetica-Bold'}),
        #     ObjectValue(attribute_name='usuario_registro_compra', top=2.4*cm, left=24.1*cm, width=BAND_WIDTH),
        #
        #     Label(text='Estado Compra:', top=3.1*cm, left=0.3*cm, width=11*cm,
        #           style={'fontName': 'Helvetica-Bold', 'fontSize': 12, 'wordWrap': True, 'borderWidth': 1,
        #                  'borderColor': red, 'borderPadding': 4, 'borderRadius': 5, 'alignment': TA_LEFT}),
        #     ObjectValue(attribute_name='estado_compra', top=3.15*cm, left=3.7*cm, width=BAND_WIDTH),
        #
        #     Label(text='Motivo Cancelacion:', top=3.1*cm, left=12*cm, style={'fontName': 'Helvetica-Bold'}),
        #     ObjectValue(attribute_name='motivo_cancelacion', top=3.1*cm, left=15.5*cm, width=BAND_WIDTH,
        #                 get_value=lambda instance: instance.motivo_cancelacion if instance.motivo_cancelacion is not None else 'N/A'),
        #
        #     Label(text='Cancelado por:', top=3.1*cm, left=21.5*cm, style={'fontName': 'Helvetica-Bold'}),
        #     ObjectValue(attribute_name='usuario_cancelacion', top=3.1*cm, left=24.1*cm, width=BAND_WIDTH,
        #                 get_value=lambda instance: instance.usuario_cancelacion if instance.usuario_cancelacion is not None else 'N/A'),
        #
        #     Label(text='Observ. Canc.:', top=3.8*cm, left=0.3*cm, style={'fontName': 'Helvetica-Bold'}),
        #     ObjectValue(attribute_name='observaciones_cancelacion', top=3.8*cm, left=3*cm, width=BAND_WIDTH,
        #                 get_value=lambda instance: instance.observaciones_cancelacion if instance.observaciones_cancelacion is not None else 'N/A'),
        #
        #     Label(text='Fecha/hora Canc.:', top=3.8*cm, left=20.8*cm, style={'fontName': 'Helvetica-Bold'}),
        #     ObjectValue(attribute_name='fecha_hora_cancelacion', top=3.8*cm, left=24*cm,
        #                 get_value=lambda instance: timezone.localtime(instance.fecha_hora_cancelacion).strftime('%d/%m/%Y %H:%M') if instance.fecha_hora_cancelacion is not None else 'N/A'),
        # ]

        borders = {'bottom': True}

    class band_page_header(ReportBand):
        height = 2*cm
        elements = [
            SystemField(expression='%(report_title)s', top=0.5*cm, left=0, width=BAND_WIDTH,
                        style={'fontName': 'Helvetica-Bold', 'fontSize': 18, 'alignment': TA_CENTER}),
            SystemField(expression=u'Pagina %(page_number)d de %(page_count)d', top=0.1*cm, width=BAND_WIDTH,
                        style={'alignment': TA_RIGHT}),
            Image(left=0.1*cm, top=0.1*cm, width=5*cm, height=3*cm,
                  filename=os.path.join(BASE_DIR, "static/compras/empresa/logo_Kilk.JPG")),
        ]
        borders = {'bottom': True}

    class band_page_footer(ReportBand):
        height = 0.5*cm
        elements = [
                Label(text='SIGB Reportes', top=0.1*cm),
                SystemField(expression=u'Impreso el %(now:%d %b de %Y)s a las %(now:%H:%M)s', top=0.1*cm,
                    width=BAND_WIDTH, style={'alignment': TA_RIGHT}),
                ]
        borders = {'top': True}

    # subreports = [
    #     SubReport(
    #         # queryset_string = '%(object)s.compradetalle_set.all()',
    #         queryset_string = '%(object)s.compradetalle_set.all().raw("SELECT *, Row_Number() Over (Order By detalle.id) AS fila FROM compras_compradetalle detalle where detalle.numero_compra_id = %%s", [%(object)s.pk])',
    #         band_header = ReportBand(
    #             height=1*cm,
    #             elements=[
    #                 Label(text='Item', top=0.3*cm, left=0.3*cm, style={'fontName': 'Helvetica-Bold'}),
    #                 Label(text='Producto', top=0.3*cm, left=1.5*cm, style={'fontName': 'Helvetica-Bold'}),
    #                 Label(text='Precio', top=0.3*cm, left=16*cm, style={'fontName': 'Helvetica-Bold'}),
    #                 Label(text='Un. Med. Compra', top=0.3*cm, left=18*cm, style={'fontName': 'Helvetica-Bold'}),
    #                 Label(text='Cantidad', top=0.3*cm, left=22*cm, style={'fontName': 'Helvetica-Bold'}),
    #                 Label(text='Total', top=0.3*cm, left=25*cm, style={'fontName': 'Helvetica-Bold'}),
    #                 ],
    #             borders={'top': True, 'bottom': True, 'left': True, 'right': True},
    #             # borders = {'bottom': Line(stroke_color=red, stroke_width=3)}
    #         ),
    #         band_detail = ReportBand(
    #             height=1*cm,
    #             # width=12*cm,
    #             elements=[
    #                 ObjectValue(attribute_name='fila', top=0.3*cm, left=0.3*cm),
    #                 ObjectValue(attribute_name='producto_compra', top=0.3*cm, left=1.5*cm, width=BAND_WIDTH),
    #                 ObjectValue(attribute_name='precio_producto_compra', top=0.3*cm, left=16*cm,
    #                             get_value=lambda instance: '{0:n}'.format(instance.precio_producto_compra)),
    #                 ObjectValue(attribute_name='unidad_medida_compra', top=0.3*cm, left=18*cm),
    #                 ObjectValue(attribute_name='cantidad_producto_compra', top=0.3*cm, left=22*cm,
    #                             get_value=lambda instance: '{0:n}'.format(instance.cantidad_producto_compra)),
    #                 ObjectValue(attribute_name='total_producto_compra', top=0.3*cm, left=25*cm,
    #                             get_value=lambda instance: '{0:n}'.format(instance.total_producto_compra)),
    #                 ],
    #             borders={'left': True, 'right': True},
    #         ),
    #         band_footer = ReportBand(
    #             height=1*cm,
    #             elements=[
    #                 Label(text='Total Compra', top=0.3*cm, left=18*cm, style={'fontName': 'Helvetica-Bold'}),
    #                 ObjectValue(attribute_name='total_producto_compra', top=0.15*cm, left=-1*cm, width=BAND_WIDTH,
    #                             action=FIELD_ACTION_SUM, display_format='%s',  # '{0:n}'.format(int('s')),
    #                             style={'fontName': 'Helvetica-Bold', 'fontSize': 16, 'textColor': red, 'alignment': TA_RIGHT}),
    #                 ],
    #             borders={'top': True, 'bottom': True, 'left': True, 'right': True},
    #         ),
    #     ),
    # ]