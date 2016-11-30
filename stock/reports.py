# coding=utf-8
from decimal import Decimal
from plistlib import Data
from re import sub
from django.utils import timezone
from geraldo.utils import FIELD_ACTION_DISTINCT_COUNT, FIELD_ACTION_MIN
import locale

locale.setlocale(locale.LC_ALL, '')

__author__ = 'pmmr'

import os
cur_dir = os.path.dirname(os.path.abspath(__file__))
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

from django.contrib.auth.models import User, Permission

from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm
from reportlab.lib.colors import navy, yellow, red, purple, orange, green, white, blue
from reportlab.lib.enums import TA_RIGHT, TA_CENTER, TA_JUSTIFY, TA_LEFT

from geraldo import Report, landscape, ReportBand, ObjectValue, SystemField, BAND_WIDTH, Label, ReportGroup, \
    SubReport, RoundRect, Rect, Line, Circle, Arc, Ellipse, Image, FIELD_ACTION_COUNT, FIELD_ACTION_SUM, FIELD_ACTION_VALUE


class AjusteInventarioReport(Report):
    title = 'Ajuste de Inventario'
    author = 'Pedro Molas'

    page_size = A4
    margin_left = 1.5*cm
    margin_top = 0.5*cm
    margin_right = 1.5*cm
    margin_bottom = 0.5*cm

    class band_detail(ReportBand):
        height = 2.7*cm
        margin_top=0.5*cm
        # margin_bottom=0.5*cm
        # queryset_string = '%(object)s.ordencompradetalle_set.all()',
        elements = [
            Label(text="ID Ajuste Invent.:", top=0.2*cm, left=13*cm, width=4.8*cm,
                  style={'fontName': 'Helvetica-Bold', 'fontSize': 12, 'wordWrap': True, 'borderWidth': 1,
                         'borderColor': red, 'borderPadding': 4, 'borderRadius': 5, 'alignment': TA_LEFT}),
            ObjectValue(attribute_name='id', top=0.2*cm, left=-0.2*cm, width=BAND_WIDTH,
                        style={'fontName': 'Helvetica-Bold', 'fontSize': 12, 'alignment': TA_RIGHT}),

            Label(text='Deposito:', top=0.3*cm, left=0.1*cm, style={'fontName': 'Helvetica-Bold'}),
            ObjectValue(attribute_name='deposito', top=0.3*cm, left=1.8*cm, width=BAND_WIDTH,
                        get_value=lambda instance: instance.deposito if instance.deposito is not None else 'N/A'),

            Label(text='Fecha/hora Ajuste Invent.:', top=1*cm, left=0.1*cm, style={'fontName': 'Helvetica-Bold'}),
            ObjectValue(attribute_name='fecha_hora_registro_ajuste', top=1*cm, left=4.6*cm, width=BAND_WIDTH,
                        get_value=lambda instance: timezone.localtime(instance.fecha_hora_registro_ajuste).strftime('%d/%m/%Y %H:%M') if instance.fecha_hora_registro_ajuste is not None else 'N/A'),

            Label(text='Estado Ajuste Invent.:', top=1.7*cm, left=0.2*cm, width=7*cm,
                  style={'fontName': 'Helvetica-Bold', 'fontSize': 12, 'wordWrap': True, 'borderWidth': 1,
                         'borderColor': red, 'borderPadding': 3, 'borderRadius': 3, 'alignment': TA_LEFT}),
            ObjectValue(attribute_name='estado_ajuste', top=1.75*cm, left=4.8*cm, width=BAND_WIDTH,
                        get_value=lambda instance: instance.estado_ajuste.get_estado_ajuste_stock_display() if instance.estado_ajuste is not None else 'N/A'),

            Label(text='Usuario Ajuste Invent.:', top=1.7*cm, left=9*cm, style={'fontName': 'Helvetica-Bold'}),
            ObjectValue(attribute_name='usuario_registra_ajuste', top=1.7*cm, left=12.9*cm, width=BAND_WIDTH,
                        get_value=lambda instance: instance.usuario_registra_ajuste.usuario.username if instance.usuario_registra_ajuste is not None else 'N/A'),
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

    class band_summary(ReportBand):
        height = 5.5*cm
        elements = [
            Line(left=1.5*cm, top=3*cm, right=7.5*cm, bottom=3*cm),
            Label(text='Firma y sello Responsable Ajuste de Inventario', top=3.5*cm, left=0*cm, width=9*cm, style={'fontName': 'Helvetica-Bold', 'alignment': TA_CENTER}),
            ObjectValue(attribute_name='usuario_registra_ajuste', top=4.2*cm, left=0*cm, width=9*cm, style={'alignment': TA_CENTER},
                        get_value=lambda instance: instance.usuario_registra_ajuste.nombre_completo if instance.usuario_registra_ajuste is not None else 'N/A'),
            Label(text='Cargo:', top=4.9*cm, left=-2*cm, width=9*cm, style={'fontName': 'Helvetica-Bold', 'alignment': TA_CENTER}),
            ObjectValue(attribute_name='usuario_registra_ajuste', top=4.9*cm, left=0.5*cm, width=9*cm, style={'alignment': TA_CENTER},
                        get_value=lambda instance: instance.usuario_registra_ajuste.cargo.get_cargo_display() if instance.usuario_registra_ajuste is not None else 'N/A'),

            Line(left=10.5*cm, top=3*cm, right=16.5*cm, bottom=3*cm),
            Label(text='Firma y sello Supervisor', top=3.5*cm, left=9*cm, width=9*cm, style={'fontName': 'Helvetica-Bold', 'alignment': TA_CENTER}),
        ]
        # borders={'top': True, 'bottom': True, 'left': True, 'right': True}

    class band_page_footer(ReportBand):
        height = 0.5*cm
        elements = [
                Label(text='SIGB Reportes', top=0.1*cm),
                SystemField(expression=u'Impreso el %(now:%d %B de %Y)s a las %(now:%H:%M)s', top=0.1*cm,
                    width=BAND_WIDTH, style={'alignment': TA_RIGHT}),
                ]
        borders = {'top': True}

    subreports = [
        SubReport(
            # queryset_string = '%(object)s.ordencompradetalle_set.all()',
            queryset_string = '%(object)s.ajustestockdetalle_set.all().raw("SELECT *, Row_Number() Over (Order By detalle.id) AS fila FROM stock_ajustestockdetalle detalle where detalle.ajustar=True and detalle.ajuste_stock_id = %%s", [%(object)s.pk])',
            band_header = ReportBand(
                height=1*cm,
                elements=[
                    Label(text='Item', top=0.3*cm, left=0*cm, width=1*cm, style={'fontName': 'Helvetica-Bold', 'alignment': TA_CENTER}),
                    Label(text='Producto', top=0.3*cm, left=1*cm, width=6*cm, style={'fontName': 'Helvetica-Bold', 'alignment': TA_CENTER}),
                    Label(text='Un. de Med.', top=0.3*cm, left=7.1*cm, width=2*cm, style={'fontName': 'Helvetica-Bold', 'alignment': TA_CENTER}),
                    Label(text='Cant. Existente', top=0.1*cm, left=9.2*cm, width=2*cm, style={'fontName': 'Helvetica-Bold', 'alignment': TA_CENTER}),
                    Label(text='Cant. Ajuste', top=0.1*cm, left=11*cm, width=2*cm, style={'fontName': 'Helvetica-Bold', 'alignment': TA_CENTER}),
                    Label(text='Motivo Ajuste', top=0.3*cm, left=13*cm, width=5*cm, style={'fontName': 'Helvetica-Bold', 'alignment': TA_CENTER}),
                    ],
                borders={'top': True, 'bottom': True, 'left': True, 'right': True},
                # borders = {'bottom': Line(stroke_color=red, stroke_width=3)}
            ),
            band_detail = ReportBand(
                height=1*cm,
                # width=12*cm,
                elements=[
                    ObjectValue(attribute_name='fila', top=0.3*cm, left=0.1*cm, width=1*cm, style={'alignment': TA_CENTER}),
                    ObjectValue(attribute_name='producto_ajuste', top=0.1*cm, left=1.2*cm, width=6*cm, style={'alignment': TA_LEFT}),
                    ObjectValue(attribute_name='unidad_medida', top=0.3*cm, left=7.1*cm, width=2*cm, style={'alignment': TA_CENTER},
                                get_value=lambda instance: instance.unidad_medida.get_unidad_medida_producto_display() if instance.unidad_medida is not None else 'N/A'),
                    ObjectValue(attribute_name='cantidad_existente_producto', top=0.3*cm, left=9.2*cm, width=2*cm, style={'alignment': TA_CENTER},
                                get_value=lambda instance: '{0:n}'.format(instance.cantidad_existente_producto)),
                    ObjectValue(attribute_name='cantidad_ajustar_producto', top=0.3*cm, left=11*cm, width=2*cm, style={'alignment': TA_CENTER},
                                get_value=lambda instance: '{0:n}'.format(instance.cantidad_ajustar_producto)),
                    ObjectValue(attribute_name='motivo_ajuste', top=0.1*cm, left=13*cm, width=5*cm, style={'alignment': TA_LEFT}),
                    ],
                borders={'bottom': True, 'left': True, 'right': True},
            ),
            # band_footer = ReportBand(
            #     height=1*cm,
            #     elements=[
            #         Label(text='Total Pedido', top=0.3*cm, left=10*cm, style={'fontName': 'Helvetica-Bold'}),
            #         ObjectValue(attribute_name='total_producto_pedido', top=0.15*cm, left=-1*cm, width=BAND_WIDTH,
            #                     action=FIELD_ACTION_SUM,  # display_format='%s permissions found',
            #                     style={'fontName': 'Helvetica-Bold', 'fontSize': 16, 'textColor': red, 'alignment': TA_RIGHT}),
            #         ],
            #     borders={'top': True, 'bottom': True, 'left': True, 'right': True},
            # ),
        ),
    ]