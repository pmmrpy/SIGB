from django.db import models
from django.utils import timezone
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
from django.utils.safestring import mark_safe
from bar.models import TipoProducto, UnidadMedidaProducto

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
    unidad_medida_contenido = models.ForeignKey('bar.UnidadMedidaProducto', related_name='un_med_contenido',  # default=1,
                                                verbose_name='Unidad de Medida Contenido')
    contenido = models.DecimalField(max_digits=10, decimal_places=3,  # default=0,
                                    verbose_name='Cantidad del Contenido',
                                    help_text='Ingrese el Contenido del producto de acuerdo a su Unidad de Medida.')
    compuesto = models.BooleanField(verbose_name='Es compuesto?',  # default=False,
                                    help_text='Marque la casilla si el Producto es Compuesto.')

    # Analizar si debe ser un atributo del Producto
    # Debe ser el ultimo definido en PrecioVentaProducto.
    # Cuando el Tipo de Producto es Insumo se debe poner en read-only este campo y dejar su valor en 0.
    precio_venta = models.DecimalField(max_digits=18, decimal_places=0,  # default=1,
                                       verbose_name='Precio Venta',
                                       help_text='Ingrese el Precio de Venta del Producto.')

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
        verbose_name = 'Producto - Compuesto o Elaborado (Receta)'
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
        self.unidad_medida_contenido = UnidadMedidaProducto.objects.get(unidad_medida_producto="UN")
        self.contenido = 1
        self.compuesto = True

    def clean(self):
        # Valida que el precio_venta no sea 0.
        if self.precio_venta == 0:
            raise ValidationError({'precio_venta': _('El Precio de Venta del Producto Compuesto o Elaborado no puede '
                                                     'ser 0.')})

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
        verbose_name = 'Producto - Inventario'
        verbose_name_plural = 'Productos - Inventarios'

    # VALIDACIONES/FUNCIONALIDADES
    # 1) Controlar que la cantidad_existente no sea menor que el stock_minimo y alertar en caso de ser menor.
    # 2) Validar que la cantidad_existente no sea negativa.
    # 3) Realizar el calculo de la cantidad_existente (suma total de cantidad_entrante - cantidad_saliente)
    # 4) Idear una vista HTML que presente la Cantidad Total Existente del Producto.

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
    ubicacion = models.ForeignKey('bar.Deposito', help_text='Ubicacion del Stock.')
    cantidad_entrante = models.DecimalField(max_digits=10, decimal_places=3, verbose_name='Cantidad Entrante',
                                            help_text='Cantidad entrante al Stock del producto.')
    cantidad_saliente = models.DecimalField(max_digits=10, decimal_places=3, verbose_name='Cantidad Saliente',
                                            help_text='Cantidad saliente del Stock del producto.')
    fecha_hora_registro_stock = models.DateTimeField(auto_now_add=True,  # default=timezone.now()
                                                     verbose_name='Fecha/hora registro movimiento',
                                                     help_text='La fecha y hora se asignan al momento de guardar los '
                                                               'datos del Detalle del Stock. No se requiere el ingreso '
                                                               'de este dato.')

    class Meta:
        verbose_name = 'Producto - Detalle de Inventario'
        verbose_name_plural = 'Productos - Detalles de Inventarios'

    # def __unicode__(self):
    #     return str(self.producto) + ' - ' + str(self.marca)


# ======================================================================================================================
class SolicitaTransferenciaStock(models.Model):
    """
    21/06/2016: Transferir productos del Deposito Central a los Depositos Operativos.

    Las Compras ingresan totalmente al Deposito Central y a partir de ahi se transfieren a los Depositos Operativos
    segun pedidos de transferencias: Deposito Barra Principal, Deposito Barra Arriba, Cocina y Barrita.

    Estos pedidos de transferencias deben cargarse desde el Deposito solicitante y ser autorizados por el Deposito
    Central.

    Los Depositos que realizan las ventas son los Depositos Operativos exceptuando a la Cocina.
    """
    producto_transferencia = models.ForeignKey('Producto', related_name='producto_transferencia',
                                               verbose_name='Producto a Transferir',
                                               help_text='Seleccione el producto a Transferir entre depositos.')
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
                                                          verbose_name='Usuario Solicitante',
                                                          help_text='El usuario logueado que realice la solicitud de '
                                                                    'Transferencia sera registrado automaticamente '
                                                                    'como el Solicitante.')
    deposito_proveedor_transferencia = models.ForeignKey('bar.Deposito', related_name='deposito_proveedor',
                                                         verbose_name='Deposito Proveedor',
                                                         help_text='Seleccione el Deposito que se encargara de '
                                                                   'procesar la Transferencia.')
    usuario_autorizante_transferencia = models.ForeignKey('personal.Empleado', related_name='usuario_autorizante',
                                                          # limit_choices_to='',
                                                          verbose_name='Usuario Autorizante',
                                                          help_text='El usuario logueado que autorice la solicitud de'
                                                                    ' Transferencia sera registrado automaticamente '
                                                                    'como el Autorizante.')
    estado_transferencia = models.ForeignKey('bar.TransferenciaStockEstado')
    fecha_hora_registro_transferencia = models.DateTimeField(auto_now_add=True,
                                                             verbose_name='Fecha/hora registro transferencia',
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

    def __unicode__(self):
        return "ID: %s - Prod. Trans: %s" % (self.id, self.producto_transferencia)


class ConfirmaTransferenciaStock(models.Model):
    """
    21/06/2016: Transferir productos del Deposito Central a los Depositos Operativos.

    Las Compras ingresan totalmente al Deposito Central y a partir de ahi se transfieren a los Depositos Operativos
    segun pedidos de transferencias: Deposito Barra Principal, Deposito Barra Arriba, Cocina y Barrita.

    Estos pedidos de transferencias deben cargarse desde el Deposito solicitante y ser autorizados por el Deposito
    Central.

    Los Depositos que realizan las ventas son los Depositos Operativos exceptuando a la Cocina.
    """
    producto_transferencia = models.ForeignKey('Producto', related_name='producto_transferencia',
                                               verbose_name='Producto a Transferir',
                                               help_text='Seleccione el producto a Transferir entre depositos.')
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
                                                          verbose_name='Usuario Solicitante',
                                                          help_text='El usuario logueado que realice la solicitud de '
                                                                    'Transferencia sera registrado automaticamente '
                                                                    'como el Solicitante.')
    deposito_proveedor_transferencia = models.ForeignKey('bar.Deposito', related_name='deposito_proveedor',
                                                         verbose_name='Deposito Proveedor',
                                                         help_text='Seleccione el Deposito que se encargara de '
                                                                   'procesar la Transferencia.')
    usuario_autorizante_transferencia = models.ForeignKey('personal.Empleado', related_name='usuario_autorizante',
                                                          # limit_choices_to='',
                                                          verbose_name='Usuario Autorizante',
                                                          help_text='El usuario logueado que autorice la solicitud de'
                                                                    ' Transferencia sera registrado automaticamente '
                                                                    'como el Autorizante.')
    estado_transferencia = models.ForeignKey('bar.TransferenciaStockEstado')
    fecha_hora_registro_transferencia = models.DateTimeField(auto_now_add=True,
                                                             verbose_name='Fecha/hora registro transferencia',
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