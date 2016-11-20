# coding=utf-8
from decimal import Decimal
from re import sub
from django.utils import timezone
from geraldo.utils import FIELD_ACTION_DISTINCT_COUNT, FIELD_ACTION_MIN
import locale
from compras.models import Empresa, OrdenPagoDetalle

locale.setlocale(locale.LC_ALL, '')

__author__ = 'pmmr'

import os
cur_dir = os.path.dirname(os.path.abspath(__file__))
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

from models import Pedido
from django.contrib.auth.models import User, Permission

from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm
from reportlab.lib.colors import navy, yellow, red, purple, orange, green, white, blue
from reportlab.lib.enums import TA_RIGHT, TA_CENTER, TA_JUSTIFY, TA_LEFT

from geraldo import Report, landscape, ReportBand, ObjectValue, SystemField, BAND_WIDTH, Label, ReportGroup, \
    SubReport, RoundRect, Rect, Line, Circle, Arc, Ellipse, Image, FIELD_ACTION_COUNT, FIELD_ACTION_SUM, FIELD_ACTION_VALUE


# class SubReporte(SubReport):
#     def __init__(self):
#         super(SubReporte, self).__init__()
#         self.get_queryset = lambda self, parent_object:


class PedidoReport(Report):
    title = 'Pedido de Cliente'
    author = 'Pedro Molas'

    page_size = A4
    margin_left = 1.5*cm
    margin_top = 0.5*cm
    margin_right = 1.5*cm
    margin_bottom = 0.5*cm

    # def __init__(self, queryset=None,subqueryset=None):
    #     super(OrdenCompraReport, self).__init__(queryset)
    #     self.subqueryset = subqueryset

    class band_detail(ReportBand):
        height = 4.5*cm
        margin_top=0.5*cm
        # margin_bottom=0.5*cm
        # queryset_string = '%(object)s.ordencompradetalle_set.all()',
        elements = [
            Label(text="Nro. Pedido:", top=0.2*cm, left=13*cm, width=4.8*cm,
                  style={'fontName': 'Helvetica-Bold', 'fontSize': 12, 'wordWrap': True, 'borderWidth': 1,
                         'borderColor': red, 'borderPadding': 4, 'borderRadius': 5, 'alignment': TA_LEFT}),
            ObjectValue(attribute_name='numero_pedido', top=0.2*cm, left=-0.2*cm, width=BAND_WIDTH,
                        style={'fontName': 'Helvetica-Bold', 'fontSize': 12, 'alignment': TA_RIGHT}),

            Label(text='Reserva:', top=0.3*cm, left=0.1*cm, style={'fontName': 'Helvetica-Bold'}),
            ObjectValue(attribute_name='reserva.id', top=0.3*cm, left=1.6*cm,
                        get_value=lambda instance: instance.reserva.id if instance.reserva.id is not None else 'N/A'),

            Label(text='Fecha Reserva:', top=0.3*cm, left=2.6*cm, style={'fontName': 'Helvetica-Bold'}),
            ObjectValue(attribute_name='reserva.fecha_hora_reserva', top=0.3*cm, left=5.3*cm,
                        get_value=lambda instance: timezone.localtime(instance.reserva.fecha_hora_reserva).strftime('%d/%m/%Y %H:%M') if instance.reserva.fecha_hora_reserva is not None else 'N/A'),

            Label(text='ID Cliente:', top=1*cm, left=0.1*cm, style={'fontName': 'Helvetica-Bold'}),
            ObjectValue(attribute_name='reserva.cliente.id', top=1*cm, left=1.9*cm,
                        get_value=lambda instance: instance.reserva.cliente.id if instance.reserva.cliente.id is not None else 'N/A'),

            Label(text='Nombre Cliente:', top=1*cm, left=2.7*cm, style={'fontName': 'Helvetica-Bold'}),
            ObjectValue(attribute_name='reserva.cliente.nombre_completo', top=1*cm, left=5.5*cm, width=BAND_WIDTH,
                        get_value=lambda instance: instance.reserva.cliente.nombre_completo if instance.reserva.cliente.nombre_completo is not None else 'N/A'),

            Label(text='Monto Entrega:', top=1*cm, left=13*cm, style={'fontName': 'Helvetica-Bold'}),
            ObjectValue(attribute_name='reserva.pago', top=1*cm, left=15.7*cm, width=11*cm,
                        get_value=lambda instance: '{0:n}'.format(instance.reserva.pago) if instance.reserva.pago is not None else 'N/A'),

            # Label(text='Pais:', top=1.0*cm, left=13*cm, style={'fontName': 'Helvetica-Bold'}),
            # ObjectValue(attribute_name='proveedor_orden_compra.pais', top=1.0*cm, left=14*cm, width=BAND_WIDTH),
            #
            # Label(text='Ciudad:', top=1.0*cm, left=16*cm, style={'fontName': 'Helvetica-Bold'}),
            # ObjectValue(attribute_name='proveedor_orden_compra.ciudad', top=1.0*cm, left=17.4*cm, width=BAND_WIDTH),

            Label(text='Fecha/hora Pedido:', top=1.7*cm, left=0.1*cm, style={'fontName': 'Helvetica-Bold'}),
            ObjectValue(attribute_name='fecha_hora_pedido', top=1.7*cm, left=3.5*cm,
                        get_value=lambda instance: timezone.localtime(instance.fecha_hora_pedido).strftime('%d/%m/%Y %H:%M')),

            # Label(text='Fecha/hora Entrega:', top=1.7*cm, left=9*cm, style={'fontName': 'Helvetica-Bold'}),
            # ObjectValue(attribute_name='fecha_entrega_orden_compra', top=1.7*cm, left=12.5*cm,
            #             get_value=lambda instance: timezone.localtime(instance.fecha_entrega_orden_compra).strftime('%d/%m/%Y %H:%M')),
            #
            # Label(text='Forma de Pago:', top=1.7*cm, left=16*cm, style={'fontName': 'Helvetica-Bold'}),
            # ObjectValue(attribute_name='forma_pago_orden_compra', top=1.7*cm, left=18.8*cm, width=BAND_WIDTH),
            #
            # Label(text='Lugar de Entrega:', top=2.4*cm, left=0.3*cm, style={'fontName': 'Helvetica-Bold'}),
            # Label(text=u'Triskel S.A. (Kilkenny)', top=2.4*cm, left=3.4*cm),
            #
            # Label(text='Direccion:', top=2.4*cm, left=8*cm, style={'fontName': 'Helvetica-Bold'}),
            # Label(text=u'Malutin y España - Paseo Carmelitas', top=2.4*cm, left=9.8*cm, width=BAND_WIDTH),
            #
            # Label(text='Telefono:', top=2.4*cm, left=16.5*cm, style={'fontName': 'Helvetica-Bold'}),
            # Label(text=u'595 985 155179', top=2.4*cm, left=18.2*cm, width=BAND_WIDTH),

            Label(text='Atendido por:', top=2.4*cm, left=13.5*cm, style={'fontName': 'Helvetica-Bold'}),
            ObjectValue(attribute_name='mozo_pedido', top=2.4*cm, left=15.9*cm, width=BAND_WIDTH),

            Label(text='Estado Pedido:', top=3.1*cm, left=0.1*cm, width=5*cm,
                  style={'fontName': 'Helvetica-Bold', 'fontSize': 12, 'wordWrap': True, 'borderWidth': 1,
                         'borderColor': red, 'borderPadding': 4, 'borderRadius': 5, 'alignment': TA_LEFT}),
            ObjectValue(attribute_name='estado_pedido', top=3.15*cm, left=3.2*cm, width=BAND_WIDTH),

            Label(text='Motivo Canc.:', top=3.1*cm, left=6*cm, style={'fontName': 'Helvetica-Bold'}),
            ObjectValue(attribute_name='motivo_cancelacion', top=3.1*cm, left=8.4*cm, width=BAND_WIDTH,
                        get_value=lambda instance: instance.motivo_cancelacion if instance.motivo_cancelacion is not None else 'N/A'),

            Label(text='Cancelado por:', top=3.1*cm, left=13.5*cm, style={'fontName': 'Helvetica-Bold'}),
            ObjectValue(attribute_name='usuario_cancelacion', top=3.1*cm, left=16.1*cm, width=BAND_WIDTH,
                        get_value=lambda instance: instance.usuario_cancelacion if instance.usuario_cancelacion is not None else 'N/A'),

            Label(text='Observ. Canc.:', top=3.8*cm, left=0.1*cm, style={'fontName': 'Helvetica-Bold'}),
            ObjectValue(attribute_name='observaciones_cancelacion', top=3.8*cm, left=2.7*cm, width=BAND_WIDTH,
                        get_value=lambda instance: instance.observaciones_cancelacion if instance.observaciones_cancelacion is not None else 'N/A'),

            Label(text='Fecha/hora Canc.:', top=3.8*cm, left=12*cm, style={'fontName': 'Helvetica-Bold'}),
            ObjectValue(attribute_name='fecha_hora_cancelacion', top=3.8*cm, left=15.1*cm,
                        get_value=lambda instance: timezone.localtime(instance.fecha_hora_cancelacion).strftime('%d/%m/%Y %H:%M') if instance.fecha_hora_cancelacion is not None else 'N/A'),
        ]

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

    subreports = [
        SubReport(
            # queryset_string = '%(object)s.ordencompradetalle_set.all()',
            queryset_string = '%(object)s.pedidodetalle_set.all().raw("SELECT *, Row_Number() Over (Order By detalle.id) AS fila FROM ventas_pedidodetalle detalle where detalle.procesado=True and detalle.anulado=False and detalle.pedido_id = %%s", [%(object)s.pk])',
            band_header = ReportBand(
                height=1*cm,
                elements=[
                    Label(text='Item', top=0.3*cm, left=0.3*cm, style={'fontName': 'Helvetica-Bold'}),
                    Label(text='Producto', top=0.3*cm, left=1.5*cm, style={'fontName': 'Helvetica-Bold'}),
                    Label(text='Precio', top=0.3*cm, left=9.5*cm, style={'fontName': 'Helvetica-Bold'}),
                    # Label(text='Un. Med. Compra', top=0.3*cm, left=12*cm, style={'fontName': 'Helvetica-Bold'}),
                    Label(text='Cantidad', top=0.3*cm, left=11.2*cm, style={'fontName': 'Helvetica-Bold'}),
                    Label(text='Total', top=0.3*cm, left=13.5*cm, style={'fontName': 'Helvetica-Bold'}),
                    Label(text='Fecha/hora', top=0.3*cm, left=15*cm, style={'fontName': 'Helvetica-Bold'}),
                    ],
                borders={'top': True, 'bottom': True, 'left': True, 'right': True},
                # borders = {'bottom': Line(stroke_color=red, stroke_width=3)}
            ),
            band_detail = ReportBand(
                height=1*cm,
                # width=12*cm,
                elements=[
                    ObjectValue(attribute_name='fila', top=0.3*cm, left=0.3*cm),
                    ObjectValue(attribute_name='producto_pedido', top=0.3*cm, left=1.5*cm, width=7.5*cm),
                    ObjectValue(attribute_name='precio_producto_pedido', top=0.3*cm, left=9.5*cm,
                                get_value=lambda instance: '{0:n}'.format(instance.precio_producto_pedido)),
                    # ObjectValue(attribute_name='unidad_medida_orden_compra', top=0.3*cm, left=18*cm),
                    ObjectValue(attribute_name='cantidad_producto_pedido', top=0.3*cm, left=11.5*cm,
                                get_value=lambda instance: '{0:n}'.format(instance.cantidad_producto_pedido)),
                    ObjectValue(attribute_name='total_producto_pedido', top=0.3*cm, left=13.5*cm,
                                get_value=lambda instance: '{0:n}'.format(instance.total_producto_pedido)),
                    ObjectValue(attribute_name='fecha_pedido_detalle', top=0.3*cm, left=15*cm,
                                get_value=lambda instance: timezone.localtime(instance.fecha_pedido_detalle).strftime('%d/%m/%Y %H:%M') if instance.fecha_pedido_detalle is not None else 'N/A'),
                    ],
                borders={'left': True, 'right': True},
            ),
            band_footer = ReportBand(
                height=1*cm,
                elements=[
                    Label(text='Total Pedido', top=0.3*cm, left=10*cm, style={'fontName': 'Helvetica-Bold'}),
                    ObjectValue(attribute_name='total_producto_pedido', top=0.15*cm, left=-1*cm, width=BAND_WIDTH,
                                action=FIELD_ACTION_SUM,  # display_format='%s permissions found',
                                style={'fontName': 'Helvetica-Bold', 'fontSize': 16, 'textColor': red, 'alignment': TA_RIGHT}),
                    ],
                borders={'top': True, 'bottom': True, 'left': True, 'right': True},
            ),
        ),
    ]


class VentaReport(Report):
    title = 'Factura de Venta'
    author = 'Pedro Molas'

    page_size = A4
    margin_left = 1.5*cm
    margin_top = 0.5*cm
    margin_right = 1.5*cm
    margin_bottom = 0.5*cm

    # def __init__(self, queryset=None,subqueryset=None):
    #     super(OrdenCompraReport, self).__init__(queryset)
    #     self.subqueryset = subqueryset

    class band_detail(ReportBand):
        height = 4.5*cm
        margin_top=0.5*cm
        # margin_bottom=0.5*cm
        # queryset_string = '%(object)s.ordencompradetalle_set.all()',
        # elements = [
        #     Label(text="Nro. Pedido:", top=0.2*cm, left=13*cm, width=4.8*cm,
        #           style={'fontName': 'Helvetica-Bold', 'fontSize': 12, 'wordWrap': True, 'borderWidth': 1,
        #                  'borderColor': red, 'borderPadding': 4, 'borderRadius': 5, 'alignment': TA_LEFT}),
        #     ObjectValue(attribute_name='numero_pedido', top=0.2*cm, left=-0.2*cm, width=BAND_WIDTH,
        #                 style={'fontName': 'Helvetica-Bold', 'fontSize': 12, 'alignment': TA_RIGHT}),
        #
        #     Label(text='Reserva:', top=0.3*cm, left=0.1*cm, style={'fontName': 'Helvetica-Bold'}),
        #     ObjectValue(attribute_name='reserva.id', top=0.3*cm, left=1.6*cm,
        #                 get_value=lambda instance: instance.reserva.id if instance.reserva.id is not None else 'N/A'),
        #
        #     Label(text='Fecha Reserva:', top=0.3*cm, left=2.6*cm, style={'fontName': 'Helvetica-Bold'}),
        #     ObjectValue(attribute_name='reserva.fecha_hora_reserva', top=0.3*cm, left=5.3*cm,
        #                 get_value=lambda instance: timezone.localtime(instance.reserva.fecha_hora_reserva).strftime('%d/%m/%Y %H:%M') if instance.reserva.fecha_hora_reserva is not None else 'N/A'),
        #
        #     Label(text='ID Cliente:', top=1*cm, left=0.1*cm, style={'fontName': 'Helvetica-Bold'}),
        #     ObjectValue(attribute_name='reserva.cliente.id', top=1*cm, left=1.9*cm,
        #                 get_value=lambda instance: instance.reserva.cliente.id if instance.reserva.cliente.id is not None else 'N/A'),
        #
        #     Label(text='Nombre Cliente:', top=1*cm, left=2.7*cm, style={'fontName': 'Helvetica-Bold'}),
        #     ObjectValue(attribute_name='reserva.cliente.nombre_completo', top=1*cm, left=5.5*cm, width=BAND_WIDTH,
        #                 get_value=lambda instance: instance.reserva.cliente.nombre_completo if instance.reserva.cliente.nombre_completo is not None else 'N/A'),
        #
        #     Label(text='Monto Entrega:', top=1*cm, left=13*cm, style={'fontName': 'Helvetica-Bold'}),
        #     ObjectValue(attribute_name='reserva.pago', top=1*cm, left=15.7*cm, width=11*cm,
        #                 get_value=lambda instance: '{0:n}'.format(instance.reserva.pago) if instance.reserva.pago is not None else 'N/A'),
        #
        #     # Label(text='Pais:', top=1.0*cm, left=13*cm, style={'fontName': 'Helvetica-Bold'}),
        #     # ObjectValue(attribute_name='proveedor_orden_compra.pais', top=1.0*cm, left=14*cm, width=BAND_WIDTH),
        #     #
        #     # Label(text='Ciudad:', top=1.0*cm, left=16*cm, style={'fontName': 'Helvetica-Bold'}),
        #     # ObjectValue(attribute_name='proveedor_orden_compra.ciudad', top=1.0*cm, left=17.4*cm, width=BAND_WIDTH),
        #
        #     Label(text='Fecha/hora Pedido:', top=1.7*cm, left=0.1*cm, style={'fontName': 'Helvetica-Bold'}),
        #     ObjectValue(attribute_name='fecha_hora_pedido', top=1.7*cm, left=3.5*cm,
        #                 get_value=lambda instance: timezone.localtime(instance.fecha_hora_pedido).strftime('%d/%m/%Y %H:%M')),
        #
        #     # Label(text='Fecha/hora Entrega:', top=1.7*cm, left=9*cm, style={'fontName': 'Helvetica-Bold'}),
        #     # ObjectValue(attribute_name='fecha_entrega_orden_compra', top=1.7*cm, left=12.5*cm,
        #     #             get_value=lambda instance: timezone.localtime(instance.fecha_entrega_orden_compra).strftime('%d/%m/%Y %H:%M')),
        #     #
        #     # Label(text='Forma de Pago:', top=1.7*cm, left=16*cm, style={'fontName': 'Helvetica-Bold'}),
        #     # ObjectValue(attribute_name='forma_pago_orden_compra', top=1.7*cm, left=18.8*cm, width=BAND_WIDTH),
        #     #
        #     # Label(text='Lugar de Entrega:', top=2.4*cm, left=0.3*cm, style={'fontName': 'Helvetica-Bold'}),
        #     # Label(text=u'Triskel S.A. (Kilkenny)', top=2.4*cm, left=3.4*cm),
        #     #
        #     # Label(text='Direccion:', top=2.4*cm, left=8*cm, style={'fontName': 'Helvetica-Bold'}),
        #     # Label(text=u'Malutin y España - Paseo Carmelitas', top=2.4*cm, left=9.8*cm, width=BAND_WIDTH),
        #     #
        #     # Label(text='Telefono:', top=2.4*cm, left=16.5*cm, style={'fontName': 'Helvetica-Bold'}),
        #     # Label(text=u'595 985 155179', top=2.4*cm, left=18.2*cm, width=BAND_WIDTH),
        #
        #     Label(text='Atendido por:', top=2.4*cm, left=13.5*cm, style={'fontName': 'Helvetica-Bold'}),
        #     ObjectValue(attribute_name='mozo_pedido', top=2.4*cm, left=15.9*cm, width=BAND_WIDTH),
        #
        #     Label(text='Estado Pedido:', top=3.1*cm, left=0.1*cm, width=5*cm,
        #           style={'fontName': 'Helvetica-Bold', 'fontSize': 12, 'wordWrap': True, 'borderWidth': 1,
        #                  'borderColor': red, 'borderPadding': 4, 'borderRadius': 5, 'alignment': TA_LEFT}),
        #     ObjectValue(attribute_name='estado_pedido', top=3.15*cm, left=3.2*cm, width=BAND_WIDTH),
        #
        #     Label(text='Motivo Canc.:', top=3.1*cm, left=6*cm, style={'fontName': 'Helvetica-Bold'}),
        #     ObjectValue(attribute_name='motivo_cancelacion', top=3.1*cm, left=8.4*cm, width=BAND_WIDTH,
        #                 get_value=lambda instance: instance.motivo_cancelacion if instance.motivo_cancelacion is not None else 'N/A'),
        #
        #     Label(text='Cancelado por:', top=3.1*cm, left=13.5*cm, style={'fontName': 'Helvetica-Bold'}),
        #     ObjectValue(attribute_name='usuario_cancelacion', top=3.1*cm, left=16.1*cm, width=BAND_WIDTH,
        #                 get_value=lambda instance: instance.usuario_cancelacion if instance.usuario_cancelacion is not None else 'N/A'),
        #
        #     Label(text='Observ. Canc.:', top=3.8*cm, left=0.1*cm, style={'fontName': 'Helvetica-Bold'}),
        #     ObjectValue(attribute_name='observaciones_cancelacion', top=3.8*cm, left=2.7*cm, width=BAND_WIDTH,
        #                 get_value=lambda instance: instance.observaciones_cancelacion if instance.observaciones_cancelacion is not None else 'N/A'),
        #
        #     Label(text='Fecha/hora Canc.:', top=3.8*cm, left=12*cm, style={'fontName': 'Helvetica-Bold'}),
        #     ObjectValue(attribute_name='fecha_hora_cancelacion', top=3.8*cm, left=15.1*cm,
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
    #         # queryset_string = '%(object)s.ordencompradetalle_set.all()',
    #         queryset_string = '%(object)s.pedidodetalle_set.all().raw("SELECT *, Row_Number() Over (Order By detalle.id) AS fila FROM ventas_pedidodetalle detalle where detalle.procesado=True and detalle.anulado=False and detalle.pedido_id = %%s", [%(object)s.pk])',
    #         band_header = ReportBand(
    #             height=1*cm,
    #             elements=[
    #                 Label(text='Item', top=0.3*cm, left=0.3*cm, style={'fontName': 'Helvetica-Bold'}),
    #                 Label(text='Producto', top=0.3*cm, left=1.5*cm, style={'fontName': 'Helvetica-Bold'}),
    #                 Label(text='Precio', top=0.3*cm, left=9.5*cm, style={'fontName': 'Helvetica-Bold'}),
    #                 # Label(text='Un. Med. Compra', top=0.3*cm, left=12*cm, style={'fontName': 'Helvetica-Bold'}),
    #                 Label(text='Cantidad', top=0.3*cm, left=11.2*cm, style={'fontName': 'Helvetica-Bold'}),
    #                 Label(text='Total', top=0.3*cm, left=13.5*cm, style={'fontName': 'Helvetica-Bold'}),
    #                 Label(text='Fecha/hora', top=0.3*cm, left=15*cm, style={'fontName': 'Helvetica-Bold'}),
    #                 ],
    #             borders={'top': True, 'bottom': True, 'left': True, 'right': True},
    #             # borders = {'bottom': Line(stroke_color=red, stroke_width=3)}
    #         ),
    #         band_detail = ReportBand(
    #             height=1*cm,
    #             # width=12*cm,
    #             elements=[
    #                 ObjectValue(attribute_name='fila', top=0.3*cm, left=0.3*cm),
    #                 ObjectValue(attribute_name='producto_pedido', top=0.3*cm, left=1.5*cm, width=7.5*cm),
    #                 ObjectValue(attribute_name='precio_producto_pedido', top=0.3*cm, left=9.5*cm,
    #                             get_value=lambda instance: '{0:n}'.format(instance.precio_producto_pedido)),
    #                 # ObjectValue(attribute_name='unidad_medida_orden_compra', top=0.3*cm, left=18*cm),
    #                 ObjectValue(attribute_name='cantidad_producto_pedido', top=0.3*cm, left=11.5*cm,
    #                             get_value=lambda instance: '{0:n}'.format(instance.cantidad_producto_pedido)),
    #                 ObjectValue(attribute_name='total_producto_pedido', top=0.3*cm, left=13.5*cm,
    #                             get_value=lambda instance: '{0:n}'.format(instance.total_producto_pedido)),
    #                 ObjectValue(attribute_name='fecha_pedido_detalle', top=0.3*cm, left=15*cm,
    #                             get_value=lambda instance: timezone.localtime(instance.fecha_pedido_detalle).strftime('%d/%m/%Y %H:%M') if instance.fecha_pedido_detalle is not None else 'N/A'),
    #                 ],
    #             borders={'left': True, 'right': True},
    #         ),
    #         band_footer = ReportBand(
    #             height=1*cm,
    #             elements=[
    #                 Label(text='Total Pedido', top=0.3*cm, left=10*cm, style={'fontName': 'Helvetica-Bold'}),
    #                 ObjectValue(attribute_name='total_producto_pedido', top=0.15*cm, left=-1*cm, width=BAND_WIDTH,
    #                             action=FIELD_ACTION_SUM,  # display_format='%s permissions found',
    #                             style={'fontName': 'Helvetica-Bold', 'fontSize': 16, 'textColor': red, 'alignment': TA_RIGHT}),
    #                 ],
    #             borders={'top': True, 'bottom': True, 'left': True, 'right': True},
    #         ),
    #     ),
    # ]


class CierreCajaReport(Report):
    title = 'Cierre de Caja'
    author = 'Pedro Molas'

    page_size = A4
    margin_left = 1.5*cm
    margin_top = 0.5*cm
    margin_right = 1.5*cm
    margin_bottom = 0.5*cm

    # def __init__(self, queryset=None,subqueryset=None):
    #     super(OrdenCompraReport, self).__init__(queryset)
    #     self.subqueryset = subqueryset

    class band_detail(ReportBand):
        height = 4.5*cm
        margin_top=0.5*cm
        # margin_bottom=0.5*cm
        # queryset_string = '%(object)s.ordencompradetalle_set.all()',
        # elements = [
        #     Label(text="Nro. Pedido:", top=0.2*cm, left=13*cm, width=4.8*cm,
        #           style={'fontName': 'Helvetica-Bold', 'fontSize': 12, 'wordWrap': True, 'borderWidth': 1,
        #                  'borderColor': red, 'borderPadding': 4, 'borderRadius': 5, 'alignment': TA_LEFT}),
        #     ObjectValue(attribute_name='numero_pedido', top=0.2*cm, left=-0.2*cm, width=BAND_WIDTH,
        #                 style={'fontName': 'Helvetica-Bold', 'fontSize': 12, 'alignment': TA_RIGHT}),
        #
        #     Label(text='Reserva:', top=0.3*cm, left=0.1*cm, style={'fontName': 'Helvetica-Bold'}),
        #     ObjectValue(attribute_name='reserva.id', top=0.3*cm, left=1.6*cm,
        #                 get_value=lambda instance: instance.reserva.id if instance.reserva.id is not None else 'N/A'),
        #
        #     Label(text='Fecha Reserva:', top=0.3*cm, left=2.6*cm, style={'fontName': 'Helvetica-Bold'}),
        #     ObjectValue(attribute_name='reserva.fecha_hora_reserva', top=0.3*cm, left=5.3*cm,
        #                 get_value=lambda instance: timezone.localtime(instance.reserva.fecha_hora_reserva).strftime('%d/%m/%Y %H:%M') if instance.reserva.fecha_hora_reserva is not None else 'N/A'),
        #
        #     Label(text='ID Cliente:', top=1*cm, left=0.1*cm, style={'fontName': 'Helvetica-Bold'}),
        #     ObjectValue(attribute_name='reserva.cliente.id', top=1*cm, left=1.9*cm,
        #                 get_value=lambda instance: instance.reserva.cliente.id if instance.reserva.cliente.id is not None else 'N/A'),
        #
        #     Label(text='Nombre Cliente:', top=1*cm, left=2.7*cm, style={'fontName': 'Helvetica-Bold'}),
        #     ObjectValue(attribute_name='reserva.cliente.nombre_completo', top=1*cm, left=5.5*cm, width=BAND_WIDTH,
        #                 get_value=lambda instance: instance.reserva.cliente.nombre_completo if instance.reserva.cliente.nombre_completo is not None else 'N/A'),
        #
        #     Label(text='Monto Entrega:', top=1*cm, left=13*cm, style={'fontName': 'Helvetica-Bold'}),
        #     ObjectValue(attribute_name='reserva.pago', top=1*cm, left=15.7*cm, width=11*cm,
        #                 get_value=lambda instance: '{0:n}'.format(instance.reserva.pago) if instance.reserva.pago is not None else 'N/A'),
        #
        #     # Label(text='Pais:', top=1.0*cm, left=13*cm, style={'fontName': 'Helvetica-Bold'}),
        #     # ObjectValue(attribute_name='proveedor_orden_compra.pais', top=1.0*cm, left=14*cm, width=BAND_WIDTH),
        #     #
        #     # Label(text='Ciudad:', top=1.0*cm, left=16*cm, style={'fontName': 'Helvetica-Bold'}),
        #     # ObjectValue(attribute_name='proveedor_orden_compra.ciudad', top=1.0*cm, left=17.4*cm, width=BAND_WIDTH),
        #
        #     Label(text='Fecha/hora Pedido:', top=1.7*cm, left=0.1*cm, style={'fontName': 'Helvetica-Bold'}),
        #     ObjectValue(attribute_name='fecha_hora_pedido', top=1.7*cm, left=3.5*cm,
        #                 get_value=lambda instance: timezone.localtime(instance.fecha_hora_pedido).strftime('%d/%m/%Y %H:%M')),
        #
        #     # Label(text='Fecha/hora Entrega:', top=1.7*cm, left=9*cm, style={'fontName': 'Helvetica-Bold'}),
        #     # ObjectValue(attribute_name='fecha_entrega_orden_compra', top=1.7*cm, left=12.5*cm,
        #     #             get_value=lambda instance: timezone.localtime(instance.fecha_entrega_orden_compra).strftime('%d/%m/%Y %H:%M')),
        #     #
        #     # Label(text='Forma de Pago:', top=1.7*cm, left=16*cm, style={'fontName': 'Helvetica-Bold'}),
        #     # ObjectValue(attribute_name='forma_pago_orden_compra', top=1.7*cm, left=18.8*cm, width=BAND_WIDTH),
        #     #
        #     # Label(text='Lugar de Entrega:', top=2.4*cm, left=0.3*cm, style={'fontName': 'Helvetica-Bold'}),
        #     # Label(text=u'Triskel S.A. (Kilkenny)', top=2.4*cm, left=3.4*cm),
        #     #
        #     # Label(text='Direccion:', top=2.4*cm, left=8*cm, style={'fontName': 'Helvetica-Bold'}),
        #     # Label(text=u'Malutin y España - Paseo Carmelitas', top=2.4*cm, left=9.8*cm, width=BAND_WIDTH),
        #     #
        #     # Label(text='Telefono:', top=2.4*cm, left=16.5*cm, style={'fontName': 'Helvetica-Bold'}),
        #     # Label(text=u'595 985 155179', top=2.4*cm, left=18.2*cm, width=BAND_WIDTH),
        #
        #     Label(text='Atendido por:', top=2.4*cm, left=13.5*cm, style={'fontName': 'Helvetica-Bold'}),
        #     ObjectValue(attribute_name='mozo_pedido', top=2.4*cm, left=15.9*cm, width=BAND_WIDTH),
        #
        #     Label(text='Estado Pedido:', top=3.1*cm, left=0.1*cm, width=5*cm,
        #           style={'fontName': 'Helvetica-Bold', 'fontSize': 12, 'wordWrap': True, 'borderWidth': 1,
        #                  'borderColor': red, 'borderPadding': 4, 'borderRadius': 5, 'alignment': TA_LEFT}),
        #     ObjectValue(attribute_name='estado_pedido', top=3.15*cm, left=3.2*cm, width=BAND_WIDTH),
        #
        #     Label(text='Motivo Canc.:', top=3.1*cm, left=6*cm, style={'fontName': 'Helvetica-Bold'}),
        #     ObjectValue(attribute_name='motivo_cancelacion', top=3.1*cm, left=8.4*cm, width=BAND_WIDTH,
        #                 get_value=lambda instance: instance.motivo_cancelacion if instance.motivo_cancelacion is not None else 'N/A'),
        #
        #     Label(text='Cancelado por:', top=3.1*cm, left=13.5*cm, style={'fontName': 'Helvetica-Bold'}),
        #     ObjectValue(attribute_name='usuario_cancelacion', top=3.1*cm, left=16.1*cm, width=BAND_WIDTH,
        #                 get_value=lambda instance: instance.usuario_cancelacion if instance.usuario_cancelacion is not None else 'N/A'),
        #
        #     Label(text='Observ. Canc.:', top=3.8*cm, left=0.1*cm, style={'fontName': 'Helvetica-Bold'}),
        #     ObjectValue(attribute_name='observaciones_cancelacion', top=3.8*cm, left=2.7*cm, width=BAND_WIDTH,
        #                 get_value=lambda instance: instance.observaciones_cancelacion if instance.observaciones_cancelacion is not None else 'N/A'),
        #
        #     Label(text='Fecha/hora Canc.:', top=3.8*cm, left=12*cm, style={'fontName': 'Helvetica-Bold'}),
        #     ObjectValue(attribute_name='fecha_hora_cancelacion', top=3.8*cm, left=15.1*cm,
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
    #         # queryset_string = '%(object)s.ordencompradetalle_set.all()',
    #         queryset_string = '%(object)s.pedidodetalle_set.all().raw("SELECT *, Row_Number() Over (Order By detalle.id) AS fila FROM ventas_pedidodetalle detalle where detalle.procesado=True and detalle.anulado=False and detalle.pedido_id = %%s", [%(object)s.pk])',
    #         band_header = ReportBand(
    #             height=1*cm,
    #             elements=[
    #                 Label(text='Item', top=0.3*cm, left=0.3*cm, style={'fontName': 'Helvetica-Bold'}),
    #                 Label(text='Producto', top=0.3*cm, left=1.5*cm, style={'fontName': 'Helvetica-Bold'}),
    #                 Label(text='Precio', top=0.3*cm, left=9.5*cm, style={'fontName': 'Helvetica-Bold'}),
    #                 # Label(text='Un. Med. Compra', top=0.3*cm, left=12*cm, style={'fontName': 'Helvetica-Bold'}),
    #                 Label(text='Cantidad', top=0.3*cm, left=11.2*cm, style={'fontName': 'Helvetica-Bold'}),
    #                 Label(text='Total', top=0.3*cm, left=13.5*cm, style={'fontName': 'Helvetica-Bold'}),
    #                 Label(text='Fecha/hora', top=0.3*cm, left=15*cm, style={'fontName': 'Helvetica-Bold'}),
    #                 ],
    #             borders={'top': True, 'bottom': True, 'left': True, 'right': True},
    #             # borders = {'bottom': Line(stroke_color=red, stroke_width=3)}
    #         ),
    #         band_detail = ReportBand(
    #             height=1*cm,
    #             # width=12*cm,
    #             elements=[
    #                 ObjectValue(attribute_name='fila', top=0.3*cm, left=0.3*cm),
    #                 ObjectValue(attribute_name='producto_pedido', top=0.3*cm, left=1.5*cm, width=7.5*cm),
    #                 ObjectValue(attribute_name='precio_producto_pedido', top=0.3*cm, left=9.5*cm,
    #                             get_value=lambda instance: '{0:n}'.format(instance.precio_producto_pedido)),
    #                 # ObjectValue(attribute_name='unidad_medida_orden_compra', top=0.3*cm, left=18*cm),
    #                 ObjectValue(attribute_name='cantidad_producto_pedido', top=0.3*cm, left=11.5*cm,
    #                             get_value=lambda instance: '{0:n}'.format(instance.cantidad_producto_pedido)),
    #                 ObjectValue(attribute_name='total_producto_pedido', top=0.3*cm, left=13.5*cm,
    #                             get_value=lambda instance: '{0:n}'.format(instance.total_producto_pedido)),
    #                 ObjectValue(attribute_name='fecha_pedido_detalle', top=0.3*cm, left=15*cm,
    #                             get_value=lambda instance: timezone.localtime(instance.fecha_pedido_detalle).strftime('%d/%m/%Y %H:%M') if instance.fecha_pedido_detalle is not None else 'N/A'),
    #                 ],
    #             borders={'left': True, 'right': True},
    #         ),
    #         band_footer = ReportBand(
    #             height=1*cm,
    #             elements=[
    #                 Label(text='Total Pedido', top=0.3*cm, left=10*cm, style={'fontName': 'Helvetica-Bold'}),
    #                 ObjectValue(attribute_name='total_producto_pedido', top=0.15*cm, left=-1*cm, width=BAND_WIDTH,
    #                             action=FIELD_ACTION_SUM,  # display_format='%s permissions found',
    #                             style={'fontName': 'Helvetica-Bold', 'fontSize': 16, 'textColor': red, 'alignment': TA_RIGHT}),
    #                 ],
    #             borders={'top': True, 'bottom': True, 'left': True, 'right': True},
    #         ),
    #     ),
    # ]