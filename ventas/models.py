# -*- coding: utf-8 -*-
from decimal import Decimal
from django.core.validators import MinValueValidator
from django.db import models
from django.db.models.aggregates import Sum
from django.utils import timezone
import datetime
from django.db.models import Q
from django.core.exceptions import ValidationError, ObjectDoesNotExist
from django.utils.translation import ugettext_lazy as _
from django.views.generic.dates import timezone_today
from bar.models import FacturaVenta, NumeroFacturaVenta, Mesa
from personal.models import Empleado

# Create your models here.


# def get_reservas_today():
#     pass


class Pedido(models.Model):
    """
    Registrar los datos de la cabecera del Pedido.

    * Registrar que mozo/barman realizo el pedido.
    * Anular pedido.
    * Transferir pedidos entre mesas. (menos prioritario)
    """
    numero_pedido = models.AutoField(primary_key=True,
                                     verbose_name='Nro. Pedido',
                                     help_text='Este dato se genera automaticamente cada vez que se va crear un '
                                               'Pedido.')
    jornada = models.ForeignKey('InicioJornada',  # default=1,
                                verbose_name='Jornada',
                                help_text='Se asigna dependiendo del usuario logueado y de si posee una Jornada '
                                          'vigente.')

    # Desplegar las Reservas que tienen estado "Vigente" unicamente. OK!
    # La Reserva es opcional por lo tanto se asigna blank=True y null=True
    reserva = models.ForeignKey('clientes.Reserva', blank=True, null=True,
                                limit_choices_to={'fecha_hora_reserva__gte': timezone.make_aware(datetime.datetime.combine(timezone.now().date(), datetime.time(hour=18, minute=0)), timezone.get_default_timezone()), 'fecha_hora_reserva__lte': timezone.make_aware(datetime.datetime.combine(timezone.now().date(), datetime.time(hour=21, minute=0)), timezone.get_default_timezone()), 'estado__reserva_estado': "VIG"},
                                # limit_choices_to={'fecha_hora_reserva__year': timezone_today().year, 'fecha_hora_reserva__month': timezone_today().month, 'fecha_hora_reserva__day': timezone_today().day, 'estado__reserva_estado': "VIG"},
                                # limit_choices_to={'fecha_hora_reserva__gte': timezone.now, 'estado__reserva_estado': "VIG"},
                                # limit_choices_to={'fecha_hora_reserva__range': [(datetime.datetime.combine(timezone_today(), datetime.time.min).replace(tzinfo=timezone.utc), datetime.datetime.combine(timezone_today(), datetime.time.max).replace(tzinfo=timezone.utc))], 'estado__reserva_estado': "VIG"},
                                # limit_choices_to={'fecha_hora_reserva__startswith': timezone_today(), 'estado__reserva_estado': "VIG"},
                                # limit_choices_to={'estado__reserva_estado': "VIG"},
                                # limit_choices_to=(Q(fecha_hora_reserva__startswith=timezone_today())),  # Q(estado__reserva_estado="VIG") &
                                # verbose_name='Reserva',
                                help_text='Seleccione una Reserva en caso de que el Cliente haya realizado una.')

    # 1) Al seleccionar la Reserva se debe controlar que la misma corresponda a la fecha y hora indicada y se deben
    # cargar los datos de las Mesas Reservadas y el Monto de la Entrega.
    # monto_entrega_reserva = models.DecimalField(max_digits=18, decimal_places=0, default=0, blank=True, null=True,
    #                                             verbose_name='Monto Entrega',
    #                                             help_text='Ingrese el monto a pagar por la Reserva. Este monto luego '
    #                                                       'se acredita en consumision.')

    # Si el Cliente tiene una Reserva los datos de las Mesas se debe tomar de 'clientes.Reserva'
    mesa_pedido = models.ManyToManyField('bar.Mesa',  # through='PedidoMesaPedido',
                                         # limit_choices_to={'estado__mesa_estado': "DI"},  # Si se filtran las Mesas con estado "DI" no son visualizadas en el filter_horizontal en el form
                                         # limit_choices_to=(~Q(numero_mesa=9999)),  # Si se filtran las Mesas con estado "DI" no son visualizadas en el filter_horizontal en el form
                                         # limit_choices_to={'numero_mesa__exclude': '9999'},  # Si se filtran las Mesas con estado "DI" no son visualizadas en el filter_horizontal en el form
                                         verbose_name='Mesas',
                                         help_text='Indique la/s mesa/s que sera/n ocupada/s por el/los Cliente/s.')

    # Debe ser el usuario con el cual se esta registrando el Pedido, no se debe poder seleccionar el usuario.
    mozo_pedido = models.ForeignKey('personal.Empleado',
                                    related_name='mozo_pedido',
                                    # limit_choices_to=Q(cargo__cargo__exact="MO") | Q(cargo__cargo__exact="BM"),
                                    # to_field='usuario',
                                    verbose_name='Atendido por?',
                                    help_text='Este dato se completara automaticamente cuando el Pedido sea guardado.')
    estado_pedido = models.ForeignKey('bar.PedidoEstado',  # default=1,  # default={'pedido_estado': "VIG"},
                                      verbose_name='Estado del Pedido',
                                      help_text='El estado del Pedido se establece automaticamente.')
    fecha_hora_pedido = models.DateTimeField(auto_now_add=True, verbose_name='Fecha/Hora del Pedido',
                                             help_text='La fecha y hora del Pedido se asignaran automaticamente una '
                                                       'vez que sea guardado.')  # default=timezone.now()
    total_pedido = models.DecimalField(max_digits=18, decimal_places=0, default=0,
                                       verbose_name='Total del Pedido')

    usuario_modifica_pedido = models.ForeignKey('personal.Empleado', null=True, blank=True,  # default=17,
                                                related_name='usuario_modifica_pedido',
                                                # limit_choices_to='',
                                                # to_field='usuario',
                                                verbose_name='Modificado por?',
                                                help_text='Usuario que modifico el Pedido.')
    motivo_cancelacion = models.CharField(max_length=200, null=True, blank=True)
    observaciones_cancelacion = models.CharField(max_length=200, null=True, blank=True)
    usuario_cancelacion = models.ForeignKey('personal.Empleado', null=True, blank=True,
                                            related_name='usuario_cancelacion_pedido',
                                            # limit_choices_to='',
                                            #  to_field='usuario',
                                            verbose_name='Cancelado por?',
                                            help_text='Usuario que cancelo el Pedido.')
    fecha_hora_cancelacion = models.DateTimeField(null=True, blank=True)

    class Meta:
        verbose_name = 'Pedido'
        verbose_name_plural = 'Pedidos'

    # VALIDACIONES/FUNCIONALIDADES
    # ============================
    # 1) Al seleccionar la Reserva se deben cargar los datos del Monto de la Entrega y de las Mesas Reservadas.
    # 2.1) Al guardar el Pedido se debe cambiar el estado de la Reserva a UTILIZADA en caso de que se haya utilizado una
    # 2.2) Al guardar el Pedido se debe descontar los productos solicitados del Stock.
    # 2.3) Al guardar el Pedido se debe modificar el estado de las Mesas seleccionadas a Ocupadas.
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

    # def limit_mozo_pedido_choices(self):
    #     return Empleado.objects.get(Q(cargo__cargo__exact="MO") | Q(cargo__cargo__exact="BM"))
    # limit_choices_to = limit_mozo_pedido_choices

    def get_sector(self):
        """Retorna el Sector para la Jornada correspondiente."""
        return '%s' % self.jornada.sector
    # nombre_completo = property(get_nombre_completo)
    get_sector.short_description = 'Sector'

    def clean(self):
        # Valida que el Total del Pedido no sea 0
        if self.total_pedido == 0:
            raise ValidationError({'total_pedido': _('El Total del Pedido no puede ser 0.')})

    def __unicode__(self):
        # if self is not None:
        #     return "Nro. Ped: %s - Fec. Ped: %s" % (self.numero_pedido, datetime.datetime.strftime(timezone.localtime(self.fecha_hora_pedido), '%d/%m/%Y %H:%M'))
        # else:
        return u"%s" % self.numero_pedido


class PedidoDetalle(models.Model):
    """
    Registrar los datos del detalle del Pedido.

    * Imprimir comanda.
    """
    pedido = models.ForeignKey('Pedido')

    # Se deben desplegar solo los Productos con Tipo de Producto "VE - Para la Venta" y los Productos Compuestos o
    # Elaborados.
    producto_pedido = models.ForeignKey('stock.ProductoVenta',  # limit_choices_to={'tipo_producto': "VE"},
                                        verbose_name='Producto a ordenar',
                                        help_text='Seleccione el Producto ordenado por el Cliente.')

    # El PrecioVenta se debe desplegar de acuerdo al Producto seleccionado
    # precio_producto_pedido = models.ForeignKey('stock.PrecioVentaProducto', default=1,
    #                                            verbose_name='Precio Venta del Producto',
    #                                            help_text='El Precio de Venta se define de acuerdo al Producto '
    #                                                      'seleccionado.')
    precio_producto_pedido = models.DecimalField(max_digits=18, decimal_places=0,
                                                 verbose_name='Precio Venta Producto',
                                                 help_text='El Precio de Venta del Producto se define en la pantalla '
                                                           'de Productos.')

    cantidad_producto_pedido = models.DecimalField(max_digits=10, decimal_places=3, default=1,
                                                   verbose_name='Cantidad del Producto',
                                                   help_text='Ingrese la cantidad del producto solicitado por el '
                                                             'Cliente.')
    total_producto_pedido = models.DecimalField(max_digits=18, decimal_places=0, default=0,
                                                verbose_name='Total del Producto',
                                                help_text='Este valor se calcula automaticamente tomando el '
                                                          'Precio Venta del Producto por la Cantidad del Producto.')
    fecha_pedido_detalle = models.DateTimeField(auto_now_add=True,  # default=timezone.now()
                                                verbose_name='Fecha/hora del Pedido',
                                                help_text='Registra la fecha y hora en que se realizo el detalle del '
                                                          'Pedido, util cuando el cliente pide mas productos.')
    procesado = models.BooleanField(default=False, verbose_name='Procesado?',
                                    help_text='Esta casilla se marca cuando el Pedido es procesado por el Deposito '
                                              'correspondiente.')
    cancelado = models.BooleanField(default=False, verbose_name='Cancelar?',
                                    help_text='Seleccione esta casilla si desea cancelar el Producto solicitado.')
    # id_mov_stock = models.PositiveIntegerField(null=True, blank=True, help_text='Registra el dato del ID '
    #                                                                             'MovimientoStock para poder recuperar '
    #                                                                             'los datos necesarios para realizar '
    #                                                                             'la reversion de los descuentos de '
    #                                                                             'Stock cuando se cancela un Producto o '
    #                                                                             'todo el Pedido en la pantalla de '
    #                                                                             'Pedidos.')

    class Meta:
        verbose_name = 'Pedido - Detalle'
        verbose_name_plural = 'Pedidos - Detalles'

    # VALIDACIONES/FUNCIONALIDADES
    # ============================
    # 1) En caso de registrarse un Pedido para la Cocina se debe imprimir una Comanda con el detalle del Pedido.
    # 2) Calcular automaticamente el campo "total_producto_pedido" como la multiplicacion
    # de "precio_producto_pedido * cantidad_producto_pedido"

    # def __unicode__(self):
    #     return "%s" % (self.id, self.pedido)


class Venta(models.Model):
    """
    Registrar los datos de la cabecera de la Venta.
    * Registrar ventas con sus respectivas formas de pago.
    * Registrar movimientos de caja.
    * Cerrar venta.
    * Anular venta.
    * Restar los productos vendidos del stock.
    * Emitir comprobantes. Factura o ticket.
    * Ventas cerradas no deben ser modificadas.

    * Listar las ventas mensuales, ventas al contado. Ranking de ventas por cliente, por productos, por marcas.
    """
    FORMAS_PAGO_VENTA = (
        ('EF', 'Efectivo'),
        ('TC', 'Tarjeta de Credito'),
        ('TD', 'Tarjeta de Debito'),
        ('OM', 'Otros medios'),
    )

    empresa = models.ForeignKey('compras.Empresa', default=9)

    timbrado = models.ForeignKey('bar.Timbrado',  # default=2,
                                 limit_choices_to={'estado_timbrado': "AC"})
    # Debe tomar el dato  de la tabla donde se lleva la numeracion de las facturas por Punto de Expedicion
    # numero_factura = models.DecimalField(max_digits=7, decimal_places=0, default=1)
    numero_factura_venta = models.OneToOneField('bar.NumeroFacturaVenta',  # default=1,
                                                related_name='numero_factura_venta',
                                                # to_field='numero_factura_actual', unique=True,
                                                verbose_name='Numero de Factura',
                                                help_text='El Numero de Factura se asigna al momento de confirmarse la '
                                                          'Venta.')
    fecha_hora_venta = models.DateTimeField(auto_now=True,  # default=timezone.now()
                                            verbose_name='Fecha/hora de la Venta',
                                            help_text='Registra la fecha y hora en la que se confirmo la Venta.')

    # Seria ideal que tome el dato de la Caja de acuerdo al usuario logueado y a la Caja aperturada.
    apertura_caja = models.ForeignKey('AperturaCaja',  # default=1,
                                      # limit_choices_to={'cajero':request.user, 'estado_apertura_caja':"VIG"},
                                      verbose_name='Apertura de Caja',
                                      help_text='Este valor se asigna dependiendo del usuario logueado y de si posee '
                                                'una Apertura de Caja vigente.')

    # Si el Cliente tiene una Reserva seria conveniente tomar sus datos de la Reserva.
    # reserva = models.ForeignKey('clientes.Reserva')
    # posee_reserva = models.BooleanField(default=False, verbose_name='Posee reserva?')
    # entrega_reserva = models.DecimalField(max_digits=18, decimal_places=0, default=0,
    #                                       verbose_name='Entrega Reserva',
    #                                       help_text='Monto entregado por la Reserva. Este monto se acredita en '
    #                                                 'consumision y se descuenta del Total de la Venta.')
    cliente_factura = models.ForeignKey('clientes.Cliente', null=True, blank=True,  # default=1,
                                        verbose_name='Cliente',
                                        help_text='Corrobore con el Cliente si son correctos sus datos '
                                                  'antes de confirmar la Venta.')

    # cliente_documento_factura = models.ForeignKey('clientes.ClienteDocumento', null=True, blank=True,
    cliente_documento_factura = models.CharField(max_length=50, null=True, blank=True,  # default='',
                                                 verbose_name='Documento Factura',
                                                 help_text='Seleccione el Documento del Cliente el cual se registrara '
                                                           'en la factura.')

    # numero_pedido = models.OneToOneField('Pedido', blank=True,  # null=True,
    numero_pedido = models.ForeignKey('Pedido',  # blank=True,  # null=True,  default=1,
                                      limit_choices_to={'estado_pedido__pedido_estado__in': ('VIG', 'PEN')},
                                      verbose_name='Numero de Pedido',
                                      help_text='Seleccione el Numero de Pedido para el cual se registrara la Venta.')

    # forma_pago = models.ForeignKey('bar.FormaPagoVenta',  # default=1,
    #                                verbose_name='Forma de Pago',
    #                                help_text='Seleccione la Forma de Pago.')
    forma_pago = models.CharField(max_length=2, choices=FORMAS_PAGO_VENTA,
                                  verbose_name='Forma de Pago',
                                  null=True, blank=True,
                                  help_text='Seleccione la Forma de Pago.')
    total_venta = models.DecimalField(max_digits=18, decimal_places=0, default=0,
                                      verbose_name='Total Venta')
    efectivo_recibido = models.DecimalField(max_digits=18, decimal_places=0, default=0, null=True, blank=True,
                                            verbose_name='Efectivo Recibido')
    vuelto = models.DecimalField(max_digits=18, decimal_places=0, default=0, null=True, blank=True,
                                 verbose_name='Vuelto')
    voucher = models.CharField(max_length=15, null=True, blank=True,
                               verbose_name='Numero de Voucher')

    estado_venta = models.ForeignKey('bar.VentaEstado',  # default=1,
                                     verbose_name='Estado Venta',
                                     help_text='El estado de la Venta se establece automaticamente una vez que es '
                                               'confirmada la misma.')
    venta_ocasional = models.BooleanField(default=False)

    motivo_cancelacion = models.CharField(max_length=200, null=True, blank=True)
    observaciones_cancelacion = models.CharField(max_length=200, null=True, blank=True)
    usuario_cancelacion = models.ForeignKey('personal.Empleado', null=True, blank=True,
                                            related_name='usuario_cancelacion_venta',
                                            # limit_choices_to='',
                                            #  to_field='usuario',
                                            verbose_name='Cancelado por?',
                                            help_text='Usuario que cancelo la Venta.')
    fecha_hora_cancelacion = models.DateTimeField(null=True, blank=True)

    class Meta:
        verbose_name = 'Venta con Pedido'
        verbose_name_plural = 'Ventas con Pedido'

    # VALIDACIONES/FUNCIONALIDADES
    # ============================
    # 1) Registrar Ventas con sus respectivas Formas de Pago.
    # 2) Registrar Movimientos de Caja (serian las Ventas propiamente)
    # 3) Cerrar venta.
    # 4) Anular venta.
    # 5) Restar los productos vendidos del stock.
    # 6) Emitir comprobantes. Factura o ticket.
    # 7) Ventas cerradas no deben ser modificadas.

    # @property
    def get_numero_caja(self):
        """Retorna el Numero de Caja para la Apertura de Caja correspondiente."""
        return '%s' % self.apertura_caja.caja
    # nombre_completo = property(get_nombre_completo)
    get_numero_caja.short_description = 'Caja'

    @property
    def cajero(self):
        """Retorna el Cajero para la Apertura de Caja correspondiente."""
        return '%s' % self.apertura_caja.cajero
    # nombre_completo = property(get_nombre_completo)
    # get_cajero.short_description = 'Cajero'

    def get_sector(self):
        """Retorna el Sector para la Apertura de Caja correspondiente."""
        return '%s' % self.apertura_caja.sector
    # nombre_completo = property(get_nombre_completo)
    get_sector.short_description = 'Sector'

    def get_fecha_hora_apertura_caja(self):
        """Retorna la Fecha/Hora de Apertura de Caja para la Apertura de Caja correspondiente."""
        return '%s' % datetime.datetime.strftime(timezone.localtime(self.apertura_caja.fecha_hora_apertura_caja), '%d/%m/%Y %H:%M')
    # nombre_completo = property(get_nombre_completo)
    get_fecha_hora_apertura_caja.short_description = 'Fecha/hora Apertura Caja'

    def clean(self):
        super(Venta, self).clean()

        # import pdb
        # pdb.set_trace()

        if self.pk is None:

            # try:
            #     field = Venta._meta.get_field('apertura_caja')
            # except FieldDoesNotExist:
            #     # field does not exist
            #     pass

            if hasattr(self, 'apertura_caja'):
                # if getattr(self, 'apertura_caja'):
                # if hasattr(self, 'numero_pedido'):
                #     pedido = getattr(self, 'numero_pedido')
                # if id_pedido is not None and id_pedido != '':
                #     pedido = Pedido.objects.get(pk=id_pedido)
                # if self.venta_ocasional is True or self.venta_ocasional is False and hasattr(self, 'numero_pedido') is False and self.numero_pedido.reserva is None or \

                # 24/11/2016: Situaciones en las que se genera un Numero de Factura para la Venta
                if self.venta_ocasional is True \
                        or self.venta_ocasional is False and hasattr(self, 'numero_pedido') is True and self.numero_pedido.reserva is None \
                        or self.venta_ocasional is False and hasattr(self, 'numero_pedido') is True and self.numero_pedido.reserva is not None \
                                and self.numero_pedido.reserva.pago <= self.numero_pedido.total_pedido:

                    try:
                        factura = FacturaVenta.objects.get(caja=self.apertura_caja.caja, estado='ACT')
                    except ObjectDoesNotExist:
                        raise ValidationError('No existe una Serie de Facturas con estado Vigente para la Caja %s. Cargue '
                                              'una en la pantalla de "Parametrizaciones - Ventas - Series de Facturas"'
                                              % self.apertura_caja.caja)
                    # except self.apertura_caja.DoesNotExist:
                    #     pass

                    try:
                        nro_factura = NumeroFacturaVenta.objects.filter(serie=factura.id).latest('numero_factura')
                        if nro_factura.numero_factura == factura.numero_factura_final:
                            raise ValidationError('Numero de Factura final alcanzado para la Caja %s. Cargue una nueva Serie '
                                                  'en la pantalla de "Parametrizaciones - Ventas - Series de Facturas".'
                                                  % self.apertura_caja.caja)
                        else:
                            nuevo_nro_factura = NumeroFacturaVenta(serie=factura,
                                                                   numero_factura=nro_factura.numero_factura + 1)
                            nuevo_nro_factura.save()
                            self.numero_factura_venta = nuevo_nro_factura
                    except ObjectDoesNotExist:
                        nuevo_nro_factura = NumeroFacturaVenta(serie=factura,
                                                               numero_factura=factura.numero_factura_inicial)
                        nuevo_nro_factura.save()
                        self.numero_factura_venta = nuevo_nro_factura

    def __unicode__(self):
        return u"ID Venta: %s - Fecha Venta: %s" % (self.id, datetime.datetime.strftime(timezone.localtime(self.fecha_hora_venta), '%d/%m/%Y %H:%M'))


class VentaDetalle(models.Model):
    """
    07/07/2016: Registrar los detalles de las Ventas.
    """
    venta = models.ForeignKey('Venta')
    # Los datos de la Venta deben ser copiados del Pedido.
    producto_venta = models.ForeignKey('stock.ProductoVenta', verbose_name='Producto',
                                       help_text='Seleccione el Producto ordenado por el Cliente.')

    # El PrecioVenta se debe desplegar de acuerdo al Producto seleccionado
    # precio_producto_venta = models.ForeignKey('stock.PrecioVentaProducto', default=1,
    #                                           verbose_name='Precio de Venta del Producto',
    #                                           help_text='El Precio de Venta del Producto se asigna de acuerdo al '
    #                                                     'Producto seleccionado.')
    precio_producto_venta = models.DecimalField(max_digits=18, decimal_places=0,
                                                verbose_name='Precio Venta Producto',
                                                help_text='El Precio de Venta del Producto se define en la pantalla '
                                                          'de Productos.')

    cantidad_producto_venta = models.DecimalField(max_digits=10, decimal_places=3, validators=[MinValueValidator(Decimal('0.001'))],
                                                  verbose_name='Cantidad del Producto',
                                                  help_text='Ingrese la cantidad del producto solicitada por el '
                                                            'Cliente.')
    total_producto_venta = models.DecimalField(max_digits=18, decimal_places=0, default=0,
                                               verbose_name='Total del Producto',
                                               help_text='Este valor se calcula automaticamente tomando el Precio de '
                                                         'Venta del Producto por la Cantidad del Producto solicitada '
                                                         'por el Cliente..')

    class Meta:
        verbose_name = 'Venta - Detalle'
        verbose_name_plural = 'Ventas - Detalles'


class VentaOcasional(Venta):
    class Meta:
        proxy = True
        verbose_name = 'Venta Ocasional'
        verbose_name_plural = 'Ventas Ocasionales'

    def __init__(self, *args, **kwargs):
        super(VentaOcasional, self).__init__(*args, **kwargs)
        self.venta_ocasional = True


class VentaOcasionalDetalle(VentaDetalle):
    class Meta:
        proxy = True
        verbose_name = 'Venta Ocasional - Detalle'
        verbose_name_plural = 'Ventas Ocasionales - Detalles'


class Comanda(models.Model):
    """
    Llevar el control de los Pedidos (Comandas) realizados a la Cocina y su cumplimiento.

    Recepcionar comanda.
    """
    # AREA = (
    #     ('COC', 'Cocina'),
    #     ('BAR', 'Barra'),
    # )
    ESTADO_COMANDA = (
        ('PEN', 'Pendiente'),
        ('PRO', 'Procesada'),
        ('CAN', 'Cancelada'),
    )
    ESTADO_VERIFICACION_COMANDA = (
        ('PEN', 'Pendiente'),
        ('PRO', 'Procesada'),
        ('CAN', 'Cancelada'),
    )
    numero_pedido = models.ForeignKey('Pedido', verbose_name='Numero de Pedido')
    id_pedido_detalle = models.ForeignKey('PedidoDetalle')  # default=2
    area_solicitante = models.ForeignKey('bar.Sector',  # default=2,
                                         related_name='area_solicitante_comanda',
                                         verbose_name='Area Solicitante')
    usuario_solicitante = models.ForeignKey('personal.Empleado',  # default=14,
                                            related_name='usuario_solicitante_comanda',
                                            # limit_choices_to=Q(cargo__cargo__exact="MO") | Q(cargo__cargo__exact="BM"),
                                            # to_field='usuario',
                                            verbose_name='Solicitado por?',
                                            help_text='Este dato se completara automaticamente cuando el Pedido '
                                                      'sea guardado.')
    producto_a_entregar = models.ForeignKey('stock.ProductoVenta',  # default=2,
                                            verbose_name='Producto Solicitado')
    cantidad_solicitada = models.DecimalField(max_digits=10, decimal_places=3, default=1, validators=[MinValueValidator(Decimal('0.001'))],
                                              verbose_name='Cantidad Solicitada')
    # area_encargada = models.CharField(max_length=3, choices=AREA, verbose_name='Area Encargada')
    area_encargada = models.ForeignKey('bar.Sector',  # default=2,
                                       related_name='area_encargada_comanda',
                                       verbose_name='Area Encargada')
    fecha_hora_pedido_comanda = models.DateTimeField(verbose_name='Fecha/hora Comanda')
    tiempo_estimado_procesamiento = models.TimeField(verbose_name='Tiempo Estimado Procesamiento',
                                                     # default=datetime.time(00, 15, 00),
                                                     help_text='Corresponde al tiempo estimado que tomara elaborar el '
                                                               'Producto Compuesto')
    estado_comanda = models.CharField(max_length=3, choices=ESTADO_COMANDA, verbose_name='Estado Comanda')
    fecha_hora_procesamiento_comanda = models.DateTimeField(null=True, blank=True,
                                                            verbose_name='Fecha/hora Procesamiento Comanda')
    usuario_procesa = models.ForeignKey('personal.Empleado', null=True, blank=True,
                                        related_name='usuario_procesa_comanda',
                                        # limit_choices_to='',
                                        #  to_field='usuario',
                                        verbose_name='Procesado por?',
                                        help_text='Usuario que proceso la Comanda.')

    # estado_verificacion = models.CharField(max_length=3, choices=ESTADO_VERIFICACION_COMANDA, null=True, blank=True,
    #                                        verbose_name='Estado Verificacion Comanda')
    # observacion_verificacion = models.CharField(max_length=200, null=True, blank=True,
    #                                             verbose_name='Observacion Verificacion')
    # usuario_verifica = models.ForeignKey('personal.Empleado', null=True, blank=True,
    #                                      related_name='usuario_verifica_comanda',
    #                                      # limit_choices_to='',
    #                                      # to_field='usuario',
    #                                      verbose_name='Verificado por?',
    #                                      help_text=u'Usuario que verificó la Comanda.')

    class Meta:
        verbose_name = 'Comanda'
        verbose_name_plural = 'Comandas'

    def __unicode__(self):
        return u"Com: %s - Ped: %s - Fec/hora Com: %s" % (self.id, self.numero_pedido,
                                                                         datetime.datetime.strftime(timezone.localtime(self.fecha_hora_pedido_comanda), '%d/%m/%Y %H:%M'))

    # VALIDACIONES/FUNCIONALIDADES
    # =============================
    # 1) Controlar el procesamiento de los Pedidos realizados a la Cocina.
    # 2) Alertar en caso de que un Pedido lleve mas tiempo de lo normal.
    # 3)


# ======================================================================================================================
class AperturaCaja(models.Model):
    """
    * Registrar apertura de caja: La Apertura de Caja debe ser registrado como un modelo o como un metodo de un modelo?
    """
    ESTADO_APERTURA_CAJA = (
        ('VIG', 'Vigente'),
        ('EXP', 'Expirada'),
        ('CER', 'Cerrada'),
    )
    caja = models.ForeignKey('bar.Caja', limit_choices_to={'estado_caja': "CER"},
                             verbose_name='Caja',
                             help_text='Seleccione la Caja a aperturar.')
    cajero = models.ForeignKey('personal.Empleado',  # default=request.user,
                               # limit_choices_to={'cargo__cargo': "CA"},
                               verbose_name='Cajero',
                               help_text='Seleccione el Cajero que realizara movimientos en esta Caja.')
    sector = models.ForeignKey('bar.Sector',  # default=2,
                               help_text='Seleccione el Sector en donde desempenara sus funciones el Empleado.')
    horario = models.ForeignKey('personal.Horario')  # , default='NO')
    monto_apertura = models.DecimalField(max_digits=18, decimal_places=0, default=0,
                                         verbose_name='Monto Apertura',
                                         help_text='Ingrese el monto de efectivo utilizado para aperturar la Caja.')

    jornada = models.OneToOneField('InicioJornada',  # default=1,
                                   # blank=True,
                                   related_name='jornada_apertura_caja',
                                   verbose_name='Jornada',
                                   help_text='Se genera automaticamente al Confirmar la Apertura de Caja.')

    fecha_hora_apertura_caja = models.DateTimeField(default=timezone.now,  # auto_now_add=True,
                                                    verbose_name='Fecha/hora Apertura Caja',
                                                    help_text='Fecha en la que se realiza la Apertura de Caja.')
    duracion_apertura = models.TimeField(default=datetime.time(10, 00, 00), verbose_name='Duracion Apert. Caja')
    fecha_hora_fin_apertura_caja = models.DateTimeField(default=(timezone.now() + datetime.timedelta(hours=10)),
                                                        # blank=True,
                                                        verbose_name='Fecha/hora Fin Apertura Caja',
                                                        help_text='Fecha/hora de Finalizacion de la Apertura de Caja.')
    fecha_hora_registro_apertura_caja = models.DateTimeField(auto_now_add=True,
                                                             verbose_name='Fecha/hora registro Apert. Caja')
    estado_apertura_caja = models.CharField(max_length=3, choices=ESTADO_APERTURA_CAJA,  # default='VIG',
                                            verbose_name='Estado Apert. Caja')
    en_proceso_cierre = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Apertura de Caja'
        verbose_name_plural = 'Cajas - Aperturas'

    # VALIDACIONES/FUNCIONALIDADES
    # ============================
    # 1) Cierre de Caja
    # 2) Ingreso de Valores: Se ejecuta en la Apertura de la Caja y genera un Comprobante para la impresion.
    # 3) Retiro de Valores: Se ejecuta en el Cierre de la Caja y genera un Comprobante para la impresion.
    # 4) Al confirmar la Apertura de Caja se debe modificar el estado de la Caja a "ABierta".

# ==> Cantidad Total Operaciones Pendientes <==
    def get_cantidad_total_operaciones_pendientes(self):
        count = Venta.objects.filter(apertura_caja_id=self.id, estado_venta__venta_estado='PEN').count()
        return count

# ==> Cantidad Total Operaciones Canceladas <==
    def get_cantidad_total_operaciones_canceladas(self):
        count = Venta.objects.filter(apertura_caja_id=self.id, estado_venta__venta_estado='CAN').count()
        return count

# ==> Efectivo <==
    def get_cantidad_operaciones_efectivo_procesadas(self):
        count = Venta.objects.filter(apertura_caja_id=self.id, forma_pago='EF',
                                     estado_venta__venta_estado='PRO').count()
        return count

    def get_cantidad_operaciones_efectivo_pendientes(self):
        count = Venta.objects.filter(apertura_caja_id=self.id, forma_pago='EF',
                                     estado_venta__venta_estado='PEN').count()
        return count

    def get_cantidad_operaciones_efectivo_canceladas(self):
        count = Venta.objects.filter(apertura_caja_id=self.id, forma_pago='EF',
                                     estado_venta__venta_estado='CAN').count()
        return count

    def get_monto_registro_efectivo(self):
        total = Venta.objects.filter(apertura_caja_id=self.id, forma_pago='EF',
                                     estado_venta__venta_estado='PRO').aggregate(total=Sum('total_venta'))['total']
        return total

# ==> TCs <==
    def get_cantidad_operaciones_tcs_procesadas(self):
        count = Venta.objects.filter(apertura_caja_id=self.id, forma_pago='TC',
                                     estado_venta__venta_estado='PRO').count()
        return count

    def get_cantidad_operaciones_tcs_pendientes(self):
        count = Venta.objects.filter(apertura_caja_id=self.id, forma_pago='TC',
                                     estado_venta__venta_estado='PEN').count()
        return count

    def get_cantidad_operaciones_tcs_canceladas(self):
        count = Venta.objects.filter(apertura_caja_id=self.id, forma_pago='TC',
                                     estado_venta__venta_estado='CAN').count()
        return count

    def get_monto_registro_tcs(self):
        total = Venta.objects.filter(apertura_caja_id=self.id, forma_pago='TC',
                                     estado_venta__venta_estado='PRO').aggregate(total=Sum('total_venta'))['total']
        return total

# ==> TDs <==
    def get_cantidad_operaciones_tds_procesadas(self):
        count = Venta.objects.filter(apertura_caja_id=self.id, forma_pago='TD',
                                     estado_venta__venta_estado='PRO').count()
        return count

    def get_cantidad_operaciones_tds_pendientes(self):
        count = Venta.objects.filter(apertura_caja_id=self.id, forma_pago='TD',
                                     estado_venta__venta_estado='PEN').count()
        return count

    def get_cantidad_operaciones_tds_canceladas(self):
        count = Venta.objects.filter(apertura_caja_id=self.id, forma_pago='TD',
                                     estado_venta__venta_estado='CAN').count()
        return count

    def get_monto_registro_tds(self):
        total = Venta.objects.filter(apertura_caja_id=self.id, forma_pago='TD',
                                     estado_venta__venta_estado='PRO').aggregate(total=Sum('total_venta'))['total']
        return total

# ==> Otros Medios de Pago <==
    def get_cantidad_operaciones_otros_medios_procesadas(self):
        count = Venta.objects.filter(apertura_caja_id=self.id, forma_pago='OM',
                                     estado_venta__venta_estado='PRO').count()
        return count

    def get_cantidad_operaciones_otros_medios_pendientes(self):
        count = Venta.objects.filter(apertura_caja_id=self.id, forma_pago='OM',
                                     estado_venta__venta_estado='PEN').count()
        return count

    def get_cantidad_operaciones_otros_medios_canceladas(self):
        count = Venta.objects.filter(apertura_caja_id=self.id, forma_pago='OM',
                                     estado_venta__venta_estado='CAN').count()
        return count

    def get_monto_registro_otros_medios(self):
        total = Venta.objects.filter(apertura_caja_id=self.id, forma_pago='OM',
                                     estado_venta__venta_estado='PRO').aggregate(total=Sum('total_venta'))['total']
        return total

    def clean(self):
        super(AperturaCaja, self).clean()

        # import pdb
        # pdb.set_trace()

        # El monto_apertura no puede ser 0.
        if self.monto_apertura == 0:
            raise ValidationError({'monto_apertura': _('El Monto de Apertura no puede ser 0.')})

        if self.pk is None:

            # try:
            #     field = Venta._meta.get_field('apertura_caja')
            # except FieldDoesNotExist:
            #     # field does not exist
            #     pass

            if hasattr(self, 'cajero'):
            # if getattr(self, 'apertura_caja'):
                working_day = InicioJornada(mozo=self.cajero,
                                            sector=self.sector,
                                            horario=self.horario,
                                            fecha_hora_inicio_jornada=timezone.now(),
                                            duracion_jornada=self.duracion_apertura,
                                            fecha_hora_fin_jornada=timezone.localtime(timezone.now() + datetime.timedelta(hours=self.duracion_apertura.hour, minutes=self.duracion_apertura.minute)),
                                            estado_jornada='VIG')
                working_day.save()

                self.jornada = working_day


    # def save(self, force_insert=False, force_update=False, using=None,
    #          update_fields=None):
    #
    #     import pdb
    #     pdb.set_trace()
    #
    #     super(AperturaCaja, self).save(force_insert, force_update, using, update_fields)

    def __unicode__(self):
        # return "ID Apert. Caja: %s - Nro. Caja: %s - Cajero: % - Fecha Apert: %s" % (self.id, self.caja, self.cajero, self.fecha_apertura_caja)
        # return "ID: %s - Fec/hora Apert: %s" % (self.id, datetime.datetime.strftime(timezone.localtime(self.fecha_hora_apertura_caja), '%d/%m/%Y %H:%M'))
        return u"ID: %s" % self.id


# def get_limit_choices_to(request):
#     usuario = Empleado.objects.get(usuario=request.user)
#     if usuario.usuario.is_superuser is True:
#         cierres = CierreCaja.objects.all().values('apertura_caja')
#         aperturas = AperturaCaja.objects.filter(estado_apertura_caja__in=['VIG', 'EXP']).exclude(id__in=cierres)
#     else:
#         cierres = CierreCaja.objects.all().values('apertura_caja')
#         aperturas = AperturaCaja.objects.filter(cajero=usuario, estado_apertura_caja__in=['VIG', 'EXP']).exclude(id__in=cierres)
#
#     return {'id': aperturas['id']}


class CierreCaja(models.Model):
    """
    * Cierre de Caja.
    """

    # Estos datos ya se encuentran en la Apertura de Caja
    # caja = models.ForeignKey('bar.Caja', limit_choices_to={'estado__caja_estado': "CE"},
    #                          verbose_name='Caja a Aperturar',
    #                          help_text='Seleccione la Caja a aperturar.')
    # cajero = models.ForeignKey('personal.Empleado',
    #                            limit_choices_to={'cargo__cargo': "CA"},
    #                            verbose_name='Cajero',
    #                            help_text='Seleccione el Cajero que realizara movimientos en esta Caja.')
    # monto_apertura = models.DecimalField(max_digits=18, decimal_places=0, default=0,
    #                                      verbose_name='Monto usado en Apertura',
    #                                      help_text='Ingrese el monto de efectivo utilizado para aperturar la Caja.')

    apertura_caja = models.ForeignKey('AperturaCaja',
                                      # limit_choices_to=get_limit_choices_to(request=),
                                      limit_choices_to={'estado_apertura_caja__in': ('VIG', 'EXP')},  # , 'en_proceso_cierre': False
                                      # limit_choices_to=Q(estado_apertura_caja="VIG") | Q(estado_apertura_caja="EXP"),
                                      verbose_name='Apertura de Caja',
                                      help_text='Seleccione la Apertura de Caja para la cual se realizara el cierre.')
    # fecha_cierre_caja = models.DateField()
    fecha_hora_registro_cierre_caja = models.DateTimeField(auto_now=True,  # default=timezone.now,  # auto_now_add=True,
                                                           verbose_name='Fecha/hora registro Cierre de Caja')

    cantidad_total_operaciones_pendientes = models.PositiveIntegerField(default=0, verbose_name='Ventas Pendientes')
    cantidad_total_operaciones_canceladas = models.PositiveIntegerField(default=0, verbose_name='Ventas Canceladas')

    total_efectivo = models.DecimalField(max_digits=18, decimal_places=0, default=0,
                                         verbose_name='Total Efectivo')
                                         # help_text='Corresponde a la suma del Monto de Apertura con el Monto '
                                         #           'Registrado en Efectivo.')
    total_diferencia = models.DecimalField(max_digits=18, decimal_places=0, default=0,
                                           verbose_name='Total Diferencia',
                                           help_text='Si el Total Diferencia es negativo posee un sobrante.')
    usuario_cierre_caja = models.ForeignKey('personal.Empleado', null=True, blank=True,  # default=17,
                                            related_name='usuario_cierre_caja',
                                            # limit_choices_to='',
                                            #  to_field='usuario',
                                            verbose_name='Cierre de Caja realizado por?',
                                            help_text='Usuario que realizo el Cierre de Caja.')

# ==> Efectivo <==
    cantidad_operaciones_efectivo_procesadas = models.PositiveIntegerField(default=0, verbose_name='Cant. Oper. Efectivo Procesadas')
    cantidad_operaciones_efectivo_pendientes = models.PositiveIntegerField(default=0, verbose_name='Cant. Oper. Efectivo Pendientes')
    cantidad_operaciones_efectivo_canceladas = models.PositiveIntegerField(default=0, verbose_name='Cant. Oper. Efectivo Canceladas')
    monto_registro_efectivo = models.DecimalField(max_digits=18, decimal_places=0, default=0,
                                                  verbose_name='Monto Registrado Efectivo',
                                                  help_text='')
    rendicion_efectivo = models.DecimalField(max_digits=18, decimal_places=0, default=0,
                                             verbose_name='Monto Rendicion Efectivo',
                                             help_text='')
    diferencia_efectivo = models.DecimalField(max_digits=18, decimal_places=0, default=0,
                                              verbose_name='Diferencia Registro/Rendicion Efectivo',
                                              help_text='')
# ==> TCs <==
    cantidad_operaciones_tcs_procesadas = models.PositiveIntegerField(default=0, verbose_name='Cant. Oper. TCs Procesadas')
    cantidad_operaciones_tcs_pendientes = models.PositiveIntegerField(default=0, verbose_name='Cant. Oper. TCs Pendientes')
    cantidad_operaciones_tcs_canceladas = models.PositiveIntegerField(default=0, verbose_name='Cant. Oper. TCs Canceladas')
    monto_registro_tcs = models.DecimalField(max_digits=18, decimal_places=0, default=0,
                                             verbose_name='Monto Registrado TCs',
                                             help_text='')
    rendicion_tcs = models.DecimalField(max_digits=18, decimal_places=0, default=0,
                                        verbose_name='Monto Rendicion TCs',
                                        help_text='')
    diferencia_tcs = models.DecimalField(max_digits=18, decimal_places=0, default=0,
                                         verbose_name='Diferencia Registro/Rendicion TCs',
                                         help_text='')
# ==> TDs <==
    cantidad_operaciones_tds_procesadas = models.PositiveIntegerField(default=0, verbose_name='Cant. Oper. TDs Procesadas')
    cantidad_operaciones_tds_pendientes = models.PositiveIntegerField(default=0, verbose_name='Cant. Oper. TDs Pendientes')
    cantidad_operaciones_tds_canceladas = models.PositiveIntegerField(default=0, verbose_name='Cant. Oper. TDs Canceladas')
    monto_registro_tds = models.DecimalField(max_digits=18, decimal_places=0, default=0,
                                             verbose_name='Monto Registrado TDs',
                                             help_text='')
    rendicion_tds = models.DecimalField(max_digits=18, decimal_places=0, default=0,
                                        verbose_name='Monto Rendicion TDs',
                                        help_text='')
    diferencia_tds = models.DecimalField(max_digits=18, decimal_places=0, default=0,
                                         verbose_name='Diferencia Registro/Rendicion TDs',
                                         help_text='')
# ==> Otros Medios de Pago <==
    cantidad_operaciones_otros_medios_procesadas = models.PositiveIntegerField(default=0, verbose_name='Cant. Oper. Otros Medios Procesadas')
    cantidad_operaciones_otros_medios_pendientes = models.PositiveIntegerField(default=0, verbose_name='Cant. Oper. Otros Medios Pendientes')
    cantidad_operaciones_otros_medios_canceladas = models.PositiveIntegerField(default=0, verbose_name='Cant. Oper. Otros Medios Canceladas')
    monto_registro_otros_medios = models.DecimalField(max_digits=18, decimal_places=0, default=0,
                                                      verbose_name='Monto Registrado Otros Medios',
                                                      help_text='')
    rendicion_otros_medios = models.DecimalField(max_digits=18, decimal_places=0, default=0,
                                                 verbose_name='Monto Rendicion Otros Medios',
                                                 help_text='')
    diferencia_otros_medios = models.DecimalField(max_digits=18, decimal_places=0, default=0,
                                                  verbose_name='Diferencia Registro/Rendicion Otros Medios',
                                                  help_text='')

    class Meta:
        verbose_name = 'Cierre de Caja'
        verbose_name_plural = 'Cajas - Cierres'

    # @property
    def get_cajero(self):
        """Retorna el Cajero para la Apertura de Caja correspondiente."""
        return '%s' % self.apertura_caja.cajero
    # nombre_completo = property(get_nombre_completo)
    get_cajero.short_description = 'Cajero'

    # @property
    def get_numero_caja(self):
        """Retorna el Numero de Caja para la Apertura de Caja correspondiente."""
        return '%s' % self.apertura_caja.caja
    get_numero_caja.short_description = 'Caja'

    def get_sector(self):
        """Retorna el Sector para la Apertura de Caja correspondiente."""
        return '%s' % self.apertura_caja.sector
    get_sector.short_description = 'Sector'

    def get_horario(self):
        """Retorna el Horario para la Apertura de Caja correspondiente."""
        return '%s' % self.apertura_caja.horario
    get_horario.short_description = 'Horario'

    def get_jornada(self):
        """Retorna la Jornada para la Apertura de Caja correspondiente."""
        return '%s' % self.apertura_caja.jornada
    get_jornada.short_description = 'Jornada'

    def get_fecha_hora_apertura_caja(self):
        """Retorna la Fecha/Hora de Apertura de Caja para la Apertura de Caja correspondiente."""
        return '%s' % datetime.datetime.strftime(timezone.localtime(self.apertura_caja.fecha_hora_apertura_caja), '%d/%m/%Y %H:%M')
    # nombre_completo = property(get_nombre_completo)
    get_fecha_hora_apertura_caja.short_description = 'Fecha/hora Apert. Caja'

    def get_monto_apertura(self):
        """Retorna el Monto de Apertura para la Apertura de Caja correspondiente."""
        return '%s' % self.apertura_caja.monto_apertura
    # nombre_completo = property(get_nombre_completo)
    get_monto_apertura.short_description = 'Monto Apertura'

    def get_estado_apertura_caja(self):
        """Retorna el Estdo de la Apertura de Ccaja para la Apertura de Caja correspondiente."""
        return '%s' % self.apertura_caja.get_estado_apertura_caja_display()
    # nombre_completo = property(get_nombre_completo)
    get_estado_apertura_caja.short_description = 'Estado Apert. Caja'

    # def clean(self):
    #     super(CierreCaja, self).clean()
    #
    #     if self.total_diferencia > 20000:
    #         raise ValidationError({'total_diferencia': 'El Total de la Diferencia no puede ser superior a 20.000 Gs. '
    #                                                    'Realice los ajustes necesarios en la rendicion para reducir '
    #                                                    'la diferencia.'})

    def __unicode__(self):
        # return "ID Cierre Caja: %s - ID Apert. Caja: %s" % (self.id, self.apertura_caja)
        return u"ID Cierre Caja: %s - ID Apert. Caja: %s - Fec/hora Cierre: %s" % (self.id, self.apertura_caja, datetime.datetime.strftime(timezone.localtime(self.fecha_hora_registro_cierre_caja), '%d/%m/%Y %H:%M'))


class Jornada(models.Model):
    """
    Inicio de Jornada para Mozos
    """
    ESTADOS_JORNADA = (
        ('VIG', 'Vigente'),
        ('EXP', 'Expirada'),
        ('CER', 'Cerrada'),
    )
    mozo = models.ForeignKey('personal.Empleado',  # default=request.user, # limit_choices_to={'cargo__cargo': "CA"},
                             related_name='mozo',
                             verbose_name='Mozo/Barman',
                             help_text='Se define de acuerdo al usuario logueado al Sistema.')
    sector = models.ForeignKey('bar.Sector',  # default=2,
                               help_text='Seleccione el Sector en donde desempenara sus funciones el Empleado.')
    horario = models.ForeignKey('personal.Horario')  # default=1
    fecha_hora_inicio_jornada = models.DateTimeField(default=timezone.now,  # auto_now_add=True,  #
                                                     verbose_name='Fecha/hora Inicio Jornada',
                                                     help_text='Fecha/hora de Inicio de la Jornada.')
    duracion_jornada = models.TimeField(default=datetime.time(10, 00, 00), verbose_name='Duracion Jornada')
    fecha_hora_fin_jornada = models.DateTimeField(default=(timezone.now() + datetime.timedelta(hours=10)),
                                                  verbose_name='Fecha/hora Fin Jornada',
                                                  help_text='Fecha/hora de Finalizacion de la Jornada.')
    estado_jornada = models.CharField(max_length=3, choices=ESTADOS_JORNADA,  # default='VIG',
                                      blank=True,
                                      verbose_name='Estado')
    cantidad_pedidos_procesados = models.PositiveIntegerField(null=True, blank=True,
                                                              verbose_name='Cant. Pedidos Procesados')
    cantidad_pedidos_pendientes = models.PositiveIntegerField(null=True, blank=True,
                                                              verbose_name='Cant. Pedidos Pendientes')
    cantidad_pedidos_cancelados = models.PositiveIntegerField(null=True, blank=True,
                                                              verbose_name='Cant. Pedidos Cancelados')
    fecha_hora_cierre_jornada = models.DateTimeField(null=True, blank=True,  # auto_now_add=True,  # default=timezone.now,
                                                     verbose_name='Fecha/hora Cierre Jornada',
                                                     help_text='Fecha/hora de Cierre de la Jornada.')
    usuario_cierre_jornada = models.ForeignKey('personal.Empleado', null=True, blank=True,  # default=17,
                                               related_name='usuario_cierre_jornada',
                                               # limit_choices_to='',
                                               # to_field='usuario',
                                               verbose_name='Cerrado por?',
                                               help_text='Usuario que realizo el Cierre de la Jornada.')

    def get_cantidad_pedidos_procesados(self):
        count = Pedido.objects.filter(jornada_id=self.id, estado_pedido__pedido_estado='PRO').count()
        return count

    def get_cantidad_pedidos_pendientes(self):
        count = Pedido.objects.filter(jornada_id=self.id, estado_pedido__pedido_estado__in=['VIG', 'PEN']).count()
        return count

    def get_cantidad_pedidos_cancelados(self):
        count = Pedido.objects.filter(jornada_id=self.id, estado_pedido__pedido_estado='CAN').count()
        return count

    def get_estado_jornada(self):

        # import pdb
        # pdb.set_trace()

        now = timezone.localtime(timezone.now())
        if self.estado_jornada == 'VIG' and timezone.localtime(self.fecha_hora_fin_jornada) < now:
            estado_jornada = 'EXP'
        else:
            estado_jornada = self.estado_jornada
        return estado_jornada

    def __unicode__(self):
        return u"ID: %s - Inicio: %s" % (self.id, datetime.datetime.strftime(timezone.localtime(self.fecha_hora_inicio_jornada), '%d/%m/%Y %H:%M'))


class InicioJornada(Jornada):
    class Meta:
        proxy = True
        verbose_name = 'Mozos/Barmans - Inicio de Jornada'
        verbose_name_plural = 'Mozos/Barmans - Inicios de Jornadas'

    def __unicode__(self):
        return u"ID: %s - Inicio: %s" % (self.id, datetime.datetime.strftime(timezone.localtime(self.fecha_hora_inicio_jornada), '%d/%m/%Y %H:%M'))


class FinJornada(Jornada):
    class Meta:
        proxy = True
        verbose_name = 'Mozos/Barmans - Cierre de Jornada'
        verbose_name_plural = 'Mozos/Barmans - Cierres de Jornadas'

    def __unicode__(self):
        return u"ID: %s - Inicio: %s - Fin: %s" % (self.id, datetime.datetime.strftime(timezone.localtime(self.fecha_hora_inicio_jornada), '%d/%m/%Y %H:%M'), datetime.datetime.strftime(timezone.localtime(self.fecha_hora_fin_jornada), '%d/%m/%Y %H:%M'))


# class MovimientoCaja(models.Model):
#     """
#     * Cierre de Caja.
#     * Emitir estado de cuenta de caja.
#     * Registrar movimientos de caja.
#     """
#
#     class Meta:
#         verbose_name = 'Caja - Movimiento'
#         verbose_name_plural = 'Cajas - Movimientos'
# ======================================================================================================================
# En la revision del 07/09/2016 con el Prof. Diego Ruiz Diaz Gamarra me indico que podiamos descartar programar
# las pantallas de Devoluciones en el modulo de Stock.
#
# class IngresoValorCaja(models.Model):
#     """
#     # 2) Ingreso de Valores: Se ejecuta en la Apertura de la Caja y genera un Comprobante para la impresion.
#     """
#
#     class Meta:
#         verbose_name = 'Caja - Ingreso de Valores'
#         verbose_name_plural = 'Cajas - Ingreso de Valores'
#
#
# class RetiroValorCaja(models.Model):
#     """
#     # 3) Retiro de Valores: Se ejecuta en el Cierre de la Caja y genera un Comprobante para la impresion.
#     """
#
#     class Meta:
#         verbose_name = 'Caja - Retiro de Valores'
#         verbose_name_plural = 'Cajas - Retiro de Valores'