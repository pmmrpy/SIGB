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
    ubicacion = models.ForeignKey('MesaUbicacion')
    estado = models.ForeignKey('MesaEstado')

    class Meta:
        verbose_name = 'Mesa'
        verbose_name_plural = 'Mesas'

    def __unicode__(self):
        return "Nro. Mesa: %s - %s - Ubic: %s" % (self.numero_mesa, self.nombre_mesa, self.ubicacion)


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
    numero_caja = models.PositiveIntegerField(verbose_name='Numero de Caja', unique=True,
                                              help_text='Ingrese el Numero de Caja.')
    ubicacion = models.ForeignKey('CajaUbicacion')
    estado = models.ForeignKey('CajaEstado')

    class Meta:
        verbose_name = 'Caja'
        verbose_name_plural = 'Cajas'

    def __unicode__(self):
        return "%s - %s" % (self.numero_caja, self.ubicacion)


class CajaEstado(models.Model):
    """
    Diversos ESTADOS que puede tener una Caja.
    """
    ESTADOS_CAJA = (
        ('AB', 'Abierta'),
        ('CE', 'Cerrada'),
        ('CL', 'Clausurada')
    )
    caja_estado = models.CharField(max_length=2, choices=ESTADOS_CAJA, verbose_name='Estado de la Caja',
                                   help_text='Ingrese el identificador del Estado de la Caja. (Hasta 2 caracteres')
    descripcion = models.CharField(max_length=200, verbose_name='Descripcion del Estado',
                                   help_text='Ingrese la descripcion del Estado de la Caja. (Hasta 200 caracteres)')

    class Meta:
        verbose_name = 'Caja - Estado'
        verbose_name_plural = 'Cajas - Estados'

    def __unicode__(self):
        return "%s" % (self.get_caja_estado_display())


class CajaUbicacion(models.Model):
    """
    Registra las ubicaciones de Cajas.

    Existen en total 3 puntos de cobranzas:
    1) Un cajero en el sector Barra Arriba que cobraria tanto los pedidos de los clientes como los cierres de mesa de
    mozos.
    2) Un cajero en el sector Barrita que cobraria exclusivamente los cierres de mesas de mozos que operan en Planta
    Baja.
    3) Un cajero en el sector Barra Principal, los barmans solo atienden y registran las ventas, no tienen la
    posibilidad de cerrar ventas.
    """
    caja_ubicacion = models.CharField(max_length=30, verbose_name='Ubicacion de la Caja',
                                      help_text='Ingrese un nombre o identificador de la ubicacion de la Caja. '
                                                '(Hasta 30 caracteres)')
    descripcion = models.CharField(max_length=100, verbose_name='Descripcion de la Ubicacion',
                                   help_text='Ingrese la descripcion de la Ubicacion de la Caja. (Hasta 100 '
                                             'caracteres)')

    class Meta:
        verbose_name = 'Caja - Ubicacion'
        verbose_name_plural = 'Cajas - Ubicaciones'

    def __unicode__(self):
        return "%s" % self.caja_ubicacion


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
        ('CO', 'Contado'),
        ('TC', 'Tarjeta de Credito'),
        ('TD', 'Tarjeta de Debito'),
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


class TipoDeposito(models.Model):
    """
    Tipos de Depositos.

    La empresa cuenta con 1 Deposito Central y 4 Depositos Operativos.
    """
    tipo_deposito = models.CharField(max_length=2, verbose_name='Tipo de Deposito', unique=True,
                                     help_text='Ingrese el identificador del Tipo de Deposito. (Hasta 2 caracteres)')
    #     choices=(
    #     ('DC', 'Deposito Central'),
    #     ('DO', 'Deposito Operativo'),
    # ),
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
    deposito = models.CharField(max_length=3, verbose_name='Deposito',
                                help_text='Ingrese el identificador del Deposito. (Hasta 3 caracteres)')
    #     choices=(
    #     ('DCE', 'Deposito Central'),
    #     ('DBP', 'Deposito Barra Principal'),
    #     ('DBA', 'Deposito Barra Arriba'),
    #     ('DCO', 'Deposito Cocina'),
    #     ('DBI', 'Deposito Barrita'),
    # ),
    descripcion = models.CharField(max_length=200, verbose_name='Descripcion del Deposito',
                                   help_text='Ingrese la descripcion del Deposito. (Hasta 200 caracteres)')
    tipo_deposito = models.ForeignKey('TipoDeposito')

    class Meta:
        verbose_name = 'Deposito'
        verbose_name_plural = 'Depositos'

    def __unicode__(self):
        return "%s - %s" % (self.deposito, self.descripcion)


class CategoriaProducto(models.Model):
    """
    Categorias de Productos.
    """
    categoria = models.CharField(max_length=2, verbose_name='Categoria', unique=True,
                                 help_text='Ingrese el identificador de la Categoria de los productos. '
                                           '(Hasta 2 caracteres)')
    #     choices=(
    #     ('BE', 'Bebidas'),
    #     ('CO', 'Comidas'),
    #     ('CI', 'Cigarrillos'),
    #     ('GO', 'Golosinas'),
    # ),
    descripcion = models.CharField(max_length=200, verbose_name='Descripcion de la Categoria',
                                   help_text='Ingrese la descripcion de la Categoria de los productos. '
                                             '(Hasta 200 caracteres)')

    class Meta:
        verbose_name = 'Producto - Categoria'
        verbose_name_plural = 'Productos - Categorias'

    def __unicode__(self):
        return "%s - %s" % (self.categoria, self.descripcion)


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
        return "%s - %s - %s" % (self.codigo_operadora_telefono, self.get_tipo_operadora_display(),
                                 self.codigo_pais_telefono)


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
        return "%s - %s" % (self.ciudad, self.pais)
        # return str(self.ciudad)


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


class PedidoEstado(models.Model):
    """
    Diversos ESTADOS que puede tener un Pedido.
    """
    ESTADOS_PEDIDO = (
        ('VIG', 'Vigente'),
        # ('CAD', 'Caducado'),
        ('PRO', 'Procesado'),
        ('CAN', 'Cancelado'),
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
        ('ABI', 'Abierta'),
        ('CER', 'Cerrada'),
        ('ANU', 'Anulada'),
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
    empresa = models.ForeignKey('compras.Empresa')
    timbrado = models.DecimalField(max_digits=8, decimal_places=0, verbose_name='Numero de Timbrado', default=1,
                                   help_text='Ingrese el numero de Timbrado.')
    descripcion_timbrado = models.CharField(max_length=200, verbose_name='Descripcion del Timbrado',
                                            help_text='Ingrese la descripcion del Timbrado. (Hasta 200 caracteres)')
    fecha_autorizacion_timbrado = models.DateField(default=timezone.datetime.today(),
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

    # def clean(self):
    #     Valida que la fecha_limite_vigencia_timbrado sea mayor a la fecha_autorizacion_timbrado
    #     if self.fecha_limite_vigencia_timbrado <= self.fecha_autorizacion_timbrado:
    #         raise ValidationError({'fecha_limite_vigencia_timbrado': _('La Fecha Limite de Vigencia del Timbrado '
    #                                                                    'debe ser mayor a la Fecha de Autorizacion '
    #                                                                    'del Timbrado.')})
    #
    #     Validar que exista un unico Timbrado como Activo.

    def __unicode__(self):
        return "%s - %s" % (self.timbrado, self.descripcion_timbrado)


class Factura(models.Model):
    """
    Mantiene los datos de los Numeros de Factura por Punto de Expedicion (Cajas).
    """
    caja = models.OneToOneField('Caja')
    numero_factura_inicial = models.PositiveIntegerField()
    numero_factura_final = models.PositiveIntegerField()
    numero_factura_actual = models.PositiveIntegerField()


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