from django.db import models
from django.utils import timezone
from django.utils.safestring import mark_safe

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
    codigo_barra = models.CharField(max_length=100, verbose_name='Codigo de Barra', blank=True,
                                    help_text='Ingrese el codigo de barra del Producto si posee.')
    marca = models.CharField(max_length=100, verbose_name='Marca',
                             help_text='Ingrese la marca del Producto.')
    tipo_producto = models.ForeignKey('bar.TipoProducto')
    categoria = models.ForeignKey('bar.CategoriaProducto')
    subcategoria = models.ForeignKey('bar.SubCategoriaProducto')
    unidad_medida_contenido = models.ForeignKey('bar.UnidadMedidaProducto', related_name='un_med_contenido',
                                                verbose_name='Unidad Medida Contenido')
    contenido = models.PositiveIntegerField(default=1)
    unidad_medida_compra = models.ForeignKey('bar.UnidadMedidaProducto', related_name='un_med_trading',
                                             verbose_name='Unidad Medida Compra', default=1)
    imagen = models.ImageField(upload_to='stock/productos/', verbose_name='Archivo de Imagen',
                               help_text='Seleccione el archivo con la imagen del Producto.')
    fecha_alta_producto = models.DateTimeField(auto_now_add=True, editable=True,  # default=timezone.now(),
                                               verbose_name='Fecha de Alta',
                                               help_text='La Fecha de Alta se asigna al momento de guardar los datos '
                                                         'del Producto. No se requiere el ingreso de este dato.')

    # precio_venta = models.ForeignKey('PrecioProducto', related_name='precio')
    # Debe ser el ultimo definido en PrecioProducto. \
    # Analizar si debe ser un atributo del Producto

    def thumb(self):
        if self.imagen:
            return mark_safe('<img src="%s" width=60 height=60 />' % self.imagen.url)
        else:
            return u'Imagen no disponible.'
    thumb.short_description = 'Vista de Imagen'

    def __unicode__(self):
        return "%s - %s" % (self.producto, self.marca)


# Mantener el historico de precios de venta por producto
class PrecioProducto(models.Model):
    """
    Registra el historico de asignaciones de Precios de Venta a los Productos.

    * Listar precios de venta de los productos.
    """
    producto = models.ForeignKey('Producto')
    fecha_precio_producto = models.DateTimeField(default=timezone.now(),
                                                 help_text='Ingrese la fecha y hora en la que se define el '
                                                           'precio de venta del producto.')
    precio_venta = models.DecimalField(max_digits=20, decimal_places=0, help_text='Ingrese el precio de venta del '
                                                                                  'producto.')
    activo = models.BooleanField(default=True, help_text='Indique si este precio es el que se encuentra activo '
                                                         'actualmente. El producto puede tener un unico precio activo.')

    class Meta:
        ordering = ('-fecha_precio_producto',)
        verbose_name = 'Producto - Precio de Venta'
        verbose_name_plural = 'Productos - Precios de Venta'

    def __unicode__(self):
        return "%s - %s" % (self.producto, self.precio_venta)


# class Receta(models.Model):
#     """
#     21/06/2016: Registro de Recetas para elaboracion de comidas y tragos.
#
#     Los Productos Compuestos o Elaborados no se suman o restan al Stock como tales, se lleva el Control de Inventario
#     de los Productos que son utilizados como Insumos de estos Productos Compuestos.
#
#     Estos Productos Compuestos poseen algunos atributos similares a los Productos registrados como Insumos o
#     Para la Venta.
#     """
#     producto_compuesto = models.CharField(max_length=100)
#     # productos = models.ManyToManyField('Producto', through='RecetaDetalle')
#     # Analizar si una receta puede estar activa o inactiva
#     # estado = models.CharField(max_length=2)
#     tipo_producto = models.ForeignKey('bar.TipoProducto')
#     categoria = models.ForeignKey('bar.CategoriaProducto')
#     subcategoria = models.ForeignKey('bar.SubCategoriaProducto')
#     unidad_medida_contenido = models.ForeignKey('bar.UnidadMedidaProducto', related_name='un_med_contenido',
#                                                 verbose_name='Un. Med. Cont.')
#     contenido = models.PositiveIntegerField(default=1)
#     unidad_medida_comercializacion = models.ForeignKey('bar.UnidadMedidaProducto', related_name='un_med_trading',
#                                                        verbose_name='Un. Med. Comerc.')
#     imagen = models.ImageField(default=1)
#     fecha_alta_producto = models.DateTimeField(default=timezone.now(),  # auto_now_add=True, editable=True,
#                                                verbose_name='Fecha de Alta',
#                                                help_text='La Fecha de Alta se asigna al momento de guardar los datos '
#                                                          'del Producto. No se requiere el ingreso de este dato.')
#
#     class Meta:
#         verbose_name = 'Productos Compuestos o Elaborados (Recetas)'
#         verbose_name_plural = 'Productos Compuestos o Elaborados (Recetas)'
#
#     def __unicode__(self):
#         return "%s - %s" % (self.receta, self.estado)
#
#
# # Validar la unidad de medida del producto
# class RecetaDetalle(models.Model):
#     receta = models.ForeignKey('Receta')
#     producto = models.ForeignKey('Producto')
#     cantidad_producto = models.DecimalField(max_digits=20, decimal_places=2)
#
#     class Meta:
#         verbose_name = 'Receta - Detalle'
#         verbose_name_plural = 'Recetas - Detalles'
#
#     def __unicode__(self):
#         return "%s" % self.receta


class Stock(models.Model):
    """
    21/06/2016: Registrar inventario y ajustes de inventario.

    * Listar los Productos y/o Stock disponible.
    """
    producto_stock = models.ForeignKey(Producto, related_name='producto_stock', verbose_name='Producto')
    ubicacion = models.ForeignKey('bar.Deposito', help_text='Ubicacion del Stock.')
    # Manejo de stock minimo. Alertar cuando llega a este minimo.
    stock_minimo = models.DecimalField(max_digits=10, decimal_places=3, verbose_name='Stock Minimo',
                                       help_text='Cantidad minima del producto a mantener en Stock.')
    cantidad_existente = models.DecimalField(max_digits=10, decimal_places=3, verbose_name='Cantidad Existente',
                                             help_text='Cantidad existente en Stock.')
    cantidad_entrante = models.DecimalField(max_digits=10, decimal_places=3, verbose_name='Cantidad Entrante',
                                            help_text='Cantidad entrante al Stock del producto.')
    cantidad_saliente = models.DecimalField(max_digits=10, decimal_places=3, verbose_name='Cantidad Saliente',
                                            help_text='Cantidad saliente del Stock del producto.')
    fecha_hora_registro_stock = models.DateTimeField(default=timezone.now(), verbose_name='Fecha y hora de registro',
                                                     help_text='Fecha y hora de registro en el Stock.')

    class Meta:
        # En la tabla solo puede existir un registro para cada Producto en cada Deposito
        # Consultar si es correcto aplicar esta restriccion de esta manera
        unique_together = ("producto_stock", "ubicacion")
        verbose_name = 'Inventario de Productos'
        verbose_name_plural = 'Inventario de Productos'

    # def __unicode__(self):
    #     return str(self.producto) + ' - ' + str(self.marca)


# class Transferencia(models.Model):
#     """
#     21/06/2016: Transferir productos del Deposito Central a los Depositos Operativos.
#
#     Las Compras ingresan totalmente al Deposito Central y a partir de ahi se transfieren a los Depositos Operativos
#     segun pedidos de transferencias: Deposito Barra Principal, Deposito Barra Arriba, Cocina y Barrita.
#
#     Estos pedidos de transferencias deben cargarse desde el Deposito solicitante y ser autorizados por el Deposito
#     Central.
#
#     Los Depositos que realizan las ventas son los Depositos Operativos exceptuando a la Cocina.
#     """


# class Mermas(models.Model):
#     """
#     21/06/2016: Registrar mermas de productos. Las mermas descuentan el stock existente.
#     """


# class Devolucion(models.Model):
#     """
#     Cuando la Compra llega a los estados de CON o CAN ya no puede volver a ser modificada.
#     En el caso de que una Compra confirmada deba ser devuelta se debe registrar el proceso en el modelo de
#     Devoluciones.
#     """
