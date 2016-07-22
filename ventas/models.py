from django.db import models
from django.utils import timezone

# Create your models here.


class Pedido(models.Model):
    """
    Registrar los datos de la cabecera del Pedido.

    * Registrar que mozo/barman realizo el pedido.
    * Anular pedido.
    * Transferir pedidos entre mesas. (menos prioritario)
    """
    fecha_pedido = models.DateTimeField(default=timezone.now(), verbose_name='', help_text='')
    # reserva = models.ForeignKey('clientes.Reserva')
    mesa_pedido = models.ForeignKey('bar.Mesa')
    mozo_pedido = models.ForeignKey('personal.Empleado', default=3)
    total_pedido = models.DecimalField(max_digits=20, decimal_places=0, default=0,
                                       verbose_name='Total del Pedido')
    estado_pedido = models.ForeignKey('bar.PedidoEstado', default=1,
                                      verbose_name='Estado del Pedido',
                                      help_text='El estado del Pedido se establece automaticamente de acuerdo a...')

    class Meta:
        verbose_name = 'Pedido'
        verbose_name_plural = 'Pedidos'

    def __unicode__(self):
        return "%s - %s" % (self.id, self.fecha_pedido)


class PedidoDetalle(models.Model):
    """
    Registrar los datos del detalle del Pedido.

    * Imprimir comanda.
    """
    pedido = models.ForeignKey('Pedido')
    fecha_pedido_detalle = models.DateTimeField(default=timezone.now())
    producto_pedido = models.ForeignKey('stock.Producto')
    precio_producto_pedido = models.ForeignKey('stock.PrecioProducto', default=1)
    cantidad_producto_pedido = models.DecimalField(max_digits=10, decimal_places=3, default=1,
                                                   verbose_name='Cantidad del Producto',
                                                   help_text='Ingrese la cantidad del producto solicitada por el '
                                                             'Cliente.')
    total_producto_pedido = models.DecimalField(max_digits=20, decimal_places=0, default=0,
                                                verbose_name='Total del Producto ordenado por el Cliente.',
                                                help_text='Este valor se calcula automaticamente tomando el '
                                                          'Precio del Producto por la Cantidad del Producto.')

    class Meta:
        verbose_name = 'Pedido - Detalle'
        verbose_name_plural = 'Pedidos - Detalles'

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
    empresa = models.ForeignKey('compras.Empresa')
    fecha_venta = models.DateTimeField(default=timezone.now())
    cliente = models.ForeignKey('clientes.Cliente')
    reserva = models.ForeignKey('clientes.Reserva')
    forma_pago = models.ForeignKey('bar.FormaPagoVenta')
    total_venta = models.DecimalField(max_digits=20, decimal_places=0, default=0, verbose_name='Total de la Venta')
    estado_venta = models.ForeignKey('bar.VentaEstado', default=1,
                                     verbose_name='Estado de la Venta',
                                     help_text='El estado de la Venta se establece de acuerdo a...')

    class Meta:
        verbose_name = 'Venta'
        verbose_name_plural = 'Ventas'

    def __unicode__(self):
        return "%s - %s - %s" % (self.id, self.cliente, self.fecha_venta)


class VentaDetalle(models.Model):
    """
    07/07/2016: Registrar los detalles de las Ventas.
    """
    venta = models.ForeignKey('Venta')
    producto_venta = models.ForeignKey('stock.Producto')
    precio_producto_venta = models.ForeignKey('stock.PrecioProducto')
    cantidad_producto_venta = models.DecimalField(max_digits=10, decimal_places=3,
                                                  verbose_name='Cantidad del Producto',
                                                  help_text='Ingrese la cantidad del producto solicitada por el '
                                                            'Cliente.')
    total_producto_venta = models.DecimalField(max_digits=20, decimal_places=0, default=0,
                                               verbose_name='Total del Producto ordenado por el Cliente.',
                                               help_text='Este valor se calcula automaticamente tomando el '
                                                         'Precio del Producto por la Cantidad del Producto.')

    class Meta:
        verbose_name = 'Venta - Detalle'
        verbose_name_plural = 'Ventas - Detalles'


class Cocina(models.Model):
    """
    Llevar el control de los Pedidos (Comandas) realizados a la Cocina y su cumplimiento.

    Recepcionar comanda.
    """


class AperturaCaja(models.Model):
    """
    * Registrar apertura de caja: La Apertura de Caja debe ser registrado como un modelo o como un metodo de un modelo?
    * Cierre de Caja.
    * Emitir estado de cuenta de caja.
    """
    caja = models.ForeignKey('bar.Caja')
    cajero = models.ForeignKey('personal.Empleado')
    fecha_hora_apertura_caja = models.DateTimeField()
    monto_apertura = models.DecimalField(max_digits=20, decimal_places=0, default=0,
                                         verbose_name='',
                                         help_text='')

# Cierre de Caja
# Ingreso de Valores: Se ejecuta en la Apertura de la Caja y genera un Comprobante para la impresion.
# Retiro de Valores: Se ejecuta en el Cierre de la Caja y genera un Comprobante para la impresion.