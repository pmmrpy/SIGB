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

from models import OrdenCompra, OrdenCompraDetalle, Proveedor
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


class OrdenCompraReport(Report):
    title = 'Orden de Compra'
    author = 'Pedro Molas'

    page_size = landscape(A4)
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
            Label(text="Nro. Orden Compra:", top=0.3*cm, left=20*cm, width=6.5*cm,
                  style={'fontName': 'Helvetica-Bold', 'fontSize': 12, 'wordWrap': True, 'borderWidth': 1,
                         'borderColor': red, 'borderPadding': 6, 'borderRadius': 5, 'alignment': TA_LEFT}),
            ObjectValue(attribute_name='numero_orden_compra', top=0.3*cm, left=-0.2*cm, width=BAND_WIDTH,
                        style={'fontName': 'Helvetica-Bold', 'fontSize': 12, 'alignment': TA_RIGHT}),

            Label(text='Proveedor:', top=0.3*cm, left=0.3*cm, style={'fontName': 'Helvetica-Bold'}),
            ObjectValue(attribute_name='proveedor_orden_compra', top=0.3*cm, left=2.3*cm, width=BAND_WIDTH),

            Label(text='RUC:', top=0.3*cm, left=10*cm, style={'fontName': 'Helvetica-Bold'}),
            ObjectValue(attribute_name='proveedor_orden_compra.ruc', top=0.3*cm, left=11*cm),
            Label(text='-', top=0.3*cm, left=12.7*cm),
            ObjectValue(attribute_name='proveedor_orden_compra.digito_verificador', top=0.3*cm, left=12.9*cm),

            Label(text='Direccion:', top=1.0*cm, left=0.3*cm, style={'fontName': 'Helvetica-Bold'}),
            ObjectValue(attribute_name='proveedor_orden_compra.direccion', top=1.0*cm, left=2.1*cm, width=11*cm),

            Label(text='Pais:', top=1.0*cm, left=13*cm, style={'fontName': 'Helvetica-Bold'}),
            ObjectValue(attribute_name='proveedor_orden_compra.pais', top=1.0*cm, left=14*cm, width=BAND_WIDTH),

            Label(text='Ciudad:', top=1.0*cm, left=16*cm, style={'fontName': 'Helvetica-Bold'}),
            ObjectValue(attribute_name='proveedor_orden_compra.ciudad', top=1.0*cm, left=17.4*cm, width=BAND_WIDTH),

            Label(text='Fecha/hora Ord. Compra:', top=1.7*cm, left=0.3*cm, style={'fontName': 'Helvetica-Bold'}),
            ObjectValue(attribute_name='fecha_orden_compra', top=1.7*cm, left=4.6*cm,
                        get_value=lambda instance: timezone.localtime(instance.fecha_orden_compra).strftime('%d/%m/%Y %H:%M')),

            Label(text='Fecha/hora Entrega:', top=1.7*cm, left=9*cm, style={'fontName': 'Helvetica-Bold'}),
            ObjectValue(attribute_name='fecha_entrega_orden_compra', top=1.7*cm, left=12.5*cm,
                        get_value=lambda instance: timezone.localtime(instance.fecha_entrega_orden_compra).strftime('%d/%m/%Y %H:%M')),

            Label(text='Forma de Pago:', top=1.7*cm, left=16*cm, style={'fontName': 'Helvetica-Bold'}),
            ObjectValue(attribute_name='forma_pago_orden_compra', top=1.7*cm, left=18.8*cm, width=BAND_WIDTH),

            Label(text='Lugar de Entrega:', top=2.4*cm, left=0.3*cm, style={'fontName': 'Helvetica-Bold'}),
            Label(text=u'Triskel S.A. (Kilkenny)', top=2.4*cm, left=3.4*cm),

            Label(text='Direccion:', top=2.4*cm, left=8*cm, style={'fontName': 'Helvetica-Bold'}),
            Label(text=u'Malutin y España - Paseo Carmelitas', top=2.4*cm, left=9.8*cm, width=BAND_WIDTH),

            Label(text='Telefono:', top=2.4*cm, left=16.5*cm, style={'fontName': 'Helvetica-Bold'}),
            Label(text=u'595 985 155179', top=2.4*cm, left=18.2*cm, width=BAND_WIDTH),

            Label(text='Elaborado por:', top=2.4*cm, left=21.5*cm, style={'fontName': 'Helvetica-Bold'}),
            ObjectValue(attribute_name='usuario_registro_orden_compra', top=2.4*cm, left=24.1*cm, width=BAND_WIDTH),

            Label(text='Estado Ord. Compra:', top=3.1*cm, left=0.3*cm, width=11*cm,
                  style={'fontName': 'Helvetica-Bold', 'fontSize': 12, 'wordWrap': True, 'borderWidth': 1,
                         'borderColor': red, 'borderPadding': 4, 'borderRadius': 5, 'alignment': TA_LEFT}),
            ObjectValue(attribute_name='estado_orden_compra', top=3.15*cm, left=4.7*cm, width=BAND_WIDTH),

            Label(text='Motivo Cancelacion:', top=3.1*cm, left=12*cm, style={'fontName': 'Helvetica-Bold'}),
            ObjectValue(attribute_name='motivo_cancelacion', top=3.1*cm, left=15.5*cm, width=BAND_WIDTH,
                        get_value=lambda instance: instance.motivo_cancelacion if instance.motivo_cancelacion is not None else 'N/A'),

            Label(text='Cancelado por:', top=3.1*cm, left=21.5*cm, style={'fontName': 'Helvetica-Bold'}),
            ObjectValue(attribute_name='usuario_cancelacion', top=3.1*cm, left=24.1*cm, width=BAND_WIDTH,
                        get_value=lambda instance: instance.usuario_cancelacion if instance.usuario_cancelacion is not None else 'N/A'),

            Label(text='Observ. Canc.:', top=3.8*cm, left=0.3*cm, style={'fontName': 'Helvetica-Bold'}),
            ObjectValue(attribute_name='observaciones_cancelacion', top=3.8*cm, left=3*cm, width=BAND_WIDTH,
                        get_value=lambda instance: instance.observaciones_cancelacion if instance.observaciones_cancelacion is not None else 'N/A'),

            Label(text='Fecha/hora Canc.:', top=3.8*cm, left=20.8*cm, style={'fontName': 'Helvetica-Bold'}),
            ObjectValue(attribute_name='fecha_hora_cancelacion', top=3.8*cm, left=24*cm,
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
            queryset_string = '%(object)s.ordencompradetalle_set.all().raw("SELECT *, Row_Number() Over (Order By detalle.id) AS fila FROM compras_ordencompradetalle detalle where detalle.numero_orden_compra_id = %%s", [%(object)s.pk])',
            band_header = ReportBand(
                height=1*cm,
                elements=[
                    Label(text='Item', top=0.3*cm, left=0.3*cm, style={'fontName': 'Helvetica-Bold'}),
                    Label(text='Producto', top=0.3*cm, left=1.5*cm, style={'fontName': 'Helvetica-Bold'}),
                    Label(text='Precio', top=0.3*cm, left=16*cm, style={'fontName': 'Helvetica-Bold'}),
                    Label(text='Un. Med. Compra', top=0.3*cm, left=18*cm, style={'fontName': 'Helvetica-Bold'}),
                    Label(text='Cantidad', top=0.3*cm, left=22*cm, style={'fontName': 'Helvetica-Bold'}),
                    Label(text='Total', top=0.3*cm, left=25*cm, style={'fontName': 'Helvetica-Bold'}),
                    ],
                borders={'top': True, 'bottom': True, 'left': True, 'right': True},
                # borders = {'bottom': Line(stroke_color=red, stroke_width=3)}
            ),
            band_detail = ReportBand(
                height=1*cm,
                # width=12*cm,
                elements=[
                    ObjectValue(attribute_name='fila', top=0.3*cm, left=0.3*cm),
                    ObjectValue(attribute_name='producto_orden_compra', top=0.3*cm, left=1.5*cm, width=BAND_WIDTH),
                    ObjectValue(attribute_name='precio_producto_orden_compra', top=0.3*cm, left=16*cm,
                                get_value=lambda instance: '{0:n}'.format(instance.precio_producto_orden_compra)),
                    ObjectValue(attribute_name='unidad_medida_orden_compra', top=0.3*cm, left=18*cm),
                    ObjectValue(attribute_name='cantidad_producto_orden_compra', top=0.3*cm, left=22*cm,
                                get_value=lambda instance: '{0:n}'.format(instance.cantidad_producto_orden_compra)),
                    ObjectValue(attribute_name='total_producto_orden_compra', top=0.3*cm, left=25*cm,
                                get_value=lambda instance: '{0:n}'.format(instance.total_producto_orden_compra)),
                    ],
                borders={'left': True, 'right': True},
            ),
            band_footer = ReportBand(
                height=1*cm,
                elements=[
                    Label(text='Total Orden Compra', top=0.3*cm, left=18*cm, style={'fontName': 'Helvetica-Bold'}),
                    ObjectValue(attribute_name='total_producto_orden_compra', top=0.15*cm, left=-1*cm, width=BAND_WIDTH,
                                action=FIELD_ACTION_SUM,  # display_format='%s permissions found',
                                style={'fontName': 'Helvetica-Bold', 'fontSize': 16, 'textColor': red, 'alignment': TA_RIGHT}),
                    ],
                borders={'top': True, 'bottom': True, 'left': True, 'right': True},
            ),
        ),
    ]


class CompraReport(Report):
    title = 'Confirmacion de Orden de Compra'
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
        elements = [
            # Ocultar el Nro. Compra, visualizar solo el Nro. Orden Compra
            # Label(text="Nro. Compra:", top=0.3*cm, left=20*cm, width=6.5*cm,
            #       style={'fontName': 'Helvetica-Bold', 'fontSize': 12, 'wordWrap': True, 'borderWidth': 1,
            #              'borderColor': red, 'borderPadding': 5, 'borderRadius': 5, 'alignment': TA_LEFT}),
            # ObjectValue(attribute_name='numero_compra', top=0.3*cm, left=-0.2*cm, width=BAND_WIDTH,
            #             style={'fontName': 'Helvetica-Bold', 'fontSize': 12, 'alignment': TA_RIGHT}),
            Label(text="Nro. Orden Compra:", top=0.3*cm, left=20*cm, width=6.5*cm,
                  style={'fontName': 'Helvetica-Bold', 'fontSize': 12, 'wordWrap': True, 'borderWidth': 1,
                         'borderColor': red, 'borderPadding': 5, 'borderRadius': 5, 'alignment': TA_LEFT}),
            ObjectValue(attribute_name='numero_orden_compra', top=0.3*cm, left=-0.2*cm, width=BAND_WIDTH,
                        style={'fontName': 'Helvetica-Bold', 'fontSize': 12, 'alignment': TA_RIGHT}),

            Label(text='Proveedor:', top=0.3*cm, left=0.3*cm, style={'fontName': 'Helvetica-Bold'}),
            ObjectValue(attribute_name='proveedor', top=0.3*cm, left=2.3*cm, width=BAND_WIDTH),

            Label(text='RUC:', top=0.3*cm, left=10*cm, style={'fontName': 'Helvetica-Bold'}),
            ObjectValue(attribute_name='proveedor.ruc', top=0.3*cm, left=11*cm),
            Label(text='-', top=0.3*cm, left=12.7*cm),
            ObjectValue(attribute_name='proveedor.digito_verificador', top=0.3*cm, left=12.9*cm),

            Label(text='Direccion:', top=1.0*cm, left=0.3*cm, style={'fontName': 'Helvetica-Bold'}),
            ObjectValue(attribute_name='proveedor.direccion', top=1.0*cm, left=2.1*cm, width=11*cm),  # width=BAND_WIDTH

            Label(text='Pais:', top=1.0*cm, left=13*cm, style={'fontName': 'Helvetica-Bold'}),
            ObjectValue(attribute_name='proveedor.pais', top=1.0*cm, left=14*cm, width=BAND_WIDTH),

            Label(text='Ciudad:', top=1.0*cm, left=16*cm, style={'fontName': 'Helvetica-Bold'}),
            ObjectValue(attribute_name='proveedor.ciudad', top=1.0*cm, left=17.4*cm, width=BAND_WIDTH),

            Label(text='Fecha/hora Compra:', top=1.7*cm, left=0.3*cm, style={'fontName': 'Helvetica-Bold'}),
            ObjectValue(attribute_name='fecha_compra', top=1.7*cm, left=3.9*cm,
                        get_value=lambda instance: timezone.localtime(instance.fecha_compra).strftime('%d/%m/%Y %H:%M')),

            # Label(text='Fecha/hora Entrega:', top=1.7*cm, left=9*cm, style={'fontName': 'Helvetica-Bold'}),
            # ObjectValue(attribute_name='fecha_entrega_orden_compra', top=1.7*cm, left=12.5*cm,
            #             get_value=lambda instance: timezone.localtime(instance.fecha_entrega_orden_compra).strftime('%d/%m/%Y %H:%M')),

            Label(text='Forma de Pago:', top=1.7*cm, left=10*cm, style={'fontName': 'Helvetica-Bold'}),
            ObjectValue(attribute_name='numero_orden_compra.forma_pago_orden_compra', top=1.7*cm, left=12.8*cm, width=BAND_WIDTH),

            Label(text='Numero de Factura:', top=2.4*cm, left=0.3*cm, style={'fontName': 'Helvetica-Bold'}),
            ObjectValue(attribute_name='numero_factura_compra', top=2.4*cm, left=3.7*cm, width=BAND_WIDTH),

            Label(text='Tipo Factura:', top=2.4*cm, left=8*cm, style={'fontName': 'Helvetica-Bold'}),
            ObjectValue(attribute_name='tipo_factura_compra', top=2.4*cm, left=10.3*cm, width=BAND_WIDTH),

            Label(text='Fecha Factura:', top=2.4*cm, left=15*cm, style={'fontName': 'Helvetica-Bold'}),
            ObjectValue(attribute_name='fecha_factura_compra', top=2.4*cm, left=17.6*cm),
                        # get_value=lambda instance: instance.fecha_factura_compra.strftime('%d/%m/%Y')),

            Label(text='Elaborado por:', top=2.4*cm, left=21.5*cm, style={'fontName': 'Helvetica-Bold'}),
            ObjectValue(attribute_name='usuario_registro_compra', top=2.4*cm, left=24.1*cm, width=BAND_WIDTH),

            Label(text='Estado Compra:', top=3.1*cm, left=0.3*cm, width=11*cm,
                  style={'fontName': 'Helvetica-Bold', 'fontSize': 12, 'wordWrap': True, 'borderWidth': 1,
                         'borderColor': red, 'borderPadding': 4, 'borderRadius': 5, 'alignment': TA_LEFT}),
            ObjectValue(attribute_name='estado_compra', top=3.15*cm, left=3.7*cm, width=BAND_WIDTH),

            Label(text='Motivo Cancelacion:', top=3.1*cm, left=12*cm, style={'fontName': 'Helvetica-Bold'}),
            ObjectValue(attribute_name='motivo_cancelacion', top=3.1*cm, left=15.5*cm, width=BAND_WIDTH,
                        get_value=lambda instance: instance.motivo_cancelacion if instance.motivo_cancelacion is not None else 'N/A'),

            Label(text='Cancelado por:', top=3.1*cm, left=21.5*cm, style={'fontName': 'Helvetica-Bold'}),
            ObjectValue(attribute_name='usuario_cancelacion', top=3.1*cm, left=24.1*cm, width=BAND_WIDTH,
                        get_value=lambda instance: instance.usuario_cancelacion if instance.usuario_cancelacion is not None else 'N/A'),

            Label(text='Observ. Canc.:', top=3.8*cm, left=0.3*cm, style={'fontName': 'Helvetica-Bold'}),
            ObjectValue(attribute_name='observaciones_cancelacion', top=3.8*cm, left=3*cm, width=BAND_WIDTH,
                        get_value=lambda instance: instance.observaciones_cancelacion if instance.observaciones_cancelacion is not None else 'N/A'),

            Label(text='Fecha/hora Canc.:', top=3.8*cm, left=20.8*cm, style={'fontName': 'Helvetica-Bold'}),
            ObjectValue(attribute_name='fecha_hora_cancelacion', top=3.8*cm, left=24*cm,
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
            # queryset_string = '%(object)s.compradetalle_set.all()',
            queryset_string = '%(object)s.compradetalle_set.all().raw("SELECT *, Row_Number() Over (Order By detalle.id) AS fila FROM compras_compradetalle detalle where detalle.numero_compra_id = %%s", [%(object)s.pk])',
            band_header = ReportBand(
                height=1*cm,
                elements=[
                    Label(text='Item', top=0.3*cm, left=0.3*cm, style={'fontName': 'Helvetica-Bold'}),
                    Label(text='Producto', top=0.3*cm, left=1.5*cm, style={'fontName': 'Helvetica-Bold'}),
                    Label(text='Precio', top=0.3*cm, left=16*cm, style={'fontName': 'Helvetica-Bold'}),
                    Label(text='Un. Med. Compra', top=0.3*cm, left=18*cm, style={'fontName': 'Helvetica-Bold'}),
                    Label(text='Cantidad', top=0.3*cm, left=22*cm, style={'fontName': 'Helvetica-Bold'}),
                    Label(text='Total', top=0.3*cm, left=25*cm, style={'fontName': 'Helvetica-Bold'}),
                    ],
                borders={'top': True, 'bottom': True, 'left': True, 'right': True},
                # borders = {'bottom': Line(stroke_color=red, stroke_width=3)}
            ),
            band_detail = ReportBand(
                height=1*cm,
                # width=12*cm,
                elements=[
                    ObjectValue(attribute_name='fila', top=0.3*cm, left=0.3*cm),
                    ObjectValue(attribute_name='producto_compra', top=0.3*cm, left=1.5*cm, width=BAND_WIDTH),
                    ObjectValue(attribute_name='precio_producto_compra', top=0.3*cm, left=16*cm,
                                get_value=lambda instance: '{0:n}'.format(instance.precio_producto_compra)),
                    ObjectValue(attribute_name='unidad_medida_compra', top=0.3*cm, left=18*cm),
                    ObjectValue(attribute_name='cantidad_producto_compra', top=0.3*cm, left=22*cm,
                                get_value=lambda instance: '{0:n}'.format(instance.cantidad_producto_compra)),
                    ObjectValue(attribute_name='total_producto_compra', top=0.3*cm, left=25*cm,
                                get_value=lambda instance: '{0:n}'.format(instance.total_producto_compra)),
                    ],
                borders={'left': True, 'right': True},
            ),
            band_footer = ReportBand(
                height=1*cm,
                elements=[
                    Label(text='Total Compra', top=0.3*cm, left=18*cm, style={'fontName': 'Helvetica-Bold'}),
                    ObjectValue(attribute_name='total_producto_compra', top=0.15*cm, left=-1*cm, width=BAND_WIDTH,
                                action=FIELD_ACTION_SUM, display_format='%s',  # '{0:n}'.format(int('s')),
                                style={'fontName': 'Helvetica-Bold', 'fontSize': 16, 'textColor': red, 'alignment': TA_RIGHT}),
                    ],
                borders={'top': True, 'bottom': True, 'left': True, 'right': True},
            ),
        ),
    ]


class OrdenPagoReport(Report):
    title = 'Orden de Pago'
    author = 'Pedro Molas'

    page_size = landscape(A4)
    margin_left = 1.5*cm
    margin_top = 0.5*cm
    margin_right = 1.5*cm
    margin_bottom = 0.5*cm

    # queryset = Empresa.objects.filter(id=9)

    # def __init__(self, *args, **kwargs):
    #     super(OrdenPagoReport, self).__init__(*args, **kwargs)
    #
    #     myset = self.queryset
    #     item = 0
    #     for myline in myset:
    #         item += 1
    #     self.subreports.SubReport.band_detail.elements += [
    #         SystemField(expression=item, top=1*cm, left=26.5*cm, width=1.9*cm, style={'alignment':TA_RIGHT}),
    #         ]

    class band_detail(ReportBand):
        height = 4*cm
        margin_top=0.5*cm
        # margin_bottom=0.5*cm
        # queryset_string = '%(object)s.ordencompradetalle_set.all()',
        elements = [
            Label(text="Nro. Orden Pago:", top=0.3*cm, left=20*cm, width=6.5*cm,
                  style={'fontName': 'Helvetica-Bold', 'fontSize': 12, 'wordWrap': True, 'borderWidth': 1,
                         'borderColor': red, 'borderPadding': 6, 'borderRadius': 5, 'alignment': TA_LEFT}),
            ObjectValue(attribute_name='numero_orden_pago', top=0.3*cm, left=-0.2*cm, width=BAND_WIDTH,
                        style={'fontName': 'Helvetica-Bold', 'fontSize': 12, 'alignment': TA_RIGHT}),

            Label(text='Proveedor:', top=0.3*cm, left=0.3*cm, style={'fontName': 'Helvetica-Bold'}),
            ObjectValue(attribute_name='proveedor_orden_pago', top=0.3*cm, left=2.3*cm),

            Label(text='RUC:', top=0.3*cm, left=10*cm, style={'fontName': 'Helvetica-Bold'}),
            ObjectValue(attribute_name='proveedor_orden_pago.ruc', top=0.3*cm, left=11*cm),
            Label(text='-', top=0.3*cm, left=12.7*cm),
            ObjectValue(attribute_name='proveedor_orden_pago.digito_verificador', top=0.3*cm, left=12.9*cm),

            Label(text='Direccion:', top=1.0*cm, left=0.3*cm, style={'fontName': 'Helvetica-Bold'}),
            ObjectValue(attribute_name='proveedor_orden_pago.direccion', top=1.0*cm, left=2.1*cm, width=11*cm),

            Label(text='Pais:', top=1.0*cm, left=13*cm, style={'fontName': 'Helvetica-Bold'}),
            ObjectValue(attribute_name='proveedor_orden_pago.pais', top=1.0*cm, left=14*cm, width=BAND_WIDTH),

            Label(text='Ciudad:', top=1.0*cm, left=16*cm, style={'fontName': 'Helvetica-Bold'}),
            ObjectValue(attribute_name='proveedor_orden_pago.ciudad', top=1.0*cm, left=17.4*cm, width=BAND_WIDTH),

            Label(text='Fecha/hora Orden Pago:', top=1.7*cm, left=0.3*cm, style={'fontName': 'Helvetica-Bold'}),
            ObjectValue(attribute_name='fecha_hora_orden_pago', top=1.7*cm, left=4.5*cm,
                        get_value=lambda instance: timezone.localtime(instance.fecha_hora_orden_pago).strftime('%d/%m/%Y %H:%M')),

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

            Label(text='Elaborado por:', top=1.7*cm, left=21.5*cm, style={'fontName': 'Helvetica-Bold'}),
            ObjectValue(attribute_name='usuario_registro_orden_pago', top=1.7*cm, left=24.1*cm, width=BAND_WIDTH),

            Label(text='Estado Ord. Pago:', top=2.4*cm, left=0.3*cm, width=8*cm,
                  style={'fontName': 'Helvetica-Bold', 'fontSize': 12, 'wordWrap': True, 'borderWidth': 1,
                         'borderColor': red, 'borderPadding': 4, 'borderRadius': 5, 'alignment': TA_LEFT}),
            ObjectValue(attribute_name='estado_orden_pago', top=2.45*cm, left=4.2*cm, width=BAND_WIDTH),

            Label(text='Motivo Anulacion:', top=2.4*cm, left=12*cm, style={'fontName': 'Helvetica-Bold'}),
            ObjectValue(attribute_name='motivo_anulacion', top=2.4*cm, left=15.2*cm, width=BAND_WIDTH,
                        get_value=lambda instance: instance.motivo_anulacion if instance.motivo_anulacion is not None else 'N/A'),

            Label(text='Anulado por:', top=2.4*cm, left=21.5*cm, style={'fontName': 'Helvetica-Bold'}),
            ObjectValue(attribute_name='usuario_anulacion', top=2.4*cm, left=23.8*cm, width=BAND_WIDTH,
                        get_value=lambda instance: instance.usuario_anulacion if instance.usuario_anulacion is not None else 'N/A'),

            Label(text='Observ. Anul.:', top=3.1*cm, left=0.3*cm, style={'fontName': 'Helvetica-Bold'}),
            ObjectValue(attribute_name='observaciones_anulacion', top=3.1*cm, left=2.8*cm, width=BAND_WIDTH,
                        get_value=lambda instance: instance.observaciones_anulacion if instance.observaciones_anulacion is not None else 'N/A'),

            Label(text='Fecha/hora Anul.:', top=3.1*cm, left=20.8*cm, style={'fontName': 'Helvetica-Bold'}),
            ObjectValue(attribute_name='fecha_hora_anulacion', top=3.1*cm, left=23.9*cm,
                        get_value=lambda instance: timezone.localtime(instance.fecha_hora_anulacion).strftime('%d/%m/%Y %H:%M') if instance.fecha_hora_anulacion is not None else 'N/A'),
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
            # queryset_string = '%(object)s.ordenpagodetalle_set.all()',
            queryset_string = '%(object)s.ordenpagodetalle_set.all().raw("SELECT *, Row_Number() Over (Order By detalle.id) AS fila FROM compras_ordenpagodetalle detalle where detalle.numero_orden_pago_id = %%s", [%(object)s.pk])',
            band_header = ReportBand(
                height=1*cm,
                elements=[
                    Label(text='Item', top=0.3*cm, left=0.3*cm, style={'fontName': 'Helvetica-Bold'}),
                    Label(text='Compra Asociada', top=0.1*cm, left=2*cm, width=2*cm, style={'fontName': 'Helvetica-Bold'}),
                    Label(text='Nro. Factura', top=0.3*cm, left=4.7*cm, style={'fontName': 'Helvetica-Bold'}),
                    Label(text='Fecha Factura', top=0.3*cm, left=8.5*cm, style={'fontName': 'Helvetica-Bold'}),
                    Label(text='Tipo Factura', top=0.3*cm, left=12*cm, style={'fontName': 'Helvetica-Bold'}),
                    Label(text='Forma Pago', top=0.3*cm, left=15*cm, style={'fontName': 'Helvetica-Bold'}),
                    # Label(text='Plazo Pago', top=0.3*cm, left=14*cm, style={'fontName': 'Helvetica-Bold'}),
                    Label(text='Total Factura', top=0.3*cm, left=18.5*cm, style={'fontName': 'Helvetica-Bold'}),
                    Label(text='Estado Factura', top=0.3*cm, left=22*cm, style={'fontName': 'Helvetica-Bold'}),
                    ],
                borders={'top': True, 'bottom': True, 'left': True, 'right': True},
                # borders = {'bottom': Line(stroke_color=red, stroke_width=3)}
            ),
            band_detail = ReportBand(
                height=1*cm,
                # width=12*cm,
                elements=[
                    # ObjectValue(attribute_name='id', top=0.3*cm, left=0.3*cm, action=FIELD_ACTION_DISTINCT_COUNT),
                    ObjectValue(attribute_name='fila', top=0.3*cm, left=0.3*cm),
                    ObjectValue(attribute_name='compra', top=0.3*cm, left=2*cm, width=BAND_WIDTH),
                    ObjectValue(attribute_name='numero_factura_compra', top=0.3*cm, left=4.7*cm),
                    ObjectValue(attribute_name='fecha_factura_compra', top=0.3*cm, left=8.5*cm,
                                get_value=lambda instance: instance.fecha_factura_compra.strftime('%d/%m/%Y')),
                    ObjectValue(attribute_name='tipo_factura_compra', top=0.3*cm, left=12*cm),
                    ObjectValue(attribute_name='forma_pago_compra', top=0.3*cm, left=15*cm),
                    # ObjectValue(attribute_name='plazo_factura_compra', top=0.3*cm, left=14*cm),
                    ObjectValue(attribute_name='total_factura_compra', top=0.3*cm, left=18.5*cm,
                                get_value=lambda instance: '{0:n}'.format(instance.total_factura_compra)),
                    ObjectValue(attribute_name='estado_factura_compra', top=0.3*cm, left=22*cm),
                    ],
                borders={'left': True, 'right': True},
            ),
            band_footer = ReportBand(
                height=1*cm,
                elements=[
                    Label(text='Total Orden Pago', top=0.3*cm, left=18*cm, style={'fontName': 'Helvetica-Bold'}),
                    ObjectValue(attribute_name='total_factura_compra', top=0.15*cm, left=-1*cm, width=BAND_WIDTH,
                                action=FIELD_ACTION_SUM,  # display_format='%s permissions found',
                                style={'fontName': 'Helvetica-Bold', 'fontSize': 16, 'textColor': red, 'alignment': TA_RIGHT}),
                    ],
                borders={'top': True, 'bottom': True, 'left': True, 'right': True},
            ),
        ),
    ]


class ListadoOrdenesCompraReport(Report):
    title = 'Listado de Ordenes de Compras'
    author = 'Pedro Molas'

    page_size = landscape(A4)
    margin_left = 2*cm
    margin_top = 0.5*cm
    margin_right = 0.5*cm
    margin_bottom = 0.5*cm

    class band_detail(ReportBand):
        height = 0.5*cm
        elements = (
            ObjectValue(attribute_name='numero_orden_compra', left=0.5*cm),
            ObjectValue(attribute_name='fecha_orden_compra', left=3*cm,
                        get_value=lambda instance: instance.fecha_orden_compra.strftime('%d/%m/%Y')),
        )

    class band_page_header(ReportBand):
        height = 1.3*cm
        elements = [
            SystemField(expression='%(report_title)s', top=0.1*cm, left=0, width=BAND_WIDTH,
                        style={'fontName': 'Helvetica-Bold', 'fontSize': 14, 'alignment': TA_CENTER}),
            Label(text="Nro. OC", top=0.8*cm, left=0.5*cm),
            Label(text=u"Fecha OC", top=0.8*cm, left=3*cm),
            SystemField(expression=u'Pagina %(page_number)d de %(page_count)d', top=0.1*cm, width=BAND_WIDTH,
                        style={'alignment': TA_RIGHT}),
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

    groups = [
        ReportGroup(attribute_name = 'proveedor_orden_compra',
            band_header = ReportBand(
                height = 0.7*cm,
                elements = [
                    ObjectValue(attribute_name='proveedor_orden_compra', left=0, top=0.1*cm, width=20*cm,
                        get_value=lambda instance: 'Proveedor: ' + (instance.proveedor_orden_compra.proveedor),
                        style={'fontName': 'Helvetica-Bold', 'fontSize': 12})
                    ],
                borders = {'bottom': True},
                )
            ),
        ]

    # subreports = [
    #     SubReport(
    #         queryset_string = '%(object)s.ordencompradetalle_set.all()',
    #         detail_band = ReportBand(
    #             height=0.5*cm,
    #             elements=[
    #                 ObjectValue(attribute_name='producto_orden_compra', top=0, left=1*cm),
    #                 ObjectValue(attribute_name='precio_producto_orden_compra', top=0, left=5*cm),
    #                 ]
    #             ),
    #         ),
    #     ]


# ======================================================================================================================
class GraphicsReport(Report):
    title = 'Graphics demonstration'
    print_if_empty = True

    class band_begin(ReportBand):
        height = 15*cm
        elements = [
            RoundRect(left=0.2*cm, top=0.5*cm, width=3*cm, height=2*cm,
                radius=10, stroke_color=purple),
            Rect(left=4*cm, top=1.0*cm, width=3*cm, height=2*cm,
                fill=True, stroke=False, fill_color=orange),
            Line(left=8*cm, top=3*cm, right=9*cm, bottom=0),
            Line(left=9*cm, top=0, right=10*cm, bottom=3*cm),
            Line(left=8*cm, top=3*cm, right=9*cm, bottom=6*cm),
            Line(left=9*cm, top=6*cm, right=10*cm, bottom=3*cm),
            Circle(left_center=5*cm, top_center=5*cm, radius=1*cm, fill_color=yellow,
                fill=True),
            Arc(left=1*cm, top=3.0*cm, right=4*cm, bottom=5*cm,
                start_angle=150, extent=100),
            Ellipse(left=1*cm, top=6.0*cm, right=4.5*cm, bottom=8*cm,
                fill_color=blue, fill=True, stroke_width=3),
            Image(left=10*cm, top=6*cm, width=4*cm, height=5.12*cm,
                filename=os.path.join(cur_dir, 'photo.jpg')),
            Image(left=13*cm, top=6*cm,
                filename=os.path.join(cur_dir, 'photo.jpg')),
            #Poligon(), # --> uses drawPath
            Label(text="Prueba",
                left=12*cm, top=1*cm, width=6*cm, height=4*cm,
                style={'wordWrap': True, 'borderWidth': 1,
                    'borderColor': green, 'borderPadding': 4,
                    'borderRadius': 2, 'alignment': TA_JUSTIFY}),
        ]

    class band_page_header(ReportBand):
        height = 1.4*cm
        elements = [
            SystemField(expression='%(report_title)s', top=0.1*cm, left=0,
                width=BAND_WIDTH, style={'fontName': 'Helvetica-Bold',
                    'fontSize': 14, 'alignment': TA_CENTER}),
            Label(text="ID", top=0.8*cm, left=0, width=1*cm,
                style={'borderWidth': 1, 'borderColor': green,
                    'borderPadding': 1, 'borderRadius': 2, 'fontName': 'Helvetica'}),
            Label(text="Name", top=0.8*cm, left=3*cm,
                style={'backColor': red, 'textColor': white,
                'fontName': 'Helvetica'}),
        ]
        borders = {'bottom': True}


class MasterReport(Report):
    title = 'Subreports demonstration'

    class band_summary(ReportBand):
        height = 0.8*cm
        elements = [
            Label(text="Users count:", top=0.1*cm, left=0),
            ObjectValue(attribute_name='id', top=0.1*cm, left=4*cm,
                        action=FIELD_ACTION_COUNT, display_format='%s users found'),
            ]
        borders = {'top': Line(stroke_color=red, stroke_width=3)}

    class band_page_header(ReportBand):
        height = 0.8*cm
        elements = [
            SystemField(expression='%(report_title)s', top=0.1*cm, left=0, width=BAND_WIDTH,
                        style={'fontName': 'Helvetica-Bold', 'fontSize': 14, 'alignment': TA_CENTER}),
            SystemField(expression='Page # %(page_number)d of %(page_count)d', top=0.1*cm,
                        width=BAND_WIDTH, style={'alignment': TA_RIGHT}),
            ]
        borders = {'bottom': Line(stroke_color=red, stroke_width=3)}

    class band_page_footer(ReportBand):
        height = 0.5*cm
        elements = [
            Label(text='Created with Geraldo Reports', top=0.1*cm),
            SystemField(expression='Printed in %(now:%Y, %b %d)s at %(now:%H:%M)s', top=0.1*cm,
                        width=BAND_WIDTH, style={'alignment': TA_RIGHT}),
            ]
        borders = {'top': Line(stroke_color=navy)}

    class band_detail(ReportBand):
        height = 2*cm
        elements = [
            Label(text="Username", top=0, left=0, style={'fontName': 'Helvetica-Bold', 'fontSize': 14}),
            Label(text="Full name", top=1*cm, left=0.2*cm, style={'fontName': 'Helvetica-Bold'}),
            Label(text="Superuser", top=1.5*cm, left=0.2*cm, style={'fontName': 'Helvetica-Bold'}),
            ObjectValue(attribute_name='username', top=0, left=4*cm, style={'fontName': 'Helvetica', 'fontSize': 14}),
            ObjectValue(attribute_name='get_full_name', top=1*cm, left=4*cm, style={'fontName': 'Helvetica'}),
            ObjectValue(attribute_name='is_superuser', top=1.5*cm, left=4*cm, style={'fontName': 'Helvetica'}),
            ]
        borders = {'bottom': Line(stroke_color=navy)}

    subreports = [
        SubReport(
            queryset_string = '%(object)s.user_permissions.all()',
            band_header = ReportBand(
                height=0.5*cm,
                elements=[
                    Label(text='ID', top=0, left=0.2*cm, style={'fontName': 'Helvetica-Bold'}),
                    Label(text='Name', top=0, left=4*cm, style={'fontName': 'Helvetica-Bold'}),
                    ],
            borders={'top': True, 'left': True, 'right': True},
                ),
            band_detail = ReportBand(
                height=0.5*cm,
                # width=12*cm,
                elements=[
                    ObjectValue(attribute_name='id', top=0, left=0.2*cm),
                    ObjectValue(attribute_name='name', top=0, left=4*cm),
                    ],
                borders={'left': True, 'right': True},
                ),
            band_footer = ReportBand(
                height=0.5*cm,
                elements=[
                    ObjectValue(attribute_name='id', left=4*cm,
                                action=FIELD_ACTION_COUNT, display_format='%s permissions found',
                                style={'fontName': 'Helvetica-Bold'}),
                    ],
                borders={'bottom': True, 'left': True, 'right': True},
                ),
            ),
        ]