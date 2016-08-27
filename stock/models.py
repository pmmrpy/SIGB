import datetime
from django.db import models
from django.utils import timezone
from django.db.models import Q
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
from django.utils.safestring import mark_safe
from bar.models import TipoProducto, UnidadMedidaProducto, TransferenciaStockEstado
from personal.models import Empleado

# Create your models here.


class Producto(models.Model):
    """
    21/06/2016: Registrar productos.

    Tipo Producto: Diferencia un Producto que es adquirido para ser puesto a la Venta directamente de un Insumo.
    Categoria:
    SubCategoria:
    """
    producto = models.CharField(max_length=100, verbose_name='Nombre del Producto',
                                help_text='Ingrese el nombre o descripcion del Producto.')
    # Realizar alguna validacion sobre el ingreso del codigo_barra, por lo menos cantidad de caracteres
    codigo_barra = models.CharField(max_length=100, verbose_name='Codigo de Barra',  # default=1,
                                    help_text='Ingrese el codigo de barra del Producto si posee.')
    marca = models.CharField(max_length=100, verbose_name='Marca',  # default='Marca',
                             help_text='Ingrese la marca del Producto.')
    unidad_medida_compra = models.ForeignKey('bar.UnidadMedidaProducto', related_name='un_med_compra',  # default=1,
                                             verbose_name='Unidad de Medida Compra')
    # stock_minimo = models.DecimalField(max_digits=10, decimal_places=3, default=1,
    #                                    verbose_name='Stock Minimo',
    #                                    help_text='Cantidad minima del producto a mantener en Stock.')
    imagen = models.ImageField(upload_to='stock/productos/', verbose_name='Archivo de Imagen',
                               help_text='Seleccione el archivo con la imagen del Producto.')
    fecha_alta_producto = models.DateTimeField(auto_now_add=True, editable=True,  # default=timezone.now(),
                                               verbose_name='Fecha de Alta',
                                               help_text='La Fecha de Alta se asigna al momento de guardar los datos '
                                                         'del Producto. No se requiere el ingreso de este dato.')
    tipo_producto = models.ForeignKey('bar.TipoProducto', verbose_name='Tipo de Producto',  # default="VE",
                                      help_text='Seleccione el Tipo de Producto.')
    categoria = models.ForeignKey('bar.CategoriaProducto', help_text='Seleccione la Categoria del Producto.')
    subcategoria = models.ForeignKey('bar.SubCategoriaProducto', help_text='Seleccione la SubCategoria del Producto.')
    # unidad_medida_contenido = models.ForeignKey('bar.UnidadMedidaProducto', related_name='un_med_contenido',
    #                                             verbose_name='Unidad de Medida Contenido')  # default=1,
    contenido = models.DecimalField(max_digits=10, decimal_places=3,  # default=0,
                                    verbose_name='Cantidad del Contenido',
                                    help_text='Ingrese el Contenido del producto de acuerdo a su Unidad de Medida.')
    compuesto = models.BooleanField(verbose_name='Es compuesto?',  # default=False,
                                    help_text='La casilla se marca automicamente si el Producto a ser registrado es '
                                              'Compuesto o no.')
    cantidad_existente_stock = models.DecimalField(max_digits=10, decimal_places=3, default=0,
                                                   verbose_name='Cantidad Existente',
                                                   help_text='Corresponde a la cantidad existente del Producto '
                                                             'registrada en la tabla Stock.')
    porcentaje_ganancia = models.DecimalField(max_digits=3, decimal_places=0, default=30,
                                              verbose_name='Porcentaje de Ganancia',
                                              help_text='Ingrese el Margen de Utilidad o Porcentaje de Ganancia que '
                                                        'desea obtener de la venta del Producto.')
    # Analizar si precio_venta debe ser un atributo del Producto
    # Debe ser el ultimo definido en PrecioVentaProducto.
    # Cuando el Tipo de Producto es Insumo se debe poner en read-only este campo y dejar su valor en 0.
    precio_venta_sugerido = models.DecimalField(max_digits=18, decimal_places=0, default=0,
                                                verbose_name='Precio Venta Sugerido',
                                                help_text='Precio de Venta sugerido calculado a partir del promedio '
                                                          'del Costo de Compra del producto en el ultimo mes por el '
                                                          'Porcentaje de Ganancia.')
    perecedero = models.BooleanField(verbose_name='Es perecedero?', default=False,
                                     help_text='Marque la casilla si el Producto a registrar es Perecedero.')
    # fecha_elaboracion = models.DateField(verbose_name='Fecha de Elaboracion', default=datetime.date.today(),
    #                                      help_text='Ingrese la fecha de elaboracion del Producto.')
    # fecha_vencimiento = models.DateField(default=(datetime.date.today() + datetime.timedelta(days=30)),
    #                                      verbose_name='Fecha de Vencimiento',
    #                                      help_text='Ingrese la fecha de vencimiento del Producto.')
    costo_elaboracion = models.DecimalField(max_digits=18, decimal_places=0, default=0,
                                            verbose_name='Costo de Elaboracion del Producto',
                                            help_text='Suma de los Totales de Costo del detalle del Producto '
                                                      'Compuesto.')

    class Meta:
        # ordering =
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'

    # VALIDACIONES/FUNCIONALIDADES

    def thumb(self):
        if self.imagen:
            return mark_safe('<img src="%s" width=60 height=60 />' % self.imagen.url)
        else:
            return u'Imagen no disponible.'
    thumb.short_description = 'Vista de Imagen'

    def __init__(self, *args, **kwargs):
        self._meta.get_field('compuesto').default = False
        self._meta.get_field('costo_elaboracion').default = 0
        super(Producto, self).__init__(*args, **kwargs)

    def __unicode__(self):
        return "ID Prod: %s - Prod: %s - Marca: %s - Un. Med. Compra: %s" % (self.id, self.producto, self.marca,
                                                                             self.unidad_medida_compra)


# class PrecioVentaProducto(models.Model):
#     """
#     Registra el historico de asignaciones de Precios de Venta a los Productos.
#
#     # Mantener el historico de Precios de Venta por Producto
#     * Listar Precios de Venta de los Productos.
#     """
#     producto = models.ForeignKey('Producto')
#     fecha_precio_venta_producto = models.DateTimeField(auto_now_add=True,  # default=timezone.now(),
#                                                        verbose_name='Fecha registro Precio Venta',
#                                                        help_text='La fecha y hora se asignan automaticamente al '
#                                                                  'momento de guardar los datos del Precio de Venta '
#                                                                  'del Producto. No se requiere el ingreso de este '
#                                                                  'dato.')
#     precio_venta = models.DecimalField(max_digits=20, decimal_places=0, verbose_name='Precio Venta',
#                                        help_text='Ingrese el precio de venta del Producto.')
#     activo = models.BooleanField(default=True, help_text='Indique si este precio es el que se encuentra activo '
#                                                          'actualmente. El producto puede tener un unico precio '
#                                                          'activo.')
#
#     class Meta:
#         ordering = ('-fecha_precio_venta_producto',)
#         verbose_name = 'Producto - Precio de Venta'
#         verbose_name_plural = 'Productos - Precios de Venta'
#
#     # VALIDACIONES/FUNCIONALIDADES
#     # Validar que el Producto tenga un unico Precio de Venta como Activo.
#
#     def __unicode__(self):
#         return "%s - %s" % (self.producto, self.precio_venta)


class ProductoCompuesto(Producto):
    """
    21/06/2016: Registro de Recetas para elaboracion de comidas y tragos.

    Los Productos Compuestos o Elaborados no se suman o restan al Stock como tales, se lleva el Control de Inventario
    de los Productos que son utilizados como Insumos de estos Productos Compuestos.

    Estos Productos Compuestos poseen algunos atributos similares a los Productos registrados como Insumos o
    Para la Venta.

    El TipoProducto solo puede ser "'VE', 'Para la venta'" para los Productos Compuestos.
    El campo "compuesto" debe ser True por defecto para los Productos Compuestos.
    """

    class Meta:
        proxy = True
        verbose_name = 'Producto Compuesto o Elaborado (Receta)'
        verbose_name_plural = 'Productos - Compuestos o Elaborados (Recetas)'

    # tipo_producto = "VE"
    # compuesto = True

    # Intento de asignacion de los valores por defecto para los campos tipo_producto = "VE" y compuesto = True
    def __init__(self, *args, **kwargs):
        super(ProductoCompuesto, self).__init__(*args, **kwargs)
        # self._meta.get_field('tipo_producto').default = TipoProducto.objects.get(tipo_producto="VE")
        # self._meta.get_field('compuesto').default = True
        self.codigo_barra = "N/A"
        self.marca = "N/A"
        self.unidad_medida_compra = UnidadMedidaProducto.objects.get(unidad_medida_producto="UN")
        self.tipo_producto = TipoProducto.objects.get(tipo_producto="VE")
        # self.unidad_medida_contenido = UnidadMedidaProducto.objects.get(unidad_medida_producto="UN")
        self.contenido = 1
        self.compuesto = True
        self.perecedero = True
        # self.fecha_elaboracion = datetime.date.today()
        # self.fecha_vencimiento = datetime.date.today() + datetime.timedelta(days=3)
        self._meta.get_field('precio_venta_sugerido').help_text = 'Precio de Venta sugerido calculado a partir del ' \
                                                                  'Costo de Elaboracion por el Porcentaje de Ganancia.'

    def clean(self):
        # Valida que el porcentaje_ganancia no sea 0.
        if self.porcentaje_ganancia == 0:
            raise ValidationError({'precio_venta': _('El Porcentaje de Ganancia del Producto Compuesto o Elaborado '
                                                     'no puede ser 0.')})

    def __unicode__(self):
        return "ID Prod: %s - Prod: %s" % (self.id, self.producto)


class ProductoCompuestoDetalle(models.Model):
    producto_compuesto = models.ForeignKey('ProductoCompuesto', related_name="producto_cabecera", null=True)

    # Limitar los Productos que pueden ser seleccionados a los que poseen TipoProducto igual a Insumos.
    producto = models.ForeignKey('Producto', related_name="producto_detalle", null=True,
                                 limit_choices_to={'tipo_producto__tipo_producto': "IN"},
                                 verbose_name='Nombre del Producto',
                                 help_text='Seleccione el o los Productos que componen este Producto Compuesto.')
    cantidad_producto = models.DecimalField(max_digits=10, decimal_places=3,
                                            verbose_name='Cantidad Producto',
                                            help_text='Ingrese la cantidad del producto.')
    costo_unidad_medida = models.DecimalField(max_digits=18, decimal_places=0, default=0,
                                              verbose_name='Costo por Unidad de Medida',
                                              help_text='Corresponde al costo de 1 unidad del Producto de acuerdo '
                                                        'a su Unidad de Medida del Contenido.')
    total_costo = models.DecimalField(max_digits=18, decimal_places=0, default=0,
                                      verbose_name='Total Costo',
                                      help_text='Valor calculado entre la Cantidad del Producto por el Costo por '
                                                'Unidad de Medida del Producto.')

    class Meta:
        verbose_name = 'Producto - Detalle de Compuesto o Elaborado (Receta)'
        verbose_name_plural = 'Productos - Detalles de Compuestos o Elaborados (Recetas)'

    # VALIDACIONES/FUNCIONALIDADES
    # Validar la unidad de medida del producto

    def __unicode__(self):
        return "%s" % self.producto_compuesto

# ======================================================================================================================
# class ProductoCompuesto(models.Model):
#     """
#     21/06/2016: Registro de Recetas para elaboracion de comidas y tragos.
#
#     Los Productos Compuestos o Elaborados no se suman o restan al Stock como tales, se lleva el Control de Inventario
#     de los Productos que son utilizados como Insumos de estos Productos Compuestos.
#
#     Estos Productos Compuestos poseen algunos atributos similares a los Productos registrados como Insumos o
#     Para la Venta.
#     """
#     producto_compuesto = models.CharField(max_length=100, verbose_name='Nombre del Producto Compuesto o Elaborado',
#                                           help_text='Ingrese el nombre o descripcion del Producto Compuesto o '
#                                                     'Elaborado.')
#     # productos = models.ManyToManyField('Producto', through='RecetaDetalle')
#
#     # Analizar si un ProductoCompuesto (Receta) puede estar activo o inactivo
#     # estado = models.CharField(max_length=2)
#
#     # El TipoProducto solo puede ser "'VE', 'Para la venta'" para los Productos Compuestos
#     tipo_producto = models.ForeignKey('bar.TipoProducto', default="bar.TipoProducto.tipo_producto='VE'")
#     categoria = models.ForeignKey('bar.CategoriaProducto')
#     subcategoria = models.ForeignKey('bar.SubCategoriaProducto')
#
#     # unidad_medida_contenido = models.ForeignKey('bar.UnidadMedidaProducto', related_name='un_med_contenido',
#     #                                             verbose_name='Un. Med. Cont.')
#     # contenido = models.PositiveIntegerField(default=1)
#     # unidad_medida_comercializacion = models.ForeignKey('bar.UnidadMedidaProducto', related_name='un_med_trading',
#     #                                                    verbose_name='Un. Med. Comerc.')
#
#     fecha_alta_producto_compuesto = models.DateTimeField(auto_now_add=True,  # default=timezone.now(), editable=True,
#                                                          verbose_name='Fecha de Alta',
#                                                          help_text='La Fecha de Alta se asigna al momento de guardar '
#                                                                    'los datos del Producto. No se requiere el ingreso'
#                                                                    ' de este dato.')
#     imagen = models.ImageField(default=1)
#
#     class Meta:
#         verbose_name = 'Productos Compuestos o Elaborados (Recetas)'
#         verbose_name_plural = 'Productos Compuestos o Elaborados (Recetas)'
#
#     # VALIDACIONES/FUNCIONALIDADES
#
#     def thumb(self):
#         if self.imagen:
#             return mark_safe('<img src="%s" width=60 height=60 />' % self.imagen.url)
#         else:
#             return u'Imagen no disponible.'
#     thumb.short_description = 'Vista de Imagen'
#
#     def __unicode__(self):
#         return "%s" % self.producto_compuesto
# ======================================================================================================================


# class Stock2(models.Model):
#     """
#     21/06/2016: Registrar inventario y ajustes de inventario.
#     * Registro de los Movimientos de Inventario.
#
#     * Listar los Productos y/o Stock disponible.
#     """
#     producto_stock = models.OneToOneField('Producto', related_name='producto_stock',
#                                           verbose_name='Producto',
#                                           help_text='Seleccione el Producto a registrar en el Stock.')
#     # Manejo de stock minimo. Alertar cuando llega a este minimo.
#     stock_minimo = models.DecimalField(max_digits=10, decimal_places=3, verbose_name='Stock Minimo',
#                                        help_text='Cantidad minima del producto a mantener en Stock.')
#     cantidad_existente = models.DecimalField(max_digits=10, decimal_places=3, verbose_name='Cantidad Existente',
#                                              help_text='Cantidad existente en Stock.')
#     tipo_movimiento = models.ForeignKey('bar.TipoMovimientoStock', default=1,
#                                         verbose_name='Tipo de Movimiento',
#                                         help_text='Seleccione el identificador del Tipo de Movimiento de Stock.')
#     id_movimiento = models.PositiveIntegerField(verbose_name='ID Movimiento',  # default=1,
#                                                 help_text='Identificador del movimiento en el Stock.')
#     ubicacion_origen = models.ForeignKey('bar.Deposito', related_name='ubicacion_origen',  # default=6,
#                                          verbose_name='Ubicacion Origen',
#                                          help_text='Ubicacion desde donde se origina el movimiento de Stock.')
#     ubicacion_destino = models.ForeignKey('bar.Deposito', related_name='ubicacion_destino',  # default=1,
#                                           verbose_name='Ubicacion Destino',
#                                           help_text='Ubicacion a donde se dirige el movimiento de Stock.')
#     cantidad_entrante = models.DecimalField(max_digits=10, decimal_places=3,
#                                             verbose_name='Cantidad Entrante',
#                                             help_text='Cantidad entrante al Stock del producto.')
#     cantidad_saliente = models.DecimalField(max_digits=10, decimal_places=3,
#                                             verbose_name='Cantidad Saliente',
#                                             help_text='Cantidad saliente del Stock del producto.')
#     fecha_hora_registro_stock = models.DateTimeField(auto_now_add=True,  # default=timezone.now()
#                                                      verbose_name='Fecha/hora registro movimiento',
#                                                      help_text='La fecha y hora se asignan al momento de guardar los '
#                                                                'datos del Detalle del Stock. No se requiere el ingreso '
#                                                                'de este dato.')
#
#     class Meta:
#         # En la tabla solo puede existir un registro para cada Producto en cada Deposito
#         # Consultar si es correcto aplicar esta restriccion de esta manera
#         # 08/08/2016: Finalmente traslade el campo "ubicacion" a StockDetalle
#         # unique_together = ("producto_stock", "ubicacion")
#         verbose_name = 'Inventario de Producto'
#         verbose_name_plural = 'Productos - Inventarios'
#
#     # VALIDACIONES/FUNCIONALIDADES
#     # 1) Controlar que la cantidad_existente no sea menor que el stock_minimo y alertar en caso de ser menor.
#     # 2) Validar que la cantidad_existente no sea negativa.
#     # 3) Realizar el calculo de la cantidad_existente (suma total de cantidad_entrante - cantidad_saliente)
#     # 4) Idear una vista HTML que presente la Cantidad Total Existente del Producto.
#
#     def clean(self):
#         # 2) Valida que la cantidad_existente no sea negativa.
#         if self.cantidad_existente < 0:
#             raise ValidationError({'cantidad_existente': _('La cantidad existente del Producto no puede ser menor a '
#                                                            'cero o negativa.')})
#
#     @staticmethod
#     def verifica_estado_stock():
#         """
#         Maneja 3 estados:
#             Stock suficiente: Se asigna este estado en color Verde cuando la cantidad_existente supera al stock_minimo
#             Menor a stock minimo: Se asigna este estado en color Amarillo cuando la cantidad_existente es mayor a cero
#             e igual o menor al stock_minimo.
#             Sin stock: Se asigna este estado en color Rojo cuando la cantidad_existente es igual a cero.
#         """
#
#     def __unicode__(self):
#         return "Prod: %s - Cant. Exist: %s" % (self.producto_stock, self.cantidad_existente)
# ======================================================================================================================


class Stock(models.Model):
    """
    21/06/2016: Registrar inventario y ajustes de inventario.

    * Listar los Productos y/o Stock disponible.
    """
    producto_stock = models.OneToOneField('Producto', related_name='producto_stock',
                                          verbose_name='Producto',
                                          help_text='Seleccione el Producto a registrar en el Stock.')
    # Manejo de stock minimo. Alertar cuando llega a este minimo.
    stock_minimo = models.DecimalField(max_digits=10, decimal_places=3, verbose_name='Stock Minimo',
                                       help_text='Cantidad minima del producto a mantener en Stock.')
    cantidad_existente = models.DecimalField(max_digits=10, decimal_places=3, verbose_name='Cantidad Existente',
                                             help_text='Cantidad existente en Stock.')

    class Meta:
        # En la tabla solo puede existir un registro para cada Producto en cada Deposito
        # Consultar si es correcto aplicar esta restriccion de esta manera
        # 08/08/2016: Finalmente traslade el campo "ubicacion" a StockDetalle
        # unique_together = ("producto_stock", "ubicacion")
        verbose_name = 'Inventario de Producto'
        verbose_name_plural = 'Productos - Inventarios'

    # VALIDACIONES/FUNCIONALIDADES
    # 1) Controlar que la cantidad_existente no sea menor que el stock_minimo y alertar en caso de ser menor.
    # 2) Validar que la cantidad_existente no sea negativa.
    # 3) Realizar el calculo de la cantidad_existente (suma total de cantidad_entrante - cantidad_saliente)
    # 4) Idear una vista HTML que presente la Cantidad Total Existente del Producto.

    def clean(self):
        # 2) Valida que la cantidad_existente no sea negativa.
        if self.cantidad_existente < 0:
            raise ValidationError({'cantidad_existente': _('La cantidad existente del Producto no puede ser menor a '
                                                           'cero o negativa.')})

    @staticmethod
    def verifica_estado_stock():
        """
        Maneja 3 estados:
            Stock suficiente: Se asigna este estado en color Verde cuando la cantidad_existente supera al stock_minimo
            Menor a stock minimo: Se asigna este estado en color Amarillo cuando la cantidad_existente es mayor a cero
            e igual o menor al stock_minimo.
            Sin stock: Se asigna este estado en color Rojo cuando la cantidad_existente es igual a cero.
        """

    def __unicode__(self):
        return "Prod: %s - Cant. Exist: %s" % (self.producto_stock, self.cantidad_existente)


class StockDetalle(models.Model):
    """
    Registro de los Movimientos de Inventario.
    """
    stock = models.ForeignKey('Stock')
    tipo_movimiento = models.ForeignKey('bar.TipoMovimientoStock', default=1,
                                        verbose_name='Tipo de Movimiento',
                                        help_text='Seleccione el identificador del Tipo de Movimiento de Stock.')
    id_movimiento = models.PositiveIntegerField(verbose_name='ID Movimiento',  # default=1,
                                                help_text='Identificador del movimiento en el Stock.')
    ubicacion_origen = models.ForeignKey('bar.Deposito', related_name='ubicacion_origen',  # default=6,
                                         verbose_name='Ubicacion Origen',
                                         help_text='Ubicacion desde donde se origina el movimiento de Stock.')
    ubicacion_destino = models.ForeignKey('bar.Deposito', related_name='ubicacion_destino',  # default=1,
                                          verbose_name='Ubicacion Destino',
                                          help_text='Ubicacion a donde se dirige el movimiento de Stock.')
    cantidad_entrante = models.DecimalField(max_digits=10, decimal_places=3,
                                            verbose_name='Cantidad Entrante',
                                            help_text='Cantidad entrante al Stock del producto.')
    cantidad_saliente = models.DecimalField(max_digits=10, decimal_places=3,
                                            verbose_name='Cantidad Saliente',
                                            help_text='Cantidad saliente del Stock del producto.')
    fecha_hora_registro_stock = models.DateTimeField(auto_now_add=True,  # default=timezone.now()
                                                     verbose_name='Fecha/hora registro movimiento',
                                                     help_text='La fecha y hora se asignan al momento de guardar los '
                                                               'datos del Detalle del Stock. No se requiere el ingreso '
                                                               'de este dato.')

    class Meta:
        verbose_name = 'Detalle de Inventario del Producto'
        verbose_name_plural = 'Productos - Detalles de Inventarios'

    # def __unicode__(self):
    #     return str(self.producto) + ' - ' + str(self.marca)
# ======================================================================================================================


class StockProducto(models.Model):
    """
    Genera una vista con la agrupacion de los movimientos de Stock por Producto calculando el campo "cantidad_existente"
    """

    class Meta:
        verbose_name = 'Inventario por Producto'
        verbose_name_plural = 'Stock - Inventarios por Productos'


class StockDeposito(models.Model):
    """
    Genera una vista con la agrupacion de los movimientos de Stock por Deposito calculando el campo "cantidad_existente"
    """

    class Meta:
        verbose_name = 'Inventario por Deposito'
        verbose_name_plural = 'Stock - Inventarios por Depositos'


# ======================================================================================================================
class TransferenciaStock(models.Model):
    """
    21/06/2016: Transferir productos del Deposito Central a los Depositos Operativos.

    Las Compras ingresan totalmente al Deposito Central y a partir de ahi se transfieren a los Depositos Operativos
    segun pedidos de transferencias: Deposito Barra Principal, Deposito Barra Arriba, Cocina y Barrita.

    Estos pedidos de transferencias deben cargarse desde el Deposito solicitante y ser autorizados por el Deposito
    Central.

    Los Depositos que realizan las ventas son los Depositos Operativos exceptuando a la Cocina.
    """
    producto_transferencia = models.ForeignKey('Stock', related_name='producto_solicitado',
                                               # limit_choices_to={'cantidad_existente' > 0},
                                               limit_choices_to=Q(cantidad_existente__gt=0),
                                               verbose_name='Producto a Transferir',
                                               help_text='Seleccione el producto a Transferir entre depositos.')
    cantidad_existente_stock = models.DecimalField(max_digits=10, decimal_places=3, default=0,
                                                   verbose_name='Cantidad Existente',
                                                   help_text='Despliega la cantidad existente del Producto en el '
                                                             'Deposito Proveedor seleccionado.')
    cantidad_producto_transferencia = models.DecimalField(max_digits=10, decimal_places=3,
                                                          verbose_name='Cantidad a Transferir',
                                                          help_text='Cantidad a Transferir del producto.')
    deposito_solicitante_transferencia = models.ForeignKey('bar.Deposito', related_name='deposito_solicitante',
                                                           verbose_name='Deposito Solicitante',
                                                           help_text='Seleccione el Deposito desde donde se solicita '
                                                                     'la Transferencia.')
    # Se debe registrar el usuario del Solicitante de la Transferencia que deberia ser el usuario logueado.
    usuario_solicitante_transferencia = models.ForeignKey('personal.Empleado', related_name='usuario_solicitante',
                                                          # limit_choices_to='request.user',
                                                          to_field='usuario',
                                                          verbose_name='Usuario Solicitante',
                                                          help_text='El usuario logueado que realice la solicitud de '
                                                                    'Transferencia sera registrado automaticamente '
                                                                    'como el Solicitante.')
    deposito_proveedor_transferencia = models.ForeignKey('bar.Deposito', related_name='deposito_proveedor',
                                                         verbose_name='Deposito Proveedor',
                                                         help_text='Seleccione el Deposito que se encargara de '
                                                                   'procesar la Transferencia.')
    # Se debe registrar el usuario del Autorizante de la Transferencia que deberia ser el usuario logueado.
    usuario_autorizante_transferencia = models.ForeignKey('personal.Empleado', null=True, blank=True,
                                                          related_name='usuario_autorizante',
                                                          # limit_choices_to='',
                                                          to_field='usuario',
                                                          verbose_name='Usuario Autorizante',
                                                          help_text='El usuario logueado que autorice la solicitud de'
                                                                    ' Transferencia sera registrado automaticamente '
                                                                    'como el Autorizante.')
    estado_transferencia = models.ForeignKey('bar.TransferenciaStockEstado', default=1,
                                             verbose_name='Estado Transferencia',
                                             help_text='El estado de la Transferencia se asigna de forma automatica.')
    fecha_hora_registro_transferencia = models.DateTimeField(auto_now_add=True,
                                                             verbose_name='Fecha/hora registro Transferencia',
                                                             help_text='La fecha y hora se asignan al momento de '
                                                                       'guardar los datos de la Transferencia. No se '
                                                                       'requiere el ingreso de este dato.')

    class Meta:
        verbose_name = 'Transferencias de Productos entre Depositos'
        verbose_name_plural = 'Transferencias de Productos entre Depositos'

    # VALIDACIONES/FUNCIONALIDADES
    # 1) Al confirmarse la Transferencia se deben generar dos registros en StockDetalle, uno que reste la
    # "cantidad_producto_transferencia" del "deposito_proveedor_transferencia" y otro que sume
    # "cantidad_producto_transferencia" al "deposito_solicitante_transferencia".
    # 2) Validar que el "deposito_proveedor_transferencia" disponga de la cantidad suficiente del producto solicitado
    # para que se pueda realizar la transferencia al "deposito_solicitante_transferencia".
    # 3) Las Mermas y Devoluciones podrian ser registrados como Transferencias o Movimientos. Analizar esta
    # alternativa.

    def clean(self):
        # Valida que la cantidad_producto_transferencia no sea mayor a la cantidad_existente_stock
        if self.cantidad_producto_transferencia > self.cantidad_existente_stock:
            raise ValidationError({'cantidad_producto_transferencia': _('La cantidad solicitada a transferir no puede '
                                                                        'ser mayor que la cantidad existente del '
                                                                        'Producto.')})

    def __unicode__(self):
        return "ID: %s - Prod. Trans: %s" % (self.id, self.producto_transferencia)


class SolicitaTransferenciaStock(TransferenciaStock):
    """
    Pantalla para registrar la Solicitud de Transferencias de Productos entre Depositos.
    """

    class Meta:
        proxy = True
        verbose_name = 'Solicitud de Transferencia de Producto entre Deposito'
        verbose_name_plural = 'Stock - Transferencias de Productos entre Depositos - Solicitudes'

    # VALIDACIONES/FUNCIONALIDADES
    # 1) Al confirmarse la Transferencia se deben generar dos registros en StockDetalle, uno que reste la
    # "cantidad_producto_transferencia" del "deposito_proveedor_transferencia" y otro que sume
    # "cantidad_producto_transferencia" al "deposito_solicitante_transferencia".
    # 2) Validar que el "deposito_proveedor_transferencia" disponga de la cantidad suficiente del producto solicitado
    # para que se pueda realizar la transferencia al "deposito_solicitante_transferencia".
    # 3) Las Mermas y Devoluciones podrian ser registrados como Transferencias o Movimientos. Analizar esta
    # alternativa.

    def __init__(self, *args, **kwargs):
        super(SolicitaTransferenciaStock, self).__init__(*args, **kwargs)
        self.estado_transferencia = TransferenciaStockEstado.objects.get(estado_transferencia_stock="PEN")
        # self.usuario_autorizante_transferencia = Empleado.objects.get(usuario__username='admin')

    def __unicode__(self):
        return "ID: %s - Prod. Trans: %s" % (self.id, self.producto_transferencia)


class ConfirmaTransferenciaStock(TransferenciaStock):
    """
    Pantalla para registrar la Confirmacion de Transferencias de Productos entre Depositos.
    """

    class Meta:
        proxy = True
        verbose_name = 'Confirmacion de Transferencia de Producto entre Deposito'
        verbose_name_plural = 'Stock - Transferencias de Productos entre Depositos - Confirmaciones'

    # VALIDACIONES/FUNCIONALIDADES
    # 1) Al confirmarse la Transferencia se deben generar dos registros en StockDetalle, uno que reste la
    # "cantidad_producto_transferencia" del "deposito_proveedor_transferencia" y otro que sume
    # "cantidad_producto_transferencia" al "deposito_solicitante_transferencia".
    # 2) Validar que el "deposito_proveedor_transferencia" disponga de la cantidad suficiente del producto solicitado
    # para que se pueda realizar la transferencia al "deposito_solicitante_transferencia".
    # 3) Las Mermas y Devoluciones podrian ser registrados como Transferencias o Movimientos. Analizar esta
    # alternativa.

    def clean(self):
        # Valida que el usuario_autorizante_transferencia no sea vacio o nulo, esta condicion no deberia darse ya que
        # este campo se completa con el dato del usuario logueado al Sistema al momento de confirmar la transferencia.
        if self.usuario_autorizante_transferencia is None:
            raise ValidationError({'usuario_autorizante_transferencia': _('Se debe seleccionar el Usuario Autorizante '
                                                                          'de la Transferencia que debe ser el usuario '
                                                                          'logueado al Sistema.')})

    def __unicode__(self):
        return "ID: %s - Prod. Trans: %s" % (self.id, self.producto_transferencia)
# ======================================================================================================================


# class Mermas(models.Model):
#     """
#     21/06/2016: Registrar mermas de productos. Las mermas descuentan el stock existente.
#     """


class Devolucion(models.Model):
    """
    Cuando la Compra llega a los estados de CON o CAN ya no puede volver a ser modificada.
    En el caso de que una Compra confirmada deba ser devuelta se debe registrar el proceso en el modelo de
    Devoluciones.
    """

    class Meta:
        verbose_name = 'Stock - Devolucion'
        verbose_name_plural = 'Stock - Devoluciones'