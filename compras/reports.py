__author__ = 'pmmr'

import os
cur_dir = os.path.dirname(os.path.abspath(__file__))

from models import OrdenCompra, OrdenCompraDetalle, Proveedor
from django.contrib.auth.models import User, Permission

from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm
from reportlab.lib.colors import navy, yellow, red, purple, orange, green, white, blue
from reportlab.lib.enums import TA_RIGHT, TA_CENTER, TA_JUSTIFY

from geraldo import Report, landscape, ReportBand, ObjectValue, SystemField, BAND_WIDTH, Label, ReportGroup, \
    SubReport, RoundRect, Rect, Line, Circle, Arc, Ellipse, Image, FIELD_ACTION_COUNT, FIELD_ACTION_SUM


class ReportOrdenCompra(Report):
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