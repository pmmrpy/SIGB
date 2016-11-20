# -*- coding: utf-8 -*-
import datetime
from django.utils import timezone
from ventas.models import AperturaCaja, Pedido

__author__ = 'pmmr'

import json
from django.http.response import HttpResponse
from clientes.models import Reserva, Cliente, ClienteTelefono


def calcular_dv(numero, base=11):
    total = 0
    k = 2
    for i in range(len(numero) - 1, - 1, - 1):
        k = 2 if k > base else k
        total += int(numero[i]) * k
        k += 1
    resto = total % 11
    return (11 - resto) if resto > 1 else 0


def get_reserva(request):

    # import pdb
    # pdb.set_trace()

    if request.method == 'GET':
        id_reserva = request.GET.get('id_reserva', None)
        print 'get_reserva.id_reserva: ', id_reserva
        response_data = {}

        # try:
        #     reserva = Reserva.objects.get(pk=id_reserva)
        # except Reserva.DoesNotExist or ValueError:
        #     reserva = None
        # cliente = Cliente.objects.get(pk=reserva.cliente)

        if id_reserva != '' and id_reserva is not None:
            reserva = Reserva.objects.get(pk=id_reserva)
        else:
            reserva = None

        if id_reserva and reserva is not None:
            response_data.update({'cliente': {'id': str(reserva.cliente.pk), 'nombre_cliente': str(reserva.cliente.nombre_completo)}})
            # response_data.update({'documentos': [{'t_doc': str(d.tipo_documento.documento), 'num_doc': str(d.numero_documento)} for d in reserva.cliente.clientedocumento_set.all()]})
            response_data.update({'documentos': str(reserva.cliente_documento_reserva)})
            # response_data.update({'documentos': [{'t_doc': str(d.tipo_documento.documento), 'num_doc': str(d.numero_documento), 'dv': str(calcular_dv(d.numero_documento, 11)) if d.tipo_documento.documento == 'RUC' else 0} for d in cliente.clientedocumento_set.all()]})
            response_data.update({'monto_entrega': str(reserva.pago) or '0'})
            response_data.update({'mesas': [{'id': m.pk, 'descripcion': str(m)} for m in reserva.mesas.all()]})
        else:
            response_data.update({'cliente': {'id': '', 'nombre_cliente': ''}})
            # response_data.update({'documentos': [{'t_doc': '', 'num_doc': ''}]})
            response_data.update({'documentos': ''})
            response_data.update({'monto_entrega': '0'})
            response_data.update({'mesas': [{'id': '', 'descripcion': ''}]})

        # print response_data

        return HttpResponse(
            json.dumps(response_data),
            content_type="application/json"
        )


def get_cliente(request):

    # import pdb
    # pdb.set_trace()

    if request.method == 'GET':
        id_cliente = request.GET.get('id_cliente', False)
        print 'get_cliente.id_cliente: ', id_cliente
        response_data = {}

        if id_cliente != '':
            try:
                cliente = Cliente.objects.get(pk=id_cliente)
                # reserva = Reserva.objects.get(pk=id_reserva)
            except Cliente.DoesNotExist:
                cliente = None

            if cliente is not None:
                response_data.update({'cliente': {'id': str(cliente.pk), 'nombre_cliente': str(cliente.nombre_completo)}})
                response_data.update({'documentos': [{'t_doc': str(d.tipo_documento.documento), 'num_doc': str(d.numero_documento), 'dv': str(calcular_dv(d.numero_documento, 11)) if d.tipo_documento.documento == 'RUC' else 0} for d in cliente.clientedocumento_set.all()]})
                response_data.update({'direccion': unicode(cliente.direccion)})
                response_data.update({'pais': str(cliente.pais)})
                response_data.update({'ciudad': str(cliente.ciudad)})
                response_data.update({'telefonos': " - ".join(['%s%s%s' % (t.codigo_pais_telefono.codigo_pais_telefono, t.codigo_operadora_telefono.codigo_operadora_telefono, t.telefono) for t in ClienteTelefono.objects.filter(cliente_id=cliente.pk)])})
                response_data.update({'email': str(cliente.email)})

                # for d in cliente.clientedocumento_set.all():
                #     if d.tipo_documento.documento == 'RUC':
                #         response_data.update({'documentos': [{'t_doc': str(d.tipo_documento.documento), 'num_doc': str(d.numero_documento + '-') + str(calcular_dv(d.numero_documento, 11))}]})
                #     else:
                #         response_data.update({'documentos': [{'t_doc': str(d.tipo_documento.documento), 'num_doc': str(d.numero_documento)}]})

        else:
            response_data.update({'cliente': {'id': '', 'nombre_cliente': ''}})
            response_data.update({'documentos': [{'t_doc': '', 'num_doc': ''}]})
            response_data.update({'direccion': ''})
            response_data.update({'pais': ''})
            response_data.update({'ciudad': ''})
            response_data.update({'telefonos': ''})
            response_data.update({'email': ''})

        # print response_data

        return HttpResponse(
            json.dumps(response_data),
            content_type="application/json"
        )


def get_apertura_caja(request):

    # import pdb
    # pdb.set_trace()

    if request.method == 'GET':
        id_apertura_caja = request.GET.get('id_apertura_caja', False)
        print 'get_apertura_caja.id_apertura_caja: ', id_apertura_caja
        response_data = {}

        try:
            apertura = AperturaCaja.objects.get(pk=id_apertura_caja)
        except AperturaCaja.DoesNotExist:
            apertura = None

        if id_apertura_caja and apertura is not None:
            response_data.update({'cajero': str(apertura.cajero.nombre_completo)})
            response_data.update({'caja': str(apertura.caja)})
            response_data.update({'sector': str(apertura.sector)})
            response_data.update({'horario': str(apertura.horario)})
            response_data.update({'jornada': str(apertura.jornada)})
            response_data.update({'fecha_hora_apertura_caja': datetime.datetime.strftime(timezone.localtime(apertura.fecha_hora_apertura_caja), '%d/%m/%Y %H:%M')})
            response_data.update({'monto_apertura': str(apertura.monto_apertura) or '0'})
            response_data.update({'estado_apertura_caja': str(apertura.get_estado_apertura_caja_display())})
# ==> Cantidad Total Operaciones Pendientes <==
            response_data.update({'cantidad_total_operaciones_pendientes': str(apertura.get_cantidad_total_operaciones_pendientes()) or '0'})
# ==> Cantidad Total Operaciones Canceladas <==
            response_data.update({'cantidad_total_operaciones_canceladas': str(apertura.get_cantidad_total_operaciones_canceladas()) or '0'})
# ==> Efectivo <==
            response_data.update({'cantidad_operaciones_efectivo_procesadas': str(apertura.get_cantidad_operaciones_efectivo_procesadas()) or '0'})
            response_data.update({'cantidad_operaciones_efectivo_pendientes': str(apertura.get_cantidad_operaciones_efectivo_pendientes()) or '0'})
            response_data.update({'cantidad_operaciones_efectivo_canceladas': str(apertura.get_cantidad_operaciones_efectivo_canceladas()) or '0'})
            response_data.update({'monto_registro_efectivo': str(apertura.get_monto_registro_efectivo()) if apertura.get_monto_registro_efectivo() is not None else '0'})
            response_data.update({'total_efectivo': str(apertura.get_monto_registro_efectivo() + apertura.monto_apertura) if apertura.get_monto_registro_efectivo() is not None else str(apertura.monto_apertura)})
# ==> TCs <==
            response_data.update({'cantidad_operaciones_tcs_procesadas': str(apertura.get_cantidad_operaciones_tcs_procesadas()) or '0'})
            response_data.update({'cantidad_operaciones_tcs_pendientes': str(apertura.get_cantidad_operaciones_tcs_pendientes()) or '0'})
            response_data.update({'cantidad_operaciones_tcs_canceladas': str(apertura.get_cantidad_operaciones_tcs_canceladas()) or '0'})
            response_data.update({'monto_registro_tcs': str(apertura.get_monto_registro_tcs()) if apertura.get_monto_registro_tcs() is not None else '0'})
# ==> TDs <==
            response_data.update({'cantidad_operaciones_tds_procesadas': str(apertura.get_cantidad_operaciones_tds_procesadas()) or '0'})
            response_data.update({'cantidad_operaciones_tds_pendientes': str(apertura.get_cantidad_operaciones_tds_pendientes()) or '0'})
            response_data.update({'cantidad_operaciones_tds_canceladas': str(apertura.get_cantidad_operaciones_tds_canceladas()) or '0'})
            response_data.update({'monto_registro_tds': str(apertura.get_monto_registro_tds()) if apertura.get_monto_registro_tds() is not None else '0'})
# ==> Otros Medios de Pago <==
            response_data.update({'cantidad_operaciones_otros_medios_procesadas': str(apertura.get_cantidad_operaciones_otros_medios_procesadas()) or '0'})
            response_data.update({'cantidad_operaciones_otros_medios_pendientes': str(apertura.get_cantidad_operaciones_otros_medios_pendientes()) or '0'})
            response_data.update({'cantidad_operaciones_otros_medios_canceladas': str(apertura.get_cantidad_operaciones_otros_medios_canceladas()) or '0'})
            response_data.update({'monto_registro_otros_medios': str(apertura.get_monto_registro_otros_medios()) if apertura.get_monto_registro_otros_medios() is not None else '0'})
        else:
            response_data.update({'cajero': ''})
            response_data.update({'caja': ''})
            response_data.update({'sector': ''})
            response_data.update({'horario': ''})
            response_data.update({'jornada': ''})
            response_data.update({'fecha_hora_apertura_caja': ''})
            response_data.update({'monto_apertura': '0'})
            response_data.update({'estado_apertura_caja': ''})
            response_data.update({'cantidad_total_operaciones_pendientes': '0'})
            response_data.update({'cantidad_total_operaciones_canceladas': '0'})
# ==> Efectivo <==
            response_data.update({'cantidad_operaciones_efectivo_procesadas': '0'})
            response_data.update({'cantidad_operaciones_efectivo_pendientes': '0'})
            response_data.update({'cantidad_operaciones_efectivo_canceladas': '0'})
            response_data.update({'monto_registro_efectivo': '0'})
            response_data.update({'total_efectivo': '0'})
# ==> TCs <==
            response_data.update({'cantidad_operaciones_tcs_procesadas': '0'})
            response_data.update({'cantidad_operaciones_tcs_pendientes': '0'})
            response_data.update({'cantidad_operaciones_tcs_canceladas': '0'})
            response_data.update({'monto_registro_tcs': '0'})
# ==> TDs <==
            response_data.update({'cantidad_operaciones_tds_procesadas': '0'})
            response_data.update({'cantidad_operaciones_tds_pendientes': '0'})
            response_data.update({'cantidad_operaciones_tds_canceladas': '0'})
            response_data.update({'monto_registro_tds': '0'})
# ==> Otros Medios de Pago <==
            response_data.update({'cantidad_operaciones_otros_medios_procesadas': '0'})
            response_data.update({'cantidad_operaciones_otros_medios_pendientes': '0'})
            response_data.update({'cantidad_operaciones_otros_medios_canceladas': '0'})
            response_data.update({'monto_registro_otros_medios': '0'})

        # print response_data

        return HttpResponse(
            json.dumps(response_data),
            content_type="application/json"
        )


def get_pedido(request):

    # import pdb
    # pdb.set_trace()

    if request.method == 'GET':
        id_pedido = request.GET.get('id_pedido', False)
        print 'get_pedido.id_pedido: ', id_pedido
        response_data = {}

        if id_pedido != '':
            try:
                pedido = Pedido.objects.get(pk=id_pedido)
                # reserva = Reserva.objects.get(pk=id_reserva)
            except Pedido.DoesNotExist:
                pedido = None

            if pedido is not None:
                response_data.update({'total_pedido': str(pedido.total_pedido) or '0'})

                if pedido.reserva:
                    response_data.update({'reserva': str(pedido.reserva)})
                    response_data.update({'entrega_reserva': str(pedido.reserva.pago) or '0'})
                    response_data.update({'cliente': {'id': str(pedido.reserva.cliente.pk), 'nombre_cliente': str(pedido.reserva.cliente.nombre_completo)}})
                    response_data.update({'documentos': [{'t_doc': str(d.tipo_documento.documento), 'num_doc': str(d.numero_documento), 'dv': str(calcular_dv(d.numero_documento, 11)) if d.tipo_documento.documento == 'RUC' else 0} for d in pedido.reserva.cliente.clientedocumento_set.all()]})
                    response_data.update({'direccion': unicode(pedido.reserva.cliente.direccion)})
                    response_data.update({'pais': str(pedido.reserva.cliente.pais)})
                    response_data.update({'ciudad': str(pedido.reserva.cliente.ciudad)})
                    response_data.update({'telefonos': " - ".join(['%s%s%s' % (t.codigo_pais_telefono.codigo_pais_telefono, t.codigo_operadora_telefono.codigo_operadora_telefono, t.telefono) for t in ClienteTelefono.objects.filter(cliente_id=pedido.reserva.cliente.pk)])})
                    response_data.update({'email': str(pedido.reserva.cliente.email)})
                else:
                    response_data.update({'reserva': 'No posee Reserva'})
                    response_data.update({'entrega_reserva': '0'})
                    response_data.update({'cliente': {'id': '', 'nombre_cliente': ''}})
                    response_data.update({'documentos': [{'t_doc': '', 'num_doc': ''}]})
                    response_data.update({'direccion': ''})
                    response_data.update({'pais': ''})
                    response_data.update({'ciudad': ''})
                    response_data.update({'telefonos': ''})
                    response_data.update({'email': ''})

                # for d in cliente.clientedocumento_set.all():
                #     if d.tipo_documento.documento == 'RUC':
                #         response_data.update({'documentos': [{'t_doc': str(d.tipo_documento.documento), 'num_doc': str(d.numero_documento + '-') + str(calcular_dv(d.numero_documento, 11))}]})
                #     else:
                #         response_data.update({'documentos': [{'t_doc': str(d.tipo_documento.documento), 'num_doc': str(d.numero_documento)}]})

        else:
            response_data.update({'total_pedido': '0'})
            response_data.update({'reserva': 'No posee Reserva'})
            response_data.update({'entrega_reserva': '0'})
            response_data.update({'cliente': {'id': '', 'nombre_cliente': ''}})
            response_data.update({'documentos': [{'t_doc': '', 'num_doc': ''}]})
            response_data.update({'direccion': ''})
            response_data.update({'pais': ''})
            response_data.update({'ciudad': ''})
            response_data.update({'telefonos': ''})
            response_data.update({'email': ''})

        # print response_data

        return HttpResponse(
            json.dumps(response_data),
            content_type="application/json"
        )