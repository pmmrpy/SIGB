# coding=utf-8
from django.db import models
from django.utils import timezone

# Create your models here.


class ReservaEstado(models.Model):
    reserva_estado = models.CharField(max_length=1)
    descripcion = models.CharField(max_length=50)
    #     choices=(
    #     ('V', 'Vigente'),
    #     ('C', 'Caducada'),
    # ),

    class Meta:
        verbose_name = 'Reserva - Estado'
        verbose_name_plural = 'Reservas - Estados'

    def __unicode__(self):
        return self.reserva_estado + ' - ' + self.descripcion


class Mesa(models.Model):
    # id = models.AutoField("mesa_id", primary_key=True)
    nombre = models.CharField(max_length=20)
    ubicacion = models.ForeignKey('MesaUbicacion')
    estado = models.ForeignKey('MesaEstado')

    def __unicode__(self):
        return self.nombre


class MesaEstado(models.Model):
    mesa_estado = models.CharField(max_length=3)
    descripcion = models.CharField(max_length=50)
    #    choices=(
    #     ('A', 'Activa'),
    #     ('I', 'Inactiva'),
    #     ('O', 'Ocupada'),
    #     ('D', 'Disponible'),
    # ),

    class Meta:
        verbose_name = 'Mesa - Estado'
        verbose_name_plural = 'Mesas - Estados'

    def __unicode__(self):
        return self.mesa_estado + ' - ' + self.descripcion


class MesaUbicacion(models.Model):
    ubicacion = models.CharField(max_length=30)
    descripcion = models.CharField(max_length=50)

    class Meta:
        verbose_name = 'Mesa - Ubicacion'
        verbose_name_plural = 'Mesas - Ubicaciones'

    def __unicode__(self):
        return self.ubicacion


class Caja(models.Model):
    numero = models.IntegerField()
    ubicacion = models.ForeignKey('CajaUbicacion')
    estado = models.ForeignKey('CajaEstado')

    def __unicode__(self):
        return str(self.numero) + ' - ' + str(self.ubicacion)


class CajaEstado(models.Model):
    caja_estado = models.CharField(max_length=3)
    descripcion = models.CharField(max_length=50)
    #    choices=(
    #     ('A', 'Abierta'),
    #     ('C', 'Cerrada'),
    # ),

    class Meta:
        verbose_name = 'Caja - Estado'
        verbose_name_plural = 'Cajas - Estados'

    def __unicode__(self):
        return self.caja_estado + ' - ' + self.descripcion


class CajaUbicacion(models.Model):
    ubicacion = models.CharField(max_length=30)
    #     choices=(
    #     ('DC', 'Deposito Central'),
    #     ('DO', 'Deposito Operativo'),
    # ),
    descripcion = models.CharField(max_length=50)

    class Meta:
        verbose_name = 'Caja - Ubicacion'
        verbose_name_plural = 'Cajas - Ubicaciones'

    def __unicode__(self):
        return self.ubicacion


class Documento(models.Model):
    # id = models.AutoField(primary_key=True)
    documento = models.CharField(max_length=3)
    #     choices=(
    #     ('CI', 'Cedula de Identidad'),
    #     ('RUC', 'Registro Unico del Contribuyente'),
    #     ('P', 'Pasaporte'),
    #     ('RC', 'Registro de Conducir'),
    # ),
    descripcion = models.CharField(max_length=50)

    def __unicode__(self):
        # return self.documento
        return str(self.documento) + ' - ' + str(self.descripcion)


class FormaPagoVenta(models.Model):
    forma_pago_venta = models.CharField(max_length=50, help_text='Contado / TC / TD')

    class Meta:
        verbose_name = 'Forma de Pago - Venta'
        verbose_name_plural = 'Formas de Pago - Venta'

    def __unicode__(self):
        return self.forma_pago_venta


class FormaPagoCompra(models.Model):
    forma_pago_compra = models.CharField(max_length=50, help_text='Contado / Credito')
    plazo_compra = models.IntegerField(help_text='En caso de Credito establecer el plazo de tiempo en días para el '
                                                 'pago.')

    class Meta:
        verbose_name = 'Forma de Pago - Compra'
        verbose_name_plural = 'Formas de Pago - Compra'

    def __unicode__(self):
        return self.forma_pago_compra + ' - ' + str(self.plazo_compra)  # + ' días.'


class TipoDeposito(models.Model):
    tipo_deposito = models.CharField(max_length=2)
    #     choices=(
    #     ('DC', 'Deposito Central'),
    #     ('DO', 'Deposito Operativo'),
    # ),
    descripcion = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'Deposito - Tipo'
        verbose_name_plural = 'Depositos - Tipos'

    def __unicode__(self):
        return self.descripcion


class CategoriaProducto(models.Model):
    categoria = models.CharField(max_length=2)
    #     choices=(
    #     ('BE', 'Bebidas'),
    #     ('CO', 'Comidas'),
    #     ('CI', 'Cigarrillos'),
    # ),
    descripcion = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'Producto - Categoria'
        verbose_name_plural = 'Productos - Categorias'

    def __unicode__(self):
        return self.descripcion


class TipoProducto(models.Model):
    tipo_producto = models.CharField(max_length=2)
    #     choices=(
    #     ('SF', 'Sin Fraccionar'),
    #     ('FR', 'Fraccionados'),
    #     ('PR', 'Preparados'), # Los tragos y las comidas entrarían en esta categoria, deben tener una receta asociada
    #
    #     ('CO', 'Compuesto'), # Los tragos y las comidas entrarían en esta categoria, deben tener una receta asociada
    #     ('VE', 'Para la venta'),
    #     ('IN', 'Insumos'),
    # ),
    descripcion = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'Producto - Tipo'
        verbose_name_plural = 'Productos - Tipos'

    def __unicode__(self):
        return self.descripcion


class Moneda(models.Model):
    codigo_moneda = models.IntegerField(help_text='Corresponde al codigo internacional de la moneda. EJ: Gs - 600')
    moneda = models.CharField(max_length=100, help_text='Nombre de la moneda.')
    abreviacion_moneda = models.CharField(default='US$', max_length=5, help_text='Abreviacion o simbolo '
                                                                                 'de la moneda. EJ: Guaranies - Gs.')

    def __unicode__(self):
        return str(self.codigo_moneda) + ' - ' + str(self.abreviacion_moneda)


class Cotizacion(models.Model):
    moneda = models.ForeignKey('Moneda', help_text='Seleccione la moneda para la cual definir su cotizacion.')
    fecha_cotizacion = models.DateTimeField(default=timezone.now(), help_text='Registra la fecha en la '
                                                                              'que se definio la cotizacion. '
                                                                              'Corresponde a la fecha y hora actual.')
    cotizacion = models.DecimalField(max_digits=20, decimal_places=2, help_text='Ingrese cotizacion.')

    class Meta:
        verbose_name = 'Cotizacion'
        verbose_name_plural = 'Cotizaciones'

    def __unicode__(self):
        return str(self.moneda) + ' - ' + str(self.fecha_cotizacion)


class CodigoPaisTelefono(models.Model):
    codigo_pais_telefono = models.IntegerField(verbose_name='Codigo Pais', help_text='Codigo internacional del pais al '
                                                                                     'cual corresponde el telefono.')
    pais = models.CharField(max_length=100, help_text='Pais al cual corresponde el codigo.')

    class Meta:
        verbose_name = 'Telefono - Codigo intern. por pais'
        verbose_name_plural = 'Telefonos - Codigos intern. por pais'

    def __unicode__(self):
        return str(self.codigo_pais_telefono) + ' - ' + str(self.pais)


class CodigoCiudadOperadoraTelefono(models.Model):
    codigo_pais_telefono = models.ForeignKey('CodigoPaisTelefono')
    codigo_ciudad_operadora_telefono = models.IntegerField(default=21, verbose_name='Codigo Ciudad/Operadora',
                                                           help_text='Codigo de ciudad o de la operadora de telefonia'
                                                                     ' movil.')
    ciudad_operadora = models.CharField(max_length=100, verbose_name='Descripcion Ciudad/Operadora',
                                        help_text='Descripcion de la ciudad o de la operadora de telefonia movil.')

    class Meta:
        verbose_name = 'Telefono - Codigo por ciudad/operadora'
        verbose_name_plural = 'Telefonos - Codigos por ciudad/operadora'

    def __unicode__(self):
        return str(self.codigo_ciudad_operadora_telefono) + ' - ' + str(self.ciudad_operadora)


class Pais(models.Model):
    pais = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'Pais'
        verbose_name_plural = 'Paises'

    def __unicode__(self):
        return self.pais


class Ciudad(models.Model):
    pais = models.ForeignKey('Pais')
    ciudad = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'Ciudad'
        verbose_name_plural = 'Ciudades'

    def __unicode__(self):
        return self.ciudad