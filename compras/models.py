import datetime
# import uuid
# import string
# import random
from django.db import models
# from polymorphic.models import PolymorphicModel
from django.utils import timezone
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
from bar.models import CompraEstado, OrdenCompraEstado


# Create your models here.
class SerialField(models.Field):
    def db_type(self, connection):
        return 'serial'


class Proveedor(models.Model):
    """
    Almacena datos de los Proveedores.

    21/06/2016: Registrar proveedores.

    * Listar Proveedores.
    """
    proveedor = models.CharField(max_length=100, verbose_name='Razon Social o Nombre',
                                 help_text='Ingrese la Razon Social o el Nombre del Proveedor. (Hasta 100 caracteres)')
    ruc = models.CharField(max_length=15, unique=True, verbose_name='RUC', help_text='Ingrese el RUC del Proveedor.')
    persona_proveedor = models.ForeignKey('bar.Persona', default=1, verbose_name='Persona',
                                          help_text='Indique si el Proveedor tiene personeria Fisica o Juridica.')

    # El Digito Verificador debe ser calculado tomando el RUC ingresado por el usuario.
    digito_verificador = models.IntegerField(default=1, help_text='Digito verificador del RUC del Proveedor. Este '
                                                                  'campo se calcula tomando el RUC ingresado.')

    # @property
    # def digito_verificador(self):
    #     """
    #     El Digito Verificador debe ser calculado tomando el RUC ingresado por el usuario.
    #     """
    #     # return calcular(self.ruc, 11)
    #     return self._digito_verificador

    # def calcular(numero, basemax):

    # Agregados el 18/05/2016
    direccion = models.CharField(max_length=200, null=True, help_text='Ingrese la Direccion del Proveedor. '
                                                                      '(Hasta 200 caracteres)')
    pais_proveedor = models.ForeignKey('bar.Pais', verbose_name='Pais', help_text='Seleccione el Pais del Proveedor.')
    ciudad_proveedor = models.ForeignKey('bar.Ciudad', verbose_name='Ciudad',
                                         help_text='Seleccione la Ciudad del Proveedor.')
    pagina_web = models.URLField(null=True, blank=True)

    # Agregado el 24/05/2016
    fecha_alta_proveedor = models.DateTimeField(default=timezone.now(),  # auto_now_add=True, editable=True,
                                                verbose_name='Fecha de Alta',
                                                help_text='La Fecha de Alta se asigna al momento de guardar los datos '
                                                          'del Proveedor. No se requiere el ingreso de este dato.')

    class Meta:
        verbose_name = 'Proveedor'
        verbose_name_plural = 'Proveedores'

    def __unicode__(self):
        return str(self.proveedor)


class LineaCreditoProveedor(models.Model):
    """
    Agregado el 24/05/2016.
    Registra los montos de las Lineas de Credito ofrecidas por el Proveedor en el tiempo.
    Solo una Linea de Credito puede estar vigente a la vez. Se debe controlar el estado de las Lineas de Credito.
    Con este parametro se debe controlar que las compras a credito realizadas no superen la Linea de Credito.

    21/06/2016: Registrar creditos con proveedores.
    """
    # id = models.AutoField(primary_key=True)
    proveedor = models.ForeignKey('Proveedor')
    fecha_linea_credito_proveedor = models.DateTimeField(default=timezone.now(),
                                                         verbose_name='Fecha de registro',
                                                         help_text='Ingrese la fecha en la que se registra la Linea de '
                                                                   'Credito ofrecida por el Proveedor.')
    linea_credito_proveedor = models.IntegerField(verbose_name='Monto',
                                                  help_text='Ingrese el monto ofrecido por el proveedor como Linea de '
                                                            'Credito.')
    estado_linea_credito_proveedor = models.BooleanField(verbose_name='Activo?',  # unique=True,
                                                         help_text='Solo una Linea de Credito puede estar activa.'
                                                                   'La intencion es llevar un control de los cambios '
                                                                   'de la Linea de Credito en el tiempo.')


class ProveedorTelefono(models.Model):
    # id = models.AutoField(primary_key=True)
    proveedor = models.ForeignKey('Proveedor')
    codigo_pais_telefono = models.ForeignKey('bar.CodigoPaisTelefono')  # default=595
    codigo_operadora_telefono = models.ForeignKey('bar.CodigoOperadoraTelefono',  # default=21
                                                  help_text='Seleccione o ingrese el codigo de ciudad u '
                                                            'operadora de telefonia movil.')
    telefono = models.IntegerField(help_text='Ingrese el telefono fijo o movil del proveedor. El dato debe contener '
                                             'solo numeros.')
    interno = models.IntegerField(null=True, blank=True, help_text='Ingrese el numero de interno.')
    contacto = models.CharField(max_length=100, null=True, blank=True, help_text='Nombre de la persona a la cual '
                                                                                 'contactar en este numero. (Hasta 100 '
                                                                                 'caracteres)')

    class Meta:
        verbose_name = 'Proveedor - Telefono'
        verbose_name_plural = 'Proveedores - Telefonos'

    def __unicode__(self):
        return "%s - %s - %s - %s" % (self.proveedor, self.codigo_pais_telefono, self.codigo_operadora_telefono,
                                      self.telefono)


# class PagoProveedor(models.Model):
#     """
#     21/06/2016: Registrar pagos a proveedores.
#     """
#     compra = models.ForeignKey('Compra')
#     monto_pago_proveedor = models.DecimalField(max_digits=20, decimal_places=0, default=0,
#                                                verbose_name='',
#                                                help_text='')
#     fecha_pago_proveedor = models.DateTimeField(default=timezone.now(), verbose_name='',
#                                                 help_text='')
#
#     class Meta:
#         verbose_name = 'Pago a Proveedores'
#         verbose_name_plural = 'Pagos a Proveedores'
#
#     # VALIDACIONES
#     # 1) Validar que la suma de los pagos para una factura no supere el monto total de la factura
#     # def clean(self):
#
#     def __unicode__(self):
#         return str(self.id)


class ProductoProveedor(models.Model):
    proveedor = models.ForeignKey('Proveedor')
    producto = models.ForeignKey('stock.Producto')

    class Meta:
        verbose_name = 'Producto por Proveedor'
        verbose_name_plural = 'Productos por Proveedores'

    def __unicode__(self):
        return str(self.proveedor) + ' - ' + str(self.producto)


class Empresa(Proveedor):
    timbrado = models.CharField(max_length=100)


# ======================================================================================================================
# Crear la clase OrdenCompra o Pedido
class OrdenCompra(models.Model):
    """
    Este modelo almacena los datos de las Ordenes de Compras o Pedidos realizados a los Proveedores.
    Se desea guardar el historial de las Ordenes de Compras por lo tanto son creados modelos diferentes para las
    Ordenes de Compras (Pedidos) y las Compras propiamente.
    Cuando el Proveedor trae los articulos solicitados en la Orden de Compra se ingresa y confirma la Compra mediante
    la pantalla de Confirmacion de Compras relacionado al modelo Compras.

    21/06/2016: Registrar pedidos.
    """
    # id = models.AutoField(primary_key=True)
    numero_orden_compra = models.AutoField(primary_key=True,
                                           verbose_name='Numero de Orden de Compra',
                                           help_text='Este dato se genera automaticamente cada vez que se va crear '
                                                     'una Orden de Compra.')
    # numero_orden_compra = models.AutoField(primary_key=True,
    # numero_orden_compra = SerialField(max_length=12, unique=True,
    # numero_orden_compra = models.UUIDField(default=uuid.uuid4, max_length=6
    # models.IntegerField(default=lambda: OrdenCompra.objects.latest('id').serial + 1,
    # models.AutoField(primary_key=False, editable=True,
    # models.CharField(default='XXXXXX', max_length=6, unique=True,

    fecha_orden_compra = models.DateTimeField(default=timezone.now(),  # auto_now_add=True, editable=True
                                              verbose_name='Fecha de la Orden de Compra',
                                              help_text='La fecha y hora de la Orden de Compra se asignan al momento '
                                                        'de guardar los datos del pedido. No se requiere el ingreso de '
                                                        'este dato.')
    # Aumenta 1 dia la fecha_entrega a partir de la fecha actual
    fecha_entrega_orden_compra = models.DateTimeField(default=(timezone.now() + datetime.timedelta(days=1)),
                                                      verbose_name='Fecha de Entrega',
                                                      help_text='Indique la fecha y hora en la que el proveedor debe '
                                                                'entregar la Orden de Compra.')
    proveedor_orden_compra = models.ForeignKey('Proveedor', verbose_name='Proveedor', on_delete=models.PROTECT,
                                               help_text='Seleccione el Proveedor al cual se le realizara la Orden de '
                                                         'Compra.')
    forma_pago_orden_compra = models.ForeignKey('bar.FormaPagoCompra', verbose_name='Forma de Pago',
                                                help_text='Seleccione la Forma de Pago para esta Orden de Compra.')

    # Se debe definir un metodo o funcion que compare OrdenCompra.fecha_entrega_orden_compra contra la fecha actual y
    # modificar si corresponde el ESTADO de la Orden de Compra.
    estado_orden_compra = models.ForeignKey('bar.OrdenCompraEstado', default=1,
                                            verbose_name='Estado de la Orden de Compra',
                                            help_text='El estado de la Orden de Compra se establece automaticamente de '
                                                      'acuerdo a la Fecha de Entrega ingresada.')

    # Calcular la suma de todos los totales de compra de cada producto
    # Debe ir en la cabecera y no en el detalle
    total_orden_compra = models.DecimalField(max_digits=20, decimal_places=0, default=0,
                                             verbose_name='Total de la Orden de Compra')  # blank=False (Defau is False)

    class Meta:
        verbose_name = 'Orden de Compra'
        verbose_name_plural = 'Ordenes de Compras'

    # VALIDACIONES
    def clean(self):
        # Valida que la fecha_entrega sea mayor o igual a la fecha_orden_compra
        if self.fecha_entrega_orden_compra < self.fecha_orden_compra:
            raise ValidationError({'fecha_entrega_orden_compra': _('La Fecha de Entrega no puede ser menor que la '
                                                                   'Fecha del Pedido de la Orden de Compra.')})
        # Valida que el Total de la Orden de Compra no sea 0
        if self.total_orden_compra == 0:
            raise ValidationError({'total_orden_compra': _('El Total de la Orden de Compra no puede ser 0.')})

    # Se debe definir un metodo o funcion que compare OrdenCompra.fecha_entrega_orden_compra contra la fecha actual y
    # modificar si corresponde el ESTADO de la Orden de Compra.
    def verifica_estado_orden_compra(self):
        if self.estado_orden_compra not in ('ENT', 'CAN') and self.fecha_entrega_orden_compra < timezone.now():
            self.estado_orden_compra == OrdenCompraEstado.objects.get(estado_orden_compra='PEP')
            self.estado_orden_compra.save()
        elif self.estado_orden_compra not in ('ENT', 'CAN') and self.fecha_entrega_orden_compra >= timezone.now():
            self.estado_orden_compra == OrdenCompraEstado.objects.get(estado_orden_compra='EPP')
            self.estado_orden_compra.save()

    # def from_db(cls, db, field_names, values):
    #     verifica_estado_orden_compra

    def __unicode__(self):
        return "%d - %s" % (self.numero_orden_compra, self.proveedor_orden_compra.proveedor)

    # ===============================================================================================================
    # Se puede agregar una funcion para asignar el Numero Orden de Compra
    # Se probo con SerialField, no funciono
    # Se probo con UUIDField, tampoco funciono. El error recibido fue:
        # (django.db.utils.ProgrammingError: la columna "numero_orden_compra" no puede convertirse automaticamente al
        # tipo uuid
        # HINT:  Especifique una expresion USING para llevar a cabo la conversion.)

    # def id_generator(size, chars=string.ascii_uppercase + string.digits):
    #     return ''.join(random.choice(chars) for _ in range(size))
    #
    # def save(self):
    #     if not self.numero_orden_compra:
    #         # Generate ID once, then check the db. If exists, keep trying.
    #         self.numero_orden_compra = self.id_generator(6)
    #         while OrdenCompra.objects.filter(numero_orden_compra=self.numero_orden_compra).exists():
    #             self.numero_orden_compra = self.id_generator(6)
    #     super(OrdenCompra, self).save()

    # def _get_numero_orden_compra(self):
    #     """
    #     Genera el Numero de Orden de Compra de forma automatica
    #     """
    #     return self.objects.latest('id').serial + 1
    # numero_orden_compra = property(_get_numero_orden_compra)

    # def save(self):
    #     if not self.numero_orden_compra:
    #         self.numero_orden_compra = 1
    #     else:
    #         self.numero_orden_compra = self.objects.latest('numero_orden_compra').serial + 1
    #     super(OrdenCompra, self).save()
    # ===============================================================================================================


class OrdenCompraDetalle(models.Model):
    numero_orden_compra = models.ForeignKey('OrdenCompra')

    # La idea es filtrar los Productos de acuerdo al Proveedor seleccionado.
    producto_orden_compra = models.ForeignKey('stock.Producto', related_name='orden_compra_productos',
                                              verbose_name='Producto',
                                              help_text='Seleccione un Producto a ordenar.')
    precio_producto_orden_compra = models.DecimalField(max_digits=20, decimal_places=0,
                                                       verbose_name='Precio del Producto',
                                                       help_text='Ingrese el precio de compra del producto definido '
                                                                 'por el proveedor.')
    cantidad_producto_orden_compra = models.DecimalField(max_digits=10, decimal_places=3,
                                                         verbose_name='Cantidad del Producto',
                                                         help_text='Ingrese la cantidad a adquirir del producto.')

    # La Unidad de Medida del Producto ya esta definida en la clase Producto en la app de Stock.
    unidad_medida_orden_compra = models.ForeignKey('bar.UnidadMedidaProducto', default=1,  # to_field='unidad_medida',
                                                   verbose_name='Unidad de Medida del Producto',
                                                   help_text='Debe ser la definida en los datos del Producto, no debe '
                                                             'ser seleccionada por el usuario.')

    # Calcular "cantidad_producto_orden_compra" x "precio_producto_orden_compra"
    total_producto_orden_compra = models.DecimalField(max_digits=20, decimal_places=0, default=0,
                                                      verbose_name='Total del Producto',
                                                      help_text='Este valor se calcula automaticamente tomando el '
                                                                'Precio del Producto por la Cantidad del Producto.')

    # @property
    # def total_orden_compra_producto(self):
    #     """
    #     Calcula "cantidad_producto * precio_compra_producto" y retorna el valor para el campo total_compra_producto
    #     como una propiedad o atributo del modelo.
    #     """
    #     return self.cantidad_producto * self.precio_compra_producto

    # total_orden_compra_producto = property(_get_total_compra_producto())

    class Meta:
        verbose_name = 'Orden de Compra - Detalle'
        verbose_name_plural = 'Ordenes de Compras - Detalles'

    # def __unicode__(self):
    #     return self.compra + ' - ' + self.producto


# ======================================================================================================================
class Compra(models.Model):
    """
    21/06/2061: Registrar compras.
                Sumar los productos comprados al stock.
                Listar las Compras realizadas por unidad de tiempo y/o proveedor.

    Las Compras de los productos o insumos se realizan por dia. Se realiza un pedido al proveedor de lo que se en ese
    dia. Esto es porque el Deposito en el cual se guardan los productos es muy limitado en cuando a espacio fisico.
    Ademas realizando de esta manera se mejora el control de stock.

    Las Compras ingresan totalmente al Deposito Central y a partir de ahi se transfieren a los Depositos Operativos
    segun pedidos de transferencias: Deposito Barra Principal, Deposito Barra Arriba, Cocina y Barrita.
    """
    # id = models.AutoField(primary_key=True)
    numero_compra = models.AutoField(primary_key=True, verbose_name='ID de Compra',
                                     help_text='Este dato se genera automaticamente cada vez que se va a confirmar '
                                               'una Compra.')
    numero_orden_compra = models.ForeignKey('OrdenCompra', verbose_name='Numero de Orden de Compra',
                                            help_text='Seleccione el Numero de Orden de Compra para la cual se '
                                                      'confirmara la Compra.')
    fecha_compra = models.DateTimeField(default=timezone.now(),  # auto_now_add=True, editable=True
                                        verbose_name='Fecha y hora de la Compra',
                                        help_text='La fecha y hora se asignan al momento de guardar los datos de la '
                                                  'Compra. No se requiere el ingreso de este dato.')
    # proveedor = models.ForeignKey('Compra', to_field='proveedor', related_name='proveedor')
    total_compra = models.DecimalField(max_digits=20, decimal_places=2, default=0)
    numero_factura_compra = models.IntegerField(verbose_name='Numero de Factura de la Compra', default=1,
                                                help_text='Ingrese el Numero de Factura que acompana la Compra.')
    fecha_factura_compra = models.DateField(default=timezone.now(), verbose_name='Fecha de la Factura de la Compra',
                                            help_text='Ingrese la fecha de la factura.')
    numero_nota_credito_compra = models.IntegerField(verbose_name='Numero Nota de Credito', default=1,
                                                     help_text='Ingrese el Numero de la Nota de Credito que acompana '
                                                               'la Compra en caso de que la Forma de Pago de la misma '
                                                               'sea a Credito.')
    estado_compra = models.ForeignKey('bar.CompraEstado', default=1,
                                      help_text='La Compra puede tener 3 estados: PENDIENTE, CONFIRMADA o CANCELADA. '
                                                'El estado se asigna de forma automatica de acuerdo a la accion '
                                                'realizada.')

    class Meta:
        # proxy = True
        verbose_name = 'Confirmacion de Compra'
        verbose_name_plural = 'Confirmaciones de Compras'

    # def registrar_compra(self):
    #
    # def actualizar_stock(self):
    #
    # def listar_compra(self):

    def __unicode__(self):
        return str(self.numero_compra)


class CompraDetalle(models.Model):
    numero_compra = models.ForeignKey('Compra')
    producto_compra = models.ForeignKey('ProductoProveedor', default=1, related_name='compra_productos',
                                        help_text='Seleccione un producto a comprar.')
    precio_producto_compra = models.DecimalField(max_digits=20, decimal_places=2,
                                                 help_text='Ingrese el precio de compra del producto definido por el '
                                                           'proveedor.')
    cantidad_producto_compra = models.DecimalField(max_digits=10, decimal_places=3,
                                                   help_text='Ingrese la cantidad a adquirir del producto.')
    unidad_medida_compra = models.ForeignKey('bar.UnidadMedidaProducto', default=1,  # to_field='unidad_medida',
                                             verbose_name='Unidad de Medida del Producto',
                                             help_text='Debe ser la definida en los datos del Producto, no debe '
                                                       'ser seleccionada por el usuario.')
    total_producto_compra = models.DecimalField(max_digits=20, decimal_places=2, default=0)

    # @property
    # def total_compra_producto(self):
    #     """
    #     Calcula "cantidad_producto * precio_compra_producto" y retorna el valor para el campo total_compra_producto
    #     """
    #     return self.cantidad_producto * self.precio_compra_producto

    # total_compra_producto = property(_get_total_compra_producto())

    # Calcular cantidad_producto x precio_compra_producto
    # total_compra_producto = models.DecimalField(max_digits=20, decimal_places=2)

    # Calcular la suma de todos los totales de compra de cada producto
    # total_compra = models.DecimalField(max_digits=20, decimal_places=2, default=0)
    # Debe ir en la cabecera y no en el detalle

    class Meta:
        verbose_name = 'Compra - Detalle'
        verbose_name_plural = 'Compras - Detalles'

    # def __unicode__(self):
    #     return self.compra + ' - ' + self.producto


# ======================================================================================================================
# class ModelA(PolymorphicModel):
#     field1 = models.CharField(max_length=10)
#
#
# class ModelB(ModelA):
#     field2 = models.CharField(max_length=10)
#
#
# class ModelC(ModelB):
#     field3 = models.CharField(max_length=10)