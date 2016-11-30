# coding=utf-8
from decimal import Decimal
from plistlib import Data
from re import sub
from django.utils import timezone
from geraldo.utils import FIELD_ACTION_DISTINCT_COUNT, FIELD_ACTION_MIN
import locale
from clientes.models import ClienteTelefono
from compras.models import Empresa, OrdenPagoDetalle, ProveedorTelefono

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


class PedidoReport(Report):
    title = 'Pedido de Cliente'
    author = 'Pedro Molas'

    page_size = A4
    margin_left = 1.5*cm
    margin_top = 0.5*cm
    margin_right = 1.5*cm
    margin_bottom = 0.5*cm

    class band_detail(ReportBand):
        height = 5*cm
        margin_top=0.5*cm
        # margin_bottom=0.5*cm
        # queryset_string = '%(object)s.ordencompradetalle_set.all()',
        elements = [
            Label(text="Nro. Pedido:", top=0.2*cm, left=13*cm, width=4.8*cm,
                  style={'fontName': 'Helvetica-Bold', 'fontSize': 12, 'wordWrap': True, 'borderWidth': 1,
                         'borderColor': red, 'borderPadding': 4, 'borderRadius': 5, 'alignment': TA_LEFT}),
            ObjectValue(attribute_name='numero_pedido', top=0.2*cm, left=-0.2*cm, width=BAND_WIDTH,
                        style={'fontName': 'Helvetica-Bold', 'fontSize': 12, 'alignment': TA_RIGHT}),

            Label(text='Jornada:', top=0.3*cm, left=0.1*cm, style={'fontName': 'Helvetica-Bold'}),
            ObjectValue(attribute_name='jornada', top=0.3*cm, left=1.6*cm, width=BAND_WIDTH),

            Label(text='Atendido por:', top=0.3*cm, left=7.5*cm, style={'fontName': 'Helvetica-Bold'}),
            ObjectValue(attribute_name='mozo_pedido', top=0.3*cm, left=9.9*cm, width=BAND_WIDTH),

            Label(text='Fecha/hora Pedido:', top=1*cm, left=0.1*cm, style={'fontName': 'Helvetica-Bold'}),
            ObjectValue(attribute_name='fecha_hora_pedido', top=1*cm, left=3.4*cm,
                        get_value=lambda instance: timezone.localtime(instance.fecha_hora_pedido).strftime('%d/%m/%Y %H:%M')),

            Label(text='Mesas:', top=1*cm, left=7.5*cm, style={'fontName': 'Helvetica-Bold'}),
            ObjectValue(attribute_name='mesa_pedido', top=1*cm, left=8.8*cm, width=BAND_WIDTH,
                        get_value=lambda instance: " - ".join([str(m.nombre_mesa) for m in instance.mesa_pedido.all()])),

            Label(text='Reserva:', top=1.7*cm, left=0.1*cm, style={'fontName': 'Helvetica-Bold'}),
            ObjectValue(attribute_name='reserva.id', top=1.7*cm, left=1.7*cm,
                        get_value=lambda instance: instance.reserva.id if instance.reserva is not None else 'N/A'),

            Label(text='Fecha Reserva:', top=1.7*cm, left=2.6*cm, style={'fontName': 'Helvetica-Bold'}),
            ObjectValue(attribute_name='reserva.fecha_hora_reserva', top=1.7*cm, left=5.3*cm,
                        get_value=lambda instance: timezone.localtime(instance.reserva.fecha_hora_reserva).strftime('%d/%m/%Y %H:%M') if instance.reserva is not None else 'N/A'),

            Label(text='Monto Entrega:', top=1.7*cm, left=13*cm, style={'fontName': 'Helvetica-Bold'}),
            ObjectValue(attribute_name='reserva.pago', top=1.7*cm, left=15.7*cm, width=11*cm,
                        get_value=lambda instance: '{0:n}'.format(instance.reserva.pago) if instance.reserva is not None else 'N/A'),

            Label(text='ID Cliente:', top=2.4*cm, left=0.1*cm, style={'fontName': 'Helvetica-Bold'}),
            ObjectValue(attribute_name='reserva.cliente.id', top=2.4*cm, left=1.9*cm,
                        get_value=lambda instance: instance.reserva.cliente.id if instance.reserva is not None else 'N/A'),

            Label(text='Nombre Cliente:', top=2.4*cm, left=3*cm, style={'fontName': 'Helvetica-Bold'}),
            ObjectValue(attribute_name='reserva.cliente.nombre_completo', top=2.4*cm, left=5.8*cm, width=BAND_WIDTH,
                        get_value=lambda instance: instance.reserva.cliente.nombre_completo if instance.reserva is not None else 'N/A'),

            Label(text='Doc. Cliente:', top=2.4*cm, left=13*cm, style={'fontName': 'Helvetica-Bold'}),
            ObjectValue(attribute_name='reserva.cliente_documento_reserva', top=2.4*cm, left=15.3*cm, width=BAND_WIDTH,
                        get_value=lambda instance: instance.reserva.cliente_documento_reserva if instance.reserva is not None else 'N/A'),

            Label(text='Estado Pedido:', top=3.1*cm, left=0.1*cm, width=5*cm,
                  style={'fontName': 'Helvetica-Bold', 'fontSize': 12, 'wordWrap': True, 'borderWidth': 1,
                         'borderColor': red, 'borderPadding': 4, 'borderRadius': 5, 'alignment': TA_LEFT}),
            ObjectValue(attribute_name='estado_pedido', top=3.15*cm, left=3.3*cm, width=BAND_WIDTH),

            Label(text='Motivo Canc.:', top=3.8*cm, left=0.1*cm, style={'fontName': 'Helvetica-Bold'}),
            ObjectValue(attribute_name='motivo_cancelacion', top=3.8*cm, left=2.5*cm, width=BAND_WIDTH,
                        get_value=lambda instance: instance.motivo_cancelacion if instance.motivo_cancelacion is not None else 'N/A'),

            Label(text='Cancelado por:', top=3.8*cm, left=12.5*cm, style={'fontName': 'Helvetica-Bold'}),
            ObjectValue(attribute_name='usuario_cancelacion', top=3.8*cm, left=15.1*cm, width=BAND_WIDTH,
                        get_value=lambda instance: instance.usuario_cancelacion if instance.usuario_cancelacion is not None else 'N/A'),

            Label(text='Observ. Canc.:', top=4.4*cm, left=0.1*cm, style={'fontName': 'Helvetica-Bold'}),
            ObjectValue(attribute_name='observaciones_cancelacion', top=4.4*cm, left=2.7*cm, width=BAND_WIDTH,
                        get_value=lambda instance: instance.observaciones_cancelacion if instance.observaciones_cancelacion is not None else 'N/A'),

            Label(text='Fecha/hora Canc.:', top=4.4*cm, left=12*cm, style={'fontName': 'Helvetica-Bold'}),
            ObjectValue(attribute_name='fecha_hora_cancelacion', top=4.4*cm, left=15.1*cm,
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
            # queryset_string = '%(object)s.pedidodetalle_set.all().raw("SELECT *, Row_Number() Over (Order By detalle.id) AS fila FROM ventas_pedidodetalle detalle where detalle.procesado=True and detalle.cancelado=False and detalle.pedido_id = %%s", [%(object)s.pk])',
            queryset_string = '%(object)s.pedidodetalle_set.all().raw("SELECT *, Row_Number() Over (Order By detalle.id) AS fila FROM ventas_pedidodetalle detalle where detalle.pedido_id = %%s", [%(object)s.pk])',
            band_header = ReportBand(
                height=1*cm,
                elements=[
                    Label(text='Item', top=0.3*cm, left=0.1*cm, style={'fontName': 'Helvetica-Bold'}),
                    Label(text='Producto', top=0.3*cm, left=1*cm, style={'fontName': 'Helvetica-Bold'}),
                    Label(text='Precio', top=0.3*cm, left=8.6*cm, style={'fontName': 'Helvetica-Bold'}),
                    # Label(text='Un. Med. Compra', top=0.3*cm, left=12*cm, style={'fontName': 'Helvetica-Bold'}),
                    Label(text='Cant.', top=0.3*cm, left=10.1*cm, style={'fontName': 'Helvetica-Bold'}),
                    Label(text='Total', top=0.3*cm, left=11.5*cm, style={'fontName': 'Helvetica-Bold'}),
                    Label(text='Fecha/hora', top=0.3*cm, left=13.2*cm, style={'fontName': 'Helvetica-Bold'}),
                    Label(text='Canc?', top=0.3*cm, left=15.7*cm, style={'fontName': 'Helvetica-Bold'}),
                    Label(text='Proc?', top=0.3*cm, left=16.9*cm, style={'fontName': 'Helvetica-Bold'}),
                    ],
                borders={'top': True, 'bottom': True, 'left': True, 'right': True},
                # borders = {'bottom': Line(stroke_color=red, stroke_width=3)}
            ),
            band_detail = ReportBand(
                height=1*cm,
                # width=12*cm,
                elements=[
                    ObjectValue(attribute_name='fila', top=0.3*cm, left=0.2*cm),
                    ObjectValue(attribute_name='producto_pedido', top=0.3*cm, left=1*cm, width=7.5*cm),
                    ObjectValue(attribute_name='precio_producto_pedido', top=0.3*cm, left=7.7*cm, width=2*cm, style={'alignment': TA_RIGHT},
                                get_value=lambda instance: '{0:n}'.format(instance.precio_producto_pedido)),
                    # ObjectValue(attribute_name='unidad_medida_orden_compra', top=0.3*cm, left=18*cm),
                    ObjectValue(attribute_name='cantidad_producto_pedido', top=0.3*cm, left=10*cm, width=1*cm, style={'alignment': TA_CENTER},
                                get_value=lambda instance: '{0:n}'.format(int(instance.cantidad_producto_pedido))),
                    ObjectValue(attribute_name='total_producto_pedido', top=0.3*cm, left=10.4*cm, width=2*cm, style={'alignment': TA_RIGHT},
                                get_value=lambda instance: '{0:n}'.format(instance.total_producto_pedido)),
                    ObjectValue(attribute_name='fecha_pedido_detalle', top=0.3*cm, left=12.8*cm,
                                get_value=lambda instance: timezone.localtime(instance.fecha_pedido_detalle).strftime('%d/%m/%Y %H:%M') if instance.fecha_pedido_detalle is not None else 'N/A'),
                    ObjectValue(attribute_name='cancelado', top=0.3*cm, left=16*cm,
                                get_value=lambda instance: instance.cancelado and 'Si' or 'No'),
                    ObjectValue(attribute_name='procesado', top=0.3*cm, left=17.1*cm,
                                get_value=lambda instance: instance.procesado and 'Si' or 'No'),
                    ],
                borders={'left': True, 'right': True},
            ),
            band_footer = ReportBand(
                height=1*cm,
                elements=[
                    Label(text='Total Pedido', top=0.3*cm, left=10*cm, style={'fontName': 'Helvetica-Bold'}),
                    ObjectValue(attribute_name='total_producto_pedido', top=0.15*cm, left=-1*cm, width=BAND_WIDTH,
                                action=FIELD_ACTION_SUM,  # display_format='{:,}'.format('%n'),  # float(str('%s')),  #float('%s'),
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
        height = 3.3*cm
        # margin_top=0.5*cm
        # margin_bottom=0.5*cm
        # queryset_string = '%(object)s.ordencompradetalle_set.all()',

        elements = [

            ObjectValue(attribute_name='empresa.proveedor', top=-3*cm, left=0, width=16*cm,
                        style={'fontName': 'Helvetica-Bold', 'fontSize': 18, 'alignment': TA_CENTER}),

            ObjectValue(attribute_name='empresa.actividad_economica', top=-2*cm, left=0, width=16*cm,
                        style={'fontName': 'Helvetica', 'fontSize': 12, 'alignment': TA_CENTER}),

            ObjectValue(attribute_name='empresa.direccion', top=-1.5*cm, left=0, width=16*cm,
                        style={'fontName': 'Helvetica', 'fontSize': 10, 'alignment': TA_CENTER}),

            ObjectValue(attribute_name='empresa.ciudad', top=-1*cm, left=6.4*cm, width=16*cm,
                        style={'fontName': 'Helvetica', 'fontSize': 10}),
            Label(text='-', top=-1*cm, left=0*cm, width=16*cm, style={'fontName': 'Helvetica', 'fontSize': 10, 'alignment': TA_CENTER}),
            ObjectValue(attribute_name='empresa.pais', top=-1*cm, left=8.2*cm, width=16*cm,
                        style={'fontName': 'Helvetica', 'fontSize': 10}),

            Label(text=u'Tel.:', top=-0.5*cm, left=4.2*cm, width=16*cm, style={'fontName': 'Helvetica', 'fontSize': 10}),
            ObjectValue(attribute_name='empresa', top=-0.5*cm, left=5*cm, width=BAND_WIDTH,
                        # get_value=lambda instance: instance.cliente_factura.clientetelefono_set if instance.cliente_factura.clientetelefono_set is not None else 'N/A'),
                        get_value=lambda instance: " - ".join(['%s%s%s' % (t.codigo_pais_telefono.codigo_pais_telefono, t.codigo_operadora_telefono.codigo_operadora_telefono, t.telefono) for t in ProveedorTelefono.objects.filter(proveedor_id=instance.empresa.pk)]) if instance.empresa is not None else 'N/A'),

            Label(text='-', top=-0.5*cm, left=7.5*cm, width=16*cm, style={'fontName': 'Helvetica', 'fontSize': 10}),
            ObjectValue(attribute_name='empresa.pagina_web', top=-0.5*cm, left=7.7*cm, width=16*cm, style={'fontName': 'Helvetica', 'fontSize': 10}),

            # ==========================================================================================================
            Line(left=12.5*cm, top=-3*cm, right=12.5*cm, bottom=0*cm),
            # ==========================================================================================================

            Label(text='Timbrado N°:', top=-3*cm, left=13.3*cm, style={'fontName': 'Helvetica-Bold'}),
            ObjectValue(attribute_name='timbrado.timbrado', top=-3*cm, left=15.6*cm, width=11*cm),

            Label(text='Fecha Inicio Vig.:', top=-2.5*cm, left=12.9*cm, style={'fontName': 'Helvetica-Bold'}),
            ObjectValue(attribute_name='timbrado.fecha_autorizacion_timbrado', top=-2.5*cm, left=15.9*cm, width=11*cm,
                        get_value=lambda instance: instance.timbrado.fecha_autorizacion_timbrado.strftime('%d/%m/%Y')),

            Label(text='Fecha Fin Vig.:', top=-2*cm, left=13.1*cm, style={'fontName': 'Helvetica-Bold'}),
            ObjectValue(attribute_name='timbrado.fecha_limite_vigencia_timbrado', top=-2*cm, left=15.8*cm, width=11*cm,
                        get_value=lambda instance: instance.timbrado.fecha_limite_vigencia_timbrado.strftime('%d/%m/%Y')),

            Label(text='RUC:', top=-1.5*cm, left=13.7*cm, style={'fontName': 'Helvetica-Bold'}),
            ObjectValue(attribute_name='empresa.ruc', top=-1.5*cm, left=14.7*cm, width=11*cm, style={'fontName': 'Helvetica-Bold'}),
            Label(text='-', top=-1.5*cm, left=16.3*cm, style={'fontName': 'Helvetica-Bold'}),
            ObjectValue(attribute_name='empresa.digito_verificador', top=-1.5*cm, left=16.5*cm, width=11*cm, style={'fontName': 'Helvetica-Bold'}),

            Label(text="FACTURA N°:", top=-1*cm, left=12.5*cm, width=5.5*cm,
                  style={'fontName': 'Helvetica-Bold', 'fontSize': 12, 'alignment': TA_CENTER}),

            ObjectValue(attribute_name='empresa.codigo_establecimiento', top=-0.5*cm, left=13.3*cm, width=BAND_WIDTH,
                        style={'fontName': 'Helvetica-Bold', 'fontSize': 12}),
            Label(text='-', top=-0.5*cm, left=14.1*cm, style={'fontName': 'Helvetica-Bold', 'fontSize': 12}),
            ObjectValue(attribute_name='apertura_caja.caja.punto_expedicion', top=-0.5*cm, left=14.4*cm, width=BAND_WIDTH,
                        style={'fontName': 'Helvetica-Bold', 'fontSize': 12}),
            Label(text='-', top=-0.5*cm, left=15.2*cm, style={'fontName': 'Helvetica-Bold', 'fontSize': 12}),
            ObjectValue(attribute_name='numero_factura_venta.numero_factura', top=-0.5*cm, left=15.5*cm, width=BAND_WIDTH,
                        style={'fontName': 'Helvetica-Bold', 'fontSize': 12},
                        get_value=lambda instance: '{:0>7}'.format(instance.numero_factura_venta.numero_factura)),

            # ==========================================================================================================
            Label(text=u'FECHA DE EMISION:', top=0.2*cm, left=0.1*cm, width=BAND_WIDTH, style={'fontName': 'Helvetica-Bold', 'alignment': TA_LEFT}),
            SystemField(expression=u'%(now:%d/%m/%Y)s', top=0.2*cm, left=3.7*cm, width=BAND_WIDTH, style={'alignment': TA_LEFT}),
            Label(text=u'CONDICION DE VENTA:', top=0.2*cm, left=6*cm, width=BAND_WIDTH, style={'fontName': 'Helvetica-Bold', 'alignment': TA_LEFT}),
            Label(text=u'CONTADO', top=0.2*cm, left=10.1*cm, width=BAND_WIDTH, style={'alignment': TA_LEFT}),
            Label(text=u'NOTA DE REMISION N°:', top=0.2*cm, left=12.5*cm, width=BAND_WIDTH, style={'fontName': 'Helvetica-Bold', 'alignment': TA_LEFT}),
            Line(left=0*cm, top=0.8*cm, right=18*cm, bottom=0.8*cm),

            # ==========================================================================================================

            Label(text=u'Nombre o Razón Social:', top=1*cm, left=0.1*cm, style={'fontName': 'Helvetica-Bold'}),
            ObjectValue(attribute_name='cliente_factura', top=1*cm, left=4.2*cm, width=BAND_WIDTH,
                        get_value=lambda instance: instance.cliente_factura.nombre_completo if instance.cliente_factura is not None else 'N/A'),

            Label(text=u'Documento:', top=1*cm, left=12.6*cm, style={'fontName': 'Helvetica-Bold'}),
            ObjectValue(attribute_name='cliente_documento_factura', top=1*cm, left=14.7*cm, width=11*cm,
                        # get_value=lambda instance: '{0:n}'.format(instance.cliente_documento_factura) if instance.cliente_documento_factura is not None else 'N/A'),
                        get_value=lambda instance: instance.cliente_documento_factura if instance.cliente_factura is not None else 'N/A'),

            Label(text=u'Dirección:', top=1.7*cm, left=0.1*cm, style={'fontName': 'Helvetica-Bold'}),
            ObjectValue(attribute_name='cliente_factura', top=1.7*cm, left=1.9*cm, width=10*cm,
                        get_value=lambda instance: instance.cliente_factura.direccion if instance.cliente_factura is not None else 'N/A'),

            Label(text=u'Teléfono:', top=1.7*cm, left=12*cm, style={'fontName': 'Helvetica-Bold'}),
            ObjectValue(attribute_name='cliente_factura', top=1.7*cm, left=13.7*cm, width=BAND_WIDTH,
                        # get_value=lambda instance: instance.cliente_factura.clientetelefono_set if instance.cliente_factura.clientetelefono_set is not None else 'N/A'),
                        get_value=lambda instance: " - ".join(['%s%s%s' % (t.codigo_pais_telefono.codigo_pais_telefono, t.codigo_operadora_telefono.codigo_operadora_telefono, t.telefono) for t in ClienteTelefono.objects.filter(cliente_id=instance.cliente_factura.pk)]) if instance.cliente_factura is not None else 'N/A'),

            Line(left=0*cm, top=2.4*cm, right=18*cm, bottom=2.4*cm),
            # ==========================================================================================================

            Label(text='Estado Venta:', top=2.6*cm, left=0.2*cm, width=5*cm,
                  style={'fontName': 'Helvetica-Bold', 'fontSize': 12, 'wordWrap': True, 'borderWidth': 1,
                         'borderColor': red, 'borderPadding': 3, 'borderRadius': 3, 'alignment': TA_LEFT}),
            ObjectValue(attribute_name='estado_venta', top=2.65*cm, left=3.2*cm, width=BAND_WIDTH),

            Label(text='Fecha/hora Venta:', top=2.6*cm, left=6.5*cm, style={'fontName': 'Helvetica-Bold'}),
            ObjectValue(attribute_name='fecha_hora_venta', top=2.6*cm, left=9.6*cm,
                        get_value=lambda instance: timezone.localtime(instance.fecha_hora_venta).strftime('%d/%m/%Y %H:%M')),

            # Se imprimen solo las Facturas de las Ventas que fueron procesadas correctamente, NO se imprimen las Ventas canceladas.
            # Label(text='Motivo Canc.:', top=3.3*cm, left=0.1*cm, style={'fontName': 'Helvetica-Bold'}),
            # ObjectValue(attribute_name='motivo_cancelacion', top=3.3*cm, left=2.5*cm, width=BAND_WIDTH,
            #             get_value=lambda instance: instance.motivo_cancelacion if instance.motivo_cancelacion is not None else 'N/A'),
            #
            # Label(text='Cancelado por:', top=3.3*cm, left=12.9*cm, style={'fontName': 'Helvetica-Bold'}),
            # ObjectValue(attribute_name='usuario_cancelacion', top=3.3*cm, left=15.5*cm, width=BAND_WIDTH,
            #             get_value=lambda instance: instance.usuario_cancelacion if instance.usuario_cancelacion is not None else 'N/A'),
            #
            # Label(text='Observ. Canc.:', top=3.9*cm, left=0.1*cm, style={'fontName': 'Helvetica-Bold'}),
            # ObjectValue(attribute_name='observaciones_cancelacion', top=3.9*cm, left=2.7*cm, width=BAND_WIDTH,
            #             get_value=lambda instance: instance.observaciones_cancelacion if instance.observaciones_cancelacion is not None else 'N/A'),
            #
            # Label(text='Fecha/hora Canc.:', top=3.9*cm, left=12*cm, style={'fontName': 'Helvetica-Bold'}),
            # ObjectValue(attribute_name='fecha_hora_cancelacion', top=3.9*cm, left=15.1*cm,
            #             get_value=lambda instance: timezone.localtime(instance.fecha_hora_cancelacion).strftime('%d/%m/%Y %H:%M') if instance.fecha_hora_cancelacion is not None else 'N/A'),
        ]

        borders = {'bottom': True, 'top': True, 'right': True, 'left': True}

    class band_page_header(ReportBand):
        height = 3*cm
        elements = [
            # SystemField(expression='%(report_title)s', top=0.5*cm, left=0, width=BAND_WIDTH,
            #             style={'fontName': 'Helvetica-Bold', 'fontSize': 18, 'alignment': TA_CENTER}),
            Image(left=0.1*cm, top=0.1*cm, width=5*cm, height=3*cm,
                  filename=os.path.join(BASE_DIR, "static/compras/empresa/logo_Kilk.JPG")),
        ]
        borders = {'bottom': True, 'top': True, 'right': True, 'left': True}

    class band_page_footer(ReportBand):
        height = 1*cm
        elements = [
                Label(text='SIGB Reportes', top=0.1*cm),
                # SystemField(expression=u'Impreso el %(now:%d de %B de %Y)s a las %(now:%H:%M)s', top=0.1*cm,
                SystemField(expression=u'Impreso el %(now:%d/%m/%Y)s a las %(now:%H:%M)s', top=0.6*cm,
                            width=BAND_WIDTH, style={'alignment': TA_LEFT}),
                SystemField(expression=u'Pagina %(page_number)d de %(page_count)d', top=0.1*cm, width=BAND_WIDTH,
                            style={'alignment': TA_CENTER}),
                Label(text='ORIGINAL: CLIENTE', top=0.1*cm, width=BAND_WIDTH, style={'alignment': TA_RIGHT}),
                ]
        borders = {'top': True}

    subreports = [
        SubReport(
            # queryset_string = '%(object)s.ordencompradetalle_set.all()',
            # queryset_string = '%(object)s.ventadetalle_set.all().raw("SELECT *, Row_Number() Over (Order By detalle.id) AS fila FROM ventas_ventadetalle detalle where detalle.procesado=True and detalle.anulado=False and detalle.pedido_id = %%s", [%(object)s.pk])',
            queryset_string = '%(object)s.ventadetalle_set.all().raw("SELECT *, Row_Number() Over (Order By detalle.id) AS fila FROM ventas_ventadetalle detalle where detalle.venta_id = %%s", [%(object)s.pk])',
            band_header = ReportBand(
                height=1*cm,
                elements=[
                    Label(text='Cant.', top=0.3*cm, left=0.2*cm, style={'fontName': 'Helvetica-Bold'}),
                    Line(left=1.2*cm, top=0*cm, right=1.2*cm, bottom=1*cm),
                    # Line(left=12.5*cm, top=-3*cm, right=12.5*cm, bottom=0*cm),
                    # Label(text='Item', top=0.3*cm, left=0.3*cm, style={'fontName': 'Helvetica-Bold'}),
                    Label(text='Producto', top=0.3*cm, left=1.5*cm, style={'fontName': 'Helvetica-Bold'}),
                    Line(left=9.4*cm, top=0*cm, right=9.4*cm, bottom=1*cm),
                    Label(text='Precio', top=0.3*cm, left=9.9*cm, style={'fontName': 'Helvetica-Bold'}),
                    Line(left=11.3*cm, top=0*cm, right=11.3*cm, bottom=1*cm),
                    # Label(text='Un. Med. Compra', top=0.3*cm, left=12*cm, style={'fontName': 'Helvetica-Bold'}),
                    Label(text='VALOR DE VENTA', top=0.05*cm, left=11.3*cm, width=6.7*cm, style={'fontName': 'Helvetica-Bold', 'alignment': TA_CENTER}),
                    Line(left=11.3*cm, top=0.5*cm, right=18*cm, bottom=0.5*cm),
                    Label(text='Exentas', top=0.55*cm, left=11.4*cm, width=2.1*cm, style={'fontName': 'Helvetica-Bold', 'alignment': TA_CENTER}),
                    Line(left=13.4*cm, top=0.5*cm, right=13.4*cm, bottom=1*cm),
                    Label(text='5%', top=0.55*cm, left=13.6*cm, width=2.1*cm, style={'fontName': 'Helvetica-Bold', 'alignment': TA_CENTER}),
                    Line(left=15.7*cm, top=0.5*cm, right=15.7*cm, bottom=1*cm),
                    Label(text='10%', top=0.55*cm, left=15.9*cm, width=2.33*cm, style={'fontName': 'Helvetica-Bold', 'alignment': TA_CENTER}),
                    ],
                borders={'top': True, 'bottom': True, 'left': True, 'right': True},
                # borders = {'bottom': Line(stroke_color=red, stroke_width=3)}
            ),
            band_detail = ReportBand(
                height=1*cm,
                # width=12*cm,
                elements=[
                    ObjectValue(attribute_name='cantidad_producto_venta', top=0.3*cm, left=0.2*cm, width=1*cm, style={'alignment': TA_CENTER},
                                # get_value=lambda instance: '{0:n}'.format(instance.cantidad_producto_venta)),
                                get_value=lambda instance: '{0:n}'.format(int(instance.cantidad_producto_venta))),
                    Line(left=1.2*cm, top=0*cm, right=1.2*cm, bottom=1*cm),
                    # ObjectValue(attribute_name='fila', top=0.3*cm, left=0.3*cm),
                    ObjectValue(attribute_name='producto_venta', top=0.3*cm, left=1.5*cm, width=7.5*cm),
                    Line(left=9.4*cm, top=0*cm, right=9.4*cm, bottom=1*cm),
                    ObjectValue(attribute_name='precio_producto_venta', top=0.3*cm, left=9.1*cm, width=2*cm, style={'alignment': TA_RIGHT},
                                get_value=lambda instance: '{0:n}'.format(instance.precio_producto_venta)),
                    Line(left=11.3*cm, top=0*cm, right=11.3*cm, bottom=1*cm),
                    Label(text='-', top=0.3*cm, left=11.3*cm, width=2.1*cm, style={'alignment': TA_CENTER}),
                    Line(left=13.4*cm, top=0*cm, right=13.4*cm, bottom=1*cm),
                    Label(text='-', top=0.3*cm, left=13.4*cm, width=2.1*cm, style={'alignment': TA_CENTER}),
                    Line(left=15.7*cm, top=0*cm, right=15.7*cm, bottom=1*cm),
                    # ObjectValue(attribute_name='unidad_medida_orden_compra', top=0.3*cm, left=18*cm),
                    ObjectValue(attribute_name='total_producto_venta', top=0.3*cm, left=15.9*cm, width=2.33*cm, style={'alignment': TA_CENTER},
                                get_value=lambda instance: '{0:n}'.format(instance.total_producto_venta)),
                    # ObjectValue(attribute_name='fecha_pedido_detalle', top=0.3*cm, left=15*cm,
                    #             get_value=lambda instance: timezone.localtime(instance.fecha_pedido_detalle).strftime('%d/%m/%Y %H:%M') if instance.fecha_pedido_detalle is not None else 'N/A'),
                    ],
                borders={'left': True, 'right': True},
            ),
            band_footer = ReportBand(
                height=2*cm,
                elements=[
                    Label(text='SUBTOTALES:', top=0.1*cm, left=0.2*cm, width=BAND_WIDTH, style={'fontName': 'Helvetica-Bold', 'alignment': TA_LEFT}),
                    Line(left=11.3*cm, top=0*cm, right=11.3*cm, bottom=0.7*cm),
                    Label(text='-', top=0.1*cm, left=11.3*cm, width=2.1*cm, style={'alignment': TA_CENTER}),
                    Line(left=13.4*cm, top=0*cm, right=13.4*cm, bottom=0.7*cm),
                    Label(text='-', top=0.1*cm, left=13.4*cm, width=2.1*cm, style={'alignment': TA_CENTER}),
                    Line(left=15.7*cm, top=0*cm, right=15.7*cm, bottom=0.7*cm),
                    ObjectValue(attribute_name='numero_pedido.total_pedido', top=0.1*cm, left=15.9*cm, width=2.33*cm, style={'alignment': TA_CENTER},
                                get_value=lambda instance: '{0:n}'.format(int(instance.numero_pedido.total_pedido))),
                                # action=FIELD_ACTION_SUM),  # display_format='%s permissions found',
                    Line(left=0*cm, top=0.7*cm, right=18*cm, bottom=0.7*cm),

                    Label(text='TOTAL A PAGAR GUARANIES:', top=0.8*cm, left=0.2*cm, width=BAND_WIDTH, style={'fontName': 'Helvetica-Bold', 'alignment': TA_LEFT}),
                    Line(left=15.7*cm, top=0.7*cm, right=15.7*cm, bottom=1.4*cm),
                    ObjectValue(attribute_name='total_producto_venta', top=0.8*cm, left=15.9*cm, width=2.33*cm, style={'alignment': TA_CENTER},
                                action=FIELD_ACTION_SUM),  # display_format='%s permissions found',
                    Line(left=0*cm, top=1.4*cm, right=18*cm, bottom=1.4*cm),

                    Label(text='LIQUIDACION DEL IVA:', top=1.5*cm, left=0.2*cm, width=BAND_WIDTH, style={'fontName': 'Helvetica-Bold', 'alignment': TA_LEFT}),
                    Label(text='(5%):', top=1.5*cm, left=5*cm, width=BAND_WIDTH, style={'fontName': 'Helvetica-Bold', 'alignment': TA_LEFT}),
                    Label(text='-', top=1.5*cm, left=6*cm, width=3*cm, style={'alignment': TA_LEFT}),
                    Label(text='(10%):', top=1.5*cm, left=9*cm, width=BAND_WIDTH, style={'fontName': 'Helvetica-Bold', 'alignment': TA_LEFT}),
                    ObjectValue(attribute_name='numero_pedido.total_pedido', top=1.5*cm, left=10.2*cm, width=3*cm, style={'alignment': TA_LEFT},
                                get_value=lambda instance: '{0:n}'.format(int(instance.numero_pedido.total_pedido/11))),
                    Label(text='TOTAL IVA:', top=1.5*cm, left=13*cm, width=BAND_WIDTH, style={'fontName': 'Helvetica-Bold', 'alignment': TA_LEFT}),
                    ObjectValue(attribute_name='numero_pedido.total_pedido', top=1.5*cm, left=15.1*cm, width=2.5*cm, style={'alignment': TA_LEFT},
                                get_value=lambda instance: '{0:n}'.format(int(instance.numero_pedido.total_pedido/11))),
                    ],
                borders={'top': True, 'bottom': True, 'left': True, 'right': True},
            ),
        ),
    ]


class CierreCajaReport(Report):
    title = 'Cierre de Caja'
    author = 'Pedro Molas'

    page_size = A4
    margin_left = 1.5*cm
    margin_top = 0.5*cm
    margin_right = 1.5*cm
    margin_bottom = 0.5*cm

    class band_detail(ReportBand):
        height = 4.5*cm
        margin_top=0.5*cm
        # margin_bottom=0.5*cm
        elements = [
            Label(text="ID Apert. Caja:", top=0.2*cm, left=13*cm, width=4.8*cm,
                  style={'fontName': 'Helvetica-Bold', 'fontSize': 12, 'wordWrap': True, 'borderWidth': 1,
                         'borderColor': red, 'borderPadding': 4, 'borderRadius': 5, 'alignment': TA_LEFT}),
            ObjectValue(attribute_name='apertura_caja.id', top=0.2*cm, left=-0.2*cm, width=BAND_WIDTH,
                        style={'fontName': 'Helvetica-Bold', 'fontSize': 12, 'alignment': TA_RIGHT}),

            Label(text='Cajero:', top=0.3*cm, left=0.1*cm, style={'fontName': 'Helvetica-Bold'}),
            ObjectValue(attribute_name='apertura_caja.cajero', top=0.3*cm, left=1.4*cm, width=BAND_WIDTH,
                        get_value=lambda instance: '%s - %s' % (instance.apertura_caja.cajero, instance.apertura_caja.cajero.nombre_completo) if instance.apertura_caja is not None else 'N/A'),

            Label(text='Caja:', top=1*cm, left=0.1*cm, style={'fontName': 'Helvetica-Bold'}),
            ObjectValue(attribute_name='apertura_caja.caja', top=1*cm, left=1.1*cm,
                        get_value=lambda instance: instance.apertura_caja.caja if instance.apertura_caja is not None else 'N/A'),

            Label(text='Sector:', top=1*cm, left=7*cm, style={'fontName': 'Helvetica-Bold'}),
            ObjectValue(attribute_name='apertura_caja.sector', top=1*cm, left=8.3*cm,
                        get_value=lambda instance: instance.apertura_caja.sector if instance.apertura_caja is not None else 'N/A'),

            Label(text='Horario:', top=1*cm, left=12*cm, style={'fontName': 'Helvetica-Bold'}),
            ObjectValue(attribute_name='apertura_caja.horario', top=1*cm, left=13.4*cm, width=BAND_WIDTH,
                        get_value=lambda instance: instance.apertura_caja.horario if instance.apertura_caja is not None else 'N/A'),

            Label(text='Fecha/hora Apertura:', top=1.7*cm, left=0.1*cm, style={'fontName': 'Helvetica-Bold'}),
            ObjectValue(attribute_name='apertura_caja.fecha_hora_apertura_caja', top=1.7*cm, left=3.7*cm, width=BAND_WIDTH,
                        get_value=lambda instance: timezone.localtime(instance.apertura_caja.fecha_hora_apertura_caja).strftime('%d/%m/%Y %H:%M') if instance.apertura_caja is not None else 'N/A'),

            Label(text='Jornada:', top=1.7*cm, left=8*cm, style={'fontName': 'Helvetica-Bold'}),
            ObjectValue(attribute_name='apertura_caja.jornada', top=1.7*cm, left=9.5*cm, width=BAND_WIDTH,
                        get_value=lambda instance: instance.apertura_caja.jornada if instance.apertura_caja is not None else 'N/A'),

            Label(text='Estado Apertura:', top=2.4*cm, left=0.2*cm, width=5.3*cm,
                  style={'fontName': 'Helvetica-Bold', 'fontSize': 12, 'wordWrap': True, 'borderWidth': 1,
                         'borderColor': red, 'borderPadding': 3, 'borderRadius': 3, 'alignment': TA_LEFT}),
            ObjectValue(attribute_name='apertura_caja.estado_apertura_caja', top=2.45*cm, left=3.7*cm, width=BAND_WIDTH,
                        get_value=lambda instance: instance.apertura_caja.get_estado_apertura_caja_display() if instance.apertura_caja is not None else 'N/A'),

            Label(text='Fecha/hora Cierre:', top=2.4*cm, left=6*cm, style={'fontName': 'Helvetica-Bold'}),
            ObjectValue(attribute_name='fecha_hora_registro_cierre_caja', top=2.4*cm, left=9.2*cm, width=BAND_WIDTH,
                        get_value=lambda instance: timezone.localtime(instance.fecha_hora_registro_cierre_caja).strftime('%d/%m/%Y %H:%M') if instance.fecha_hora_registro_cierre_caja is not None else 'N/A'),

            Label(text='Usuario Cierre:', top=2.4*cm, left=12.4*cm, style={'fontName': 'Helvetica-Bold'}),
            ObjectValue(attribute_name='usuario_cierre_caja', top=2.4*cm, left=15*cm, width=BAND_WIDTH,
                        get_value=lambda instance: instance.usuario_cierre_caja.usuario.username if instance.usuario_cierre_caja is not None else 'N/A'),

            Line(left=0*cm, top=3*cm, right=18*cm, bottom=3*cm),

            Label(text='RESUMEN DE VENTAS', top=3.7*cm, left=0.1*cm, width=BAND_WIDTH, style={'fontName': 'Helvetica-Bold', 'fontSize': 14, 'alignment': TA_LEFT}),

            Line(left=0*cm, top=4.5*cm, right=18*cm, bottom=4.5*cm),
            # ==========================================================================================================
            # Encabezado - Columnas
            Line(left=0*cm, top=4.5*cm, right=0*cm, bottom=9.6*cm),
            Label(text='Item', top=4.6*cm, left=0.1*cm, width=1*cm, style={'fontName': 'Helvetica-Bold', 'alignment': TA_CENTER}),
            Line(left=1.1*cm, top=4.5*cm, right=1.1*cm, bottom=8.8*cm),
            Label(text='Forma de Pago', top=4.6*cm, left=1*cm, width=3*cm, style={'fontName': 'Helvetica-Bold', 'alignment': TA_CENTER}),
            Line(left=4.1*cm, top=4.5*cm, right=4.1*cm, bottom=8.8*cm),
            Label(text='Op. Proc.', top=4.6*cm, left=4*cm, width=2*cm, style={'fontName': 'Helvetica-Bold', 'alignment': TA_CENTER}),
            Line(left=6*cm, top=4.5*cm, right=6*cm, bottom=8.8*cm),
            Label(text='Op. Pend.', top=4.6*cm, left=6*cm, width=2*cm, style={'fontName': 'Helvetica-Bold', 'alignment': TA_CENTER}),
            Line(left=8*cm, top=4.5*cm, right=8*cm, bottom=8.8*cm),
            Label(text='Op. Canc.', top=4.6*cm, left=8*cm, width=2*cm, style={'fontName': 'Helvetica-Bold', 'alignment': TA_CENTER}),
            Line(left=10*cm, top=4.5*cm, right=10*cm, bottom=8.8*cm),
            Label(text='Monto Reg.', top=4.6*cm, left=10*cm, width=2.5*cm, style={'fontName': 'Helvetica-Bold', 'alignment': TA_CENTER}),
            Line(left=12.4*cm, top=4.5*cm, right=12.4*cm, bottom=8.8*cm),
            Label(text='Rendicion', top=4.6*cm, left=12.5*cm, width=2.5*cm, style={'fontName': 'Helvetica-Bold', 'alignment': TA_CENTER}),
            Line(left=14.9*cm, top=4.5*cm, right=14.9*cm, bottom=9.6*cm),
            Label(text='Diferencia', top=4.6*cm, left=15*cm, width=3*cm, style={'fontName': 'Helvetica-Bold', 'alignment': TA_CENTER}),
            Line(left=18*cm, top=4.5*cm, right=18*cm, bottom=9.6*cm),
            Line(left=0*cm, top=5.1*cm, right=18*cm, bottom=5.1*cm),

            # Detalle - Filas
            Label(text='1', top=5.3*cm, left=0.1*cm, width=1*cm, style={'alignment': TA_CENTER}),
            Label(text='2', top=6*cm, left=0.1*cm, width=1*cm, style={'alignment': TA_CENTER}),
            Label(text='3', top=6.7*cm, left=0.1*cm, width=1*cm, style={'alignment': TA_CENTER}),
            Label(text='4', top=7.4*cm, left=0.1*cm, width=1*cm, style={'alignment': TA_CENTER}),
            Label(text='5', top=8.1*cm, left=0.1*cm, width=1*cm, style={'alignment': TA_CENTER}),

            Label(text='Monto Apertura', top=5.3*cm, left=1*cm, width=3*cm, style={'alignment': TA_CENTER}),
            Label(text='Efectivo', top=6*cm, left=1*cm, width=3*cm, style={'alignment': TA_CENTER}),
            Label(text='TCs', top=6.7*cm, left=1*cm, width=3*cm, style={'alignment': TA_CENTER}),
            Label(text='TDs', top=7.4*cm, left=1*cm, width=3*cm, style={'alignment': TA_CENTER}),
            Label(text='Otros Medios', top=8.1*cm, left=1*cm, width=3*cm, style={'alignment': TA_CENTER}),

            Label(text='-', top=5.3*cm, left=4*cm, width=2*cm, style={'alignment': TA_CENTER}),
            ObjectValue(attribute_name='cantidad_operaciones_efectivo_procesadas', top=6*cm, left=4*cm, width=2*cm, style={'alignment': TA_CENTER}),
            ObjectValue(attribute_name='cantidad_operaciones_tcs_procesadas', top=6.7*cm, left=4*cm, width=2*cm, style={'alignment': TA_CENTER}),
            ObjectValue(attribute_name='cantidad_operaciones_tds_procesadas', top=7.4*cm, left=4*cm, width=2*cm, style={'alignment': TA_CENTER}),
            ObjectValue(attribute_name='cantidad_operaciones_otros_medios_procesadas', top=8.1*cm, left=4*cm, width=2*cm, style={'alignment': TA_CENTER}),

            Label(text='-', top=5.3*cm, left=6*cm, width=2*cm, style={'alignment': TA_CENTER}),
            ObjectValue(attribute_name='cantidad_operaciones_efectivo_pendientes', top=6*cm, left=6*cm, width=2*cm, style={'alignment': TA_CENTER}),
            ObjectValue(attribute_name='cantidad_operaciones_tcs_pendientes', top=6.7*cm, left=6*cm, width=2*cm, style={'alignment': TA_CENTER}),
            ObjectValue(attribute_name='cantidad_operaciones_tds_pendientes', top=7.4*cm, left=6*cm, width=2*cm, style={'alignment': TA_CENTER}),
            ObjectValue(attribute_name='cantidad_operaciones_otros_medios_pendientes', top=8.1*cm, left=6*cm, width=2*cm, style={'alignment': TA_CENTER}),

            Label(text='-', top=5.3*cm, left=8*cm, width=2*cm, style={'alignment': TA_CENTER}),
            ObjectValue(attribute_name='cantidad_operaciones_efectivo_canceladas', top=6*cm, left=8*cm, width=2*cm, style={'alignment': TA_CENTER}),
            ObjectValue(attribute_name='cantidad_operaciones_tcs_canceladas', top=6.7*cm, left=8*cm, width=2*cm, style={'alignment': TA_CENTER}),
            ObjectValue(attribute_name='cantidad_operaciones_tds_canceladas', top=7.4*cm, left=8*cm, width=2*cm, style={'alignment': TA_CENTER}),
            ObjectValue(attribute_name='cantidad_operaciones_otros_medios_canceladas', top=8.1*cm, left=8*cm, width=2*cm, style={'alignment': TA_CENTER}),

            ObjectValue(attribute_name='instance.apertura_caja.monto_apertura', top=5.3*cm, left=10*cm, width=2.5*cm, style={'alignment': TA_CENTER},
                        get_value=lambda instance: '{0:n}'.format(instance.apertura_caja.monto_apertura)),
            ObjectValue(attribute_name='monto_registro_efectivo', top=6*cm, left=10*cm, width=2.5*cm, style={'alignment': TA_CENTER},
                        get_value=lambda instance: '{0:n}'.format(instance.monto_registro_efectivo+instance.apertura_caja.monto_apertura)),
            ObjectValue(attribute_name='monto_registro_tcs', top=6.7*cm, left=10*cm, width=2.5*cm, style={'alignment': TA_CENTER},
                        get_value=lambda instance: '{0:n}'.format(instance.monto_registro_tcs)),
            ObjectValue(attribute_name='monto_registro_tds', top=7.4*cm, left=10*cm, width=2.5*cm, style={'alignment': TA_CENTER},
                        get_value=lambda instance: '{0:n}'.format(instance.monto_registro_tds)),
            ObjectValue(attribute_name='monto_registro_otros_medios', top=8.1*cm, left=10*cm, width=2.5*cm, style={'alignment': TA_CENTER},
                        get_value=lambda instance: '{0:n}'.format(instance.monto_registro_otros_medios)),

            Label(text='-', top=5.3*cm, left=12.5*cm, width=2.5*cm, style={'alignment': TA_CENTER}),
            ObjectValue(attribute_name='rendicion_efectivo', top=6*cm, left=12.5*cm, width=2.5*cm, style={'alignment': TA_CENTER},
                        get_value=lambda instance: '{0:n}'.format(instance.rendicion_efectivo)),
            ObjectValue(attribute_name='rendicion_tcs', top=6.7*cm, left=12.5*cm, width=2.5*cm, style={'alignment': TA_CENTER},
                        get_value=lambda instance: '{0:n}'.format(instance.rendicion_tcs)),
            ObjectValue(attribute_name='rendicion_tds', top=7.4*cm, left=12.5*cm, width=2.5*cm, style={'alignment': TA_CENTER},
                        get_value=lambda instance: '{0:n}'.format(instance.rendicion_tds)),
            ObjectValue(attribute_name='rendicion_otros_medios', top=8.1*cm, left=12.5*cm, width=2.5*cm, style={'alignment': TA_CENTER},
                        get_value=lambda instance: '{0:n}'.format(instance.rendicion_otros_medios)),

            Label(text='-', top=5.3*cm, left=15*cm, width=3*cm, style={'alignment': TA_CENTER}),
            ObjectValue(attribute_name='diferencia_efectivo', top=6*cm, left=15*cm, width=3*cm, style={'alignment': TA_CENTER},
                        get_value=lambda instance: '{0:n}'.format(instance.diferencia_efectivo)),
            ObjectValue(attribute_name='diferencia_tcs', top=6.7*cm, left=15*cm, width=3*cm, style={'alignment': TA_CENTER},
                        get_value=lambda instance: '{0:n}'.format(instance.diferencia_tcs)),
            ObjectValue(attribute_name='diferencia_tds', top=7.4*cm, left=15*cm, width=3*cm, style={'alignment': TA_CENTER},
                        get_value=lambda instance: '{0:n}'.format(instance.diferencia_tds)),
            ObjectValue(attribute_name='diferencia_otros_medios', top=8.1*cm, left=15*cm, width=3*cm, style={'alignment': TA_CENTER},
                        get_value=lambda instance: '{0:n}'.format(instance.diferencia_otros_medios)),
            # ==========================================================================================================
            Line(left=0*cm, top=8.8*cm, right=18*cm, bottom=8.8*cm),

            Label(text='TOTAL DIFERENCIA', top=9*cm, left=0.5*cm, width=15*cm, style={'fontName': 'Helvetica-Bold', 'alignment': TA_LEFT}),
            ObjectValue(attribute_name='total_diferencia', top=9*cm, left=15*cm, width=3*cm, style={'alignment': TA_CENTER},
                        get_value=lambda instance: '{0:n}'.format(instance.total_diferencia)),

            Line(left=0*cm, top=9.6*cm, right=18*cm, bottom=9.6*cm),

            Label(text='* OBS: Si el Total Diferencia es negativo el Cajero posee un sobrante.', top=9.8*cm, left=0.5*cm, width=BAND_WIDTH, style={'fontSize': 8, 'alignment': TA_LEFT}),

            # ==========================================================================================================
            Line(left=1.5*cm, top=15*cm, right=7.5*cm, bottom=15*cm),
            Label(text='Firma y sello Cajero', top=15.5*cm, left=0*cm, width=9*cm, style={'fontName': 'Helvetica-Bold', 'alignment': TA_CENTER}),
            ObjectValue(attribute_name='apertura_caja.cajero', top=16.2*cm, left=0*cm, width=9*cm, style={'alignment': TA_CENTER},
                        get_value=lambda instance: instance.apertura_caja.cajero.nombre_completo if instance.apertura_caja is not None else 'N/A'),

            Line(left=10.5*cm, top=15*cm, right=16.5*cm, bottom=15*cm),
            Label(text='Firma y sello Supervisor', top=15.5*cm, left=9*cm, width=9*cm, style={'fontName': 'Helvetica-Bold', 'alignment': TA_CENTER}),
        ]

        # borders = {'bottom': True}

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
                SystemField(expression=u'Impreso el %(now:%d %B de %Y)s a las %(now:%H:%M)s', top=0.1*cm,
                    width=BAND_WIDTH, style={'alignment': TA_RIGHT}),
                ]
        borders = {'top': True}