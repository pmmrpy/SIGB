from django.db import models
from django.utils import timezone

# Create your models here.

# class SerialField(object):
#     def db_type(self, connection):
#         return 'serial'


class Proveedor(models.Model):
    proveedor = models.CharField(max_length=100, help_text='Nombre del proveedor.')
    ruc = models.CharField(max_length=15, unique=True, verbose_name='RUC', help_text='RUC del proveedor.')
    digito_verificador = models.IntegerField(default=1, help_text='Ingrese el digito verificador del RUC '
                                                                  'del proveedor.')

    class Meta:
        verbose_name = 'Proveedor'
        verbose_name_plural = 'Proveedores'

    def __unicode__(self):
        return self.proveedor


class TelefonoProveedor(models.Model):
    proveedor = models.ForeignKey('Proveedor')
    codigo_pais_telefono = models.ForeignKey('bar.CodigoPaisTelefono', default=595)
    codigo_ciudad_operadora_telefono = models.ForeignKey('bar.CodigoCiudadOperadoraTelefono', default=21,
                                                         help_text='Seleccione o ingrese el codigo de ciudad u '
                                                                   'operadora de telefonia movil.')
    telefono = models.IntegerField(help_text='Ingrese el telefono fijo o movil del proveedor. El dato debe contener '
                                             'solo numeros.')
    interno = models.IntegerField(null=True, blank=True, help_text='Ingrese el numero de interno.')
    contacto = models.CharField(max_length=100, help_text='Nombre de la persona a la cual contactar en este numero.')

    class Meta:
        verbose_name = 'Proveedor - Telefono'
        verbose_name_plural = 'Proveedores - Telefonos'


class Compra(models.Model):
    # id = models.AutoField(primary_key=True)
    numero_compra = models.IntegerField(default=1, unique=True, verbose_name='Numero Orden de Compra',
                                        help_text='Este dato se genera automaticamente cada vez que se va crear una '
                                                  'Orden de Compra.')
    fecha_pedido = models.DateTimeField(default=timezone.now(), help_text='Ingrese la fecha en la que se realiza'
                                                                          ' el pedido.')
    fecha_entrega = models.DateTimeField(default=timezone.now(), help_text='Indique la fecha en la que el proveedor'
                                                                           ' debe entregar el pedido.')
    proveedor_compra = models.ForeignKey('Proveedor', help_text='Seleccione el proveedor al cual se le '
                                                                'realizara la compra.')
    forma_pago = models.ForeignKey('bar.FormaPagoCompra', default=1, help_text='Seleccione la Forma de Pago para esta '
                                                                               'compra.')

    def __unicode__(self):
        return str(self.numero_compra)

    # Se puede agregar una funcion para asignar el Numero Orden de Compra


class CompraDetalle(models.Model):
    compra = models.ForeignKey('Compra', related_name='compra')
    # proveedor = models.ForeignKey('Compra', to_field='proveedor', related_name='proveedor')
    producto = models.ForeignKey('ProductoProveedor', related_name='productos', help_text='Seleccione un producto a '
                                                                                          'comprar.')
    cantidad_producto = models.DecimalField(max_digits=10, decimal_places=2, help_text='Ingrese la cantidad a adquirir '
                                                                                       'del producto.')
    precio_compra_producto = models.DecimalField(max_digits=20, decimal_places=2, help_text='Ingrese el precio de '
                                                                                            'compra del producto '
                                                                                            'definido por el '
                                                                                            'proveedor.')

    class Meta:
        verbose_name = 'Compra - Detalle'
        verbose_name_plural = 'Compras - Detalles'

    @property
    def total_compra_producto(self):
        """Retorna el total de compra del producto para el campo total_compra_producto"""
        return self.cantidad_producto * self.precio_compra_producto

    # total_compra_producto = property(_get_total_compra_producto())

    # total_compra_producto = models.DecimalField(max_digits=20, decimal_places=2)  # Calcular
    # cantidad_producto x precio_compra_producto

    total_compra = models.DecimalField(max_digits=20, decimal_places=2, default=0)  # Calcular la suma de todos los
    # totales de compra de cada producto

    # def __unicode__(self):
    #     return self.compra + ' - ' + self.producto


class ProductoProveedor(models.Model):
    proveedor = models.ForeignKey('Proveedor')
    producto = models.ForeignKey('stock.Producto')

    class Meta:
        verbose_name = 'Producto por Proveedor'
        verbose_name_plural = 'Productos por Proveedor'

    def __unicode__(self):
        return str(self.proveedor) + ' - ' + str(self.producto)