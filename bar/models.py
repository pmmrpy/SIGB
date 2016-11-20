# coding=utf-8
import datetime
from django.db import models
from django.utils import timezone
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _

# Create your models here.


class ReservaEstado(models.Model):
    """
    Diversos ESTADOS que puede tener una Reserva.
    """
    ESTADOS_RESERVA = (
        ('VIG', 'Vigente'),
        ('CAD', 'Caducada'),
        ('UTI', 'Utilizada'),
        ('CAN', 'Cancelada'),
    )
    reserva_estado = models.CharField(max_length=3, choices=ESTADOS_RESERVA, verbose_name='Estado de la Reserva',
                                      help_text='Ingrese el identificador del Estado de la Reserva. '
                                                '(Hasta 2 caracteres)')
    descripcion = models.CharField(max_length=200, verbose_name='Descripcion del Estado',
                                   help_text='Ingrese la descripcion del Estado de la Reserva. (Hasta 200 caracteres)')

    class Meta:
        ordering = ('id',)
        verbose_name = 'Reserva - Estado'
        verbose_name_plural = 'Reservas - Estados'

    # VALIDACIONES/FUNCIONALIDADES
    # 1)

    def __unicode__(self):
        return "%s" % (self.get_reserva_estado_display())


class Mesa(models.Model):
    """
    Registra datos de las Mesas habilitadas en el bar.
    """
    # id = models.AutoField("mesa_id", primary_key=True)
    nombre_mesa = models.CharField(max_length=20, verbose_name='Mesa', default='Mesa',
                                   help_text='Ingrese el nombre o descripcion de la Mesa. (Hasta 20 caracteres)')
    numero_mesa = models.PositiveIntegerField(verbose_name='Numero de Mesa', unique=True,
                                              help_text='Ingrese el Numero de Mesa.')
    sector = models.ForeignKey('Sector', default=2)
    ubicacion = models.ForeignKey('MesaUbicacion')
    estado = models.ForeignKey('MesaEstado')
    utilizada_por_numero_pedido = models.PositiveIntegerField(null=True, blank=True,
                                                              verbose_name='Utilizada por Nro. de Pedido')

    class Meta:
        verbose_name = 'Mesa'
        verbose_name_plural = 'Mesas'

    def __unicode__(self):
        return "Nro. Mesa: %s - %s - %s" % (self.numero_mesa, self.sector, self.ubicacion)


class MesaEstado(models.Model):
    """
    Diversos ESTADOS que puede tener una Mesa.
    """
    ESTADOS_MESA = (
        ('AC', 'Activa'),
        ('IN', 'Inactiva'),
        ('OC', 'Ocupada'),
        ('DI', 'Disponible'),
    )
    mesa_estado = models.CharField(max_length=2, choices=ESTADOS_MESA, verbose_name='Estado de la Mesa',
                                   help_text='Ingrese el identificador del Estado de la Mesa. (Hasta 2 caracteres)')
    descripcion = models.CharField(max_length=200, verbose_name='Descripcion del Estado',
                                   help_text='Ingrese la descripcion del Estado de la Mesa. (Hasta 200 caracteres)')

    class Meta:
        verbose_name = 'Mesa - Estado'
        verbose_name_plural = 'Mesas - Estados'

    def __unicode__(self):
        return "%s" % (self.get_mesa_estado_display())


class MesaUbicacion(models.Model):
    """
    Registra las ubicaciones de Mesas.
    """
    mesa_ubicacion = models.CharField(max_length=30, verbose_name='Ubicacion de la Mesa',
                                      help_text='Ingrese un nombre o identificador de la ubicacion de la Mesa. '
                                                '(Hasta 30 caracteres)')
    descripcion = models.CharField(max_length=100, verbose_name='Descripcion de la Ubicacion',
                                   help_text='Ingrese la descripcion de la Ubicacion de la Mesa. (Hasta 100 '
                                             'caracteres)')

    class Meta:
        verbose_name = 'Mesa - Ubicacion'
        verbose_name_plural = 'Mesas - Ubicaciones'

    def __unicode__(self):
        return "%s" % self.mesa_ubicacion


class Caja(models.Model):
    """
    Datos de las Cajas.
    """
    ESTADOS_CAJA = (
        ('ABI', 'Abierta'),
        ('CER', 'Cerrada'),
        ('CLA', 'Clausurada')
    )
    numero_caja = models.PositiveIntegerField(verbose_name='Numero de Caja', unique=True,
                                              help_text='Ingrese el Numero de Caja.')
    # ubicacion = models.ForeignKey('CajaUbicacion')
    sector = models.ForeignKey('Sector')  # default=2
    punto_expedicion = models.CharField(max_length=3, default="001",
                                        verbose_name='Punto de Expedicion',
                                        help_text='Ingrese el Punto de Expedicion.')
    marca = models.CharField(max_length=50, default="PC Standard",
                             verbose_name='Marca',
                             help_text='Ingrese la marca de la Caja.')
    modelo_fabricacion = models.CharField(max_length=100, default="PC Standard Proc. Intel - 4 GBs de RAM",
                                          verbose_name='Modelo de Fabricacion',
                                          help_text='Ingrese el modelo de fabricacion de la Caja.')
    numero_serie = models.CharField(max_length=20, default="1234567890",
                                    verbose_name='Numero de Serie',
                                    help_text='Ingrese el numero de serie de la Caja.')
    estado_caja = models.CharField(max_length=3, choices=ESTADOS_CAJA, default='CER',
                                   verbose_name='Estado Caja',
                                   help_text='Seleccione el identificador del Estado de la Caja.')

    class Meta:
        verbose_name = 'Caja'
        verbose_name_plural = 'Cajas'

    def __unicode__(self):
        return "Nro. Caja: %s - %s" % (self.numero_caja, self.sector)


# class CajaEstado(models.Model):
#     """
#     Diversos ESTADOS que puede tener una Caja.
#     """
#     ESTADOS_CAJA = (
#         ('AB', 'Abierta'),
#         ('CE', 'Cerrada'),
#         ('CL', 'Clausurada')
#     )
#     caja_estado = models.CharField(max_length=2, choices=ESTADOS_CAJA, verbose_name='Estado de la Caja',
#                                    help_text='Ingrese el identificador del Estado de la Caja. (Hasta 2 caracteres')
#     descripcion = models.CharField(max_length=200, verbose_name='Descripcion del Estado',
#                                    help_text='Ingrese la descripcion del Estado de la Caja. (Hasta 200 caracteres)')
#
#     class Meta:
#         verbose_name = 'Caja - Estado'
#         verbose_name_plural = 'Cajas - Estados'
#
#     def __unicode__(self):
#         return "%s" % (self.get_caja_estado_display())


# class CajaUbicacion(models.Model):
#     """
#     Registra las ubicaciones de Cajas.
#
#     Existen en total 3 puntos de cobranzas:
#     1) Un cajero en el sector Barra Arriba que cobraria tanto los pedidos de los clientes como los cierres de mesa de
#     mozos.
#     2) Un cajero en el sector Barrita que cobraria exclusivamente los cierres de mesas de mozos que operan en Planta
#     Baja.
#     3) Un cajero en el sector Barra Principal, los barmans solo atienden y registran las ventas, no tienen la
#     posibilidad de cerrar ventas.
#     """
#     caja_ubicacion = models.CharField(max_length=30, verbose_name='Ubicacion de la Caja',
#                                       help_text='Ingrese un nombre o identificador de la ubicacion de la Caja. '
#                                                 '(Hasta 30 caracteres)')
#     descripcion = models.CharField(max_length=100, verbose_name='Descripcion de la Ubicacion',
#                                    help_text='Ingrese la descripcion de la Ubicacion de la Caja. (Hasta 100 '
#                                              'caracteres)')
#
#     class Meta:
#         verbose_name = 'Caja - Ubicacion'
#         verbose_name_plural = 'Cajas - Ubicaciones'
#
#     def __unicode__(self):
#         return "%s" % self.caja_ubicacion


class Sector(models.Model):
    """
    Definicion de los Sectores en los cuales desempenan sus funciones los empleados.
    Por ej.: Los mozos son relacionados a un sector
    """
    SECTORES = (
        ('DCE', 'Deposito Central'),
        # ('DBP', 'Deposito Barra Principal'),
        # ('DBA', 'Deposito Barra Arriba'),
        # ('DBI', 'Deposito Barrita'),
        # ('DCO', 'Deposito Cocina'),
        ('BPR', 'Barra Principal'),
        ('BAR', 'Barra Arriba'),
        ('BAI', 'Barrita'),
        ('COC', 'Cocina'),
        ('ADM', 'Administracion'),
    )
    sector = models.CharField(max_length=3, choices=SECTORES,
                              verbose_name='Sector',
                              help_text='Seleccione el identificador del Sector.')
    descripcion = models.CharField(max_length=300, verbose_name='Descripcion del Sector',
                                   help_text='Ingrese la descripcion del Sector. (Hasta 100 caracteres)')
    operativo = models.BooleanField(default=False)
    deposito = models.ForeignKey('Deposito', null=True, blank=True)

    class Meta:
        verbose_name = 'Sector'
        verbose_name_plural = 'Sectores'

    def __unicode__(self):
        return "%s" % self.get_sector_display()


class Documento(models.Model):
    """
    Tipos de Documentos de Clientes.
    """
    # id = models.AutoField(primary_key=True)
    documento = models.CharField(max_length=3, verbose_name='Identificador Tipo de Documento',
                                 help_text='Ingrese el identificador del Tipo de Documento. (Hasta 3 caracteres)')
    #     choices=(
    #     ('CI', 'Cedula de Identidad'),
    #     ('RUC', 'Registro Unico del Contribuyente'),
    #     ('P', 'Pasaporte'),
    #     ('RC', 'Registro de Conducir'),
    # ),
    descripcion = models.CharField(max_length=50, verbose_name='Descripcion del Tipo de Documento',
                                   help_text='Ingrese la descripcion del Tipo de Documento. (Hasta 50 caracteres)')

    class Meta:
        verbose_name = 'Documento'
        verbose_name_plural = 'Documentos'

    def __unicode__(self):
        # return self.documento
        return "%s - %s" % (self.documento, self.descripcion)


class Persona(models.Model):
    """
    Tipo de Personas.
    """
    PERSONAS = (
        ('F', 'Fisica'),
        ('J', 'Juridica'),
    )
    persona = models.CharField(max_length=1, choices=PERSONAS, default='F')

    class Meta:
        verbose_name = 'Persona'
        verbose_name_plural = 'Personas'

    def __unicode__(self):
        return "%s" % (self.get_persona_display())


class FormaPagoVenta(models.Model):
    """
    Registra las opciones de Formas de Pagos disponibles para cerrar ventas.
    No se aceptan Pagares ni Cheques.
    """
    FORMAS_PAGO_VENTA = (
        ('EF', 'Efectivo'),
        ('TC', 'Tarjeta de Credito'),
        ('TD', 'Tarjeta de Debito'),
        ('OM', 'Otros medios'),
    )
    forma_pago_venta = models.CharField(max_length=2, choices=FORMAS_PAGO_VENTA,
                                        verbose_name='Forma de Pago Venta')

    class Meta:
        verbose_name = 'Forma de Pago - Venta'
        verbose_name_plural = 'Formas de Pago - Venta'

    def __unicode__(self):
        return "%s" % self.get_forma_pago_venta_display()


class FormaPagoCompra(models.Model):
    """
    Registra las opciones de Formas de Pagos disponibles para las compras.
    """
    FORMAS_PAGO_COMPRA = (
        ('CO', 'Contado'),
        ('CR', 'Credito'),
    )
    forma_pago_compra = models.CharField(max_length=2, choices=FORMAS_PAGO_COMPRA,
                                         verbose_name='Forma de Pago Compra')
    plazo_compra = models.PositiveIntegerField(verbose_name='Plazo de Pago Compra',
                                               help_text='En caso de Credito establecer el plazo de tiempo en dias '
                                                         'para el pago.')

    class Meta:
        verbose_name = 'Forma de Pago - Compra'
        verbose_name_plural = 'Formas de Pago - Compra'

    def __unicode__(self):
        return "%s - %d dias" % (self.get_forma_pago_compra_display(), self.plazo_compra)


# ======================================================================================================================
class TipoDeposito(models.Model):
    """
    Tipos de Depositos.

    La empresa cuenta con 1 Deposito Central y 4 Depositos Operativos.
    """
    #     choices=(
    #     ('DC', 'Deposito Central'),
    #     ('DO', 'Deposito Operativo'),
    #     ('EXT', 'Externo'),
    #     ('BAS', 'Basurero'),
    # ),
    tipo_deposito = models.CharField(max_length=2, verbose_name='Tipo de Deposito', unique=True,
                                     help_text='Ingrese el identificador del Tipo de Deposito. (Hasta 2 caracteres)')
    descripcion = models.CharField(max_length=200, verbose_name='Descripcion del Tipo de Deposito',
                                   help_text='Ingrese la descripcion del Tipo de Deposito. (Hasta 200 caracteres)')

    class Meta:
        verbose_name = 'Deposito - Tipo'
        verbose_name_plural = 'Depositos - Tipos'

    def __unicode__(self):
        return "%s - %s" % (self.tipo_deposito, self.descripcion)


class Deposito(models.Model):
    """
    Registra los datos de los Depositos.

    Las Compras ingresan totalmente al Deposito Central y a partir de ahi se transfieren a los Depositos Operativos
    segun pedidos de transferencias: Deposito Barra Principal, Deposito Barra Arriba, Cocina y Barrita.
    """
    #     choices=(
    #     ('DCE', 'Deposito Central'),
    #     ('DBP', 'Deposito Barra Principal'),
    #     ('DBA', 'Deposito Barra Arriba'),
    #     ('DCO', 'Deposito Cocina'),
    #     ('DBI', 'Deposito Barrita'),
    #     ('PRO', 'Proveedor'),
    # ),
    deposito = models.CharField(max_length=3, verbose_name='Deposito',
                                help_text='Ingrese el identificador del Deposito. (Hasta 3 caracteres)')
    descripcion = models.CharField(max_length=200, verbose_name='Descripcion del Deposito',
                                   help_text='Ingrese la descripcion del Deposito. (Hasta 200 caracteres)')
    tipo_deposito = models.ForeignKey('TipoDeposito')
    piso = models.PositiveIntegerField(default=1,
                                       verbose_name='Cantidad de Pisos')
    pasillo = models.PositiveIntegerField(default=3,
                                          verbose_name='Cantidad de Pasillos')
    estante = models.PositiveIntegerField(default=5,
                                          verbose_name='Cantidad de Estantes')
    nivel = models.PositiveIntegerField(default=5,
                                        verbose_name='Cantidad de Niveles')
    hilera = models.PositiveIntegerField(default=10,
                                         verbose_name='Cantidad de Hileras')

    class Meta:
        verbose_name = 'Deposito'
        verbose_name_plural = 'Depositos'

    def __unicode__(self):
        return "%s - %s" % (self.deposito, self.descripcion)


class Piso(models.Model):
    deposito = models.ForeignKey('Deposito', related_name='deposito_piso',)
    piso = models.CharField(max_length=50, verbose_name='Descripcion del Piso')

    def __unicode__(self):
        return "%s" % self.piso


class Pasillo(models.Model):
    deposito = models.ForeignKey('Deposito', related_name='deposito_pasillo',)
    piso = models.ForeignKey('Piso')
    pasillo = models.CharField(max_length=50, verbose_name='Descripcion del Pasillo')

    def __unicode__(self):
        return "%s" % self.pasillo


class Estante(models.Model):
    deposito = models.ForeignKey('Deposito', related_name='deposito_estante',)
    piso = models.ForeignKey('Piso')
    pasillo = models.ForeignKey('Pasillo')
    estante = models.CharField(max_length=50, verbose_name='Descripcion del Estante')

    def __unicode__(self):
        return "%s" % self.estante


class Nivel(models.Model):
    deposito = models.ForeignKey('Deposito', related_name='deposito_nivel',)
    piso = models.ForeignKey('Piso')
    pasillo = models.ForeignKey('Pasillo')
    estante = models.ForeignKey('Estante')
    nivel = models.CharField(max_length=50, verbose_name='Descripcion del Nivel')

    def __unicode__(self):
        return "%s" % self.nivel


class Hilera(models.Model):
    deposito = models.ForeignKey('Deposito', related_name='deposito_hilera',)
    piso = models.ForeignKey('Piso')
    pasillo = models.ForeignKey('Pasillo')
    estante = models.ForeignKey('Estante')
    nivel = models.ForeignKey('Nivel')
    hilera = models.CharField(max_length=50, verbose_name='Descripcion de la Hilera')
    ocupada = models.BooleanField
    producto = models.ForeignKey('stock.Producto')

    def __unicode__(self):
        return "%s" % self.hilera


class CamaraFrigorifica(models.Model):
    deposito = models.ForeignKey('Deposito', related_name='deposito_camara_frigorifica',)
    camara = models.CharField(max_length=50, verbose_name='Descripcion del Nivel')
    capacidad = models.PositiveIntegerField()
    capacidad_ocupada = models.PositiveIntegerField()

    def __unicode__(self):
        return "%s" % self.camara


# ======================================================================================================================
class CategoriaProducto(models.Model):
    """
    Categorias de Productos.
    """
    CATEGORIAS = (
        ('BE', 'Bebidas'),
        ('CO', 'Comidas'),
        ('CI', 'Cigarrillos'),
        ('GO', 'Golosinas'),
        ('AL', 'Articulos de Limpieza'),
    )
    categoria = models.CharField(max_length=2, choices=CATEGORIAS, verbose_name='Categoria', unique=True,
                                 help_text='Ingrese el identificador de la Categoria de los productos. '
                                           '(Hasta 2 caracteres)')
    descripcion = models.CharField(max_length=200, verbose_name='Descripcion de la Categoria',
                                   help_text='Ingrese la descripcion de la Categoria de los productos. '
                                             '(Hasta 200 caracteres)')

    class Meta:
        verbose_name = 'Producto - Categoria'
        verbose_name_plural = 'Productos - Categorias'

    def __unicode__(self):
        return "%s" % self.get_categoria_display()
        # return "%s" % self.get_categoria_producto_display()


class SubCategoriaProducto(models.Model):
    """
    SubCategoria de Productos en base a las Categorias definidas previamente.
    """
    categoria = models.ForeignKey('CategoriaProducto')
    subcategoria = models.CharField(max_length=3, verbose_name='SubCategoria',
                                    help_text='Ingrese el identificador de la SubCategoria de los productos. '
                                              '(Hasta 3 caracteres)')
    #     choices=(
    #     ('BEB', 'Bebidas'),
    #       ('GAS', 'Gaseosas')
    #       ('CER', 'Cervezas')
    #       ('WHI', 'Whiskies')
    #       ('LIC', 'Licores')
    #       ('TRA', 'Tragos')
    #     ('COM', 'Comidas'),
    #       ('FRI', 'Fritas')
    #       ('ALH', 'Al horno')
    #       ('VER', 'Verduras')
    #       ('FRU', 'Frutas')
    #       ('ENV', 'Envasados')
    #       ('PRE', 'Preelaborados')
    #       ('CAR', 'Carnicos')
    #     ('CIG', 'Cigarrillos'),
    # ),
    descripcion = models.CharField(max_length=200, verbose_name='Descripcion de la SubCategoria',
                                   help_text='Ingrese la descripcion de la SubCategoria de los productos. '
                                             '(Hasta 200 caracteres)')

    class Meta:
        unique_together = ['categoria', 'subcategoria']
        verbose_name = 'Producto - SubCategoria'
        verbose_name_plural = 'Productos - SubCategorias'

    def __unicode__(self):
        return "%s - %s - %s" % (self.categoria, self.subcategoria, self.descripcion)


class TipoProducto(models.Model):
    """
    Definir mejor la utilidad de los Tipos de Producto.
    La intencion es poder identificar los Productos que estan disponibles para la venta.
    Asi tambien diferenciar los Productos Compuestos de los Insumos.

    28/08/2016: Se definio no utilizar un ForeignKey a esta tabla en Stock.producto.tipo_producto
    """
    TIPOS_PRODUCTO = (
        ('VE', 'Para la venta'),
        ('IN', 'Insumos'),
    )
    tipo_producto = models.CharField(max_length=2, verbose_name='Tipo de Producto',
                                     help_text='Ingrese el identificador del Tipo de Producto. (Hasta 2 caracteres)')
    #   En principio manejaba estas opciones:
    #     choices=(
    #     ('SF', 'Sin Fraccionar'),
    #     ('FR', 'Fraccionados'),
    #     ('PR', 'Preparados'), # Los tragos y las comidas entrarían en esta categoria, deben tener una receta asociada
    #
    #   Pero finalmente se definio utilizar estas opciones:
    #     ('CO', 'Compuesto'), # Los tragos y las comidas entrarían en esta categoria, deben tener una receta asociada.
    #     ('VE', 'Para la venta'),
    #     ('IN', 'Insumos'),
    # ),
    descripcion = models.CharField(max_length=200, verbose_name='Descripcion del Tipo de Producto',
                                   help_text='Ingrese la descripcion del Tipo de Producto. (Hasta 200 caracteres)')

    class Meta:
        verbose_name = 'Producto - Tipo'
        verbose_name_plural = 'Productos - Tipos'

    def __unicode__(self):
        return "%s - %s" % (self.tipo_producto, self.descripcion)


class UnidadMedidaProducto(models.Model):
    """
    04/07/2016: Se manejaran solo las Unidades de Medida de UN, ML y GR; se descartan LI y KG de modo a
    simplificar la logica.
    22/07/2016: Se vuelven a agregar las Unidades de Medida LI y KG ya que complicaria la programacion controlar la
    correcta carga por parte del usuario, quedaria a cargo del usuario asegurar la asignacion de la Unidad de Medida
    adecuada. Se manejaran solo las Unidades de Medida de UN, LI y KG; se descartan ML y GR de modo a simplificar la
    logica.
    """
    UNIDADES_MEDIDA_PRODUCTO = (
        ('UN', 'Unidad'),
        # ('ML', 'Mililitros'),
        # ('GR', 'Gramos'),
        ('LI', 'Litros'),
        ('KG', 'Kilogramos'),
    )
    unidad_medida_producto = models.CharField(max_length=2, choices=UNIDADES_MEDIDA_PRODUCTO)
    descripcion = models.CharField(max_length=200, verbose_name='Descripcion de la Unidad de Medida',
                                   help_text='Ingrese la descripcion de la Unidad de Medida. (Hasta 200 caracteres)')

    class Meta:
        verbose_name = 'Producto - Unidad de Medida'
        verbose_name_plural = 'Productos - Unidades de Medida'

    def __unicode__(self):
        return "%s" % self.get_unidad_medida_producto_display()


class Moneda(models.Model):
    """
    Datos de las Monedas.
    """
    codigo_moneda = models.PositiveIntegerField(verbose_name='Codigo de Moneda ISO 4217', unique=True,
                                                help_text='Corresponde al codigo internacional ISO 4217 de la Moneda. '
                                                          'EJ: Gs - 600')
    moneda = models.CharField(max_length=100, unique=True, verbose_name='Moneda',
                              help_text='Nombre de la Moneda.')
    abreviacion_moneda = models.CharField(max_length=5, verbose_name='Abreviacion de la Moneda', unique=True,
                                          help_text='Abreviacion o simbolo de la Moneda. EJ: Guaranies - Gs.')

    class Meta:
        verbose_name = 'Moneda'
        verbose_name_plural = 'Monedas'

    def __unicode__(self):
        return "%s - %s" % (self.codigo_moneda, self.abreviacion_moneda)


class Cotizacion(models.Model):
    """
    Registra el historial de Cotizaciones de Monedas.
    """
    moneda = models.ForeignKey('Moneda', help_text='Seleccione la moneda para la cual definir su cotizacion.')
    fecha_cotizacion = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Cotizacion',
                                            help_text='Registra la fecha y hora en la que se definio la Cotizacion. '
                                                      'Corresponde a la fecha y hora actual.')
    cotizacion = models.DecimalField(max_digits=20, decimal_places=2,
                                     help_text='Ingrese la Cotizacion en Guaranies de la Moneda.')

    class Meta:
        verbose_name = 'Cotizacion'
        verbose_name_plural = 'Cotizaciones'

    def __unicode__(self):
        return "%s - %s - %s" % (self.moneda, self.cotizacion, self.fecha_cotizacion)


class CodigoPaisTelefono(models.Model):
    """
    Registra los Codigos Telefonicos Internacionales para cada Pais.
    Cada Pais puede tener un unico Codigo Internacional Telefonico.
    """
    codigo_pais_telefono = models.PositiveIntegerField(verbose_name='Codigo Telefonico del Pais', unique=True,
                                                       help_text='Codigo internacional del pais al cual corresponde el '
                                                                 'telefono.')
    pais = models.OneToOneField('Pais', help_text='Pais al cual corresponde el codigo.')  # unique=True,

    class Meta:
        # unique_together = ("codigo_pais_telefono", "pais")
        verbose_name = 'Telefono - Codigo intern. por pais'
        verbose_name_plural = 'Telefonos - Codigos intern. por pais'

    def __unicode__(self):
        return "%s - %s" % (self.codigo_pais_telefono, self.pais)


class CodigoOperadoraTelefono(models.Model):
    """
    Registra los Codigos Telefonicos de Operadora para cada Pais.
    Un Pais puede tener varios Codigos Telefonicos de Operadora que inclusive pueden ser los mismos que de otros paises.
    """
    codigo_pais_telefono = models.ForeignKey('CodigoPaisTelefono', verbose_name='Codigo Telefonico del Pais')
    codigo_operadora_telefono = models.PositiveIntegerField(verbose_name='Codigo Telefonico de la Operadora',
                                                            # default='21',  # unique=True,
                                                            help_text='Codigo de la Operadora de Telefonia.')

    # Se debe filtrar en base al Pais seleccionado.
    # ciudad_operadora = models.OneToOneField('Ciudad', default=1, verbose_name='Descripcion Ciudad/Operadora',
    #                                         # unique=True,
    #                                         help_text='Descripcion de la ciudad o de la operadora de telefonia
    #                                         movil.')

    tipo_operadora = models.CharField(max_length=2, verbose_name='Tipo de Operadora de Telefonia', choices=(
        ('TM', 'Telefonia Movil'),
        ('TF', 'Telefonia Fija'),
    ), help_text='Tipo de Telefonia')

    class Meta:
        unique_together = ("codigo_pais_telefono", "codigo_operadora_telefono")
        verbose_name = 'Telefono - Codigo por operadora'
        verbose_name_plural = 'Telefonos - Codigos por operadora'

    def __unicode__(self):
        return "%s - %s" % (self.codigo_operadora_telefono, self.get_tipo_operadora_display())


class Pais(models.Model):
    """
    Datos de los Paises.
    """
    pais = models.CharField(max_length=100, unique=True)

    class Meta:
        verbose_name = 'Pais'
        verbose_name_plural = 'Paises'

    def __unicode__(self):
        return "%s" % self.pais


class Ciudad(models.Model):
    """
    Datos de las Ciudades.
    """
    pais = models.ForeignKey('Pais')
    ciudad = models.CharField(max_length=100)  # unique=True

    class Meta:
        unique_together = ("pais", "ciudad")
        verbose_name = 'Ciudad'
        verbose_name_plural = 'Ciudades'

    def __unicode__(self):
        # return str(self.ciudad)
        # return "%s - %s" % (self.ciudad, self.pais)
        return "%s" % self.ciudad


class CompraEstado(models.Model):
    """
    Estos son los diversos ESTADOS que puede tener una Compra.
    Con el formulario de Confirmacion de Compra se debe modificar el ESTADO de la Orden de Compra cuando se recepcionan
    los productos.
    Se debe definir un metodo o funcion que compare OrdenCompra.fecha_entrega contra la fecha actual y modificar si
    corresponde el ESTADO de la Orden de Compra.

    Cuando la Compra llega a los estados de CON o CAN ya no puede volver a ser modificada.
    En el caso de que una Compra confirmada deba ser devuelta se debe registrar el proceso en el modelo de Devoluciones.

    El estado PEN es necesario para poder realizar la copia de los datos de la OrdenCompra a la Compra.
    """
    ESTADOS_COMPRAS = (
        ('PEN', 'Pendiente'),
        ('CON', 'Confirmada'),
        ('CAN', 'Cancelada'),
    )
    # id = models.AutoField(primary_key=True)
    estado_compra = models.CharField(max_length=3, verbose_name='Estado de la Compra', choices=ESTADOS_COMPRAS)
    descripcion = models.CharField(max_length=200, verbose_name='Descripcion del Estado de la Compra',
                                   help_text='Ingrese la descripcion del Estado de la Compra. (Hasta 200 caracteres)')

    class Meta:
        verbose_name = 'Compra - Estado'
        verbose_name_plural = 'Compras - Estados'

    def __unicode__(self):
        # return self.documento
        return "%s" % (self.get_estado_compra_display())


class OrdenCompraEstado(models.Model):
    """
    Estos son los diversos ESTADOS que puede tener una Orden de Compra.
    Con el formulario de Confirmacion de Compra se debe modificar el ESTADO de la Orden de Compra cuando se recepcionan
    los productos.
    Se debe definir un metodo o funcion que compare OrdenCompra.fecha_entrega_orden_compra contra la fecha actual y
    modificar si corresponde el ESTADO de la Orden de Compra.

    Cuando la OrdenCompra llega a los estados de ENT o CAN ya no puede volver a ser modificada.
    """
    ESTADOS_ORDENES_COMPRAS = (
        ('EPP', 'En Proceso Proveedor'),
        ('ENT', 'Entregada por el Proveedor'),
        ('PEP', 'Pendiente de Entrega por el Proveedor'),
        ('CAN', 'Cancelada'),
        ('PEN', 'Pendiente Confirmacion'),
        # ('BOR', 'Borrador'),  # El estado BOR es necesario para poder guardar un borrador del detalle de la Compra.
    )
    # id = models.AutoField(primary_key=True)
    estado_orden_compra = models.CharField(max_length=3, verbose_name='Estado de la Orden de Compra',
                                           choices=ESTADOS_ORDENES_COMPRAS)
    descripcion = models.CharField(max_length=200, verbose_name='Descripcion del Estado de la Orden de Compra',
                                   help_text='Ingrese la descripcion del Estado de la Orden de Compra. '
                                             '(Hasta 200 caracteres)')

    class Meta:
        verbose_name = 'Orden de Compra - Estado'
        verbose_name_plural = 'Ordenes de Compras - Estados'

    def __unicode__(self):
        # return self.documento
        return "%s" % (self.get_estado_orden_compra_display())


class OrdenPagoEstado(models.Model):
    """
    Estos son los diversos ESTADOS que puede tener una Orden de Pago.
    """
    ESTADOS_ORDEN_PAGO = (
        ('PEN', 'Pendiente'),
        ('CON', 'Confirmada'),
        ('ANU', 'Anulada'),
        ('CAN', 'Cancelada'),
    )
    # id = models.AutoField(primary_key=True)
    estado_orden_pago = models.CharField(max_length=3, verbose_name='Estado de la Orden de Pago',
                                         choices=ESTADOS_ORDEN_PAGO)
    descripcion = models.CharField(max_length=200, verbose_name='Descripcion del Estado de la Orden de Pago',
                                   help_text='Ingrese la descripcion del Estado de la Orden de Pago. '
                                             '(Hasta 200 caracteres)')

    class Meta:
        verbose_name = 'Orden de Pago - Estado'
        verbose_name_plural = 'Ordenes de Pagos - Estados'

    def __unicode__(self):
        # return self.documento
        return "%s" % (self.get_estado_orden_pago_display())


class FacturaProveedorEstado(models.Model):
    """
    Estos son los diversos ESTADOS que puede tener una Orden de Pago.
    """
    ESTADOS_FACTURA_COMPRA = (
        # ('PEN', 'Pendiente'),
        ('EPP', 'En Plazo de Pago'),
        ('FPP', 'Fuera del Plazo de Pago'),
        ('PAG', 'Pagada'),
        ('CAN', 'Cancelada'),
    )
    # id = models.AutoField(primary_key=True)
    estado_factura_proveedor = models.CharField(max_length=3, verbose_name='Estado de la Factura del Proveedor',
                                                choices=ESTADOS_FACTURA_COMPRA)
    descripcion = models.CharField(max_length=200, verbose_name='Descripcion del Estado de la Factura del Proveedor',
                                   help_text='Ingrese la descripcion del Estado de la Factura del Proveedor. '
                                             '(Hasta 200 caracteres)')

    class Meta:
        verbose_name = 'Factura Proveedor - Estado'
        verbose_name_plural = 'Facturas Proveedores - Estados'

    def __unicode__(self):
        # return self.documento
        return "%s" % (self.get_estado_factura_proveedor_display())


class LineaCreditoProveedorEstado(models.Model):
    """
    Estos son los diversos ESTADOS que puede tener una Linea de Credito de Proveedores.
    """
    ESTADOS_LINEA_CREDITO = (
        ('DEL', 'Dentro de la Linea de Credito'),
        ('LIM', 'En el Limite'),
        ('SOB', 'Sobregirada'),
    )
    # id = models.AutoField(primary_key=True)
    estado_linea_credito = models.CharField(max_length=3, verbose_name='Estado de la Linea de Credito con el Proveedor',
                                            choices=ESTADOS_LINEA_CREDITO)
    descripcion = models.CharField(max_length=200, verbose_name='Descripcion del Estado de la Linea de Credito con '
                                                                'el Proveedor',
                                   help_text='Ingrese la descripcion del Estado de la Linea de Credito con el '
                                             'Proveedor. (Hasta 200 caracteres)')

    class Meta:
        verbose_name = 'Linea de Credito Proveedor - Estado'
        verbose_name_plural = 'Linea de Credito Proveedores - Estados'

    def __unicode__(self):
        # return self.documento
        return "%s" % (self.get_estado_linea_credito_display())


class PedidoEstado(models.Model):
    """
    Diversos ESTADOS que puede tener un Pedido.
    """
    ESTADOS_PEDIDO = (
        ('VIG', 'Vigente'),
        # ('CAD', 'Caducado'),
        ('PRO', 'Procesado'),
        ('CAN', 'Cancelado'),
        # ('ANU', 'Anulada'),
        ('PEN', 'Pendiente Confirmacion'),
    )
    pedido_estado = models.CharField(max_length=3, choices=ESTADOS_PEDIDO, verbose_name='Estado del Pedido',
                                     help_text='Ingrese el identificador del Estado del Pedido. (Hasta 3 caracteres)')
    descripcion = models.CharField(max_length=200, verbose_name='Descripcion del Estado',
                                   help_text='Ingrese la descripcion del Estado del Pedido. (Hasta 200 caracteres)')

    class Meta:
        ordering = ('id',)
        verbose_name = 'Pedido - Estado'
        verbose_name_plural = 'Pedidos - Estados'

    def __unicode__(self):
        return "%s" % (self.get_pedido_estado_display())


class VentaEstado(models.Model):
    """
    Diversos ESTADOS que puede tener una Venta.
    """
    ESTADOS_VENTA = (
        # ('ABI', 'Abierta'),
        ('PRO', 'Procesado'),
        # ('ANU', 'Anulada'),
        ('PEN', 'Pendiente Confirmacion'),
        ('CAN', 'Cancelado'),
    )
    venta_estado = models.CharField(max_length=3, choices=ESTADOS_VENTA, verbose_name='Estado de la Venta',
                                    help_text='Ingrese el identificador del Estado de la Venta. '
                                              '(Hasta 3 caracteres)')
    descripcion = models.CharField(max_length=200, verbose_name='Descripcion del Estado',
                                   help_text='Ingrese la descripcion del Estado de la Venta. (Hasta 200 caracteres)')

    class Meta:
        ordering = ('id',)
        verbose_name = 'Venta - Estado'
        verbose_name_plural = 'Ventas - Estados'

    def __unicode__(self):
        return "%s" % (self.get_venta_estado_display())


class Timbrado(models.Model):
    """
    Registra los datos de los Timbrados para la Empresa.
    """
    ESTADOS_TIMBRADO = {
        ('AC', 'Activo'),
        ('IN', 'Inactivo'),
    }
    # empresa = models.ForeignKey('compras.Empresa')
    timbrado = models.CharField(max_length=8, unique=True,
                                verbose_name='Numero de Timbrado',
                                help_text='Ingrese el numero de Timbrado.')
    descripcion_timbrado = models.CharField(max_length=200, verbose_name='Descripcion del Timbrado',
                                            help_text='Ingrese la descripcion del Timbrado. (Hasta 200 caracteres)')
    fecha_autorizacion_timbrado = models.DateField(default=timezone.datetime.today,
                                                   verbose_name='Fecha de Autorizacion del Timbrado',
                                                   help_text='Ingrese la Fecha de Autorizacion del Timbrado')
    fecha_limite_vigencia_timbrado = models.DateField(default=(timezone.datetime.today() +
                                                               datetime.timedelta(days=365)),
                                                      verbose_name='Fecha Limite de Vigencia del Timbrado',
                                                      help_text='Ingrese la Fecha Limite de Vigencia del Timbrado')
    estado_timbrado = models.CharField(max_length=2, choices=ESTADOS_TIMBRADO,
                                       verbose_name='Estado del Timbrado',
                                       help_text='Seleccione el Estado del Timbrado (Solo un Timbrado puede tener el '
                                                 'estado ACTIVO.)')

    class Meta:
        verbose_name = 'Venta - Timbrado'
        verbose_name_plural = 'Ventas - Timbrados'

    # def clean(self):
    #     Valida que la fecha_limite_vigencia_timbrado sea mayor a la fecha_autorizacion_timbrado
    #     if self.fecha_limite_vigencia_timbrado <= self.fecha_autorizacion_timbrado:
    #         raise ValidationError({'fecha_limite_vigencia_timbrado': _('La Fecha Limite de Vigencia del Timbrado '
    #                                                                    'debe ser mayor a la Fecha de Autorizacion '
    #                                                                    'del Timbrado.')})
    #
    #     Validar que exista un unico Timbrado como Activo.

    def __unicode__(self):
        return "%s" % self.timbrado


class FacturaVenta(models.Model):
    """
    Mantiene los datos de los Numeros de Factura por Punto de Expedicion (Cajas).
    """
    ESTADOS_FACTURA_VENTA = (
        ('ACT', 'Activa'),
        ('INA', 'Inactiva'),
    )
    # empresa = models.ForeignKey('compras.Empresa', default=9)
    timbrado = models.ForeignKey('bar.Timbrado', default=2,
                                 limit_choices_to={'estado_timbrado': "AC"})
    numero_serie = models.PositiveIntegerField(unique=True, verbose_name='Numero de Serie')
    caja = models.ForeignKey('Caja')
    estado = models.CharField(max_length=3, choices=ESTADOS_FACTURA_VENTA, default="ACT",
                              help_text='Seleccione el estado de la Factura.')
    numero_factura_inicial = models.DecimalField(max_digits=7, decimal_places=0, default=1)
    numero_factura_final = models.DecimalField(max_digits=7, decimal_places=0, default=9999999)

    class Meta:
        verbose_name = 'Venta - Serie de Factura'
        verbose_name_plural = 'Ventas - Series de Facturas'

    def clean(self):
        super(FacturaVenta, self).clean()

        # import pdb
        # pdb.set_trace()

        if self.pk is None:
            facturas = FacturaVenta.objects.filter(caja=self.caja, estado='ACT')
            if facturas.exists():
                raise ValidationError({'numero_serie': ('Ya existe una Serie de Facturas para la Caja %s con estado '
                                                        'Activa. Inactive la Serie de Facturas actualmente activa e '
                                                        'intente cargar la nueva Serie nuevamente.' % self.caja)})

    def __unicode__(self):
        return "Caja: %s - Serie: %s" % (self.caja, self.numero_serie)


class NumeroFacturaVenta(models.Model):
    serie = models.ForeignKey('FacturaVenta')
    numero_factura = models.DecimalField(max_digits=7, decimal_places=0, default=1)
    venta_asociada = models.PositiveIntegerField(null=True, blank=True)
    fecha_hora_uso = models.DateTimeField(null=True, blank=True)

    class Meta:
        verbose_name = 'Venta - Numero de Factura'
        verbose_name_plural = 'Ventas - Numeros de Facturas'

    def __unicode__(self):
        return "%s" % self.numero_factura


class TipoMovimientoStock(models.Model):
    """
    Diversos TIPOS DE MOVIMIENTO que se pueden registrar en el Stock de un Producto.
    """
    TIPOS_MOVIMIENTO_STOCK = (
        ('VE', 'Venta'),
        ('CO', 'Compra'),
        ('ME', 'Mermas'),
        ('TR', 'Transferencias'),
        ('DE', 'Devoluciones'),
    )
    tipo_movimiento_stock = models.CharField(max_length=2, choices=TIPOS_MOVIMIENTO_STOCK,
                                             verbose_name='Tipo de Movimiento de Stock',
                                             help_text='Ingrese el identificador del Tipo de Movimiento de Stock. '
                                                       '(Hasta 2 caracteres)')
    descripcion = models.CharField(max_length=200, verbose_name='Descripcion del Tipo de Movimiento de Stock',
                                   help_text='Ingrese la descripcion del Tipo de Movimiento de Stock. (Hasta 200 '
                                             'caracteres)')

    class Meta:
        ordering = ('id',)
        verbose_name = 'Stock - Tipo de Movimiento'
        verbose_name_plural = 'Stock - Tipos de Movimientos'

    def __unicode__(self):
        return "%s" % self.get_tipo_movimiento_stock_display()


class TransferenciaStockEstado(models.Model):
    """
    Diversos ESTADOS que puede tener una Transferencia de Stock entre Depositos.
    """
    ESTADOS_TRANSFERENCIA = (
        ('PEN', 'Pendiente'),
        ('PRO', 'Procesada'),
        ('CAN', 'Cancelada'),
    )
    estado_transferencia_stock = models.CharField(max_length=3, choices=ESTADOS_TRANSFERENCIA,
                                                  verbose_name='Estado de la Transferencia de Stock',
                                                  help_text='Ingrese el identificador del Estado de la Transferencia '
                                                            'de Stock entre depositos. (Hasta 3 caracteres)')
    descripcion = models.CharField(max_length=200, verbose_name='Descripcion del Estado',
                                   help_text='Ingrese la descripcion del Estado del Pedido. (Hasta 200 caracteres)')

    class Meta:
        ordering = ('id',)
        verbose_name = 'Stock - Transferencia - Estado'
        verbose_name_plural = 'Stock - Transferencias - Estados'

    def __unicode__(self):
        return "%s" % (self.get_estado_transferencia_stock_display())


class TipoFacturaCompra(models.Model):
    """
    Registra las opciones de Formas de Pagos disponibles para las compras.
    """
    TIPOS_FACTURA_COMPRA = (
        ('CON', 'Contado'),
        ('CRE', 'Credito'),
    )
    tipo_factura_compra = models.CharField(max_length=3, choices=TIPOS_FACTURA_COMPRA,  # default='CON',
                                           verbose_name='Tipo de Factura Compra',
                                           help_text='Ingrese el identificador del Tipo de Factura de Compra. '
                                                     '(Hasta 3 caracteres)')
    descripcion = models.CharField(max_length=200, verbose_name='Descripcion del Tipo de Factura Compra',
                                   help_text='Ingrese la descripcion del Tipo de Factura Compra. (Hasta 200 '
                                             'caracteres)')

    class Meta:
        verbose_name = 'Compra - Tipo de Factura'
        verbose_name_plural = 'Compra - Tipo de Factura'

    def __unicode__(self):
        return "%s" % (self.get_tipo_factura_compra_display())


# class JornadaEstado(models.Model):
#     """
#     Diversos ESTADOS que puede tener un Pedido.
#     """
#     ESTADOS_JORNADA = (
#         ('VIG', 'Vigente'),
#         ('EXP', 'Expirada'),
#         ('CER', 'Cerrada'),
#     )
#     jornada_estado = models.CharField(max_length=3, choices=ESTADOS_JORNADA, verbose_name='Estado de la Jornada',
#                                       help_text='Ingrese el identificador del Estado de la Jornada. '
#                                                 '(Hasta 3 caracteres)')
#     descripcion = models.CharField(max_length=200, verbose_name='Descripcion de la Jornada',
#                                    help_text='Ingrese la descripcion del Estado de la Jornada. (Hasta 200 caracteres)')
#
#     class Meta:
#         ordering = ('id',)
#         verbose_name = 'Jornada - Estado'
#         verbose_name_plural = 'Jornada - Estados'
#
#     def __unicode__(self):
#         return "%s" % (self.get_pedido_estado_display())
