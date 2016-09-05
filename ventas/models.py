from django.db import models
from django.utils import timezone
import datetime
from django.db.models import Q
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
from personal.models import Empleado

# Create your models here.


class Pedido(models.Model):
    """
    Registrar los datos de la cabecera del Pedido.

    * Registrar que mozo/barman realizo el pedido.
    * Anular pedido.
    * Transferir pedidos entre mesas. (menos prioritario)
    """

    # Desplegar las Reservas que tienen estado "Vigente" unicamente. OK!
    # La Reserva es opcional por lo tanto se asigna blank=True y null=True
    reserva = models.ForeignKey('clientes.Reserva', blank=True, null=True,
                                limit_choices_to={'estado__reserva_estado': "VIG"},
                                help_text='Seleccione una Reserva en caso de que el Cliente haya realizado una.')

    # 1) Al seleccionar la Reserva se debe controlar que la misma corresponda a la fecha y hora indicada y se deben
    # cargar los datos de las Mesas Reservadas y el Monto de la Entrega.
    monto_entrega_reserva = models.DecimalField(max_digits=18, decimal_places=0, default=0, blank=True, null=True,
                                                verbose_name='Monto Entrega',
                                                help_text='Ingrese el monto a pagar por la Reserva. Este monto luego '
                                                          'se acredita en consumision.')

    # Si el Cliente tiene una Reserva los datos de las Mesas se debe tomar de 'clientes.Reserva'
    mesa_pedido = models.ManyToManyField('bar.Mesa', limit_choices_to={'estado__mesa_estado': "DI"},
                                         verbose_name='Mesas disponibles',
                                         help_text='Indique la/s mesa/s que sera/n ocupada/s por el/los Cliente/s.')

    # Debe ser el usuario con el cual se esta registrando el Pedido, no se debe poder seleccionar el usuario.
    mozo_pedido = models.ForeignKey(  # 'auth.User', unique=True,
                                    'personal.Empleado', limit_choices_to=Q(cargo__cargo__exact="MO") |
                                                                          Q(cargo__cargo__exact="BM"),
                                    to_field='usuario',
                                    verbose_name='Atendido por?',
                                    help_text='Este dato se completara automaticamente cuando el Pedido sea guardado.')
    estado_pedido = models.ForeignKey('bar.PedidoEstado', default=1,  # default={'pedido_estado': "VIG"},
                                      verbose_name='Estado del Pedido',
                                      help_text='El estado del Pedido se establece automaticamente.')
    fecha_pedido = models.DateTimeField(auto_now_add=True, verbose_name='Fecha/Hora del Pedido',
                                        help_text='La fecha y hora del Pedido se asignara automaticamente una vez que '
                                                  'sea guardado.')  # default=timezone.now()
    total_pedido = models.DecimalField(max_digits=18, decimal_places=0, default=0,
                                       verbose_name='Total del Pedido')

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

    def clean(self):
        # Valida que el Total del Pedido no sea 0
        if self.total_pedido == 0:
            raise ValidationError({'total_pedido': _('El Total del Pedido no puede ser 0.')})

    def __unicode__(self):
        return "Nro. Ped: %s - Fec. Ped: %s" % (self.id, datetime.datetime.strftime(timezone.localtime(self.fecha_pedido), '%d/%m/%Y'))


class PedidoDetalle(models.Model):
    """
    Registrar los datos del detalle del Pedido.

    * Imprimir comanda.
    """
    pedido = models.ForeignKey('Pedido')

    # Se deben desplegar solo los Productos con Tipo de Producto "VE - Para la Venta" y los Productos Compuestos o
    # Elaborados.
    producto_pedido = models.ForeignKey('stock.Producto', limit_choices_to={'tipo_producto__tipo_producto': "VE"},
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
                                                verbose_name='Costo Total del Producto',
                                                help_text='Este valor se calcula automaticamente tomando el '
                                                          'Precio Venta del Producto por la Cantidad del Producto.')
    fecha_pedido_detalle = models.DateTimeField(auto_now_add=True,  # default=timezone.now()
                                                verbose_name='Fecha/hora del detalle del Pedido',
                                                help_text='Registra la fecha y hora en que se realizo el detalle del '
                                                          'Pedido, util cuando el cliente pide mas productos.')

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
    empresa = models.ForeignKey('compras.Empresa', default=1)
    numero_factura_venta = models.ForeignKey('bar.FacturaVenta', default=1,
                                             # to_field='numero_factura_actual', unique=True,
                                             verbose_name='Numero de Factura de la Venta',
                                             help_text='')
    fecha_venta = models.DateTimeField(auto_now_add=True,  # default=timezone.now()
                                       verbose_name='Fecha/hora de la Venta',
                                       help_text='Registra la fecha y hora en la que se confirmo la Venta.')
    # Seria ideal que tome el dato de la Caja de acuerdo al usuario logueado y a la Caja aperturada.
    caja = models.ForeignKey('bar.Caja', default=1)
    numero_pedido = models.OneToOneField('Pedido', limit_choices_to={'estado_pedido__pedido_estado': "VIG"},
                                         verbose_name='Numero de Pedido',  # default=1,
                                         help_text='Seleccione el Numero de Pedido para el cual se registrara la '
                                                   'Venta.')
    # Si el Cliente tiene una Reserva seria conveniente tomar sus datos de la Reserva.
    reserva = models.ForeignKey('clientes.Reserva')
    cliente = models.ForeignKey('clientes.Cliente', help_text='Confirme con el Cliente si son correctos sus datos '
                                                              'antes de confirmar la Venta.')
    forma_pago = models.ForeignKey('bar.FormaPagoVenta', help_text='Seleccione la Forma de Pago.')
    total_venta = models.DecimalField(max_digits=18, decimal_places=0, default=0,
                                      verbose_name='Total de la Venta')
    estado_venta = models.ForeignKey('bar.VentaEstado', default=1,
                                     verbose_name='Estado de la Venta',
                                     help_text='El estado de la Venta se establece de acuerdo a...')

    class Meta:
        verbose_name = 'Venta'
        verbose_name_plural = 'Ventas'

    # VALIDACIONES/FUNCIONALIDADES
    # ============================
    # 1) Registrar Ventas con sus respectivas Formas de Pago.
    # 2) Registrar Movimientos de Caja (serian las Ventas propiamente)
    # 3) Cerrar venta.
    # 4) Anular venta.
    # 5) Restar los productos vendidos del stock.
    # 6) Emitir comprobantes. Factura o ticket.
    # 7) Ventas cerradas no deben ser modificadas.

    def __unicode__(self):
        return "%s - %s - %s" % (self.id, self.cliente, self.fecha_venta)


class VentaDetalle(models.Model):
    """
    07/07/2016: Registrar los detalles de las Ventas.
    """
    venta = models.ForeignKey('Venta')
    # Los datos de la Venta deben ser copiados del Pedido.
    producto_venta = models.ForeignKey('stock.Producto', verbose_name='Producto',
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

    cantidad_producto_venta = models.DecimalField(max_digits=10, decimal_places=3,
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


class Comanda(models.Model):
    """
    Llevar el control de los Pedidos (Comandas) realizados a la Cocina y su cumplimiento.

    Recepcionar comanda.
    """
    AREA = (
        ('COC', 'Cocina'),
        ('BAR', 'Barra'),
    )
    ESTADO_COMANDA = (
        ('PEN', 'Pendiente'),
        ('PRO', 'Procesada'),
        ('CAN', 'Cancelada'),
    )
    producto_a_elaborar = models.ForeignKey('stock.ProductoCompuesto')
    area_encargada = models.CharField(max_length=3, choices=AREA)
    fecha_hora_pedido_comanda = models.DateTimeField()
    estado_comanda = models.CharField(max_length=3, choices=ESTADO_COMANDA)
    fecha_hora_procesamiento_comanda = models.DateTimeField()

    class Meta:
        verbose_name = 'Comanda'
        verbose_name_plural = 'Comandas'

    # VALIDACIONES/FUNCIONALIDADES
    # =============================
    # 1) Controlar el procesamiento de los Pedidos realizados a la Cocina.
    # 2) Alertar en caso de que un Pedido lleve mas tiempo de lo normal.
    # 3)


class AperturaCaja(models.Model):
    """
    * Registrar apertura de caja: La Apertura de Caja debe ser registrado como un modelo o como un metodo de un modelo?
    """
    caja = models.ForeignKey('bar.Caja', limit_choices_to={'estado__caja_estado': "CE"},
                             verbose_name='Caja a Aperturar',
                             help_text='Seleccione la Caja a aperturar.')
    cajero = models.ForeignKey('personal.Empleado', limit_choices_to={'cargo__cargo': "CA"},
                               verbose_name='Cajero',
                               help_text='Seleccione el Cajero que realizara movimientos en esta Caja.')
    fecha_hora_apertura_caja = models.DateTimeField(auto_now_add=True)
    monto_apertura = models.DecimalField(max_digits=18, decimal_places=0, default=0,
                                         verbose_name='Monto usado en Apertura',
                                         help_text='Ingrese el monto de efectivo utilizado para aperturar la Caja.')

    class Meta:
        verbose_name = 'Caja - Apertura'
        verbose_name_plural = 'Cajas - Aperturas'

    # VALIDACIONES/FUNCIONALIDADES
    # ============================
    # 1) Cierre de Caja
    # 2) Ingreso de Valores: Se ejecuta en la Apertura de la Caja y genera un Comprobante para la impresion.
    # 3) Retiro de Valores: Se ejecuta en el Cierre de la Caja y genera un Comprobante para la impresion.
    # 4) Al confirmar la Apertura de Caja se debe modificar el estado de la Caja a "ABierta".

    def __unicode__(self):
        return "ID Apert. Caja: %s - Nro. Caja: %s - Fecha Apert: %s" % (self.id, self.caja,
                                                                         self.fecha_hora_apertura_caja)


class MovimientoCaja(models.Model):
    """
    * Cierre de Caja.
    * Emitir estado de cuenta de caja.
    * Registrar movimientos de caja.
    """

    class Meta:
        verbose_name = 'Caja - Movimiento'
        verbose_name_plural = 'Cajas - Movimientos'


class CierreCaja(models.Model):
    """
    * Cierre de Caja.
    """

    class Meta:
        verbose_name = 'Caja - Cierre'
        verbose_name_plural = 'Cajas - Cierres'


class IngresoValorCaja(models.Model):
    """
    # 2) Ingreso de Valores: Se ejecuta en la Apertura de la Caja y genera un Comprobante para la impresion.
    """

    class Meta:
        verbose_name = 'Caja - Ingreso de Valores'
        verbose_name_plural = 'Cajas - Ingreso de Valores'


class RetiroValorCaja(models.Model):
    """
    # 3) Retiro de Valores: Se ejecuta en el Cierre de la Caja y genera un Comprobante para la impresion.
    """

    class Meta:
        verbose_name = 'Caja - Retiro de Valores'
        verbose_name_plural = 'Cajas - Retiro de Valores'