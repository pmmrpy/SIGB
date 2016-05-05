from django.db import models
from django.utils import timezone

# Create your models here.


class Producto(models.Model):
    producto = models.CharField(max_length=100)
    codigo_barra = models.CharField(max_length=100)
    marca = models.CharField(max_length=100)

#   cantidad_stock = models.DecimalField(max_digits=20, decimal_places=2)
#   Analizar si debe estar en los atributos del Producto

    tipo_producto = models.ForeignKey('bar.TipoProducto', default=1)
    categoria = models.ForeignKey('bar.CategoriaProducto')
    unidad_medida = models.ForeignKey('UnidadMedida')
    contenido = models.IntegerField(default=1)
    imagen = models.ImageField(default=1)
    # precio_venta = models.ForeignKey('PrecioProducto', related_name='precio')
    # Debe ser el ultimo definido en PrecioProducto. \
    # Analizar si debe ser un atributo del Producto

    def __unicode__(self):
        return str(self.producto) + ' - ' + str(self.marca)


# Mantener el historico de precios de venta por producto
class PrecioProducto(models.Model):
    producto = models.ForeignKey('Producto')
    fecha = models.DateTimeField(default=timezone.now(), help_text='Ingrese la fecha y hora en la que se define el '
                                                                   'precio de venta del producto.')
    precio_venta = models.DecimalField(max_digits=20, decimal_places=2, help_text='Ingrese el precio de venta del '
                                                                                  'producto.')
    activo = models.BooleanField(default=True, help_text='Indique si este precio es el que se encuentra activo '
                                                         'actualmente. El producto puede tener un unico precio activo.')

    class Meta:
        verbose_name = 'Producto - Precio'
        verbose_name_plural = 'Productos - Precios'

    def __unicode__(self):
        return self.producto + ' - ' + str(self.precio_venta)


class UnidadMedida(models.Model):
    unidad_medida = models.CharField(max_length=2)
    #     choices=(
    #     ('UN', 'Unidad'),
    #     ('ML', 'Mililitros'),
    #     ('LI', 'Litros'),
    #     ('GR', 'Gramos'),
    #     ('KG', 'Kilogramos'),
    # ),
    descripcion = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'Producto - Unidad de Medida'
        verbose_name_plural = 'Productos - Unidades de Medida'

    def __unicode__(self):
        return self.descripcion


class Receta(models.Model):
    receta = models.CharField(max_length=100)
    productos = models.ManyToManyField('Producto', through='RecetaDetalle')
    estado = models.CharField(max_length=2)  # Analizar si una receta puede estar activa o inactiva

    def __unicode__(self):
        return self.receta + ' - ' + self.estado


# Validar la unidad de medida del producto
class RecetaDetalle(models.Model):
    receta = models.ForeignKey('Receta')
    producto = models.ForeignKey('Producto')
    cantidad_producto = models.DecimalField(max_digits=20, decimal_places=2)

    class Meta:
        verbose_name = 'Receta - Detalle'
        verbose_name_plural = 'Recetas - Detalles'

    def __unicode__(self):
        return str(self.receta)


class Deposito(models.Model):
    deposito = models.CharField(max_length=3)
    #     choices=(
    #     ('DCE', 'Deposito Central'),
    #     ('DBP', 'Deposito Barra Principal'),
    #     ('DBA', 'Deposito Barra Arriba'),
    #     ('DCO', 'Deposito Cocina'),
    #     ('DBI', 'Deposito Barrita'),
    # ),
    descripcion = models.CharField(max_length=100)
    tipo_deposito = models.ForeignKey('bar.TipoDeposito')

    def __unicode__(self):
        return str(self.deposito) + ' - ' + str(self.descripcion)
