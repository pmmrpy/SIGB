import datetime
from django.db import models
from django.utils import timezone
from django.db.models import Q
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
from django.utils.safestring import mark_safe
from django.views.generic.dates import timezone_today
from bar.models import TipoProducto, UnidadMedidaProducto, TransferenciaStockEstado, CompraEstado
from compras.models import Compra, CompraDetalle
from personal.models import Empleado

# Create your models here.


class Producto(models.Model):
    """
    21/06/2016: Registrar productos.

    Tipo Producto: Diferencia un Producto que es adquirido para ser puesto a la Venta directamente de un Insumo.
    Categoria:
    SubCategoria:
    """
    TIPOS_PRODUCTO = (
        ('VE', 'Para la Venta'),
        ('IN', 'Insumo'),
    )
# ==> Datos del Producto <==
    producto = models.CharField(max_length=100, verbose_name='Nombre del Producto',
                                help_text='Ingrese el nombre o descripcion del Producto.')
    # Realizar alguna validacion sobre el ingreso del codigo_barra, por lo menos cantidad de caracteres
    codigo_barra = models.CharField(max_length=100, verbose_name='Codigo de Barra',  # default=1,
                                    help_text='Ingrese el codigo de barra del Producto si posee.')
    marca = models.CharField(max_length=100, verbose_name='Marca',  # default='Marca',
                             help_text='Ingrese la marca del Producto.')
    # stock_minimo = models.DecimalField(max_digits=10, decimal_places=3, default=1,
    #                                    verbose_name='Stock Minimo',
    #                                    help_text='Cantidad minima del producto a mantener en Stock.')
    imagen = models.ImageField(upload_to='stock/productos/', verbose_name='Archivo de Imagen',
                               help_text='Seleccione el archivo con la imagen del Producto.')
    fecha_alta_producto = models.DateTimeField(auto_now_add=True, editable=True,  # default=timezone.now(),
                                               verbose_name='Fecha de Alta',
                                               help_text='La Fecha de Alta se asigna al momento de guardar los datos '
                                                         'del Producto. No se requiere el ingreso de este dato.')

# ==> Contenido del Producto <==
    # tipo_producto = models.ForeignKey('bar.TipoProducto', verbose_name='Tipo de Producto',  # default="VE",
    #                                   help_text='Seleccione el Tipo de Producto.')
    tipo_producto = models.CharField(max_length=2, choices=TIPOS_PRODUCTO, default='VE',
                                     verbose_name='Tipo de Producto',
                                     help_text='Seleccione el Tipo de Producto.')
    categoria = models.ForeignKey('bar.CategoriaProducto', help_text='Seleccione la Categoria del Producto.')
    subcategoria = models.ForeignKey('bar.SubCategoriaProducto', help_text='Seleccione la SubCategoria del Producto.')
    compuesto = models.BooleanField(verbose_name='Es compuesto?',  # default=False,
                                    help_text='La casilla se marca automicamente si el Producto a ser registrado es '
                                              'Compuesto o no.')
    perecedero = models.BooleanField(verbose_name='Es perecedero?', default=False,
                                     help_text='Marque la casilla si el Producto a registrar es Perecedero.')
    unidad_medida_contenido = models.ForeignKey('bar.UnidadMedidaProducto', related_name='un_med_contenido',
                                                verbose_name='Unidad de Medida Contenido',  # default=1,
                                                help_text='Seleccione la Unidad de Medida del Producto contenido '
                                                          'en su presentacion (envase).')
    contenido = models.DecimalField(max_digits=10, decimal_places=3,  # default=0,
                                    verbose_name='Cantidad Contenido',
                                    help_text='Ingrese la cantidad del Producto contenida en el envase de acuerdo '
                                              'a su Unidad de Medida. Los Productos del tipo Insumo comprados a '
                                              'granel (no envasados) siempre deben ser registrados con contenido igual '
                                              'a una unidad. Ej: Queso - 1 kilo, Detergente - 1 litro.')

# ==> Datos para la Compra <==
    unidad_medida_compra = models.ForeignKey('bar.UnidadMedidaProducto', related_name='un_med_compra',  # default=1,
                                             verbose_name='Unidad de Medida Compra',
                                             help_text='Seleccione la Unidad de Medida con el cual el Producto '
                                                       'es adquirido. Corresponde a la Unidad de Medida de la '
                                                       'presentacion del Producto.')
    precio_compra = models.DecimalField(max_digits=18, decimal_places=0, default=0,
                                        verbose_name='Precio Compra',
                                        help_text='Corresponde al valor del Precio de Compra almacenado en la Base de '
                                                  'Datos del Sistema. Este valor sera utilizado para operaciones a '
                                                  'realizar con el Producto.')

# ==> Utilidad <==
    porcentaje_ganancia = models.DecimalField(max_digits=3, decimal_places=0, default=0,
                                              verbose_name='Porcentaje de Ganancia',
                                              help_text='Ingrese el Porcentaje de Ganancia o Margen de Utilidad que '
                                                        'desea obtener de la venta del Producto.')
    # Analizar si precio_venta debe ser un atributo del Producto
    # Debe ser el ultimo definido en PrecioVentaProducto.
    # Cuando el Tipo de Producto es Insumo se debe poner en read-only este campo y dejar su valor en 0.
    precio_venta = models.DecimalField(max_digits=18, decimal_places=0, default=0,
                                       verbose_name='Precio Venta',
                                       help_text='Corresponde al valor del Precio de Venta almacenado en la Base de '
                                                 'Datos del Sistema. Este valor sera utilizado para operaciones a '
                                                 'realizar con el Producto.')

# ==> Datos para el Stock <==
    # cantidad_existente_stock = models.DecimalField(max_digits=10, decimal_places=3, default=0,
    #                                                verbose_name='Cantidad Existente',
    #                                                help_text='Corresponde a la cantidad existente del Producto '
    #                                                          'registrada en la tabla Stock.')

    # Manejo de stock minimo. Alertar cuando llega a este minimo.
    stock_minimo = models.DecimalField(max_digits=10, decimal_places=3, default=0,
                                       verbose_name='Stock Minimo',
                                       help_text='Cantidad minima del Producto a mantener en Stock.')

    # fecha_vencimiento = models.DateField(default=(datetime.date.today() + datetime.timedelta(days=30)),
    #                                      verbose_name='Fecha de Vencimiento',
    #                                      help_text='Ingrese la fecha de vencimiento del Producto.')

# ==> Datos para la Elaboracion <==
    costo_elaboracion = models.DecimalField(max_digits=18, decimal_places=0, default=0,
                                            verbose_name='Costo de Elaboracion del Producto',
                                            help_text='Suma de los Totales de Costo del detalle del Producto '
                                                      'Compuesto.')
    tiempo_elaboracion = models.TimeField(verbose_name='Tiempo Elaboracion',  # default=datetime.time(00, 15, 00),
                                          null=True, blank=True,
                                          help_text='Corresponde al tiempo estimado que tomara elaborar el Producto '
                                                    'Compuesto')
    # fecha_elaboracion = models.DateField(verbose_name='Fecha de Elaboracion', default=datetime.date.today(),
    #                                      help_text='Ingrese la fecha de elaboracion del Producto.')

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

        # if self.tipo_producto == 'VE':
        #     self._meta.get_field('porcentaje_ganancia').

        super(Producto, self).__init__(*args, **kwargs)

    def get_precio_venta_sugerido(self):
        producto = Producto.objects.get(id=self.pk)
        precio_venta_sugerido = (((self.get_precio_compra_sugerido() * producto.porcentaje_ganancia) / 100) +
                                 self.get_precio_compra_sugerido())
        print 'precio_compra_sugerido: %s * porcentaje_ganancia: %s - precio_venta_sugerido: %s' % \
              (self.get_precio_compra_sugerido(), producto.porcentaje_ganancia, precio_venta_sugerido)
        return precio_venta_sugerido
    # precio_venta_sugerido.help_text = 'Precio de Venta sugerido calculado a partir del promedio del Costo de ' \
    #                                   'Compra del producto en el ultimo mes por el Porcentaje de Ganancia'

    def get_precio_compra_sugerido(self):
        detalles = CompraDetalle.objects.filter(producto_compra_id=self.pk,
                                                numero_compra__estado_compra__estado_orden_compra='CON')
        # hoy = timezone_today()
        # fecha = '%s-%s-01'%(hoy.year,('0%s'%(hoy.month-1) if len(str(hoy.month-1))==1 else (hoy.month-1)))
        # fecha = datetime.date.today() - datetime.timedelta(days=30)
        fecha = timezone.now() - datetime.timedelta(days=30)
        # print 'Fecha para calculo promedio: %s' % fecha
        detalles = detalles.filter(numero_compra__fecha_compra__gte=fecha)
        total = 0
        cantidad = 0
        # precio_compra_sugerido = 0

        for detalle in detalles:
            print detalle.numero_compra.estado_compra.estado_compra
            total += detalle.precio_producto_compra
            # cantidad += detalle.cantidad_producto_compra
            cantidad += 1
        print total, cantidad
        precio_compra_sugerido = total / (cantidad if cantidad else 1)
        print 'precio_compra_sugerido: %s' % precio_compra_sugerido
        return precio_compra_sugerido if precio_compra_sugerido else 0  # total / (cantidad if cantidad else 1)
    # precio_compra_sugerido.help_text = 'Este valor se calcula promediando el Costo de Compra del Producto en los ' \
    #                                    'ultimos 30 dias.'

    def clean(self):
        # Valida que el porcentaje_ganancia no sea 0.
        if self.tipo_producto == 'VE':
            if self.porcentaje_ganancia == 0:
                raise ValidationError({'porcentaje_ganancia': _('El Porcentaje de Ganancia del Producto para la '
                                                                'venta no puede ser 0.')})

            # Valida que el precio_venta_sugerido no sea 0.
            if self.precio_venta == 0:
                raise ValidationError({'precio_venta': _('El Precio de Venta del Producto no puede ser 0.')})

        # Valida que el precio_compra no sea 0.
        if self.precio_compra == 0:
            raise ValidationError({'precio_compra': _('El Precio de Compra del Producto no puede ser 0.')})

        # Valida que el precio_compra no sea que el precio_compra_sugerido.
        if self.precio_compra < self.get_precio_compra_sugerido():
            raise ValidationError({'precio_compra': _('El Precio de Compra del Producto no puede ser menor que '
                                                      'el Precio de Compra Sugerido.')})

    def __unicode__(self):
        return "ID Prod: %s - Prod: %s - Marca: %s" % (self.id, self.producto, self.marca)


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
    # ==> Datos del Producto <==
        # self._meta.get_field('tipo_producto').default = TipoProducto.objects.get(tipo_producto="VE")
        # self._meta.get_field('compuesto').default = True
        self.codigo_barra = "N/A"
        self.marca = "N/A"
    # ==> Contenido del Producto <==
        self.tipo_producto = "VE"  # TipoProducto.objects.get(tipo_producto="VE")
        self.compuesto = True
        self.perecedero = True
        self.unidad_medida_contenido = UnidadMedidaProducto.objects.get(unidad_medida_producto="UN")
        self.contenido = 1
    # ==> Utilidad <==
        # self._meta.get_field('precio_venta_sugerido').help_text = 'Precio de Venta sugerido calculado a partir ' \
        #                                                           'del Costo de Elaboracion por el Porcentaje de ' \
        #                                                           'Ganancia.'
    # ==> Datos para la Compra <==
        self.unidad_medida_compra = UnidadMedidaProducto.objects.get(unidad_medida_producto="UN")
        self.precio_compra = 0
        # self.precio_compra_sugerido = 0
        # self.fecha_elaboracion = datetime.date.today()
        # self.fecha_vencimiento = datetime.date.today() + datetime.timedelta(days=3)

    def clean(self):
        # Valida que el porcentaje_ganancia no sea 0.
        if self.porcentaje_ganancia == 0:
            raise ValidationError({'porcentaje_ganancia': _('El Porcentaje de Ganancia del Producto Compuesto o '
                                                            'Elaborado no puede ser 0.')})

        # Valida que el precio_venta_sugerido no sea 0.
        if self.precio_venta == 0:
            raise ValidationError({'precio_venta': _('El Precio de Venta del Producto Compuesto o Elaborado no '
                                                     'puede ser 0.')})

    def __unicode__(self):
        return "ID Prod: %s - Prod: %s" % (self.id, self.producto)


class ProductoCompuestoDetalle(models.Model):
    producto_compuesto = models.ForeignKey('ProductoCompuesto', related_name="producto_cabecera", null=True)

    # Limitar los Productos que pueden ser seleccionados a los que poseen TipoProducto igual a Insumos.
    producto = models.ForeignKey('Producto', related_name="producto_detalle", null=True,
                                 limit_choices_to={'tipo_producto': "IN"},
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


class ProductoVenta(Producto):
    """
    01/10/2016: Productos disponibles para la Venta.

    Se crea esta vista para filtrar los Productos para la Venta que seran visualizados en la pantalla de Pedidos.
    No se realiza ninguna carga de datos en esta pantalla.
    """

    class Meta:
        proxy = True
        verbose_name = 'Producto para la Venta'
        verbose_name_plural = 'Productos - Productos para la Venta'

    def __unicode__(self):
        return "ID Prod: %s - Prod: %s" % (self.id, self.producto)


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
#
#     # cantidad_existente = models.DecimalField(max_digits=10, decimal_places=3, verbose_name='Cantidad Existente',
#     #                                          help_text='Cantidad existente en Stock.')
#
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
# class Stock(models.Model):
#     """
#     21/06/2016: Registrar inventario y ajustes de inventario.
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
class MovimientoStock(models.Model):
    """
    26/09/2016: Registrar inventario y ajustes de inventario.
    * Registro de los Movimientos de Inventario.

    * Listar los Productos y/o Stock disponible.
    """
    TIPOS_MOVIMIENTO_STOCK = (
        ('VE', 'Venta'),
        ('CO', 'Compra'),
        # ('ME', 'Mermas'),
        ('TR', 'Transferencias'),
        # ('DE', 'Devoluciones'),
    )

    # stock = models.ForeignKey('Stock')
    producto_stock = models.ForeignKey('Producto', related_name='producto_stock',  # default=2,
                                       verbose_name='Producto',
                                       help_text='Seleccione el Producto a registrar en el Stock.')
#     tipo_movimiento = models.ForeignKey('bar.TipoMovimientoStock', default=1,
#                                         verbose_name='Tipo de Movimiento',
#                                         help_text='Seleccione el identificador del Tipo de Movimiento de Stock.')
    tipo_movimiento = models.CharField(max_length=2, choices=TIPOS_MOVIMIENTO_STOCK,
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
        # En la tabla solo puede existir un registro para cada Producto en cada Deposito
        # Consultar si es correcto aplicar esta restriccion de esta manera
        # 08/08/2016: Finalmente traslade el campo "ubicacion" a StockDetalle
        # unique_together = ("producto_stock", "ubicacion")
        verbose_name = 'Movimientos de Stock'
        verbose_name_plural = 'Movimientos de Stock'

    # VALIDACIONES/FUNCIONALIDADES
    # 1) Controlar que la cantidad_existente no sea menor que el stock_minimo y alertar en caso de ser menor.
    # 2) Validar que la cantidad_existente no sea negativa.
    # 3) Realizar el calculo de la cantidad_existente (suma total de cantidad_entrante - cantidad_saliente)
    # 4) Idear una vista HTML que presente la Cantidad Total Existente del Producto.

    # def clean(self):
    #     # 2) Valida que la cantidad_existente no sea negativa.
    #     if self.cantidad_existente < 0:
    #         raise ValidationError({'cantidad_existente': _('La cantidad existente del Producto no puede ser menor a '
    #                                                        'cero o negativa.')})

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
        return "Prod: %s" % self.producto_stock


# ======================================================================================================================
# class IngresoDeposito(models.Model):
#     """
#     25/09/2016: Cuando una Compra es confirmada debe generar un registro en esta tabla para que el Encargado del
#     Deposito ubique los productos en un lugar preciso dentro del Deposito.
#     """
#     compra = models.ForeignKey('compras.Compra')
#     producto = models.ForeignKey('Producto')
#     piso = models.ForeignKey('bar.Piso')
#     pasillo = models.ForeignKey('bar.Pasillo')
#     estante = models.ForeignKey('bar.Estante')
#     nivel = models.ForeignKey('bar.Nivel')
#     hilera = models.ForeignKey('bar.Hilera')
#     camara = models.ForeignKey('bar.CamaraFrigorifica', default=1)
#
#     class Meta:
#         verbose_name = 'Ingreso de Producto a Deposito'
#         verbose_name_plural = 'Stock - Ingresos de Productos a Deposito'


# ======================================================================================================================
class InventarioProducto(models.Model):
    """
    Genera una vista con la agrupacion de los movimientos de Stock por Producto calculando el campo "cantidad_existente"
    """
    # id_producto = models.PositiveIntegerField()
    producto = models.CharField(max_length=50)
    total_compras = models.IntegerField()
    total_ventas = models.IntegerField()
    cantidad_existente = models.IntegerField()

    class Meta:
        # Definir si va ser una tabla proxy o multitable
        # proxy = True
        verbose_name = 'Inventario por Producto'
        verbose_name_plural = 'Stock - Inventarios por Productos'
        db_table = 'inventario_por_producto'
        managed = False


# class StockDeposito(Stock):
#     """
#     Genera una vista con la agrupacion de los movimientos de Stock por Deposito calculando el campo
#     "cantidad_existente"
#     """
#
#     class Meta:
#         # Definir si va ser una tabla proxy o multitable
#         # proxy = True
#         verbose_name = 'Inventario por Deposito'
#         verbose_name_plural = 'Stock - Inventarios por Depositos'


# class StockAjuste(Stock):
#     """
#     25/09/2016: Registrar ajustes de inventario.
#     """
#
#     class Meta:
#         # Definir si va ser una tabla proxy o multitable
#         # proxy = True
#         verbose_name = 'Ajuste de Inventario'
#         verbose_name_plural = 'Stock - Ajustes de Inventario'


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
    producto_transferencia = models.ForeignKey('Producto', related_name='producto_solicitado',
                                               # limit_choices_to={'cantidad_existente' > 0},
                                               # limit_choices_to=Q(cantidad_existente__gt=0),
                                               verbose_name='Producto a Transferir',
                                               help_text='Seleccione el producto a Transferir entre depositos.')

    deposito_origen_transferencia = models.ForeignKey('bar.Deposito', related_name='deposito_proveedor',
                                                      verbose_name='Deposito Proveedor',
                                                      help_text='Seleccione el Deposito que se encargara de '
                                                                'procesar la Transferencia.')
    cantidad_existente_stock = models.DecimalField(max_digits=10, decimal_places=3, default=0,
                                                   verbose_name='Cantidad Existente',
                                                   help_text='Despliega la cantidad existente del Producto en el '
                                                             'Deposito Proveedor seleccionado.')
    cantidad_producto_transferencia = models.DecimalField(max_digits=10, decimal_places=3,
                                                          verbose_name='Cantidad a Transferir',
                                                          help_text='Cantidad a Transferir del producto.')
    deposito_destino_transferencia = models.ForeignKey('bar.Deposito', related_name='deposito_solicitante',
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
    fecha_hora_autorizacion_transferencia = models.DateTimeField(auto_now=True, null=True, blank=True,
                                                                 verbose_name='Fecha/hora autorizacion Transferencia',
                                                                 help_text='La fecha y hora se asignan al momento de '
                                                                           'autorizarse la Transferencia. No se '
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
        # self.estado_transferencia = TransferenciaStockEstado.objects.get(estado_transferencia_stock="PEN")
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

    # def clean(self):
    #     # Valida que el usuario_autorizante_transferencia no sea vacio o nulo, esta condicion no deberia darse ya que
    #     # este campo se completa con el dato del usuario logueado al Sistema al momento de confirmar la transferencia.
    #     if self.usuario_autorizante_transferencia is None:
    #         raise ValidationError({'usuario_autorizante_transferencia': _('Se debe seleccionar el Usuario Autorizante '
    #                                                                       'de la Transferencia que debe ser el usuario '
    #                                                                       'logueado al Sistema.')})

    def __unicode__(self):
        return "ID: %s - Prod. Trans: %s" % (self.id, self.producto_transferencia)

# ======================================================================================================================
# En la revision del 07/09/2016 con el Prof. Diego Ruiz Diaz Gamarra me indico que podiamos descartar programar
# las pantallas de Devoluciones y Mermas en el modulo de Stock.
#
# class Mermas(models.Model):
#     """
#     21/06/2016: Registrar mermas de productos. Las mermas descuentan el stock existente.
#     """
#
#
# class Devolucion(models.Model):
#     """
#     Cuando la Compra llega a los estados de CON o CAN ya no puede volver a ser modificada.
#     En el caso de que una Compra confirmada deba ser devuelta se debe registrar el proceso en el modelo de
#     Devoluciones.
#     """
#
#     class Meta:
#         verbose_name = 'Stock - Devolucion'
#         verbose_name_plural = 'Stock - Devoluciones'