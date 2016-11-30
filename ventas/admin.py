import datetime
from calendarium.models import Event, EventCategory
from django.contrib import admin

# Register your models here.
from django.core.exceptions import ValidationError, ObjectDoesNotExist
from django.forms.models import inlineformset_factory
from django.shortcuts import render
from django.utils.safestring import mark_safe
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone
from django.utils.html import format_html
from bar.models import ReservaEstado, Mesa, MesaEstado, FacturaVenta, NumeroFacturaVenta, PedidoEstado, Sector, Deposito, \
    VentaEstado
from personal.models import Empleado, Horario
from stock.models import ProductoCompuesto, ProductoVenta, MovimientoStock, ProductoCompuestoDetalle, Producto, \
    StockDepositoAjusteInventario
from ventas.forms import AperturaCajaForm, VentaForm, PedidoForm, PedidoDetalleInlineForm, InicioJornadaForm, \
    FinJornadaForm, CierreCajaForm, PedidoDetalleFormSet, CambiarJornada, VentaOcasionalDetalleForm
from ventas.models import Pedido, PedidoDetalle, Venta, VentaDetalle, Comanda, AperturaCaja, CierreCaja, VentaOcasionalDetalle, VentaOcasional, Jornada, InicioJornada, FinJornada


class PedidoDetalleInline(admin.TabularInline):
    model = PedidoDetalle
    extra = 0
    min_num = 1
    form = PedidoDetalleInlineForm
    formset = PedidoDetalleFormSet
    # fields = ['producto_pedido', 'precio_producto_pedido']
    readonly_fields = ['fecha_pedido_detalle', 'procesado']
    raw_id_fields = ['producto_pedido']
    # verbose_name =
    # verbose_name_plural =

    def get_readonly_fields(self, request, obj=None):

        # import pdb
        # pdb.set_trace()

        # Metodo para capturar datos del request
        # obj.total_orden_compra = request.POST.get('total_orden_compra', '')

        # if obj is not None and obj.estado_pedido == 'VIG' and self.procesado is False:
        #     return ['producto_pedido', 'precio_producto_pedido', 'cantidad_producto_pedido', 'total_producto_pedido',
        #             'fecha_pedido_detalle', 'procesado']
        # elif obj is not None and obj.estado_pedido == 'VIG' and self.procesado is True:
        #     return [i.name for i in self.model._meta.fields] + \
        #            [i.name for i in self.model._meta.many_to_many]
        if obj is not None and obj.estado_pedido.pedido_estado in ('PRO', 'CAN', 'PEN') \
                or obj is not None and obj.pk and obj.estado_pedido.pedido_estado == 'VIG' and obj.jornada.estado_jornada in ('EXP', 'CER'):
            return [i.name for i in self.model._meta.fields] + \
                   [i.name for i in self.model._meta.many_to_many]
        else:
            return super(PedidoDetalleInline, self).get_readonly_fields(request, obj)

    def has_delete_permission(self, request, obj=None):
        return False

    # def get_formset(self, request, obj=None, **kwargs):
    #
    #     formset = super(PedidoDetalleInline, self).get_formset(request, obj, **kwargs)
    #
    #     # import pdb
    #     # pdb.set_trace()
    #
    #     formset.request = request
    #     return formset


class PedidoAdmin(admin.ModelAdmin):
    form = PedidoForm

    class Media:
        js = [
            'ventas/js/pedido.js'
        ]

    readonly_fields = ['numero_pedido', 'estado_pedido', 'fecha_hora_pedido']  # Agregar 'total_pedido', 'mozo_pedido',

    raw_id_fields = ['reserva']

    filter_horizontal = ['mesa_pedido']

    fieldsets = [
        ('Numero Pedido', {'fields': ['numero_pedido']}),
        ('Mozo/Barman - Jornada', {'fields': ['mozo_pedido', ('jornada', 'estado_jornada', 'sector')]}),
        ('Datos de la Reserva', {'fields': ['reserva', ('id_cliente_reserva', 'cliente_reserva', 'doc_ruc_cliente_reserva'),
                                            'monto_entrega_reserva', 'mesas_reserva']}),
        ('Datos del Pedido', {'fields': ['mesa_pedido', 'estado_pedido', 'fecha_hora_pedido', 'total_pedido']}),
        # ('Total', {'fields': []}),
    ]

    inlines = [PedidoDetalleInline]

    list_display = ['numero_pedido', 'mozo_pedido', 'jornada', 'get_sector', 'reserva', 'colorea_estado_pedido',
                    'fecha_hora_pedido', 'total_pedido']
    list_filter = ['numero_pedido', 'mozo_pedido', 'jornada', 'jornada__sector', 'reserva__descripcion_reserva', 'estado_pedido', 'fecha_hora_pedido']
    search_fields = ['numero_pedido', 'mozo_pedido__usuario__username', 'jornada__id', 'jornada__sector__descripcion', 'reserva__descripcion_reserva',
                     'reserva__cliente__nombres', 'reserva__cliente__apellidos', 'estado_pedido__pedido_estado', 'fecha_hora_pedido']

    # Envia los datos de las Jornadas vigentes al Modal para el Cambio de Jornada
    def change_view(self, request, object_id, form_url='', extra_context={}):
        if object_id:
            pedido = Pedido.objects.get(pk=object_id)

            if pedido.estado_pedido.pedido_estado == 'VIG' and pedido.jornada.estado_jornada in ('EXP', 'CER'):
                jornadas = InicioJornada.objects.filter(estado_jornada='VIG')
                extra_context.update({'jornadas': jornadas})

        return super(PedidoAdmin, self).change_view(request, object_id, form_url=form_url, extra_context=extra_context)

    def colorea_estado_pedido(self, obj):
        # color = 'black'
        if obj.estado_pedido.pedido_estado == 'PRO':
            color = 'green'
            return format_html('<span style="color: %s"><b> %s </b></span>' %
                               (color, obj.estado_pedido.get_pedido_estado_display()))
        elif obj.estado_pedido.pedido_estado == 'PEN':
            color = 'red'
            return format_html('<span style="color: %s"><b> %s </b></span>' %
                               (color, obj.estado_pedido.get_pedido_estado_display()))
        elif obj.estado_pedido.pedido_estado == 'CAN':
            color = 'orange'
            return format_html('<span style="color: %s"><b> %s </b></span>' %
                               (color, obj.estado_pedido.get_pedido_estado_display()))
        elif obj.estado_pedido.pedido_estado == 'VIG':
            color = 'indianred'
            return format_html('<span style="color: %s"><b> %s </b></span>' %
                               (color, obj.estado_pedido.get_pedido_estado_display()))
        return obj.estado_pedido.pedido_estado
    colorea_estado_pedido.short_description = 'Estado Pedido'

    # VALIDACIONES/FUNCIONALIDADES
    # ============================
    # 1) Al seleccionar la Reserva se deben cargar los datos del Monto de la Entrega y de las Mesas Reservadas. OK!
    # 2.1) Al guardar el Pedido se debe cambiar el estado de la Reserva a UTILIZADA en caso de que se haya
    # utilizado una. OK!
    # 2.2) Al guardar el Pedido se debe descontar los productos solicitados del Stock.
    # Correccion 05/01/2016: Se debe generar la COMANDA y una vez procesada la Comanda se deben descontar los productos del Stock.
    # 2.3) Al guardar el Pedido se debe modificar el estado de las Mesas seleccionadas a Ocupadas. OK!
    # 4) Modificar el Estado del Pedido de acuerdo a las acciones que se realicen con el mismo. Por de pronto el campo
    # estado_pedido queda como readonly.
    # 5) Se debe restar el "monto_entrega_reserva" al "total_pedido" en caso de utilizar una Reserva.
    # 6) Analizar la manera de seguir agregando productos a un mismo Pedido y como funcionara esta pantalla en ese caso.
    # 7) Se debe poder cancelar o anular el Pedido. Se podria agregar un boton de "Cancelar" que requiera el ingreso de
    # un motivo de cancelacion o anulacion. Al anularse o cancelarse un Pedido se deben sumar nuevamente al Stock los
    # Productos solicitados y que ya fueron descontados.
    # 8) Los pedidos con estado "Procesado" y "Cancelado" no deben poder ser modificados.
    # 9) Calcular automaticamente el campo "total_pedido" de acuerdo a los valores de "total_producto_pedido" para cada
    # Producto del detalle. En caso de eliminar un Producto se debe restar al campo "total_pedido"
    # 10) mozo_pedido: Debe ser el usuario con el cual se esta registrando el Pedido, no se debe poder seleccionar el
    # usuario. OK!

    def save_model(self, request, obj, form, change):

        # import pdb
        # pdb.set_trace()

        if not change:
            obj.estado_pedido = PedidoEstado.objects.get(pedido_estado='VIG')
            obj.save()

        pedido_actual = obj

        if not change and "_continue" in request.POST or not change and "_save" in request.POST:
        # if not obj.pk:
            # 2.1) Al guardar el Pedido se debe cambiar el estado de la Reserva a UTILIZADA en caso de que se haya utilizado una
            if pedido_actual.reserva:
                reserva = pedido_actual.reserva
                reserva.estado = ReservaEstado.objects.get(reserva_estado='UTI')
                reserva.save()
                evento = Event.objects.get(pk=reserva.evento_id.id)
                evento.category = EventCategory.objects.get(name='Reserva Utilizada')
                evento.save()

            # 2.3) Al guardar el Pedido se debe modificar el estado de las Mesas seleccionadas a Ocupadas.
            # Modifica el estado de las Mesas Reservadas
        #     for mesa in pedido_actual.mesa_pedido.all():
            mesas = form.cleaned_data['mesa_pedido']
            for mesa in mesas:
                if mesa != Mesa.objects.get(numero_mesa=9999):
                    mesa_reservada = Mesa.objects.get(pk=mesa.id)
                    mesa_reservada.estado = MesaEstado.objects.get(mesa_estado='OC')
                    mesa_reservada.utilizada_por_numero_pedido = pedido_actual.numero_pedido
                    mesa_reservada.save()

        elif change and "_continue" in request.POST or change and "_save" in request.POST:
            # Modifica el estado a "DI" de las Mesas que fueron seleccionadas inicialmente en el Pedido pero que luego fueron quitadas.
            # Aplica para el caso en que se cambien de Mesa/s el/los Cliente/s.

            mesas_guardadas = pedido_actual.mesa_pedido.all()
            mesas_elegidas = form.cleaned_data['mesa_pedido']

            if mesas_elegidas != mesas_guardadas:

                for mesa in mesas_guardadas:
                    if mesa not in mesas_elegidas and mesa.numero_mesa != 9999:
                        mesa.estado = MesaEstado.objects.get(mesa_estado='DI')
                        mesa.utilizada_por_numero_pedido = None
                        mesa.save()

                # Modifica el estado a "OC" de las Mesas que no fueron Reservadas pero que fueron seleccionadas para ser utilizadas dentro del Pedido.
                for mesa in mesas_elegidas:
                    # mesa_utilizada = Mesa.objects.get(pk=mesa.id)
                    if mesa.estado.mesa_estado not in ('IN', 'OC') and mesa not in mesas_guardadas and mesa.numero_mesa != 9999:
                        mesa.estado = MesaEstado.objects.get(mesa_estado='OC')
                        mesa.utilizada_por_numero_pedido = pedido_actual.numero_pedido
                        mesa.save()
                    # Las validaciones fueron pasadas al Form.
                    # elif mesa.estado.mesa_estado == 'IN':
                    #     raise ValidationError('La Mesa seleccionada se encuentra inactiva. Seleccione otra Mesa.')
                    # elif mesa.estado.mesa_estado == 'OC':
                    #     raise ValidationError('La Mesa seleccionada ya se encuentra ocupada. Seleccione otra Mesa.')

        # Si se cancela el Pedido del Cliente se asigna el estado "CAN" al Pedido.
        # Solo se puede CANCELAR el Pedido si no existen Productos con estado Procesado en el detalle.
        elif "_cancel" in request.POST:

            # import pdb
            # pdb.set_trace()

            # Cambiar el estado de la Reserva dependiendo de la fecha/hora
            if pedido_actual.reserva:
                reserva = pedido_actual.reserva
                # timezone.localtime(apertura.fecha_hora_fin_apertura_caja) < now:
                if timezone.localtime(reserva.fecha_hora_reserva) < timezone.localtime(timezone.now()):
                    reserva.estado = ReservaEstado.objects.get(reserva_estado='CAD')
                    evento = Event.objects.get(pk=reserva.evento_id.id)
                    evento.category = EventCategory.objects.get(name='Reserva Caducada')
                    evento.save()
                elif timezone.localtime(reserva.fecha_hora_reserva) >= timezone.localtime(timezone.now()):
                    reserva.estado = ReservaEstado.objects.get(reserva_estado='VIG')
                    evento = Event.objects.get(pk=reserva.evento_id.id)
                    evento.category = EventCategory.objects.get(name='Reserva Vigente')
                    evento.save()
                reserva.save()

            # Marcar las Mesas como DIsponibles ya sean las mesas guardadas como las seleccionadas.
            mesas_guardadas = pedido_actual.mesa_pedido.all()
            for mesa in mesas_guardadas:
                if mesa.numero_mesa != 9999:
                    mesa.estado = MesaEstado.objects.get(mesa_estado='DI')
                    mesa.utilizada_por_numero_pedido = None
                    mesa.save()

            if pedido_actual is not None and pedido_actual.pk and pedido_actual.estado_pedido.pedido_estado == 'VIG' \
                    and pedido_actual.jornada.estado_jornada == 'VIG':
                mesas_elegidas = form.cleaned_data['mesa_pedido']
                for mesa in mesas_elegidas:
                    if mesa.numero_mesa != 9999 and mesa not in mesas_guardadas:
                        mesa.estado = MesaEstado.objects.get(mesa_estado='DI')
                        mesa.utilizada_por_numero_pedido = None
                        mesa.save()

            pedido_actual.estado_pedido = PedidoEstado.objects.get(pedido_estado='CAN')
            pedido_actual.motivo_cancelacion = request.POST.get('motivo', '')
            pedido_actual.observaciones_cancelacion = request.POST.get('observaciones', '')
            pedido_actual.usuario_cancelacion = Empleado.objects.get(usuario_id=request.user)
            pedido_actual.fecha_hora_cancelacion = timezone.now()

        elif "cambiar_jornada" in request.POST:

            # import pdb
            # pdb.set_trace()

            # Intento de Modal - http://en.proft.me/2015/01/29/admin-actions-django-custom-form/
            # form = CambiarJornada(request.POST)
            # if form.is_valid():
            #     jornada_anterior = pedido_actual.jornada
            #     jornada_elegida = form.cleaned_data['jornada']
            #
            #     # updated = pedido_actual.update(jornada=jornada_elegida)
            #
            #     # jornada_anterior.cantidad_pedidos_procesados = jornada_anterior.get_cantidad_pedidos_procesados()
            #     jornada_anterior.cantidad_pedidos_pendientes = jornada_anterior.get_cantidad_pedidos_pendientes()
            #     # jornada_anterior.cantidad_pedidos_cancelados = jornada_anterior.get_cantidad_pedidos_cancelados()
            #     jornada_anterior.save()
            #
            #     # jornada_elegida.cantidad_pedidos_procesados = jornada_elegida.get_cantidad_pedidos_procesados()
            #     jornada_elegida.cantidad_pedidos_pendientes = jornada_elegida.get_cantidad_pedidos_pendientes()
            #     # jornada_elegida.cantidad_pedidos_cancelados = jornada_elegida.get_cantidad_pedidos_cancelados()
            #     jornada_elegida.save()
            #
            #     # messages.success(request, '{0} movies were updated'.format(updated))
            #     return
            #
            # return render(request, 'admin/ventas/pedido/cambiar_jornada.html',
            #               {'title': u'Elija la Jornada',
            #                'objects': Pedido.objects.filter(numero_pedido=pedido_actual.pk),
            #                'form': form})

            jornada_anterior = pedido_actual.jornada
            id_jornada = request.POST.get('cambiar_jornada', '')
            jornada_elegida = InicioJornada.objects.get(pk=id_jornada)

            # pedido_actual.update(jornada=jornada_elegida)
            pedido_actual.jornada = jornada_elegida

            # jornada_anterior.cantidad_pedidos_procesados = jornada_anterior.get_cantidad_pedidos_procesados()
            jornada_anterior.cantidad_pedidos_pendientes = jornada_anterior.get_cantidad_pedidos_pendientes()
            # jornada_anterior.cantidad_pedidos_cancelados = jornada_anterior.get_cantidad_pedidos_cancelados()
            jornada_anterior.save()

            # jornada_elegida.cantidad_pedidos_procesados = jornada_elegida.get_cantidad_pedidos_procesados()
            jornada_elegida.cantidad_pedidos_pendientes = jornada_elegida.get_cantidad_pedidos_pendientes()
            # jornada_elegida.cantidad_pedidos_cancelados = jornada_elegida.get_cantidad_pedidos_cancelados()
            jornada_elegida.save()

        if not change and getattr(obj, 'mozo_pedido', None) is None:
            # empleado = Empleado.objects.filter(usuario=request.user)
            obj.mozo_pedido = Empleado.objects.get(usuario_id=request.user)
            print 'obj.mozo_pedido: ', obj.mozo_pedido
        elif change and getattr(obj, 'mozo_pedido', None) is not None:
            obj.usuario_modifica_pedido = Empleado.objects.get(usuario_id=request.user)
            print 'obj.usuario_modifica_pedido: ', obj.usuario_modifica_pedido

        super(PedidoAdmin, self).save_model(request, obj, form, change)

    def save_formset(self, request, form, formset, change):

        # import pdb
        # pdb.set_trace()

        pedido = form.instance

        # if not change:
        # formset.save(commit=False)
        if "_continue" in request.POST or "_save" in request.POST:
            for form2 in formset:
                # import pdb; pdb.set_trace()
                valido = True
                try:
                     form2.clean()
                except:
                    valido = False

                if valido:
                    pedido_detalle = form2.instance
                    # import pdb; pdb.set_trace()

                    if pedido_detalle.pk:
                        pedido_detalle_guardado = PedidoDetalle.objects.get(pk=pedido_detalle.id)
                        # form.cleaned_data['nro_orden_compra']

                    # Si el checkbox "cancelado" esta marcado ya sea con pedido_detalle.pk o sin pedido_detalle.pk debe
                    # cancelar ese Producto, marcar la Comanda como cancelada y reponer el Stock.
                    if pedido_detalle.pk and pedido_detalle.procesado is False and pedido_detalle.cancelado is True and pedido_detalle_guardado.cancelado is False \
                            or not pedido_detalle.pk and pedido_detalle.procesado is False and pedido_detalle.cancelado is True:

                        # Si el detalle no esta guardado no se deben devolver los Productos descontados al Stock.
                        if pedido_detalle.pk:

                            # Verificar si existe una Comanda y marcarla como cancelado
                            try:
                                comanda = Comanda.objects.get(id_pedido_detalle_id=pedido_detalle.id)
                                comanda.estado_comanda = 'CAN'
                                comanda.save()

                                # 23/11/2016: Devolver los Productos descontados al Stock

                            except ObjectDoesNotExist:
                                # Si no existe la Comanda no es necesario crearla
                                comanda = Comanda(numero_pedido_id=pedido_detalle_guardado.pedido_id,
                                                  id_pedido_detalle_id=pedido_detalle_guardado.id,
                                                  area_solicitante=Sector.objects.get(sector=pedido_detalle_guardado.pedido.mozo_pedido.sector.sector),
                                                  usuario_solicitante=Empleado.objects.get(usuario_id=request.user),
                                                  producto_a_entregar=ProductoVenta.objects.get(id=pedido_detalle_guardado.producto_pedido.id),
                                                  cantidad_solicitada=pedido_detalle_guardado.cantidad_producto_pedido,
                                                  area_encargada=Sector.objects.get(sector=pedido_detalle_guardado.pedido.mozo_pedido.sector.sector),
                                                  fecha_hora_pedido_comanda=timezone.now(),
                                                  tiempo_estimado_procesamiento=pedido_detalle_guardado.producto_pedido.tiempo_elaboracion,
                                                  estado_comanda='CAN')
                                comanda.save()

                            # # Se asume que las Comandas deben existir indefectiblemente porque tuvieron que ser creadas al
                            # # momento de guardar el PedidoDetalle.
                            # comanda = Comanda.objects.get(id_pedido_detalle_id=pedido_detalle.id)
                            # comanda.estado_comanda = 'CAN'
                            # comanda.save()

                            # 23/11/2016: Devolver los Productos descontados al Stock
                            movimientos_stock_por_detalle_pedido = MovimientoStock.objects.filter(id_movimiento=pedido_detalle.id)
                            for movimiento in movimientos_stock_por_detalle_pedido:
                                stock = MovimientoStock(producto_stock_id=movimiento.producto_stock.id,
                                                        tipo_movimiento='CP',
                                                        id_movimiento=pedido_detalle.id,
                                                        ubicacion_origen=movimiento.ubicacion_destino,
                                                        ubicacion_destino=movimiento.ubicacion_origen,
                                                        cantidad_entrante=movimiento.cantidad_saliente,
                                                        cantidad_saliente=movimiento.cantidad_entrante,
                                                        fecha_hora_registro_stock=timezone.now())
                                stock.save()

                        pedido_detalle.cancelado = True

                        # # Un pedido_detalle que aun no ha sido guardado no debe tener una Comanda asignada ni tuvo que
                        # # haber descontado los Productos del Stock.
                        # if not pedido_detalle.pk:

                    # Si el checkbox "cancelado" esta DESmarcado ya sea con pedido_detalle.pk o sin pedido_detalle.pk debe
                    # cancelar ese Producto y reponer el Stock.
                    elif not pedido_detalle.pk and pedido_detalle.procesado is False and pedido_detalle.cancelado is False:
                        # super(PedidoAdmin, self).save_formset(request, form, formset, change)
                        pedido_detalle.pedido_id = pedido.numero_pedido
                        # import pdb
                        # pdb.set_trace()
                        if pedido_detalle.producto_pedido:
                           pedido_detalle.save()  # Graba el pedido_detalle para asi poder acceder a los datos del registro actual mediante "pedido_detalle.campo"

                        # De acuerdo a la Categoria del Producto se debe definir el "area_encargada" (Sector) para la Comanda
                        # Comandas para la COCINA
                        if pedido_detalle.producto_pedido.compuesto is True \
                                and pedido_detalle.producto_pedido.categoria.categoria == 'CO':
                            if pedido.mozo_pedido.usuario.is_superuser is True:
                                solicitante = Sector.objects.get(sector='BPR')
                            else:
                                solicitante = Sector.objects.get(sector=pedido.mozo_pedido.sector.sector)
                            encargado = Sector.objects.get(sector='COC')

                        # # Los Tragos son procesados por la Barra Principal
                        # elif venta_detalle.producto_venta.compuesto is True \
                        #         and venta_detalle.producto_venta.categoria.categoria == 'BE':
                        #         # and venta_detalle.producto_venta.subcategoria.subcategoria == 'TRA':
                        #     encargado = Sector.objects.get(sector='BPR')

                        # Finalmente se define que todos los Sectores pueden procesar todos los pedidos sin importar la Categoria
                        # y SubCategoria del Producto a excepcion de las Comidas por lo tanto la condicion para definir el
                        # "area_encargada" depende del sector al cual esta asignado el Mozo/Barman.
                        elif pedido.mozo_pedido.usuario.is_superuser is True:
                            solicitante = Sector.objects.get(sector='BPR')
                            encargado = Sector.objects.get(sector='BPR')
                        else:
                            solicitante = Sector.objects.get(sector=pedido.mozo_pedido.sector.sector)
                            encargado = Sector.objects.get(sector=pedido.mozo_pedido.sector.sector)

                        # Genera la Comanda
                        comanda = Comanda(numero_pedido_id=pedido.numero_pedido,
                                          id_pedido_detalle_id=pedido_detalle.id,
                                          area_solicitante=solicitante,
                                          usuario_solicitante=Empleado.objects.get(usuario_id=request.user),
                                          # producto_a_entregar=ProductoVenta.objects.get(id=pedido_detalle.producto_pedido.id),
                                          producto_a_entregar=pedido_detalle.producto_pedido,
                                          cantidad_solicitada=pedido_detalle.cantidad_producto_pedido,
                                          area_encargada=encargado,
                                          fecha_hora_pedido_comanda=timezone.now(),
                                          tiempo_estimado_procesamiento=pedido_detalle.producto_pedido.tiempo_elaboracion,
                                          estado_comanda='PEN')
                        comanda.save()

        # ==================================================================================================================
        # 23/11/2016: Finalmente decidi confirmar los descuentos del Stock o generacion de Movimientos de Stock al
        # momento de confirmar las VentasOcasionales o los Pedidos, esto con el fin de evitar un gap de tiempo entre
        # que se hace un Pedido y se procesa una Comanda lo cual puede reflejar un Stock incorrecto. Se debe garantizar
        # la disponibilidad de los Productos/Insumos para los Pedidos ya realizados.
        # Con esto hay que prever que al momento de Cancelar un Pedido se deben volver a sumar los Productos al Stock.
        # En las VentasOcasionales no sera necesario realizar esta reversion.
        # ==================================================================================================================

                        # import pdb
                        # pdb.set_trace()

                        # Descuenta los Productos del Stock. Analiza si el Producto es COMPUESTO y de acuerdo a la
                        # Categoria genera el Movimiento de Stock
                        if pedido_detalle.producto_pedido.compuesto is True:
                            if pedido_detalle.producto_pedido.categoria.categoria == 'CO':
                                deposito = Deposito.objects.get(deposito='DCO')
                                prod_comp_detalle = ProductoCompuestoDetalle.objects.filter(producto_compuesto_id=pedido_detalle.producto_pedido.id)

                                for producto_insumo in prod_comp_detalle:
                                # Recorrer los Insumos para determinar el ProductoInsumo del cual se descontara el Stock.
                                # =====> Se debe descontar del ProductoInsumo con menor Cantidad Existente. <=====
                                    producto_menor_cant_existente = StockDepositoAjusteInventario.objects.none
                                    menor_cant_exist_prod_insumo = 0
                                    cantidad_descontada = 0
                                    cantidad_a_descontar = producto_insumo.cantidad_insumo * pedido_detalle.cantidad_producto_pedido
                                    while cantidad_descontada < cantidad_a_descontar:
                                        productos = Producto.objects.filter(insumo_id=producto_insumo.insumo.id, tipo_producto='IN')
                                        for producto in productos:
                                            try:
                                                prod_exist_deposito = StockDepositoAjusteInventario.objects.get(id=producto.id, deposito_id=deposito.id)
                                                if prod_exist_deposito.cantidad_existente > 0:
                                                    if producto == productos.first():
                                                        menor_cant_exist_prod_insumo = prod_exist_deposito.cantidad_existente
                                                        producto_menor_cant_existente = prod_exist_deposito
                                                    elif menor_cant_exist_prod_insumo < prod_exist_deposito.cantidad_existente:
                                                        menor_cant_exist_prod_insumo = prod_exist_deposito.cantidad_existente
                                                        producto_menor_cant_existente = prod_exist_deposito

                                            except StockDepositoAjusteInventario.DoesNotExist:
                                                pass

                                        if producto_menor_cant_existente.cantidad_existente < (cantidad_a_descontar - cantidad_descontada):
                                            stock = MovimientoStock(producto_stock_id=producto_menor_cant_existente.id,
                                                                    tipo_movimiento='VE',
                                                                    id_movimiento=pedido_detalle.id,
                                                                    ubicacion_origen=encargado.deposito,
                                                                    ubicacion_destino=Deposito.objects.get(deposito='CLI'),
                                                                    cantidad_entrante=0,
                                                                    cantidad_saliente=producto_menor_cant_existente.cantidad_existente,
                                                                    fecha_hora_registro_stock=timezone.now())
                                            stock.save()
                                            cantidad_descontada += producto_menor_cant_existente.cantidad_existente
                                            # pedido_detalle.id_mov_stock = stock.id
                                        elif producto_menor_cant_existente.cantidad_existente >= (cantidad_a_descontar - cantidad_descontada):
                                            stock = MovimientoStock(producto_stock_id=producto_menor_cant_existente.id,
                                                                    tipo_movimiento='VE',
                                                                    id_movimiento=pedido_detalle.id,
                                                                    ubicacion_origen=encargado.deposito,
                                                                    ubicacion_destino=Deposito.objects.get(deposito='CLI'),
                                                                    cantidad_entrante=0,
                                                                    cantidad_saliente=(cantidad_a_descontar - cantidad_descontada),
                                                                    fecha_hora_registro_stock=timezone.now())
                                            stock.save()
                                            cantidad_descontada += (cantidad_a_descontar - cantidad_descontada)
                                            # pedido_detalle.id_mov_stock = stock.id

                            elif pedido_detalle.producto_pedido.categoria.categoria == 'BE':
                                deposito = encargado.deposito
                                prod_comp_detalle = ProductoCompuestoDetalle.objects.filter(producto_compuesto_id=pedido_detalle.producto_pedido.id)

                                for producto_insumo in prod_comp_detalle:
                                # Recorrer los Insumos para determinar el ProductoInsumo del cual se descontara el Stock.
                                # =====> Se debe descontar del ProductoInsumo con menor Cantidad Existente. <=====
                                    producto_menor_cant_existente = StockDepositoAjusteInventario.objects.none
                                    menor_cant_exist_prod_insumo = 0
                                    cantidad_descontada = 0
                                    cantidad_a_descontar = producto_insumo.cantidad_insumo * pedido_detalle.cantidad_producto_pedido
                                    while cantidad_descontada < cantidad_a_descontar:
                                        productos = Producto.objects.filter(insumo_id=producto_insumo.insumo.id, tipo_producto='IN')
                                        for producto in productos:
                                            try:
                                                prod_exist_deposito = StockDepositoAjusteInventario.objects.get(id=producto.id, deposito_id=deposito.id)
                                                if prod_exist_deposito.cantidad_existente > 0:
                                                    if producto == productos.first():
                                                        menor_cant_exist_prod_insumo = prod_exist_deposito.cantidad_existente
                                                        producto_menor_cant_existente = prod_exist_deposito
                                                    elif menor_cant_exist_prod_insumo < prod_exist_deposito.cantidad_existente:
                                                        menor_cant_exist_prod_insumo = prod_exist_deposito.cantidad_existente
                                                        producto_menor_cant_existente = prod_exist_deposito

                                            except StockDepositoAjusteInventario.DoesNotExist:
                                                pass

                                        if producto_menor_cant_existente.cantidad_existente < (cantidad_a_descontar - cantidad_descontada):
                                            stock = MovimientoStock(producto_stock_id=producto_menor_cant_existente.id,
                                                                    tipo_movimiento='VE',
                                                                    id_movimiento=pedido_detalle.id,
                                                                    ubicacion_origen=encargado.deposito,
                                                                    ubicacion_destino=Deposito.objects.get(deposito='CLI'),
                                                                    cantidad_entrante=0,
                                                                    cantidad_saliente=producto_menor_cant_existente.cantidad_existente,
                                                                    fecha_hora_registro_stock=timezone.now())
                                            stock.save()
                                            cantidad_descontada += producto_menor_cant_existente.cantidad_existente
                                            # pedido_detalle.id_mov_stock = stock.id
                                        elif producto_menor_cant_existente.cantidad_existente >= (cantidad_a_descontar - cantidad_descontada):
                                            stock = MovimientoStock(producto_stock_id=producto_menor_cant_existente.id,
                                                                    tipo_movimiento='VE',
                                                                    id_movimiento=pedido_detalle.id,
                                                                    ubicacion_origen=encargado.deposito,
                                                                    ubicacion_destino=Deposito.objects.get(deposito='CLI'),
                                                                    cantidad_entrante=0,
                                                                    cantidad_saliente=(cantidad_a_descontar - cantidad_descontada),
                                                                    fecha_hora_registro_stock=timezone.now())
                                            stock.save()
                                            cantidad_descontada += (cantidad_a_descontar - cantidad_descontada)
                                            # pedido_detalle.id_mov_stock = stock.id

                        elif pedido_detalle.producto_pedido.compuesto is False:
                            stock = MovimientoStock(producto_stock_id=pedido_detalle.producto_pedido.id,
                                                    tipo_movimiento='VE',
                                                    id_movimiento=pedido_detalle.id,
                                                    ubicacion_origen=encargado.deposito,
                                                    ubicacion_destino=Deposito.objects.get(deposito='CLI'),
                                                    cantidad_entrante=0,
                                                    cantidad_saliente=pedido_detalle.cantidad_producto_pedido,
                                                    fecha_hora_registro_stock=timezone.now())
                            stock.save()
                            # pedido_detalle.id_mov_stock = stock.id

        elif "_cancel" in request.POST:

            # import pdb
            # pdb.set_trace()

            for form in formset:
                pedido_detalle = form.instance

                if pedido_detalle.pk:
                    pedido_detalle_guardado = PedidoDetalle.objects.get(pk=pedido_detalle.id)
                    # form.cleaned_data['nro_orden_compra']

                # Si el checkbox "cancelado" esta marcado ya sea con pedido_detalle.pk o sin pedido_detalle.pk debe
                # cancelar ese Producto, marcar la Comanda como cancelada y reponer el Stock.
                # if pedido_detalle.pk and pedido_detalle.procesado is False and pedido_detalle.cancelado is False and pedido_detalle_guardado.cancelado is False:
                if pedido_detalle.pk and pedido_detalle_guardado.cancelado is False:

                    # Verificar si existe una Comanda y marcarla como cancelado
                    try:
                        comanda = Comanda.objects.get(id_pedido_detalle_id=pedido_detalle.id)
                        comanda.estado_comanda = 'CAN'
                        comanda.save()

                        # 23/11/2016: Devolver los Productos descontados al Stock

                    except ObjectDoesNotExist:
                        # Si no existe la Comanda no es necesario crearla
                        comanda = Comanda(numero_pedido_id=pedido_detalle_guardado.pedido_id,
                                          id_pedido_detalle_id=pedido_detalle_guardado.id,
                                          area_solicitante=Sector.objects.get(sector=pedido_detalle_guardado.pedido.mozo_pedido.sector.sector),
                                          usuario_solicitante=Empleado.objects.get(usuario_id=request.user),
                                          producto_a_entregar=ProductoVenta.objects.get(id=pedido_detalle_guardado.producto_pedido.id),
                                          cantidad_solicitada=pedido_detalle_guardado.cantidad_producto_pedido,
                                          area_encargada=Sector.objects.get(sector=pedido_detalle_guardado.pedido.mozo_pedido.sector.sector),
                                          fecha_hora_pedido_comanda=timezone.now(),
                                          tiempo_estimado_procesamiento=pedido_detalle_guardado.producto_pedido.tiempo_elaboracion,
                                          estado_comanda='CAN')
                        comanda.save()

                    # # Se asume que las Comandas deben existir indefectiblemente porque tuvieron que ser creadas al
                    # # momento de guardar el PedidoDetalle.
                    # comanda = Comanda.objects.get(id_pedido_detalle_id=pedido_detalle.id)
                    # comanda.estado_comanda = 'CAN'
                    # comanda.save()

                    # 23/11/2016: Devolver los Productos descontados al Stock
                    movimientos_stock_por_detalle_pedido = MovimientoStock.objects.filter(id_movimiento=pedido_detalle.id)
                    for movimiento in movimientos_stock_por_detalle_pedido:
                        stock = MovimientoStock(producto_stock_id=movimiento.producto_stock.id,
                                                tipo_movimiento='CP',
                                                id_movimiento=pedido_detalle.id,
                                                ubicacion_origen=movimiento.ubicacion_destino,
                                                ubicacion_destino=movimiento.ubicacion_origen,
                                                cantidad_entrante=movimiento.cantidad_saliente,
                                                cantidad_saliente=movimiento.cantidad_entrante,
                                                fecha_hora_registro_stock=timezone.now())
                        stock.save()

                    pedido_detalle.procesado = False
                    pedido_detalle.cancelado = True

                # Un pedido_detalle que aun no ha sido guardado no debe tener una Comanda asignada ni tuvo que
                # haber descontado los Productos del Stock. Solo se debe marcar como Cancelado el pedido_detalle.
                # elif not pedido_detalle.pk and pedido_detalle.procesado is False and pedido_detalle.cancelado is False:
                elif not pedido_detalle.pk:
                    pedido_detalle.procesado = False
                    pedido_detalle.cancelado = True

        super(PedidoAdmin, self).save_formset(request, form, formset, change)

    def get_readonly_fields(self, request, obj=None):

        # import pdb
        # pdb.set_trace()

        if obj is not None and obj.pk and obj.estado_pedido.pedido_estado == 'VIG' and obj.jornada.estado_jornada == 'VIG':  # and obj.reserva is not None
            return self.readonly_fields + ['mozo_pedido', 'jornada', 'reserva']

        elif obj is not None and obj.estado_pedido.pedido_estado in ('PRO', 'CAN', 'PEN') \
                or obj is not None and obj.pk and obj.estado_pedido.pedido_estado == 'VIG' and obj.jornada.estado_jornada in ('EXP', 'CER'):
            return [i.name for i in self.model._meta.fields] + \
                   [i.name for i in self.model._meta.many_to_many]

        else:
            return super(PedidoAdmin, self).get_readonly_fields(request, obj)

    def changeform_view(self, request, object_id=None, form_url='', extra_context=None):
        extra_context = extra_context or {}

        extra_context['show_button'] = True
        if object_id is not None:
            pedido_actual = Pedido.objects.get(pk=object_id)
            # extra_context['show_button'] = orden_compra_actual.estado_orden_compra.estado_orden_compra \
            #                                not in ('ENT', 'CAN')

            # if orden_compra_actual.estado_orden_compra.estado_orden_compra == 'PEN':
            #     extra_context['show_save_button'] = True
            #     extra_context['show_continue_button'] = True
            #     extra_context['show_addanother_button'] = True
            #     extra_context['show_cancel_button'] = False
            #     extra_context['show_imprimir_button'] = False
            if pedido_actual.estado_pedido.pedido_estado in ('PRO', 'CAN', 'PEN'):
                extra_context['show_save_button'] = False
                extra_context['show_continue_button'] = False
                extra_context['show_change_button'] = False
                extra_context['show_cancel_button'] = False
                extra_context['show_imprimir_button'] = True
            elif pedido_actual.estado_pedido.pedido_estado == 'VIG' and pedido_actual.jornada.estado_jornada == 'VIG':
                extra_context['show_save_button'] = True
                extra_context['show_continue_button'] = True
                extra_context['show_change_button'] = False
                extra_context['show_cancel_button'] = True
                extra_context['show_imprimir_button'] = True
            elif pedido_actual.estado_pedido.pedido_estado == 'VIG' and pedido_actual.jornada.estado_jornada in ('EXP', 'CER'):
                extra_context['show_save_button'] = False
                extra_context['show_continue_button'] = False
                extra_context['show_change_button'] = True
                extra_context['show_cancel_button'] = True
                extra_context['show_imprimir_button'] = True

        elif object_id is None:
            extra_context['show_save_button'] = True
            extra_context['show_continue_button'] = True
            extra_context['show_change_button'] = False
            extra_context['show_cancel_button'] = False
            extra_context['show_imprimir_button'] = False

        return super(PedidoAdmin, self).changeform_view(request, object_id, form_url, extra_context)

    def get_form(self, request, obj=None, **kwargs):

        # import pdb
        # pdb.set_trace()

        form = super(PedidoAdmin, self).get_form(request, obj=obj, **kwargs)

        if obj is None:
            # usuario = Empleado.objects.get(usuario=request.user)
            # form.base_fields['cajero'].initial = usuario
            # form.base_fields['horario'].initial = usuario.horario
            form.base_fields['mozo_pedido'].widget.attrs['readonly'] = True
            form.base_fields['jornada'].widget.attrs['readonly'] = True
            form.base_fields['jornada'].widget.attrs['style'] = 'width: 300px;'
        form.request = request
        return form

    def has_delete_permission(self, request, obj=None):
        return False

    def get_queryset(self, request):
        usuario = Empleado.objects.get(usuario_id=request.user)
        queryset = None
        if usuario.cargo.cargo in ('MO', 'BM'):
            queryset = Pedido.objects.filter(mozo_pedido=usuario)
        elif usuario.cargo.cargo == 'CA':
            queryset = Pedido.objects.filter(jornada__sector=usuario.sector)
        elif usuario.usuario.is_superuser is True:
            queryset = Pedido.objects.all()
        return queryset

    def _create_formsets(self, request, obj, change):
        formsets, inline_instances = super(PedidoAdmin, self)._create_formsets(request, obj, change)
        for formset in formsets:
            formset.request = request
        return formsets, inline_instances


class VentaDetalleInline(admin.TabularInline):
    model = VentaDetalle
    extra = 0
    # form =
    raw_id_fields = ['producto_venta']
    # verbose_name =
    # verbose_name_plural =

    def get_readonly_fields(self, request, obj=None):
        if obj is not None and obj.estado_venta.venta_estado in ('PRO', 'CAN', 'PEN'):
            return [i.name for i in self.model._meta.fields]
        else:
            return super(VentaDetalleInline, self).get_readonly_fields(request, obj)

    def has_add_permission(self, request):
        object_id = request.path.split("/")[-2]
        if object_id != "add":
            venta_actual = Venta.objects.get(pk=object_id)
            return venta_actual.estado_venta.venta_estado not in ('PRO', 'CAN', 'PEN')
        else:
            return super(VentaDetalleInline, self).has_add_permission(request)

    def has_delete_permission(self, request, obj=None):
        if obj is not None and obj.estado_venta.venta_estado in ('PRO', 'CAN', 'PEN'):
            return False
        return super(VentaDetalleInline, self).has_delete_permission(request, obj)


class VentaAdmin(admin.ModelAdmin):
    form = VentaForm

    class Media:
        js = [
            'ventas/js/venta.js'
        ]

    readonly_fields = ['empresa', 'numero_factura_venta', 'fecha_hora_venta', 'estado_venta']

    raw_id_fields = ['cliente_factura', 'numero_pedido']

    fieldsets = [
        ('Facturacion', {'fields': [('empresa', 'timbrado', 'fecha_limite_vigencia_timbrado'),
                                          'numero_factura_venta',
                                          ('apertura_caja', 'estado_apertura_caja', 'fecha_hora_apertura_caja'),
                                          ('caja', 'cajero', 'horario', 'sector')]}),
        ('Venta', {'fields': [('fecha_hora_venta', 'estado_venta')]}),
        ('Pedido', {'fields': ['numero_pedido', 'total_pedido']}),
        ('Reserva', {'fields': ['posee_reserva', 'entrega_reserva']}),
        # ('Cliente', {'fields': [('cliente_factura', 'doc_ruc_cliente_reserva'), 'cliente_documento_factura']}),
        ('Cliente', {'fields': ['cliente_factura', ('cliente_documento_factura', 'doc_ruc_cliente_reserva'), ('direccion_cliente', 'ciudad_cliente', 'pais_cliente'), ('telefonos_cliente', 'email')]}),
        ('Pago', {'fields': [('forma_pago', 'efectivo_recibido', 'voucher'), 'total_venta', 'vuelto']}),
    ]

    inlines = [VentaDetalleInline]
    list_display = ['numero_factura_venta', 'apertura_caja', 'get_fecha_hora_apertura_caja', 'get_numero_caja',
                    'cajero', 'get_sector', 'numero_pedido', 'cliente_factura', 'fecha_hora_venta', 'forma_pago', 'total_venta',
                    'colorea_estado_venta']
    list_display_links = ['numero_factura_venta']
    list_filter = ['numero_factura_venta__numero_factura', 'apertura_caja', 'apertura_caja__fecha_hora_apertura_caja',
                   'apertura_caja__caja', 'apertura_caja__cajero', 'apertura_caja__sector', 'numero_pedido__numero_pedido',
                   'cliente_factura', 'fecha_hora_venta', 'forma_pago', 'estado_venta__venta_estado']
    search_fields = ['numero_factura_venta__numero_factura', 'apertura_caja__id', 'apertura_caja__fecha_hora_apertura_caja',
                     'apertura_caja__caja__numero_caja', 'apertura_caja__cajero__usuario__username', 'apertura_caja__sector__sector',
                     'numero_pedido__numero_pedido', 'cliente_factura__nombres', 'cliente_factura__apellidos', 'fecha_hora_venta',
                     'forma_pago', 'estado_venta__venta_estado']

    def colorea_estado_venta(self, obj):
        # color = 'black'
        if obj.estado_venta.venta_estado == 'PRO':
            color = 'green'
            # print 'Entra en colorea_estado_compra:', obj.estado_compra.estado_compra, color
            return format_html('<span style="color: %s"><b> %s </b></span>' %
                               (color, obj.estado_venta.get_venta_estado_display()))
        elif obj.estado_venta.venta_estado == 'CAN':
            color = 'orange'
            return format_html('<span style="color: %s"><b> %s </b></span>' %
                               (color, obj.estado_venta.get_venta_estado_display()))
        elif obj.estado_venta.venta_estado == 'PEN':
            color = 'red'
            return format_html('<span style="color: %s"><b> %s </b></span>' %
                               (color, obj.estado_venta.get_venta_estado_display()))
        return obj.estado_venta
    colorea_estado_venta.short_description = 'Estado Venta'

    def save_model(self, request, obj, form, change):

        # import pdb
        # pdb.set_trace()

        # AddProductoVentaFormset = inlineformset_factory(Venta, VentaDetalle, extra=0)

        venta_actual = obj
        venta_anterior = None

        # Recupera la venta_anterior
        if obj.pk:  # and obj.numero_pedido is not None:
            venta_anterior = Venta.objects.get(pk=obj.id)
        else:
            # venta_actual.forma_pago = 'EF'
            venta_actual.estado_venta = VentaEstado.objects.get(venta_estado='PEN')
            venta_actual.venta_ocasional = False
            super(VentaAdmin, self).save_model(request, obj, form, change)

        if "_continue" in request.POST and venta_actual.estado_venta.venta_estado == 'PEN':
            if venta_anterior is None \
                    or venta_anterior.numero_pedido_id != venta_actual.numero_pedido_id:

                print 'venta_detalle_a_eliminar: ', VentaDetalle.objects.filter(venta_id=venta_actual.id)
                VentaDetalle.objects.filter(venta_id=venta_actual.id).delete()
                print 'venta_detalle_eliminado: ', VentaDetalle.objects.filter(venta_id=venta_actual.id)

                for detalle in PedidoDetalle.objects.filter(pedido_id=venta_actual.numero_pedido_id, cancelado=False):
                    venta_detalle = VentaDetalle(venta_id=venta_actual.id,
                                                 producto_venta_id=detalle.producto_pedido_id,
                                                 precio_producto_venta=detalle.precio_producto_pedido,
                                                 cantidad_producto_venta=detalle.cantidad_producto_pedido,
                                                 total_producto_venta=detalle.total_producto_pedido)
                    venta_detalle.save()

                pedido = venta_actual.numero_pedido

                venta_actual.estado_venta = VentaEstado.objects.get(venta_estado='PEN')
                pedido.estado_pedido = PedidoEstado.objects.get(pedido_estado='PEN')
                pedido.save()

            if venta_anterior is not None and venta_anterior.numero_pedido_id != venta_actual.numero_pedido_id:
                pedido_anterior = venta_anterior.numero_pedido
                pedido_anterior.estado_pedido = PedidoEstado.objects.get(pedido_estado='VIG')
                pedido_anterior.save()

            super(VentaAdmin, self).save_model(request, obj, form, change)

        elif "_save" in request.POST:
            venta_actual.estado_venta = VentaEstado.objects.get(venta_estado='PRO')

            pedido = venta_actual.numero_pedido
            pedido.estado_pedido = PedidoEstado.objects.get(pedido_estado='PRO')
            pedido.save()

    # ==================================================================================================================
            # 23/11/2016: Se asume que si el Cliente va pagar por la Venta es porque recibio todos los Productos que
            # solicito por lo tanto se debe marcar como Procesado el detalle del Pedido y marcar las Comandas
            # pendientes como procesadas. No se requiere restar del Stock porque esto ya fue realizado en el Pedido.
            #
            # Este proceso se puede realizar tanto en el metodo "save_model" trayendo los registros del PedidoDetalle
            # tal como se hace a continuacion como tambien en el "save_formset" recorriendo VentaDetalle.
            detalle_pedido = PedidoDetalle.objects.filter(pedido_id=pedido.numero_pedido, procesado=False, cancelado=False)
            detalle_pedido.update(procesado=True)

            comandas = Comanda.objects.filter(numero_pedido_id=pedido.numero_pedido, estado_comanda='PEN')
            # comandas.update(estado_comanda='PRO', fecha_hora_procesamiento_comanda=timezone.now(), usuario_procesa=Empleado.objects.get(usuario_id=request.user))

            for q in comandas:
                q.estado_comanda = 'PRO'
                q.fecha_hora_procesamiento_comanda = timezone.now()
                q.usuario_procesa = Empleado.objects.get(usuario_id=request.user)
                q.save()
    # ==================================================================================================================

            # Marcar las Mesas guardadas como DIsponibles.
            mesas_guardadas = pedido.mesa_pedido.all()
            for mesa in mesas_guardadas:
                if mesa.numero_mesa != 9999:
                    mesa.estado = MesaEstado.objects.get(mesa_estado='DI')
                    mesa.utilizada_por_numero_pedido = None
                    mesa.save()

            nro_factura = venta_actual.numero_factura_venta
            nro_factura.venta_asociada = venta_actual.id
            nro_factura.fecha_hora_uso = timezone.now()
            nro_factura.save()

            super(VentaAdmin, self).save_model(request, obj, form, change)

        elif "_cancel" in request.POST:
            venta_actual.estado_venta = VentaEstado.objects.get(venta_estado='CAN')
            venta_actual.motivo_cancelacion = request.POST.get('motivo', '')
            venta_actual.observaciones_cancelacion = request.POST.get('observaciones', '')
            venta_actual.usuario_cancelacion = Empleado.objects.get(usuario_id=request.user)
            venta_actual.fecha_hora_cancelacion = timezone.now()

            pedido = venta_actual.numero_pedido
            pedido.estado_pedido = PedidoEstado.objects.get(pedido_estado='VIG')
            pedido.save()

            nro_factura = venta_actual.numero_factura_venta
            nro_factura.venta_asociada = venta_actual.id
            nro_factura.fecha_hora_uso = timezone.now()
            nro_factura.save()

            super(VentaAdmin, self).save_model(request, obj, form, change)

    # def save_formset(self, request, form, formset, change):
    #
    #     venta_actual = form.instance
    #
    #     # Marcar como Procesado los Productos del detalle del Pedido y de la Comanda y descontar del stock.
    #     if "_continue" in request.POST or "_save" in request.POST:
    #         for form in formset:
    #             venta_actual_detalle = form.instance
    #
    #     super(VentaAdmin, self).save_formset(request, form, formset, change)

    def get_readonly_fields(self, request, obj=None):
        if obj is not None and obj.estado_venta.venta_estado in ('PRO', 'CAN'):
            return [i.name for i in self.model._meta.fields] + \
                   [i.name for i in self.model._meta.many_to_many]
        elif obj is None:
            return self.readonly_fields
        else:
            return super(VentaAdmin, self).get_readonly_fields(request, obj)

    def changeform_view(self, request, object_id=None, form_url='', extra_context=None):
        extra_context = extra_context or {}

        extra_context['show_button'] = True
        if object_id is not None:
            venta_actual = Venta.objects.get(pk=object_id)
            extra_context['show_button'] = venta_actual.estado_venta.venta_estado not in ('PRO', 'CAN')

            if venta_actual.estado_venta.venta_estado == 'PRO':
                extra_context['show_save_button'] = False
                extra_context['show_continue_button'] = False
                extra_context['show_cancel_button'] = False
                extra_context['show_imprimir_button'] = True
            elif venta_actual.estado_venta.venta_estado == 'CAN':
                extra_context['show_save_button'] = False
                extra_context['show_continue_button'] = False
                extra_context['show_cancel_button'] = False
                extra_context['show_imprimir_button'] = False
            elif venta_actual.estado_venta.venta_estado == 'PEN':
                extra_context['show_save_button'] = True
                extra_context['show_continue_button'] = True
                extra_context['show_cancel_button'] = True
                extra_context['show_imprimir_button'] = False

        elif object_id is None:
            extra_context['show_save_button'] = True
            extra_context['show_continue_button'] = True
            extra_context['show_cancel_button'] = False
            extra_context['show_imprimir_button'] = False

        return super(VentaAdmin, self).changeform_view(request, object_id, form_url, extra_context)

    def get_form(self, request, obj=None, **kwargs):

        # import pdb
        # pdb.set_trace()

        form = super(VentaAdmin, self).get_form(request, obj=obj, **kwargs)
        if obj is None or obj.pk and obj.estado_venta.venta_estado == 'PEN':
            # usuario = Empleado.objects.get(usuario=request.user)
            # form.base_fields['cajero'].initial = usuario
            # form.base_fields['horario'].initial = usuario.horario
            form.base_fields['apertura_caja'].widget.attrs['readonly'] = True
            form.base_fields['apertura_caja'].widget.attrs['style'] = 'width: 300px;'
            form.base_fields['timbrado'].widget.attrs['readonly'] = True
            form.base_fields['efectivo_recibido'].widget.attrs['readonly'] = True
            form.base_fields['voucher'].widget.attrs['readonly'] = True
            # form.base_fields['cajero'].widget.attrs['disabled'] = True
        form.request = request
        return form

    def get_queryset(self, request):
        usuario = Empleado.objects.get(usuario_id=request.user)
        queryset = None
        if usuario.cargo.cargo == 'CA':
            queryset = Venta.objects.filter(venta_ocasional=False, apertura_caja__cajero=usuario,
                                            apertura_caja__estado_apertura_caja__in=['VIG', 'EXP'])
        elif usuario.usuario.is_superuser is True:
            queryset = Venta.objects.filter(venta_ocasional=False)
                                            # apertura_caja__estado_apertura_caja__in=['VIG', 'EXP'])
        return queryset

    def has_delete_permission(self, request, obj=None):
        return False

    # def get_formsets_with_inlines(self, request, obj=None):


class VentaOcasionalDetalleInline(admin.TabularInline):
    model = VentaOcasionalDetalle
    extra = 0
    min_num = 1
    form = VentaOcasionalDetalleForm
    raw_id_fields = ['producto_venta']
    # verbose_name =
    # verbose_name_plural =

    def get_readonly_fields(self, request, obj=None):
        if obj is not None and obj.estado_venta.venta_estado in ('PRO', 'CAN', 'PEN'):
            return [i.name for i in self.model._meta.fields]
        else:
            return super(VentaOcasionalDetalleInline, self).get_readonly_fields(request, obj)

    def has_add_permission(self, request):
        object_id = request.path.split("/")[-2]
        if object_id != "add":
            venta_actual = VentaOcasional.objects.get(pk=object_id)
            return venta_actual.estado_venta.venta_estado not in ('PRO', 'CAN', 'PEN')
        else:
            return super(VentaOcasionalDetalleInline, self).has_add_permission(request)

    def has_delete_permission(self, request, obj=None):
        if obj is not None and obj.estado_venta.venta_estado in ('PRO', 'CAN', 'PEN'):
            return False
        return super(VentaOcasionalDetalleInline, self).has_delete_permission(request, obj)
    

class VentaOcasionalAdmin(admin.ModelAdmin):
    form = VentaForm

    class Media:
        js = [
            'ventas/js/venta_ocasional.js'
        ]

    readonly_fields = ['empresa', 'numero_factura_venta', 'fecha_hora_venta', 'estado_venta', 'numero_pedido']  # 'timbrado',

    raw_id_fields = ['cliente_factura']  #  'numero_pedido'

    fieldsets = [
        ('Facturacion', {'fields': [('empresa', 'timbrado', 'fecha_limite_vigencia_timbrado'),
                                          'numero_factura_venta',
                                          ('apertura_caja', 'estado_apertura_caja', 'fecha_hora_apertura_caja'),
                                          ('caja', 'cajero', 'horario', 'sector'),
                                          'fecha_hora_venta']}),
        # ('Pedido', {'fields': ['numero_pedido', 'total_pedido']}),
        # ('Reserva/Cliente', {'fields': ['posee_reserva', 'entrega_reserva', 'cliente_factura']}),
        ('Cliente', {'fields': ['cliente_factura', 'cliente_documento_factura', ('direccion_cliente', 'ciudad_cliente', 'pais_cliente'), ('telefonos_cliente', 'email')]}),
        ('Venta', {'fields': ['estado_venta', 'numero_pedido']}),
        ('Pago', {'fields': [('forma_pago', 'efectivo_recibido', 'voucher'), 'total_venta', 'vuelto']}),
    ]

    inlines = [VentaOcasionalDetalleInline]

    list_display = ['numero_factura_venta', 'apertura_caja', 'get_fecha_hora_apertura_caja', 'get_numero_caja',
                    'cajero', 'get_sector', 'numero_pedido', 'cliente_factura', 'fecha_hora_venta', 'forma_pago', 'total_venta',
                    'colorea_estado_venta']
    list_display_links = ['numero_factura_venta']
    list_filter = ['numero_factura_venta__numero_factura', 'apertura_caja', 'apertura_caja__fecha_hora_apertura_caja',
                   'apertura_caja__caja', 'apertura_caja__cajero', 'apertura_caja__sector', 'numero_pedido', 'cliente_factura',
                   'fecha_hora_venta', 'forma_pago', 'estado_venta__venta_estado']
    search_fields = ['numero_factura_venta__numero_factura', 'apertura_caja__id', 'apertura_caja__fecha_hora_apertura_caja',
                     'apertura_caja__caja__numero_caja', 'apertura_caja__sector__sector', 'numero_pedido__numero_pedido', 'cliente_factura__nombres',
                     'cliente_factura__apellidos', 'fecha_hora_venta', 'forma_pago__forma_pago_venta',
                     'estado_venta__venta_estado', 'apertura_caja__cajero__usuario__username']

    def colorea_estado_venta(self, obj):
        # color = 'black'
        if obj.estado_venta.venta_estado == 'PRO':
            color = 'green'
            # print 'Entra en colorea_estado_compra:', obj.estado_compra.estado_compra, color
            return format_html('<span style="color: %s"><b> %s </b></span>' %
                               (color, obj.estado_venta.get_venta_estado_display()))
        elif obj.estado_venta.venta_estado == 'CAN':
            color = 'orange'
            return format_html('<span style="color: %s"><b> %s </b></span>' %
                               (color, obj.estado_venta.get_venta_estado_display()))
        elif obj.estado_venta.venta_estado == 'PEN':
            color = 'red'
            return format_html('<span style="color: %s"><b> %s </b></span>' %
                               (color, obj.estado_venta.get_venta_estado_display()))
        return obj.estado_venta
    colorea_estado_venta.short_description = 'Estado Venta'

    def get_queryset(self, request):
        usuario = Empleado.objects.get(usuario_id=request.user)
        queryset = None
        if usuario.cargo.cargo == 'CA':
            queryset = VentaOcasional.objects.filter(venta_ocasional=True, apertura_caja__cajero=usuario,
                                                     apertura_caja__estado_apertura_caja__in=['VIG', 'EXP'])
        elif usuario.usuario.is_superuser is True:
            queryset = VentaOcasional.objects.filter(venta_ocasional=True)
                                                     # apertura_caja__estado_apertura_caja__in=['VIG', 'EXP'])
        return queryset

    def save_model(self, request, obj, form, change):

        # import pdb
        # pdb.set_trace()

        venta = obj

        venta.estado_venta = VentaEstado.objects.get(venta_estado='PRO')

        if not change:
            nro_factura = venta.numero_factura_venta
            nro_factura.venta_asociada = venta.id
            nro_factura.fecha_hora_uso = timezone.now()
            nro_factura.save()

        # pedido = Pedido(mesa_pedido=Mesa.objects.get(numero_mesa='9999'),
        pedido = Pedido(jornada=venta.apertura_caja.jornada,
                        mozo_pedido=venta.apertura_caja.jornada.mozo,
                        estado_pedido=PedidoEstado.objects.get(pedido_estado='PRO'),
                        fecha_hora_pedido=timezone.now(),
                        total_pedido=venta.total_venta)
        pedido.save()
        pedido.mesa_pedido.add(Mesa.objects.get(numero_mesa='9999'))
        venta.numero_pedido_id = pedido.numero_pedido
        # venta.save()

        super(VentaOcasionalAdmin, self).save_model(request, obj, form, change)

    def save_formset(self, request, form, formset, change):

        # import pdb
        # pdb.set_trace()

        venta = form.instance

        # if not change:
        for form in formset:
            venta_detalle = form.instance
            pedido_detalle = PedidoDetalle(pedido=venta.numero_pedido,
                                           producto_pedido=venta_detalle.producto_venta,
                                           precio_producto_pedido=venta_detalle.precio_producto_venta,
                                           cantidad_producto_pedido=venta_detalle.cantidad_producto_venta,
                                           total_producto_pedido=venta_detalle.total_producto_venta,
                                           fecha_pedido_detalle=timezone.now(),
                                           procesado=False,
                                           cancelado=False)
            pedido_detalle.save()

    # ==================================================================================================================
    # 23/11/2016: Finalmente decidi confirmar los descuentos del Stock o generacion de Movimientos de Stock al
    # momento de confirmar las VentasOcasionales o los Pedidos, esto con el fin de evitar un gap de tiempo entre
    # que se hace un Pedido y se procesa una Comanda lo cual puede reflejar un Stock incorrecto. Se debe garantizar
    # la disponibilidad de los Productos/Insumos para los Pedidos ya realizados.
    # Con esto hay que prever que al momento de Cancelar un Pedido se deben volver a sumar los Productos al Stock.
    # En las VentasOcasionales no sera necesario realizar esta reversion.
    # ==================================================================================================================

            # De acuerdo a la Categoria del Producto se debe definir el "area_encargada" (Sector) para la Comanda
            # encargado = Sector.objects.get(sector='COC')
            # Comandas para la COCINA
            if venta_detalle.producto_venta.compuesto is True \
                    and venta_detalle.producto_venta.categoria.categoria == 'CO':
                if venta.numero_pedido.mozo_pedido.usuario.is_superuser is True:
                    solicitante = Sector.objects.get(sector='BPR')
                else:
                    solicitante = Sector.objects.get(sector=venta.numero_pedido.mozo_pedido.sector.sector)
                encargado = Sector.objects.get(sector='COC')

            # # Los Tragos son procesados por la Barra Principal
            # elif venta_detalle.producto_venta.compuesto is True \
            #         and venta_detalle.producto_venta.categoria.categoria == 'BE':
            #         # and venta_detalle.producto_venta.subcategoria.subcategoria == 'TRA':
            #     encargado = Sector.objects.get(sector='BPR')

            # Finalmente se define que todos los Sectores pueden procesar todos los pedidos sin importar la Categoria
            # y SubCategoria del Producto a excepcion de las Comidas por lo tanto la condicion para definir el
            # "area_encargada" depende del sector al cual esta asignado el Mozo/Barman.
            elif venta.numero_pedido.mozo_pedido.usuario.is_superuser is True:
                solicitante = Sector.objects.get(sector='BPR')
                encargado = Sector.objects.get(sector='BPR')
            else:
                solicitante = Sector.objects.get(sector=venta.numero_pedido.mozo_pedido.sector.sector)
                encargado = Sector.objects.get(sector=venta.numero_pedido.mozo_pedido.sector.sector)

            comanda = Comanda(numero_pedido=venta.numero_pedido,
                              id_pedido_detalle_id=pedido_detalle.id,
                              area_solicitante=solicitante,
                              usuario_solicitante=Empleado.objects.get(usuario_id=request.user),
                              # producto_a_entregar=ProductoVenta.objects.get(id=venta_detalle.producto_venta.id),
                              producto_a_entregar=venta_detalle.producto_venta,
                              cantidad_solicitada=venta_detalle.cantidad_producto_venta,
                              area_encargada=encargado,
                              fecha_hora_pedido_comanda=timezone.now(),
                              tiempo_estimado_procesamiento=venta_detalle.producto_venta.tiempo_elaboracion,
                              estado_comanda='PEN')
            comanda.save()

            # import pdb
            # pdb.set_trace()

            # Descuenta los Productos del Stock. Analiza si el Producto es COMPUESTO y de acuerdo a la
            # Categoria genera el Movimiento de Stock
            if pedido_detalle.producto_pedido.compuesto is True:
                if pedido_detalle.producto_pedido.categoria.categoria == 'CO':
                    deposito = Deposito.objects.get(deposito='DCO')
                    prod_comp_detalle = ProductoCompuestoDetalle.objects.filter(producto_compuesto_id=pedido_detalle.producto_pedido.id)

                    for producto_insumo in prod_comp_detalle:
                    # Recorrer los Insumos para determinar el ProductoInsumo del cual se descontara el Stock.
                    # =====> Se debe descontar del ProductoInsumo con menor Cantidad Existente. <=====
                        producto_menor_cant_existente = StockDepositoAjusteInventario.objects.none
                        menor_cant_exist_prod_insumo = 0
                        cantidad_descontada = 0
                        cantidad_a_descontar = producto_insumo.cantidad_insumo * pedido_detalle.cantidad_producto_pedido
                        while cantidad_descontada < cantidad_a_descontar:
                            productos = Producto.objects.filter(insumo_id=producto_insumo.insumo.id, tipo_producto='IN')
                            for producto in productos:
                                try:
                                    prod_exist_deposito = StockDepositoAjusteInventario.objects.get(id=producto.id, deposito_id=deposito.id)
                                    if prod_exist_deposito.cantidad_existente > 0:
                                        if producto == productos.first():
                                            menor_cant_exist_prod_insumo = prod_exist_deposito.cantidad_existente
                                            producto_menor_cant_existente = prod_exist_deposito
                                        elif menor_cant_exist_prod_insumo < prod_exist_deposito.cantidad_existente:
                                            menor_cant_exist_prod_insumo = prod_exist_deposito.cantidad_existente
                                            producto_menor_cant_existente = prod_exist_deposito

                                except StockDepositoAjusteInventario.DoesNotExist:
                                    pass

                            if producto_menor_cant_existente.cantidad_existente < (cantidad_a_descontar - cantidad_descontada):
                                stock = MovimientoStock(producto_stock_id=producto_menor_cant_existente.id,
                                                        tipo_movimiento='VE',
                                                        id_movimiento=pedido_detalle.id,
                                                        ubicacion_origen=encargado.deposito,
                                                        ubicacion_destino=Deposito.objects.get(deposito='CLI'),
                                                        cantidad_entrante=0,
                                                        cantidad_saliente=producto_menor_cant_existente.cantidad_existente,
                                                        fecha_hora_registro_stock=timezone.now())
                                stock.save()
                                cantidad_descontada += producto_menor_cant_existente.cantidad_existente
                                # pedido_detalle.id_mov_stock = stock.id
                            elif producto_menor_cant_existente.cantidad_existente >= (cantidad_a_descontar - cantidad_descontada):
                                stock = MovimientoStock(producto_stock_id=producto_menor_cant_existente.id,
                                                        tipo_movimiento='VE',
                                                        id_movimiento=pedido_detalle.id,
                                                        ubicacion_origen=encargado.deposito,
                                                        ubicacion_destino=Deposito.objects.get(deposito='CLI'),
                                                        cantidad_entrante=0,
                                                        cantidad_saliente=(cantidad_a_descontar - cantidad_descontada),
                                                        fecha_hora_registro_stock=timezone.now())
                                stock.save()
                                cantidad_descontada += (cantidad_a_descontar - cantidad_descontada)
                                # pedido_detalle.id_mov_stock = stock.id

                elif pedido_detalle.producto_pedido.categoria.categoria == 'BE':
                    deposito = encargado.deposito
                    prod_comp_detalle = ProductoCompuestoDetalle.objects.filter(producto_compuesto_id=pedido_detalle.producto_pedido.id)

                    for producto_insumo in prod_comp_detalle:
                    # Recorrer los Insumos para determinar el ProductoInsumo del cual se descontara el Stock.
                    # =====> Se debe descontar del ProductoInsumo con menor Cantidad Existente. <=====
                        producto_menor_cant_existente = StockDepositoAjusteInventario.objects.none
                        menor_cant_exist_prod_insumo = 0
                        cantidad_descontada = 0
                        cantidad_a_descontar = producto_insumo.cantidad_insumo * pedido_detalle.cantidad_producto_pedido
                        while cantidad_descontada < cantidad_a_descontar:
                            productos = Producto.objects.filter(insumo_id=producto_insumo.insumo.id, tipo_producto='IN')
                            for producto in productos:
                                try:
                                    prod_exist_deposito = StockDepositoAjusteInventario.objects.get(id=producto.id, deposito_id=deposito.id)
                                    if prod_exist_deposito.cantidad_existente > 0:
                                        if producto == productos.first():
                                            menor_cant_exist_prod_insumo = prod_exist_deposito.cantidad_existente
                                            producto_menor_cant_existente = prod_exist_deposito
                                        elif menor_cant_exist_prod_insumo < prod_exist_deposito.cantidad_existente:
                                            menor_cant_exist_prod_insumo = prod_exist_deposito.cantidad_existente
                                            producto_menor_cant_existente = prod_exist_deposito

                                except StockDepositoAjusteInventario.DoesNotExist:
                                    pass

                            if producto_menor_cant_existente.cantidad_existente < (cantidad_a_descontar - cantidad_descontada):
                                stock = MovimientoStock(producto_stock_id=producto_menor_cant_existente.id,
                                                        tipo_movimiento='VE',
                                                        id_movimiento=pedido_detalle.id,
                                                        ubicacion_origen=encargado.deposito,
                                                        ubicacion_destino=Deposito.objects.get(deposito='CLI'),
                                                        cantidad_entrante=0,
                                                        cantidad_saliente=producto_menor_cant_existente.cantidad_existente,
                                                        fecha_hora_registro_stock=timezone.now())
                                stock.save()
                                cantidad_descontada += producto_menor_cant_existente.cantidad_existente
                                # pedido_detalle.id_mov_stock = stock.id
                            elif producto_menor_cant_existente.cantidad_existente >= (cantidad_a_descontar - cantidad_descontada):
                                stock = MovimientoStock(producto_stock_id=producto_menor_cant_existente.id,
                                                        tipo_movimiento='VE',
                                                        id_movimiento=pedido_detalle.id,
                                                        ubicacion_origen=encargado.deposito,
                                                        ubicacion_destino=Deposito.objects.get(deposito='CLI'),
                                                        cantidad_entrante=0,
                                                        cantidad_saliente=(cantidad_a_descontar - cantidad_descontada),
                                                        fecha_hora_registro_stock=timezone.now())
                                stock.save()
                                cantidad_descontada += (cantidad_a_descontar - cantidad_descontada)
                                # pedido_detalle.id_mov_stock = stock.id

            elif pedido_detalle.producto_pedido.compuesto is False:
                stock = MovimientoStock(producto_stock_id=pedido_detalle.producto_pedido.id,
                                        tipo_movimiento='VE',
                                        id_movimiento=pedido_detalle.id,
                                        ubicacion_origen=encargado.deposito,
                                        ubicacion_destino=Deposito.objects.get(deposito='CLI'),
                                        cantidad_entrante=0,
                                        cantidad_saliente=pedido_detalle.cantidad_producto_pedido,
                                        fecha_hora_registro_stock=timezone.now())
                stock.save()

        super(VentaOcasionalAdmin, self).save_formset(request, form, formset, change)

    def get_readonly_fields(self, request, obj=None):
        if obj is not None and obj.estado_venta.venta_estado in ('PRO', 'CAN'):
            return [i.name for i in self.model._meta.fields] + \
                   [i.name for i in self.model._meta.many_to_many]
        elif obj is None:
            return self.readonly_fields
        else:
            return super(VentaOcasionalAdmin, self).get_readonly_fields(request, obj)

    def changeform_view(self, request, object_id=None, form_url='', extra_context=None):
        extra_context = extra_context or {}

        extra_context['show_button'] = True
        if object_id is not None:
            venta_actual = VentaOcasional.objects.get(pk=object_id)
            extra_context['show_button'] = venta_actual.estado_venta.venta_estado not in ('PRO', 'CAN')

            if venta_actual.estado_venta.venta_estado in ('PRO', 'CAN'):
                extra_context['show_save_button'] = False
                extra_context['show_addanother_button'] = False
                # extra_context['show_cancel_button'] = False
                extra_context['show_imprimir_button'] = True
            elif venta_actual.estado_venta.venta_estado == 'PEN':
                extra_context['show_save_button'] = True
                extra_context['show_addanother_button'] = True
                # extra_context['show_cancel_button'] = True
                extra_context['show_imprimir_button'] = False

        elif object_id is None:
            extra_context['show_save_button'] = True
            extra_context['show_addanother_button'] = True
            # extra_context['show_cancel_button'] = False
            extra_context['show_imprimir_button'] = False

        return super(VentaOcasionalAdmin, self).changeform_view(request, object_id, form_url, extra_context)

    def get_form(self, request, obj=None, **kwargs):

        # import pdb
        # pdb.set_trace()

        form = super(VentaOcasionalAdmin, self).get_form(request, obj=obj, **kwargs)
        if obj is None:
            # usuario = Empleado.objects.get(usuario=request.user)
            # form.base_fields['cajero'].initial = usuario
            # form.base_fields['horario'].initial = usuario.horario
            form.base_fields['apertura_caja'].widget.attrs['readonly'] = True
            form.base_fields['apertura_caja'].widget.attrs['style'] = 'width: 300px;'
            form.base_fields['timbrado'].widget.attrs['readonly'] = True
            form.base_fields['efectivo_recibido'].widget.attrs['readonly'] = True
            form.base_fields['voucher'].widget.attrs['readonly'] = True
            # form.base_fields['cajero'].widget.attrs['disabled'] = True
        form.request = request
        return form

    def has_delete_permission(self, request, obj=None):
        return False
    

class ComandaAdmin(admin.ModelAdmin):
    # form =

    # readonly_fields = []

    actions = ['marcar_procesado']


    raw_id_fields = ['producto_a_entregar']

    fieldsets = [
        ('Pedido', {'fields': ['numero_pedido']}),
        ('Solicitante', {'fields': ['area_solicitante', 'usuario_solicitante', 'fecha_hora_pedido_comanda']}),
        ('Producto', {'fields': ['producto_a_entregar', 'cantidad_solicitada']}),
        ('Encargado', {'fields': ['area_encargada', 'tiempo_estimado_procesamiento']}),
        ('Estado', {'fields': ['estado_comanda', 'fecha_hora_procesamiento_comanda', 'usuario_procesa']}),
    ]

    list_display = ['numero_pedido', 'area_solicitante', 'usuario_solicitante', 'producto_a_entregar',
                    'cantidad_solicitada', 'area_encargada', 'fecha_hora_pedido_comanda',
                    'tiempo_estimado_procesamiento', 'colorea_estado_comanda', 'usuario_procesa',
                    'fecha_hora_procesamiento_comanda']
    list_filter = [('numero_pedido', admin.RelatedOnlyFieldListFilter), ('area_solicitante', admin.RelatedOnlyFieldListFilter), ('usuario_solicitante', admin.RelatedOnlyFieldListFilter),
                   'producto_a_entregar', ('area_encargada', admin.RelatedOnlyFieldListFilter), 'fecha_hora_pedido_comanda', 'estado_comanda', 'usuario_procesa', 'fecha_hora_procesamiento_comanda']
    search_fields = ['numero_pedido__numero_pedido', 'area_solicitante__sector', 'usuario_solicitante__usuario__username',
                     'producto_a_entregar__producto', 'area_encargada__sector', 'fecha_hora_pedido_comanda',
                     'estado_comanda', 'usuario_procesa__usuario__username', 'fecha_hora_procesamiento_comanda']

    def colorea_estado_comanda(self, obj):
        # color = 'black'
        if obj.estado_comanda == 'PRO':
            color = 'green'
            return format_html('<span style="color: %s"><b> %s </b></span>' %
                               (color, obj.get_estado_comanda_display()))
        elif obj.estado_comanda == 'PEN':
            color = 'red'
            return format_html('<span style="color: %s"><b> %s </b></span>' %
                               (color, obj.get_estado_comanda_display()))
        elif obj.estado_comanda == 'CAN':
            color = 'orange'
            return format_html('<span style="color: %s"><b> %s </b></span>' %
                               (color, obj.get_estado_comanda_display()))
        return obj.estado_comanda
    colorea_estado_comanda.short_description = 'Estado Comanda'

    def marcar_procesado(self, request, queryset):

        # import pdb
        # pdb.set_trace()

        rows_updated = 0
        queryset = queryset.filter(estado_comanda='PEN')

        # ==============================================================================================================
        # 23/11/2016: Finalmente decidi confirmar los descuentos del Stock o generacion de Movimientos de Stock al
        # momento de confirmar las VentasOcasionales o los Pedidos, esto con el fin de evitar un gap de tiempo entre
        # que se hace un Pedido y se procesa una Comanda lo cual puede reflejar un Stock incorrecto. Se debe garantizar
        # la disponibilidad de los Productos/Insumos para los Pedidos ya realizados.
        # Con esto hay que prever que al momento de Cancelar un Pedido se deben volver a sumar los Productos al Stock.
        # En las VentasOcasionales no sera necesario realizar esta reversion.
        # ==============================================================================================================

        # Marca como Procesado el detalle del Pedido y resta (descuenta) los productos del Stock.
        for q in queryset:
            # # Si el Producto es Compuesto se debe recorrer el detalle del ProductoCompuesto para poder descontar las
            # # cantidades de los Productos componentes.
            #
            # # # El "area_encargada" ya se analiza y define al momento de generar la Comanda ya sea en Pedido o VentaOcasional
            # # # No corresponde volver a hacer este analsis y definicion de "ubicacion_origen"
            # # if q.numero_pedido.mozo_pedido.usuario.is_superuser is True:
            # #     origen = Deposito.objects.get(deposito='DBP')
            # # else:
            # #     origen = Deposito.objects.get(id=q.numero_pedido.mozo_pedido.sector.deposito_id)
            #
            # if q.producto_a_entregar.compuesto is True:
            #     if q.producto_a_entregar.categoria.categoria == 'CO':
            #         deposito = Deposito.objects.get(deposito='DCO')
            #         prod_comp_detalle = ProductoCompuestoDetalle.objects.filter(producto_compuesto_id=q.producto_a_entregar.id)
            #         cantidad = 0
            #         for producto_insumo in prod_comp_detalle:
            #             # Recorrer los Insumos para determinar el ProductoInsumo del cual se descontara el Stock
            #             if producto_insumo.insumo.get_cantidad_existente_insumo_dco() > 0:
            #                 cant_posible_elaborar = producto_insumo.insumo.get_cantidad_existente_insumo_dco() / (producto_insumo.cantidad_insumo if producto_insumo.cantidad_insumo else 1)
            #
            #                 if producto_insumo == prod_comp_detalle.first():
            #                     cantidad = cant_posible_elaborar
            #
            #                 elif cant_posible_elaborar < cantidad:
            #                     cantidad = cant_posible_elaborar
            #
            #             elif producto_insumo.insumo.get_cantidad_existente_insumo() <= 0:
            #                 cantidad = 0
            #
            #         if cantidad <= 0:
            #             raise ValidationError({'producto_pedido': 'El Producto Compuesto (Comida) seleccionado no posee stock '
            #                                                      'disponible en el %s. Verifique con el Encargado de '
            #                                                      'este Deposito.' % deposito})
            #         elif self.cleaned_data['cantidad_producto_pedido'] > cantidad:
            #             self.fields['cantidad_producto_venta'].widget.attrs['readonly'] = False  # ==> PROBAR
            #             raise ValidationError({'cantidad_producto_pedido': 'La cantidad solicitada del Producto Compuesto (Comida)'
            #                                                               'seleccionado supera el stock disponible en el "%s". '
            #                                                               'Modifique la cantidad solicitada o cancele '
            #                                                               'el pedido de este Producto.' % deposito})
            #
            #         stock = MovimientoStock(producto_stock_id=insumo.producto_id,
            #                                 tipo_movimiento='VE',
            #                                 id_movimiento=q.numero_pedido.numero_pedido,
            #                                 ubicacion_origen=q.area_encargada,
            #                                 ubicacion_destino=Deposito.objects.get(deposito='CLI'),
            #                                 cantidad_entrante=0,
            #                                 cantidad_saliente=insumo.cantidad_producto * q.cantidad_solicitada,
            #                                 fecha_hora_registro_stock=timezone.now())
            #         stock.save()
            # else:
            #     stock = MovimientoStock(producto_stock_id=q.producto_a_entregar.id,
            #                             tipo_movimiento='VE',
            #                             id_movimiento=q.numero_pedido.numero_pedido,
            #                             ubicacion_origen=q.area_encargada,
            #                             ubicacion_destino=Deposito.objects.get(deposito='CLI'),
            #                             cantidad_entrante=0,
            #                             cantidad_saliente=q.cantidad_solicitada,
            #                             fecha_hora_registro_stock=timezone.now())
            #     stock.save()

            pedido_detalle = PedidoDetalle.objects.get(id=q.id_pedido_detalle_id)
            pedido_detalle.procesado = True
            pedido_detalle.save()

            q.estado_comanda = 'PRO'
            q.fecha_hora_procesamiento_comanda = timezone.now()
            q.usuario_procesa = Empleado.objects.get(usuario_id=request.user)
            q.save()
            rows_updated += 1

        if rows_updated == 1:
            message_bit = "1 Comanda fue"
        else:
            message_bit = "%s Comandas fueron" % rows_updated
        self.message_user(request, "%s correctamente marcada/s como procesada/s." % message_bit)
    marcar_procesado.short_description = "Marcar las Comandas seleccionadas como procesadas"

    def save_model(self, request, obj, form, change):

        # import pdb
        # pdb.set_trace()

        comanda = obj

    # # ==================================================================================================================
    # # 23/11/2016: Finalmente decido confirmar los descuentos del Stock o generacion de Movimientos de Stock al
    # # momento de confirmar las VentasOcasionales o los Pedidos, esto con el fin de evitar un gap de tiempo entre
    # # que se hace un Pedido y se procesa una Comanda lo cual puede reflejar un Stock incorrecto. Se debe garantizar
    # # la disponibilidad de los Productos/Insumos para los Pedidos ya realizados.
    # # Con esto hay que prever que al momento de Cancelar un Pedido se deben volver a sumar los Productos al Stock.
    # # En las VentasOcasionales no sera necesario realizar esta reversion.
    # # ==================================================================================================================
    #
    #     # Marca como Procesado el detalle del Pedido y resta (descuenta) los productos del Stock.
    #
    #     # Si el Producto es Compuesto se debe recorrer el detalle del ProductoCompuesto para poder descontar las
    #     # cantidades de los Productos componentes.
    #
    #     # ==============================================================================================================
    #     # ---> Prever la situacion de que el Producto tenga como origen la Cocina <---
    #     # ==============================================================================================================
    #     # # Comandas para la COCINA
    #     # if comanda.producto_a_entregar.compuesto is True and comanda.producto_a_entregar.categoria.categoria == 'CO':
    #     #     origen = Deposito.objects.get(deposito='DCO')
    #     # elif comanda.numero_pedido.mozo_pedido.usuario.is_superuser is True:
    #     #     origen = Deposito.objects.get(deposito='DBP')
    #     # else:
    #     #     origen = Deposito.objects.get(id=comanda.numero_pedido.mozo_pedido.sector.deposito_id)
    #
    #     if comanda.producto_a_entregar.compuesto is True:
    #         prod_comp_detalle = ProductoCompuestoDetalle.objects.filter(producto_compuesto=comanda.producto_a_entregar.id)
    #         for insumo in prod_comp_detalle:
    #             stock = MovimientoStock(producto_stock_id=insumo.producto_id,
    #                                     tipo_movimiento='VE',
    #                                     id_movimiento=comanda.numero_pedido.numero_pedido,
    #                                     ubicacion_origen=comanda.area_encargada.deposito,
    #                                     ubicacion_destino=Deposito.objects.get(deposito='CLI'),
    #                                     cantidad_entrante=0,
    #                                     cantidad_saliente=insumo.cantidad_producto,
    #                                     fecha_hora_registro_stock=timezone.now())
    #             stock.save()
    #     else:
    #         stock = MovimientoStock(producto_stock_id=comanda.producto_a_entregar.id,
    #                                 tipo_movimiento='VE',
    #                                 id_movimiento=comanda.numero_pedido.numero_pedido,
    #                                 ubicacion_origen=comanda.area_encargada.deposito,
    #                                 ubicacion_destino=Deposito.objects.get(deposito='CLI'),
    #                                 cantidad_entrante=0,
    #                                 cantidad_saliente=comanda.cantidad_solicitada,
    #                                 fecha_hora_registro_stock=timezone.now())
    #         stock.save()

        pedido_detalle = PedidoDetalle.objects.get(id=comanda.id_pedido_detalle_id)
        pedido_detalle.procesado = True
        pedido_detalle.save()

        comanda.estado_comanda = 'PRO'
        comanda.fecha_hora_procesamiento_comanda = timezone.now()
        comanda.usuario_procesa = Empleado.objects.get(usuario_id=request.user)
        # q.save()

        super(ComandaAdmin, self).save_model(request, obj, form, change)

    def get_readonly_fields(self, request, obj=None):
        if obj is not None:  # and obj.estado_apertura_caja in ('VIG', 'CER'):
            return [i.name for i in self.model._meta.fields] + \
                   [i.name for i in self.model._meta.many_to_many]
        else:
            return super(ComandaAdmin, self).get_readonly_fields(request, obj)

    def changeform_view(self, request, object_id=None, form_url='', extra_context=None):
        extra_context = extra_context or {}

        extra_context['show_button'] = True
        if object_id is not None:
            comanda_actual = Comanda.objects.get(pk=object_id)
            extra_context['show_button'] = comanda_actual.estado_comanda not in ('PRO', 'CAN')

            if comanda_actual.estado_comanda in ('PRO', 'CAN'):
                extra_context['show_save_button'] = False
                # extra_context['show_addanother_button'] = False
                # extra_context['show_cancel_button'] = False
                # extra_context['show_imprimir_button'] = True
            elif comanda_actual.estado_comanda == 'PEN':
                extra_context['show_save_button'] = True
                # extra_context['show_addanother_button'] = True
                # extra_context['show_cancel_button'] = True
                # extra_context['show_imprimir_button'] = False

        elif object_id is None:
            extra_context['show_save_button'] = True
            # extra_context['show_addanother_button'] = True
            # extra_context['show_cancel_button'] = False
            # extra_context['show_imprimir_button'] = False

        return super(ComandaAdmin, self).changeform_view(request, object_id, form_url, extra_context)

    # def get_form(self, request, obj=None, **kwargs):
    #
    #     # import pdb
    #     # pdb.set_trace()
    #
    #     form = super(ComandaAdmin, self).get_form(request, obj=obj, **kwargs)
    #     usuario = Empleado.objects.get(usuario=request.user)
    #     form.base_fields['cajero'].initial = usuario
    #     form.base_fields['horario'].initial = usuario.horario
    #     form.base_fields['cajero'].widget.attrs['readonly'] = True
    #     form.base_fields['horario'].widget.attrs['readonly'] = True
    #     # form.base_fields['cajero'].widget.attrs['disabled'] = True
    #     # form.base_fields['horario'].widget.attrs['disabled'] = True
    #     form.request = request
    #     return form

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    def get_actions(self, request):
        actions = super(ComandaAdmin, self).get_actions(request)
        usuario = Empleado.objects.get(usuario=request.user)
        if 'delete_selected' in actions:
            del actions['delete_selected']

        if usuario.usuario.is_superuser is False and usuario.cargo.cargo != 'DE':
            del actions['marcar_procesado']

        return actions

    # Descomentar para que la pantalla de Comandas sea filtrada por "area_encargada"
    def get_queryset(self, request):
        usuario = Empleado.objects.get(usuario_id=request.user)
        queryset = None
        if usuario.cargo.cargo in ('MO', 'CA', 'BM'):
            queryset = Comanda.objects.filter(area_solicitante__sector=usuario.sector.sector, usuario_solicitante=usuario)
        elif usuario.cargo.cargo == 'DE':
            queryset = Comanda.objects.filter(area_encargada__sector=usuario.sector.sector)
        elif usuario.usuario.is_superuser is True:
            queryset = Comanda.objects.all()
        return queryset


class AperturaCajaAdmin(admin.ModelAdmin):
    form = AperturaCajaForm

    class Media:
        js = [
            'ventas/js/apertura_caja.js'  # , 'ventas/css/apertura_caja.css'
        ]

    # formfield_overrides = []

    readonly_fields = ['jornada', 'fecha_hora_apertura_caja', 'fecha_hora_registro_apertura_caja',
                       'estado_apertura_caja']  # 'duracion_apertura', 'fecha_hora_fin_apertura_caja',

    raw_id_fields = ['caja', ]

    fieldsets = [
        ('Datos Apertura', {'fields': ['cajero', 'nombre_cajero', 'sector', 'horario', 'caja']}),
        ('Monto Apertura', {'fields': ['monto_apertura']}),
        ('Jornada', {'fields': ['jornada', 'fecha_hora_apertura_caja', 'duracion_apertura', 'fecha_hora_fin_apertura_caja']}),
        ('Otros datos', {'fields': ['estado_apertura_caja', 'fecha_hora_registro_apertura_caja']}),
    ]

    list_display = ['id', 'cajero', 'caja', 'sector', 'horario', 'jornada', 'fecha_hora_apertura_caja', 'monto_apertura', 'duracion_apertura',
                    'fecha_hora_fin_apertura_caja', 'colorea_estado_apertura_caja', 'fecha_hora_registro_apertura_caja']
    list_display_links = ['id']
    list_filter = ['id', 'cajero', 'caja', 'sector', 'horario', 'jornada', 'fecha_hora_apertura_caja', 'estado_apertura_caja']
    search_fields = ['cajero__usuario__username', 'caja__numero_caja', 'sector__sector', 'horario__horario', 'fecha_hora_apertura_caja',
                     'monto_apertura', 'estado_apertura_caja']

    def colorea_estado_apertura_caja(self, obj):
        # color = 'black'
        if obj.estado_apertura_caja == 'VIG':
            color = 'orange'
            return format_html('<span style="color: %s"><b> %s </b></span>' %
                               (color, obj.get_estado_apertura_caja_display()))
        elif obj.estado_apertura_caja == 'CER':
            color = 'green'
            return format_html('<span style="color: %s"><b> %s </b></span>' %
                               (color, obj.get_estado_apertura_caja_display()))
        elif obj.estado_apertura_caja == 'EXP':
            color = 'red'
            return format_html('<span style="color: %s"><b> %s </b></span>' %
                               (color, obj.get_estado_apertura_caja_display()))
        return obj.estado_apertura_caja
    colorea_estado_apertura_caja.short_description = 'Estado Apert. Caja'

    def save_model(self, request, obj, form, change):

        # import pdb
        # pdb.set_trace()

        apertura_caja_actual = obj

        # usuario = Empleado.objects.get(usuario=request.user)
        # if usuario.usuario.is_superuser is True:
        #     sector_usuario = Sector.objects.get(sector='BPR')
        # else:
        #     sector_usuario = Sector.objects.get(sector=usuario.sector.sector)

        # working_day = InicioJornada(mozo=apertura_caja_actual.cajero,
        #                             sector=apertura_caja_actual.sector,
        #                             horario=apertura_caja_actual.horario,
        #                             fecha_hora_inicio_jornada=timezone.now(),
        #                             duracion_jornada=apertura_caja_actual.duracion_apertura,
        #                             fecha_hora_fin_jornada=timezone.localtime(timezone.now() + datetime.timedelta(hours=apertura_caja_actual.duracion_apertura.hour, minutes=apertura_caja_actual.duracion_apertura.minute)),
        #                             estado_jornada='VIG')
        # working_day.save()

        caja = apertura_caja_actual.caja
        caja.estado_caja = 'ABI'
        caja.save()

        # apertura_caja_actual.jornada = working_day.id
        apertura_caja_actual.fecha_hora_fin_apertura_caja = timezone.localtime(timezone.now() + datetime.timedelta(hours=apertura_caja_actual.duracion_apertura.hour, minutes=apertura_caja_actual.duracion_apertura.minute))
        apertura_caja_actual.estado_apertura_caja = 'VIG'

        super(AperturaCajaAdmin, self).save_model(request, obj, form, change)

    # def save_related(self, request, form, formsets, change):
    #
    #     import pdb
    #     pdb.set_trace()
    #
    #     apertura_caja_actual = form.instance
    #
    #     journal = InicioJornada(mozo=apertura_caja_actual.cajero,
    #                             sector=apertura_caja_actual.sector,
    #                             horario=apertura_caja_actual.horario,
    #                             fecha_hora_inicio_jornada=timezone.now(),
    #                             duracion_jornada=apertura_caja_actual.duracion_apertura,
    #                             fecha_hora_fin_jornada=timezone.localtime(timezone.now() + datetime.timedelta(hours=apertura_caja_actual.duracion_apertura.hour, minutes=apertura_caja_actual.duracion_apertura.minute)),
    #                             estado_jornada='VIG')
    #     journal.save()
    #
    #     apertura_caja_actual.jornada = journal.id
    #
    #     super(AperturaCajaAdmin, self).save_related(request, form, formsets, change)

    def get_readonly_fields(self, request, obj=None):

        # import pdb
        # pdb.set_trace()

        if obj is not None and obj.estado_apertura_caja in ('VIG', 'EXP', 'CER'):
            return [i.name for i in self.model._meta.fields] + \
                   [i.name for i in self.model._meta.many_to_many]
        else:
            return super(AperturaCajaAdmin, self).get_readonly_fields(request, obj)

    def changeform_view(self, request, object_id=None, form_url='', extra_context=None):
        extra_context = extra_context or {}

        extra_context['show_button'] = True
        if object_id is not None:
            apertura_caja_actual = AperturaCaja.objects.get(pk=object_id)
            extra_context['show_button'] = apertura_caja_actual.estado_apertura_caja not in ('VIG', 'EXP', 'CER')
        return super(AperturaCajaAdmin, self).changeform_view(request, object_id, form_url, extra_context)

    def changelist_view(self, request, extra_context=None):
        queryset = self.get_queryset(request).filter(estado_apertura_caja='VIG')

        for apertura in queryset:
            now = timezone.localtime(timezone.now())
            print timezone.localtime(apertura.fecha_hora_fin_apertura_caja), now

            if timezone.localtime(apertura.fecha_hora_fin_apertura_caja) < now:
                apertura.estado_apertura_caja = 'EXP'
                apertura.save()

        return super(AperturaCajaAdmin, self).changelist_view(request, extra_context=extra_context)

    def get_form(self, request, obj=None, **kwargs):

        # import pdb
        # pdb.set_trace()

        form = super(AperturaCajaAdmin, self).get_form(request, obj=obj, **kwargs)
        if obj is None:
            usuario = Empleado.objects.get(usuario=request.user)
            if usuario.usuario.is_superuser is True:
                sector_usuario = Sector.objects.get(sector='BPR')
            else:
                sector_usuario = Sector.objects.get(sector=usuario.sector.sector)

            usuario = Empleado.objects.get(usuario=request.user)
            form.base_fields['cajero'].initial = usuario
            form.base_fields['cajero'].queryset = Empleado.objects.filter(usuario=request.user)
            form.base_fields['nombre_cajero'].initial = usuario.nombre_completo
            form.base_fields['sector'].initial = sector_usuario
            form.base_fields['sector'].queryset = Sector.objects.filter(sector=sector_usuario.sector)
            form.base_fields['sector'].widget.attrs['style'] = 'font-size: 14px; height: 30px; font-weight: bold; color: green;'
            form.base_fields['sector'].label = mark_safe('<strong style="font-size: 14px;">Sector</strong>')
            form.base_fields['horario'].initial = usuario.horario
            form.base_fields['horario'].queryset = Horario.objects.filter(id=usuario.horario.id)
            # form.base_fields['jornada'].queryset = InicioJornada.objects.none()
            form.base_fields['duracion_apertura'].initial = usuario.horario.duracion_jornada
            form.base_fields['fecha_hora_fin_apertura_caja'].initial = timezone.localtime(timezone.now() + datetime.timedelta(hours=usuario.horario.duracion_jornada.hour, minutes=usuario.horario.duracion_jornada.minute, seconds=usuario.horario.duracion_jornada.second))
            # form.base_fields['fecha_hora_fin_apertura_caja'].initial = datetime.datetime.strftime(timezone.localtime(timezone.now() + datetime.timedelta(hours=usuario.horario.duracion_jornada.hour, minutes=usuario.horario.duracion_jornada.minute, seconds=usuario.horario.duracion_jornada.second)), '%d/%m/%Y %H:%M:%S')
            form.base_fields['cajero'].widget.attrs['readonly'] = True
            form.base_fields['sector'].widget.attrs['readonly'] = True
            form.base_fields['horario'].widget.attrs['readonly'] = True
            # form.base_fields['jornada'].widget.attrs['readonly'] = True
            # form.base_fields['fecha_hora_fin_apertura_caja'].widget.attrs['readonly'] = True
            # form.base_fields['fecha_hora_fin_apertura_caja'].widget.attrs['disabled'] = True
            # form.base_fields['duracion_apertura'].widget.attrs['readonly'] = True
            # form.base_fields['duracion_apertura'].widget.attrs['disabled'] = True
            # form.base_fields['cajero'].widget.attrs['disabled'] = True
            # form.base_fields['horario'].widget.attrs['disabled'] = True

            # self.readonly_fields += ['fecha_hora_fin_apertura_caja']

            # sector = forms.CharField(widget=forms.TextInput(attrs={'readonly':'True', 'style': 'font-size: 14px; height: 20px; font-weight: bold; color: green;'}),
            #                          label=mark_safe('<strong style="font-size: 14px;">Sector</strong>'),
            #                          required=False)

        form.request = request
        return form

    def has_delete_permission(self, request, obj=None):
        return False

    def get_queryset(self, request):
        usuario = Empleado.objects.get(usuario_id=request.user)
        queryset = None
        if usuario.cargo.cargo == 'CA':
            queryset = AperturaCaja.objects.filter(cajero=usuario)
        elif usuario.usuario.is_superuser is True:
            queryset = AperturaCaja.objects.all()
        return queryset


class CierreCajaAdmin(admin.ModelAdmin):
    form = CierreCajaForm

    class Media:
        js = [
            'ventas/js/cierre_caja.js'
        ]

    readonly_fields = ['fecha_hora_registro_cierre_caja']  # 'monto_registro_efectivo', 'monto_registro_tcs', 'monto_registro_tds', 'monto_registro_otros_medios'

    raw_id_fields = ['apertura_caja']

    fieldsets = [
        ('Datos Apertura', {'classes': ('suit-tab', 'suit-tab-cierre',),
                            'fields': ['apertura_caja', 'cajero', 'caja', 'sector', 'horario', 'jornada',
                                       'fecha_hora_apertura_caja', 'estado_apertura_caja', 'fecha_hora_registro_cierre_caja']}),
        ('Operaciones Pendientes/Canceladas', {'classes': ('suit-tab', 'suit-tab-cierre',),
                                               'fields': ['cantidad_total_operaciones_pendientes', 'cantidad_total_operaciones_canceladas']}),
        ('Sobrante/Faltante', {'classes': ('suit-tab', 'suit-tab-cierre',),
                               'fields': ['total_diferencia']}),
        # ('Rendicion', {'fields': [('cantidad_operaciones_efectivo', 'monto_registro_efectivo', 'total_efectivo', 'rendicion_efectivo', 'diferencia_efectivo'),
        #                           ('cantidad_operaciones_tcs', 'monto_registro_tcs', 'rendicion_tcs', 'diferencia_tcs'),
        #                           ('cantidad_operaciones_tds', 'monto_registro_tds', 'rendicion_tds', 'diferencia_tds'),
        #                           ('cantidad_operaciones_otros_medios', 'monto_registro_otros_medios', 'rendicion_otros_medios', 'diferencia_otros_medios')]}),
# ==> Efectivo <==
        ('Cantidad Operaciones', {'classes': ('suit-tab', 'suit-tab-efectivo',),
                                  'fields': ['cantidad_operaciones_efectivo_procesadas', 'cantidad_operaciones_efectivo_pendientes', 'cantidad_operaciones_efectivo_canceladas']}),
        ('Registro', {'classes': ('suit-tab', 'suit-tab-efectivo',),
                      'fields': ['monto_apertura', 'monto_registro_efectivo', 'total_efectivo']}),
        ('Rendicion', {'classes': ('suit-tab', 'suit-tab-efectivo',),
                       'fields': ['rendicion_efectivo']}),
        ('Diferencia', {'classes': ('suit-tab', 'suit-tab-efectivo',),
                        'fields': ['diferencia_efectivo']}),
# ==> TCs <==
        ('Cantidad Operaciones', {'classes': ('suit-tab', 'suit-tab-tcs',),
                                  'fields': ['cantidad_operaciones_tcs_procesadas', 'cantidad_operaciones_tcs_pendientes', 'cantidad_operaciones_tcs_canceladas']}),
        ('Registro', {'classes': ('suit-tab', 'suit-tab-tcs',),
                      'fields': ['monto_registro_tcs']}),
        ('Rendicion', {'classes': ('suit-tab', 'suit-tab-tcs',),
                       'fields': ['rendicion_tcs']}),
        ('Diferencia', {'classes': ('suit-tab', 'suit-tab-tcs',),
                        'fields': ['diferencia_tcs']}),
# ==> TDs <==
        ('Cantidad Operaciones', {'classes': ('suit-tab', 'suit-tab-tds',),
                                  'fields': ['cantidad_operaciones_tds_procesadas', 'cantidad_operaciones_tds_pendientes', 'cantidad_operaciones_tds_canceladas']}),
        ('Registro', {'classes': ('suit-tab', 'suit-tab-tds',),
                      'fields': ['monto_registro_tds']}),
        ('Rendicion', {'classes': ('suit-tab', 'suit-tab-tds',),
                       'fields': ['rendicion_tds']}),
        ('Diferencia', {'classes': ('suit-tab', 'suit-tab-tds',),
                        'fields': ['diferencia_tds']}),
# ==> Otros Medios de Pago <==
        ('Cantidad Operaciones', {'classes': ('suit-tab', 'suit-tab-otros_medios',),
                                  'fields': ['cantidad_operaciones_otros_medios_procesadas', 'cantidad_operaciones_otros_medios_pendientes', 'cantidad_operaciones_otros_medios_canceladas']}),
        ('Registro', {'classes': ('suit-tab', 'suit-tab-otros_medios',),
                      'fields': ['monto_registro_otros_medios']}),
        ('Rendicion', {'classes': ('suit-tab', 'suit-tab-otros_medios',),
                       'fields': ['rendicion_otros_medios']}),
        ('Diferencia', {'classes': ('suit-tab', 'suit-tab-otros_medios',),
                        'fields': ['diferencia_otros_medios']}),
    ]

    suit_form_tabs = (('cierre', 'Datos Cierre de Caja'), ('efectivo', 'Efectivo'), ('tcs', 'TCs'), ('tds', 'TDs'), ('otros_medios', 'Otros Medios'))

    list_display = ['apertura_caja', 'get_cajero', 'get_numero_caja', 'get_sector', 'get_horario', 'get_jornada', 'get_fecha_hora_apertura_caja',
                    'get_monto_apertura', 'colorea_estado_apertura_caja', 'total_efectivo', 'total_diferencia',
                    'usuario_cierre_caja', 'fecha_hora_registro_cierre_caja']
    list_display_links = ['apertura_caja']
    list_filter = ['apertura_caja', 'apertura_caja__cajero', 'apertura_caja__caja', 'apertura_caja__sector', 'apertura_caja__horario', 'apertura_caja__jornada',
                   'apertura_caja__fecha_hora_apertura_caja', 'apertura_caja__estado_apertura_caja', 'usuario_cierre_caja', 'fecha_hora_registro_cierre_caja']
    search_fields = ['apertura_caja__id', 'apertura_caja__cajero__usuario__username', 'apertura_caja__caja__numero_caja', 'apertura_caja__sector__sector',
                     'apertura_caja__horario__horario', 'apertura_caja__fecha_hora_apertura_caja', 'apertura_caja__estado_apertura_caja',
                     'usuario_cierre_caja__usuario__username', 'fecha_hora_registro_cierre_caja']

    def colorea_estado_apertura_caja(self, obj):
        # color = 'black'
        if obj.apertura_caja.estado_apertura_caja == 'VIG':
            color = 'orange'
            return format_html('<span style="color: %s"><b> %s </b></span>' %
                               (color, obj.apertura_caja.get_estado_apertura_caja_display()))
        elif obj.apertura_caja.estado_apertura_caja == 'CER':
            color = 'green'
            return format_html('<span style="color: %s"><b> %s </b></span>' %
                               (color, obj.apertura_caja.get_estado_apertura_caja_display()))
        elif obj.apertura_caja.estado_apertura_caja == 'EXP':
            color = 'red'
            return format_html('<span style="color: %s"><b> %s </b></span>' %
                               (color, obj.apertura_caja.get_estado_apertura_caja_display()))
        return obj.apertura_caja.estado_apertura_caja
    colorea_estado_apertura_caja.short_description = 'Estado Apert. Caja'

    def save_model(self, request, obj, form, change):

        # import pdb
        # pdb.set_trace()

        # if not change:
        #     obj.estado_pedido = PedidoEstado.objects.get(pedido_estado='VIG')
        #     obj.save()

        cierre_caja_actual = obj

        # if "_continue" in request.POST:
        if not change and "_continue" in request.POST:
            apertura = cierre_caja_actual.apertura_caja
            apertura.en_proceso_cierre = True
            apertura.save()

        elif "_save" in request.POST:
            jornada = cierre_caja_actual.apertura_caja.jornada
            jornada.cantidad_pedidos_procesados = jornada.get_cantidad_pedidos_procesados()
            jornada.cantidad_pedidos_pendientes = jornada.get_cantidad_pedidos_pendientes()
            jornada.cantidad_pedidos_cancelados = jornada.get_cantidad_pedidos_cancelados()
            jornada.fecha_hora_cierre_jornada = timezone.now()
            jornada.usuario_cierre_jornada = Empleado.objects.get(usuario=request.user)
            jornada.estado_jornada = 'CER'
            jornada.save()

            apertura = cierre_caja_actual.apertura_caja
            apertura.estado_apertura_caja = 'CER'
            apertura.en_proceso_cierre = True
            apertura.save()

            caja = cierre_caja_actual.apertura_caja.caja
            caja.estado_caja = 'CER'
            caja.save()

            cierre_caja_actual.usuario_cierre_caja = Empleado.objects.get(usuario_id=request.user)

        super(CierreCajaAdmin, self).save_model(request, obj, form, change)

    def get_readonly_fields(self, request, obj=None):
        if obj is not None and obj.pk and obj.apertura_caja.estado_apertura_caja in ('VIG', 'EXP'):  # and obj.reserva is not None
            return self.readonly_fields + ['apertura_caja']
        elif obj is not None and obj.pk and obj.apertura_caja.estado_apertura_caja == 'CER':
            return [i.name for i in self.model._meta.fields] + \
                   [i.name for i in self.model._meta.many_to_many]
        else:
            return super(CierreCajaAdmin, self).get_readonly_fields(request, obj)

    def changeform_view(self, request, object_id=None, form_url='', extra_context=None):
        extra_context = extra_context or {}

        extra_context['show_button'] = True
        if object_id is not None:
            cierre_caja_actual = CierreCaja.objects.get(pk=object_id)
            if cierre_caja_actual.apertura_caja.estado_apertura_caja in ('VIG', 'EXP'):
                extra_context['show_save_button'] = True
                extra_context['show_continue_button'] = True
                # extra_context['show_cancel_button'] = False
                extra_context['show_imprimir_button'] = False
            elif cierre_caja_actual.apertura_caja.estado_apertura_caja == 'CER':
                extra_context['show_save_button'] = False
                extra_context['show_continue_button'] = False
                # extra_context['show_cancel_button'] = True
                extra_context['show_imprimir_button'] = True

        elif object_id is None:
            extra_context['show_save_button'] = True
            extra_context['show_continue_button'] = True
            # extra_context['show_cancel_button'] = False
            extra_context['show_imprimir_button'] = False

        return super(CierreCajaAdmin, self).changeform_view(request, object_id, form_url, extra_context)

    def get_form(self, request, obj=None, **kwargs):

        # import pdb
        # pdb.set_trace()

        form = super(CierreCajaAdmin, self).get_form(request, obj=obj, **kwargs)
        if obj is None:

            usuario = Empleado.objects.get(usuario=request.user)
            if usuario.usuario.is_superuser is True:
                cierres = CierreCaja.objects.all().values('apertura_caja')
                aperturas = AperturaCaja.objects.filter(estado_apertura_caja__in=['VIG', 'EXP']).exclude(id__in=cierres)
            else:
                cierres = CierreCaja.objects.all().values('apertura_caja')
                aperturas = AperturaCaja.objects.filter(cajero=usuario, estado_apertura_caja__in=['VIG', 'EXP']).exclude(id__in=cierres)

            form.base_fields['apertura_caja'].queryset = aperturas
            # form.base_fields['horario'].widget.attrs['disabled'] = True
        form.request = request
        return form

    # def formfield_for_foreignkey(self, db_field, request=None, **kwargs):
    #
    #     import pdb
    #     pdb.set_trace()
    #
    #     if db_field.name == "apertura_caja":
    #         usuario = Empleado.objects.get(usuario=request.user)
    #         if usuario.usuario.is_superuser is True:
    #             cierres = CierreCaja.objects.all().values('apertura_caja')
    #             aperturas = AperturaCaja.objects.filter(estado_apertura_caja__in=['VIG', 'EXP']).exclude(id__in=cierres)
    #         else:
    #             cierres = CierreCaja.objects.all().values('apertura_caja')
    #             aperturas = AperturaCaja.objects.filter(cajero=usuario, estado_apertura_caja__in=['VIG', 'EXP']).exclude(id__in=cierres)
    #         kwargs['queryset'] = aperturas
    #     return super(CierreCajaAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def has_delete_permission(self, request, obj=None):
        return False

    def get_queryset(self, request):
        usuario = Empleado.objects.get(usuario_id=request.user)
        queryset = None
        if usuario.cargo.cargo == 'CA':
            queryset = CierreCaja.objects.filter(apertura_caja__cajero=usuario)
        elif usuario.usuario.is_superuser is True:
            queryset = CierreCaja.objects.all()
        return queryset


class InicioJornadaAdmin(admin.ModelAdmin):
    form = InicioJornadaForm

    class Media:
        js = [
            'ventas/js/inicio_jornada.js'
        ]

    readonly_fields = ['id', 'fecha_hora_inicio_jornada', 'estado_jornada']  # 'duracion_jornada', 'fecha_hora_fin_jornada',

    fieldsets = [
        ('ID Jornada', {'fields': ['id']}),
        ('Mozo/Barman', {'fields': ['mozo', 'nombre_mozo', 'sector', 'horario']}),
        ('Datos Jornada', {'fields': ['fecha_hora_inicio_jornada', 'duracion_jornada', 'fecha_hora_fin_jornada',
                                      'estado_jornada']}),
    ]

    list_display = ['id', 'mozo', 'sector', 'horario', 'fecha_hora_inicio_jornada', 'duracion_jornada', 'fecha_hora_fin_jornada',
                    'colorea_estado_jornada']
    list_display_links = ['id']
    list_filter = ['mozo', 'sector', 'horario', 'fecha_hora_inicio_jornada', 'fecha_hora_fin_jornada', 'estado_jornada']
    search_fields = ['mozo__usuario__username', 'sector__sector', 'horario__horario', 'fecha_hora_inicio_jornada', 'fecha_hora_fin_jornada',
                     'estado_jornada']

    def colorea_estado_jornada(self, obj):
        # color = 'black'
        if obj.estado_jornada == 'VIG':
            color = 'orange'
            return format_html('<span style="color: %s"><b> %s </b></span>' %
                               (color, obj.get_estado_jornada_display()))
        elif obj.estado_jornada == 'CER':
            color = 'green'
            return format_html('<span style="color: %s"><b> %s </b></span>' %
                               (color, obj.get_estado_jornada_display()))
        elif obj.estado_jornada == 'EXP':
            color = 'red'
            return format_html('<span style="color: %s"><b> %s </b></span>' %
                               (color, obj.get_estado_jornada_display()))
        return obj.estado_jornada
    colorea_estado_jornada.short_description = 'Estado Jornada'

    def save_model(self, request, obj, form, change):

        # import pdb
        # pdb.set_trace()

        jornada_actual = obj

        if not change:
            # jornada_actual.mozo = Empleado.objects.get(usuario=self.request.user)
            # duracion = datetime.datetime.strptime(datetime.datetime.strftime(timezone.localtime(jornada_actual.duracion_jornada), '%d/%m/%Y %H:%M:%S'), '%d/%m/%Y %H:%M:%S')
            jornada_actual.fecha_hora_fin_jornada = timezone.localtime(timezone.now() + datetime.timedelta(hours=jornada_actual.duracion_jornada.hour, minutes=jornada_actual.duracion_jornada.minute, seconds=jornada_actual.duracion_jornada.second))
            jornada_actual.estado_jornada = 'VIG'

        super(InicioJornadaAdmin, self).save_model(request, obj, form, change)

    def get_readonly_fields(self, request, obj=None):
        if obj is not None and obj.estado_jornada in ('VIG', 'EXP', 'CER'):
            return [i.name for i in self.model._meta.fields] + \
                   [i.name for i in self.model._meta.many_to_many]
        else:
            return super(InicioJornadaAdmin, self).get_readonly_fields(request, obj)

    def changeform_view(self, request, object_id=None, form_url='', extra_context=None):
        extra_context = extra_context or {}

        extra_context['show_button'] = True
        if object_id is not None:
            inicio_jornada_actual = InicioJornada.objects.get(pk=object_id)
            extra_context['show_button'] = inicio_jornada_actual.estado_jornada not in ('VIG', 'EXP', 'CER')
        return super(InicioJornadaAdmin, self).changeform_view(request, object_id, form_url, extra_context)

    def changelist_view(self, request, extra_context=None):
        queryset = self.get_queryset(request).filter(estado_jornada='VIG')

        for jornada in queryset:
            now = timezone.localtime(timezone.now())
            print timezone.localtime(jornada.fecha_hora_fin_jornada), now

            if timezone.localtime(jornada.fecha_hora_fin_jornada) < now:
                jornada.estado_jornada = 'EXP'
                jornada.save()

        return super(InicioJornadaAdmin, self).changelist_view(request, extra_context=extra_context)

    def get_form(self, request, obj=None, **kwargs):

        # import pdb
        # pdb.set_trace()

        form = super(InicioJornadaAdmin, self).get_form(request, obj=obj, **kwargs)

        if obj is None:
            usuario = Empleado.objects.get(usuario=request.user)

            if usuario.usuario.is_superuser is True:
                sector_usuario = Sector.objects.get(sector='BPR')
            else:
                sector_usuario = Sector.objects.get(sector=usuario.sector.sector)

            form.base_fields['mozo'].initial = usuario
            form.base_fields['mozo'].queryset = Empleado.objects.filter(usuario=request.user)
            form.base_fields['nombre_mozo'].initial = usuario.nombre_completo

            form.base_fields['sector'].initial = sector_usuario
            form.base_fields['sector'].queryset = Sector.objects.filter(sector=sector_usuario.sector)
            form.base_fields['sector'].widget.attrs['style'] = 'font-size: 14px; height: 30px; font-weight: bold; color: green;'
            form.base_fields['sector'].label = mark_safe('<strong style="font-size: 14px;">Sector</strong>')

            form.base_fields['horario'].initial = usuario.horario
            form.base_fields['horario'].queryset = Horario.objects.filter(horario=usuario.horario)
            form.base_fields['duracion_jornada'].initial = usuario.horario.duracion_jornada
            form.base_fields['fecha_hora_fin_jornada'].initial = timezone.localtime(timezone.now() + datetime.timedelta(hours=usuario.horario.duracion_jornada.hour, minutes=usuario.horario.duracion_jornada.minute, seconds=usuario.horario.duracion_jornada.second))
            form.base_fields['mozo'].widget.attrs['readonly'] = True
            form.base_fields['sector'].widget.attrs['readonly'] = True
            form.base_fields['horario'].widget.attrs['readonly'] = True
            form.base_fields['fecha_hora_fin_jornada'].widget.attrs['readonly'] = True
            # form.base_fields['duracion_jornada'].widget.attrs['disabled'] = True
            # form.base_fields['fecha_hora_fin_jornada'].widget.attrs['disabled'] = True
        form.request = request
        return form

    def has_delete_permission(self, request, obj=None):
        return False

    def get_queryset(self, request):
        usuario = Empleado.objects.get(usuario_id=request.user)
        queryset = None
        if usuario.cargo.cargo in ('MO', 'BM'):
            queryset = Jornada.objects.filter(mozo=usuario)
        elif usuario.usuario.is_superuser is True:
            queryset = Jornada.objects.all()
        return queryset


class FinJornadaAdmin(admin.ModelAdmin):
    form = FinJornadaForm

    readonly_fields = ['id', 'mozo', 'sector', 'horario', 'fecha_hora_inicio_jornada', 'duracion_jornada', 'fecha_hora_fin_jornada',
                       'cantidad_pedidos_procesados', 'cantidad_pedidos_pendientes', 'cantidad_pedidos_cancelados',
                       'fecha_hora_cierre_jornada', 'usuario_cierre_jornada']  # 'estado_jornada',

    fieldsets = [
        ('ID Jornada', {'fields': ['id']}),
        ('Mozo/Barman', {'fields': ['mozo', 'nombre_mozo', 'sector', 'horario']}),
        ('Datos Jornada', {'fields': ['fecha_hora_inicio_jornada', 'duracion_jornada', 'fecha_hora_fin_jornada',
                                      'estado_jornada']}),
        ('Datos Cierre Jornada', {'fields': ['cantidad_pedidos_procesados', 'cantidad_pedidos_pendientes',
                                             'cantidad_pedidos_cancelados', 'fecha_hora_cierre_jornada',
                                             'usuario_cierre_jornada']}),
    ]

    list_display = ['id', 'mozo', 'sector', 'horario', 'fecha_hora_inicio_jornada', 'duracion_jornada', 'fecha_hora_fin_jornada',
                    'colorea_estado_jornada', 'cantidad_pedidos_procesados', 'cantidad_pedidos_pendientes',
                    'cantidad_pedidos_cancelados', 'fecha_hora_cierre_jornada', 'usuario_cierre_jornada']
    list_display_links = ['id']
    list_filter = ['mozo', 'sector', 'horario', 'fecha_hora_inicio_jornada', 'fecha_hora_fin_jornada', 'estado_jornada',
                   'fecha_hora_cierre_jornada']
    search_fields = ['mozo__usuario__username', 'sector__sector', 'horario__horario', 'fecha_hora_inicio_jornada',
                     'fecha_hora_fin_jornada', 'estado_jornada', 'fecha_hora_cierre_jornada']

    def colorea_estado_jornada(self, obj):
        # color = 'black'
        if obj.estado_jornada == 'VIG':
            color = 'orange'
            return format_html('<span style="color: %s"><b> %s </b></span>' %
                               (color, obj.get_estado_jornada_display()))
        elif obj.estado_jornada == 'CER':
            color = 'green'
            return format_html('<span style="color: %s"><b> %s </b></span>' %
                               (color, obj.get_estado_jornada_display()))
        elif obj.estado_jornada == 'EXP':
            color = 'red'
            return format_html('<span style="color: %s"><b> %s </b></span>' %
                               (color, obj.get_estado_jornada_display()))
        return obj.estado_jornada
    colorea_estado_jornada.short_description = 'Estado Jornada'

    def save_model(self, request, obj, form, change):

        # import pdb
        # pdb.set_trace()

        jornada_actual = obj

        # if not change:
        # jornada_actual.mozo = Empleado.objects.get(usuario=self.request.user)
        jornada_actual.estado_jornada = 'CER'
        jornada_actual.fecha_hora_cierre_jornada = timezone.now()
        jornada_actual.usuario_cierre_jornada = Empleado.objects.get(usuario_id=request.user)

        super(FinJornadaAdmin, self).save_model(request, obj, form, change)

    def changeform_view(self, request, object_id=None, form_url='', extra_context=None):
        extra_context = extra_context or {}

        extra_context['show_button'] = True
        if object_id is not None:
            inicio_jornada_actual = InicioJornada.objects.get(pk=object_id)
            extra_context['show_button'] = inicio_jornada_actual.estado_jornada not in ('CER')
        return super(FinJornadaAdmin, self).changeform_view(request, object_id, form_url, extra_context)

    def changelist_view(self, request, extra_context=None):
        # queryset = self.get_queryset(request).filter(estado_jornada__in=['VIG', 'EXP'])
        queryset = self.get_queryset(request).all()

        for jornada in queryset:
            now = timezone.localtime(timezone.now())
            print timezone.localtime(jornada.fecha_hora_fin_jornada), now

            jornada.cantidad_pedidos_procesados = jornada.get_cantidad_pedidos_procesados()
            jornada.cantidad_pedidos_pendientes = jornada.get_cantidad_pedidos_pendientes()
            jornada.cantidad_pedidos_cancelados = jornada.get_cantidad_pedidos_cancelados()
            jornada.save()

            if jornada.estado_jornada == 'VIG' and timezone.localtime(jornada.fecha_hora_fin_jornada) < now:
                jornada.estado_jornada = 'EXP'
                jornada.save()

        return super(FinJornadaAdmin, self).changelist_view(request, extra_context=extra_context)

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    def get_queryset(self, request):
        usuario = Empleado.objects.get(usuario_id=request.user)
        queryset = None
        if usuario.cargo.cargo in ('MO', 'BM'):
            queryset = Jornada.objects.filter(mozo=usuario)
        elif usuario.usuario.is_superuser is True:
            queryset = Jornada.objects.all()
        return queryset

admin.site.register(Pedido, PedidoAdmin)
admin.site.register(Venta, VentaAdmin)
admin.site.register(VentaOcasional, VentaOcasionalAdmin)
admin.site.register(Comanda, ComandaAdmin)
admin.site.register(AperturaCaja, AperturaCajaAdmin)
admin.site.register(CierreCaja, CierreCajaAdmin)
admin.site.register(InicioJornada, InicioJornadaAdmin)
admin.site.register(FinJornada, FinJornadaAdmin)