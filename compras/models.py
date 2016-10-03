import datetime
# import uuid
# import string
# import random
from django.core.validators import RegexValidator
from django.db import models
from django.db.models import Q
# from polymorphic.models import PolymorphicModel
from django.utils import timezone
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
from django.utils.safestring import mark_safe
from bar.models import CompraEstado, OrdenCompraEstado, FacturaProveedorEstado

# Create your models here.

numeric = RegexValidator(r'^[0-9]*$', 'Solo se permiten caracteres numericos.')
numero_factura = RegexValidator(r'^999-999-9999999$', 'Ingrese el Numero de Factura en el formato "999-999-9999999".')


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
    # El RUC debe ser del tipo PositiveInteger, solo se deben poder ingresar numeros positivos.
    ruc = models.CharField(max_length=10, unique=True, validators=[numeric],
                           verbose_name='RUC',  # default=1,
                           help_text='Ingrese el RUC del Proveedor.')
    persona_proveedor = models.ForeignKey('bar.Persona', default=1, verbose_name='Persona',
                                          help_text='Indique si el Proveedor tiene personeria Fisica o Juridica.')
    # El Digito Verificador debe ser calculado tomando el RUC ingresado por el usuario.
    digito_verificador = models.IntegerField(help_text='Digito verificador del RUC del Proveedor. Este campo se '
                                                       'calcula tomando el RUC ingresado.')  # default=1,

    # ===============================================================================================================
    # Intento de asignacion del Digito Verificador utilizando el decorador @property y la funcion "calcular"
    # @property
    # def digito_verificador(self):
    #     """
    #     El Digito Verificador debe ser calculado tomando el RUC ingresado por el usuario.
    #     """
    #     if self.ruc:
    #         ruc = int(self.ruc)
    #         dv = (ruc * 10 / 5) + 3
    #         # return calcular(self.ruc, 11)
    #         return int(dv)
    #     else:
    #         return u'RUC no valido.'
    # # digito_verificador.short_description = 'Digito Verificador'

    # def calcular(numero, basemax):
    # ===============================================================================================================

    # Agregados el 18/05/2016
    direccion = models.CharField(max_length=200, null=True, help_text='Ingrese la Direccion del Proveedor. '
                                                                      '(Hasta 200 caracteres)')
    pais = models.ForeignKey('bar.Pais', verbose_name='Pais', help_text='Seleccione el Pais del Proveedor.')
    ciudad = models.ForeignKey('bar.Ciudad', verbose_name='Ciudad',
                               help_text='Seleccione la Ciudad del Proveedor.')
    pagina_web = models.URLField(null=True, blank=True)

    # Agregado el 24/05/2016
    fecha_alta_proveedor = models.DateTimeField(auto_now_add=True,  # editable=True,  # default=timezone.now(),
                                                verbose_name='Fecha de Alta',
                                                help_text='La Fecha de Alta se asigna al momento de guardar los datos '
                                                          'del Proveedor. No se requiere el ingreso de este dato.')
    empresa_administrada = models.BooleanField(default=False, help_text='Diferencia las empresas administradas de las '
                                                                        'proveedoras.')

    class Meta:
        verbose_name = 'Proveedor'
        verbose_name_plural = 'Proveedores'

    # VALIDACIONES/FUNCIONALIDADES
    # ============================
    # 1) Implementar el calculo del Digito Verificador del RUC tomando la funcion publicada por la SET. OK!

    def __init__(self, *args, **kwargs):
        self._meta.get_field('empresa_administrada').default = False
        super(Proveedor, self).__init__(*args, **kwargs)

    def __unicode__(self):
        return "%s" % self.proveedor


class LineaCreditoProveedor(models.Model):
    """
    Agregado el 24/05/2016.
    Registra los montos de las Lineas de Credito ofrecidas por el Proveedor en el tiempo.
    Solo una Linea de Credito puede estar vigente a la vez. Se debe controlar el estado de las Lineas de Credito.
    Con este parametro se debe controlar que las compras a credito realizadas no superen la Linea de Credito.

    21/06/2016: Registrar creditos con proveedores.
    """
    ESTADOS_LINEA_CREDITO = (
        ('DEL', 'Dentro de la Linea de Credito'),
        ('LIM', 'En el Limite'),
        ('SOB', 'Sobregirada'),
    )

    # id = models.AutoField(primary_key=True)
    proveedor = models.OneToOneField('Proveedor')
    linea_credito_proveedor = models.DecimalField(max_digits=18, decimal_places=0, default=0,
                                                  verbose_name='Monto Linea de Credito',
                                                  help_text='Ingrese el monto ofrecido por el proveedor como Linea de '
                                                            'Credito.')
    fecha_linea_credito_proveedor = models.DateTimeField(auto_now=True,  # default=timezone.now(),
                                                         verbose_name='Fecha/hora de registro',
                                                         help_text='La fecha/hora en la que se registra la Linea de '
                                                                   'Credito ofrecida por el Proveedor se asigna de '
                                                                   'forma automatica.')
    monto_total_facturas_proveedor = models.DecimalField(max_digits=18, decimal_places=0, default=0,
                                                         verbose_name='Monto Total Facturas',
                                                         help_text='Este valor se calcula automaticamente y '
                                                                   'corresponde a la suma de todas las Facturas '
                                                                   'registradas para el Proveedor.')
    monto_total_pagos_proveedor = models.DecimalField(max_digits=18, decimal_places=0, default=0,
                                                      verbose_name='Monto Total Pagos',
                                                      help_text='Este valor se calcula automaticamente y corresponde a '
                                                                'la suma de todos los Pagos registrados para el '
                                                                'Proveedor.')
    uso_linea_credito_proveedor = models.DecimalField(max_digits=18, decimal_places=0, default=0,
                                                      verbose_name='Monto Utilizado Linea de Credito',
                                                      help_text='Este valor se calcula automaticamente como la '
                                                                'diferencia entre el Monto Total de las Facturas '
                                                                'contra el Monto Total de los Pagos.')
    disponible_linea_credito_proveedor = models.DecimalField(max_digits=18, decimal_places=0, default=0,
                                                             verbose_name='Monto Disponible Linea de Credito',
                                                             help_text='Este valor se calcula automaticamente como la '
                                                                       'diferencia entre el Monto de la Linea de '
                                                                       'Credito y el Monto Utilizado de la Linea de '
                                                                       'Credito.')
    # estado_linea_credito_proveedor = models.ForeignKey('bar.LineaCreditoProveedorEstado',  # default=1,
    estado_linea_credito_proveedor = models.CharField(max_length=3, choices=ESTADOS_LINEA_CREDITO,
                                                      blank=True,  # default='DEL', # unique=True,
                                                      verbose_name='Estado Linea de Credito',
                                                      help_text='Se asigna automaticamente de acuerdo a la '
                                                                'utilizacion de la Linea de Credito.')
    # help_text='Solo una Linea de Credito puede estar activa. '
    #         'La intencion es llevar un control de los cambios '
    #         'de la Linea de Credito en el tiempo.')

    class Meta:
        verbose_name = 'Linea de Credito Proveedor'
        verbose_name_plural = 'Proveedores - Lineas de Credito'

    # VALIDACIONES/FUNCIONALIDADES
    # ============================
    # 1) Solo una Linea de Credito puede estar vigente a la vez. Se debe controlar el estado de las Lineas de Credito.
    # 2) Con este parametro se debe controlar que las Compras a credito realizadas no superen la Linea de Credito.

    def get_monto_total_facturas_proveedor(self):
        detalle_linea_credito = LineaCreditoProveedorDetalle.objects.filter(linea_credito_proveedor_id=self.id,
                                                                            tipo_movimiento='FAC')
        total_facturas = 0
        for detalle in detalle_linea_credito:
            total_facturas += detalle.monto_movimiento
            print 'Detalle: %s - monto_movimiento: %s - total_facturas: %s' % \
                  (detalle, detalle.monto_movimiento, total_facturas)
        # self.monto_total_facturas_proveedor = total_facturas
        # self.save()
        return total_facturas

    def get_monto_total_pagos_proveedor(self):
        detalle_linea_credito = LineaCreditoProveedorDetalle.objects.filter(linea_credito_proveedor_id=self.id,
                                                                            tipo_movimiento='PAG', anulado=False)
        total_pagos = 0
        for detalle in detalle_linea_credito:
            total_pagos += detalle.monto_movimiento
            print 'Detalle: %s - monto_movimiento: %s - total_pagos: %s' % \
                  (detalle, detalle.monto_movimiento, total_pagos)
        return total_pagos

    def get_uso_linea_credito_proveedor(self):
        # uso_linea_credito = 0
        total_facturas = self.get_monto_total_facturas_proveedor()
        total_pagos = self.get_monto_total_pagos_proveedor()
        uso_linea_credito = total_facturas - total_pagos
        print 'Uso Linea Credito: %s' % uso_linea_credito
        return uso_linea_credito

    def get_disponible_linea_credito_proveedor(self):
        disponible_linea_credito = self.linea_credito_proveedor - self.get_uso_linea_credito_proveedor()
        print 'Disponible Linea Credito: %s' % disponible_linea_credito
        return disponible_linea_credito

    def get_estado_linea_credito_proveedor(self):
        estado_linea_credito_proveedor = "DEL"
        if self.get_uso_linea_credito_proveedor() < self.linea_credito_proveedor and \
                self.get_disponible_linea_credito_proveedor() > 0:
            estado_linea_credito_proveedor = "DEL"
        elif self.get_uso_linea_credito_proveedor() == self.linea_credito_proveedor and \
                self.get_disponible_linea_credito_proveedor() == 0:
            estado_linea_credito_proveedor = "LIM"
        elif self.get_uso_linea_credito_proveedor() > self.linea_credito_proveedor and \
                self.get_disponible_linea_credito_proveedor() < 0:
            estado_linea_credito_proveedor = "SOB"
        return estado_linea_credito_proveedor

    # def __init__(self, *args, **kwargs):
    #     super(LineaCreditoProveedor, self).__init__(*args, **kwargs)
    #     self._meta.get_field('monto_total_facturas_proveedor') = self.get_monto_total_facturas_proveedor()
    #     self.monto_total_facturas_proveedor = self.get_monto_total_facturas_proveedor()
    #     self.initial['monto_total_facturas_proveedor'] = self.get_monto_total_facturas_proveedor()
    #     self.initial['monto_total_pagos_proveedor'] = self.instance.get_monto_total_pagos_proveedor()
    #     self.initial['uso_linea_credito_proveedor'] = self.instance.get_uso_linea_credito_proveedor()
    #     self.initial['disponible_linea_credito_proveedor'] = self.instance.get_disponible_linea_credito_proveedor()
    #     self.initial['estado_linea_credito_proveedor'] = self.instance.get_estado_linea_credito_proveedor()

    def __unicode__(self):
        # return "%s - %s - %s" % (self.proveedor, self.linea_credito_proveedor, self.fecha_linea_credito_proveedor)
        return "%s - %s" % (self.proveedor, self.linea_credito_proveedor)


class LineaCreditoProveedorDetalle(models.Model):
    """
    Detalle de LineaCreditoProveedor que lleva el registro de las facturas y los pagos y realiza un balance para saber
    si la Linea de Credito no fue superada.
    """
    TIPOS_MOVIMIENTO = (
        ('PAG', 'Pago'),
        ('FAC', 'Factura'),
    )
    linea_credito_proveedor = models.ForeignKey('LineaCreditoProveedor')
    tipo_movimiento = models.CharField(max_length=3, choices=TIPOS_MOVIMIENTO,
                                       verbose_name='Tipo de Movimiento',
                                       help_text='Registra el Tipo de Movimiento.')
    monto_movimiento = models.DecimalField(max_digits=18, decimal_places=0, default=0,
                                           verbose_name='Monto del Movimiento',
                                           help_text='Registra el Monto del Movimiento.')
    # numero_comprobante = models.IntegerField(verbose_name='Numero Comprobante Movimiento',
    numero_comprobante = models.CharField(max_length=15,  # blank=True,  # default=1,
                                          verbose_name='Numero Comprobante Movimiento',
                                          help_text='Corresponde al Numero de Factura o Numero de Comprobante '
                                                    'de Pago del movimiento.')
    fecha_movimiento = models.DateField(default=timezone.now, verbose_name='Fecha Registro Movimiento',
                                        help_text='Registra la fecha del movimiento.')
    anulado = models.BooleanField(default=False)
    fecha_hora_anulacion = models.DateTimeField(null=True, blank=True, verbose_name='Fecha/hora Anulacion')

    class Meta:
        verbose_name = 'Detalle Linea de Credito con Proveedor'
        verbose_name_plural = 'Lineas de Credito con Proveedores - Detalles'

    def __unicode__(self):
        return "Lin. Cred: %s - ID Detalle: %s" % (self.linea_credito_proveedor, self.id)


class ProveedorTelefono(models.Model):
    """
    Almacena los datos de los numeros telefonicos de los Proveedores.
    """
    # id = models.AutoField(primary_key=True)
    proveedor = models.ForeignKey('Proveedor')
    codigo_pais_telefono = models.ForeignKey('bar.CodigoPaisTelefono',  # default=595
                                             verbose_name='Codigo Pais')
    codigo_operadora_telefono = models.ForeignKey('bar.CodigoOperadoraTelefono',  # default=21
                                                  verbose_name='Codigo Operadora',
                                                  help_text='Seleccione o ingrese el codigo de ciudad u '
                                                            'operadora de telefonia movil.')
    telefono = models.IntegerField(help_text='Ingrese el telefono fijo o movil del Proveedor. El dato debe contener '
                                             'solo numeros.')
    interno = models.IntegerField(null=True, blank=True, help_text='Ingrese el numero de interno.')
    contacto = models.CharField(max_length=100, null=True, blank=True, help_text='Nombre de la persona a la cual '
                                                                                 'contactar en este numero. (Hasta 100 '
                                                                                 'caracteres)')

    class Meta:
        verbose_name = 'Telefono del Proveedor'
        verbose_name_plural = 'Proveedores - Telefonos'

    def __unicode__(self):
        return "%s - %s - %s - %s" % (self.proveedor, self.codigo_pais_telefono, self.codigo_operadora_telefono,
                                      self.telefono)


class OrdenPago(models.Model):
    """
    11/09/2016: Registra los datos de las Ordenes de Pago de facturas de los Proveedores.
    """
    numero_orden_pago = models.AutoField(primary_key=True,
                                         verbose_name='Numero Orden de Pago',
                                         help_text='Este dato se genera automaticamente cada vez que se va crear '
                                                   'una Orden de Pago.')
    proveedor_orden_pago = models.ForeignKey('Proveedor',
                                             verbose_name='Proveedor',
                                             help_text='Seleccione el Proveedor para el cual se generara la Orden de '
                                                       'Pago.')
    fecha_hora_orden_pago = models.DateTimeField(auto_now=True,  # editable=True, auto_now_add=True,
                                                 verbose_name='Fecha/hora Orden de Pago',
                                                 help_text='La fecha y hora de la Orden de Pago se asignan al momento '
                                                           'de guardar los datos del pago. No se requiere el ingreso '
                                                           'de este dato.')
    usuario_registro_orden_pago = models.ForeignKey('personal.Empleado',  # default=1,
                                                    related_name='usuario_registro_orden_pago',
                                                    # limit_choices_to='',
                                                    # to_field='usuario',
                                                    verbose_name='Preparado por?',
                                                    help_text='Usuario que registro la Orden de Pago.')
    total_orden_pago = models.DecimalField(max_digits=18, decimal_places=0, default=0,  # blank=True,
                                           verbose_name='Total Orden de Pago')  # blank=False (Default is False)
    # estado_orden_pago = models.CharField(max_length=3, choices=ESTADOS_ORDEN_PAGO,  # default='PEN',
    estado_orden_pago = models.ForeignKey('bar.OrdenPagoEstado',  # default=1,
                                          blank=True,  # unique=True,
                                          verbose_name='Estado Orden de Pago',
                                          help_text='Se asigna automaticamente de acuerdo a la accion que se realice '
                                                    'con la Orden de Pago.')

    motivo_anulacion = models.CharField(max_length=200, null=True, blank=True)
    observaciones_anulacion = models.CharField(max_length=200, null=True, blank=True)
    usuario_anulacion = models.ForeignKey('personal.Empleado', null=True, blank=True,
                                          related_name='usuario_anulacion_orden_pago',
                                          # limit_choices_to='',
                                          #  to_field='usuario',
                                          verbose_name='Anulado por?',
                                          help_text='Usuario que anulo la Orden de Pago.')
    fecha_hora_anulacion = models.DateTimeField(null=True, blank=True)

    class Meta:
        verbose_name = 'Orden de Pago Proveedor'
        verbose_name_plural = 'Proveedores - Ordenes de Pago'

    def clean(self):

        # import pdb
        # pdb.set_trace()

        # Valida que el Total de la Orden de Pago no sea 0
        if self.pk is not None:
            orden_pago_inicial = OrdenPago.objects.get(pk=self.pk)
            if self.proveedor_orden_pago == orden_pago_inicial.proveedor_orden_pago:
                if self.total_orden_pago == 0:
                    raise ValidationError({'total_orden_pago': _('El Total de la Orden de Pago no puede ser 0.')})

    def __unicode__(self):
        return "Nro. Orden Pago: %s - Proveedor: %s" % (self.numero_orden_pago, self.proveedor_orden_pago)


class OrdenPagoDetalle(models.Model):
    """
    18/09/2016: Registra los datos del detalle de las Ordenes de Pago de facturas de los Proveedores.
    """
    ESTADOS_FACTURA_COMPRA = (
        # ('PEN', 'Pendiente'),
        ('EPP', 'En Plazo de Pago'),
        ('FPP', 'Fuera del Plazo de Pago'),
        ('PAG', 'Pagada'),
        ('CAN', 'Cancelada'),
    )
    numero_orden_pago = models.ForeignKey('OrdenPago')
    compra = models.ForeignKey('Compra', limit_choices_to={'estado_compra__estado_orden_compra': "ENT"},
                               verbose_name='Compra Asociada',
                               help_text='Seleccione la Compra cuya Factura sera registrada.')
    # Verificar que se inserte correctamente el dato del Proveedor en esta tabla.
    proveedor = models.ForeignKey('Proveedor',  # default=2,
                                  verbose_name='Proveedor',
                                  help_text='Seleccione el Proveedor.')
    numero_factura_compra = models.CharField(max_length=15,  # blank=True,  # default=1,
                                             # validators=[numero_factura],
                                             verbose_name='Numero de Factura',
                                             help_text='Ingrese el Numero de Factura que acompana la Compra.')
    fecha_factura_compra = models.DateField(default=datetime.date.today,
                                            verbose_name='Fecha de la Factura',
                                            help_text='Ingrese la fecha de la Factura.')
    tipo_factura_compra = models.ForeignKey('bar.TipoFacturaCompra', verbose_name='Tipo de Factura',
                                            help_text='Seleccione el Tipo de Factura.')
    forma_pago_compra = models.ForeignKey('bar.FormaPagoCompra', verbose_name='Forma de Pago',
                                          help_text='Seleccione la Forma de Pago para esta Factura.')
    plazo_factura_compra = models.PositiveIntegerField(verbose_name='Plazo de Pago',
                                                       help_text='En caso de Credito establecer el plazo de tiempo en '
                                                                 'dias para el pago.')
    total_factura_compra = models.DecimalField(max_digits=18, decimal_places=0, default=0,
                                               verbose_name='Monto Total de la Factura',
                                               help_text='Este valor se calcula automaticamente en funcion al detalle '
                                                         'de la Compra.')
    # estado_factura_compra = models.CharField(max_length=3, choices=ESTADOS_FACTURA_COMPRA,
    estado_factura_compra = models.ForeignKey('bar.FacturaProveedorEstado',  # default=1,
                                              blank=True,  # default="EPP",
                                              verbose_name='Estado de la Factura',
                                              help_text='Indique el Estado de la Factura de la Compra de acuerdo a los '
                                                        'pagos aplicados para la misma.')
    procesado = models.BooleanField(default=False, verbose_name='Procesar?',
                                    help_text='Marque esta casilla si la factura sera incluida en la Orden de Pago.')

    class Meta:
        verbose_name = 'Detalle Orden de Pago Proveedor'
        verbose_name_plural = 'Ordenes de Pago Proveedores - Detalles'

    def __unicode__(self):
        return "Nro. Orden Pago: %s - ID Detalle: %s" % (self.numero_orden_pago, self.id)


class PagoProveedor(models.Model):
    """
    21/06/2016: Registrar pagos a proveedores.
    """
    factura_proveedor = models.ForeignKey('FacturaProveedor',  # default=1,
                                          verbose_name='Factura Proveedor',
                                          help_text='Seleccione la Factura a la cual se aplicara el Pago.')
    monto_pago_proveedor = models.DecimalField(max_digits=18, decimal_places=0,  # default=0,
                                               verbose_name='Monto de Pago al Proveedor',
                                               help_text='Ingrese el monto abonado al Proveedor.')
    fecha_pago_proveedor = models.DateField(default=timezone.now, verbose_name='Fecha Pago Proveedor',
                                            # default=timezone.now(), auto_now_add=True,
                                            help_text='Ingrese la fecha del Pago al Proveedor.')
    numero_comprobante_pago = models.IntegerField(verbose_name='Numero de Comprobante de Pago',  # default=0,
                                                  help_text='Ingrese el Numero del Comprobante de Pago. El '
                                                            'comprobante puede ser una Nota de Credito que anula o '
                                                            'cancela la factura de la Compra en caso de que la misma '
                                                            'se haya devuelto o cancelado.')
    # numero_nota_credito = models.IntegerField(verbose_name='Numero Nota de Credito', default=0,
    #                                           help_text='Ingrese el Numero de la Nota de Credito que anula o cancela '
    #                                                     'la factura de la Compra en caso de que la misma se haya '
    #                                                     'devuelto o cancelado.')
    procesado = models.BooleanField(default=False)
    anulado = models.BooleanField(default=False)
    fecha_hora_anulacion = models.DateTimeField(null=True, blank=True, verbose_name='Fecha/hora Anulacion')

    class Meta:
        verbose_name = 'Pago a Proveedores'
        verbose_name_plural = 'Pagos a Proveedores'

    # VALIDACIONES/FUNCIONALIDADES
    # ============================
    # 1) Deshabilitar "Agregar Pago A Proveedores adicional." cuando se intenta agregar una Factura/Pago.
    # 2) Validar la LineaCreditoProveedor con el Proveedor de acuerdo a las Ordenes de Compra y Pagos realizados.
    # La suma de las Ordenes de Compra contra los Pagos realizados no debe superar la Linea de Credito habilitada con
    # el Proveedor.
    # Al guardar un PagoProveedor se debe generar un registro en LineaCreditoProveedorDetalle

    def __unicode__(self):
        return "ID: %s - Pago: %s" % (self.id, self.monto_pago_proveedor)


class FacturaProveedor(models.Model):
    """
    Registrar facturas pendienes de pago.
    """
    # Filtrar las Compras que estan pendientes de pago
    compra = models.ForeignKey('Compra', limit_choices_to={'estado_compra__estado_orden_compra': "ENT"},
                               verbose_name='Compra Asociada',
                               help_text='Seleccione la Compra cuya Factura sera registrada.')
    # Verificar que se inserte correctamente el dato del Proveedor en esta tabla.
    proveedor = models.ForeignKey('Proveedor', default=2,
                                  verbose_name='Proveedor',
                                  help_text='Seleccione el Proveedor.')

    # numero_orden_pago = models.OneToOneField('OrdenPago', null=True)

    numero_factura_compra = models.CharField(max_length=15,  # blank=True,  # default=1,
                                             # validators=[numero_factura],
                                             verbose_name='Numero de Factura',
                                             help_text='Ingrese el Numero de Factura que acompana la Compra.')
    fecha_factura_compra = models.DateField(default=datetime.date.today,
                                            verbose_name='Fecha de la Factura',
                                            help_text='Ingrese la fecha de la Factura.')
    tipo_factura_compra = models.ForeignKey('bar.TipoFacturaCompra', verbose_name='Tipo de Factura',
                                            help_text='Seleccione el Tipo de Factura.')
    forma_pago_compra = models.ForeignKey('bar.FormaPagoCompra', verbose_name='Forma de Pago',
                                          help_text='Seleccione la Forma de Pago para esta Factura.')
    plazo_factura_compra = models.PositiveIntegerField(verbose_name='Plazo de Pago',
                                                       help_text='En caso de Credito establecer el plazo de tiempo en '
                                                                 'dias para el pago.')
    total_factura_compra = models.DecimalField(max_digits=18, decimal_places=0, default=0,
                                               verbose_name='Monto Total de la Factura',
                                               help_text='Este valor se calcula automaticamente en funcion al detalle '
                                                         'de la Compra.')
    total_pago_factura = models.DecimalField(max_digits=18, decimal_places=0, default=0,
                                             verbose_name='Monto Total Pagado de la Factura',
                                             help_text='Este valor se calcula automaticamente en funcion a los pagos '
                                                       'registrados para la Factura.')
    # estado_factura_compra = models.CharField(max_length=3, choices=ESTADOS_FACTURA_COMPRA,
    estado_factura_compra = models.ForeignKey('bar.FacturaProveedorEstado',  # default=1,
                                              blank=True,  # default="EPP",
                                              verbose_name='Estado de la Factura',
                                              help_text='Indique el Estado de la Factura de la Compra de acuerdo a los '
                                                        'pagos aplicados para la misma.')

    class Meta:
        # No deben existir dos Facturas con el mismo numero para un mismo Proveedor en la tabla.
        unique_together = ['proveedor', 'numero_factura_compra', 'fecha_factura_compra']
        verbose_name = 'Factura/Pago Proveedor'
        verbose_name_plural = 'Proveedores - Facturas/Pagos'

    # VALIDACIONES/FUNCIONALIDADES
    # ============================
    # 1) Validar que la suma de los pagos para una factura no supere el monto total de la factura. OK!

    def clean(self):
        # 1) Validar que la suma de los pagos para una factura no supere el monto total de la factura.
        if self.total_pago_factura > self.total_factura_compra:
            raise ValidationError({'total_pago_factura': _('La suma de los pagos no debe superar el monto de la '
                                                           'factura.')})

    def get_total_pago_factura(self):
        detalle_pagos = PagoProveedor.objects.filter(factura_proveedor_id=self.id, procesado=True, anulado=False)
        total_pagos = 0
        for detalle in detalle_pagos:
            total_pagos += detalle.monto_pago_proveedor
            print 'Detalle: %s - monto_pago_proveedor: %s - total_pagos: %s' % \
                  (detalle, detalle.monto_pago_proveedor, total_pagos)
        # self.monto_total_facturas_proveedor = total_facturas
        # self.save()
        return total_pagos

    def get_estado_factura_compra(self):
        estado_factura_compra = FacturaProveedorEstado.objects.get(estado_factura_proveedor="EPP")
        if self.get_total_pago_factura() >= self.total_factura_compra:
            estado_factura_compra = FacturaProveedorEstado.objects.get(estado_factura_proveedor="PAG")
        if self.get_total_pago_factura() < self.total_factura_compra:
            today = datetime.date.today()
            if self.tipo_factura_compra.tipo_factura_compra == 'CRE':
                # print ('factura.fecha_factura_compra: %s - factura.plazo_factura_compra: %s') %
                # (factura.fecha_factura_compra, factura.plazo_factura_compra)
                calculo = (self.fecha_factura_compra + datetime.timedelta(days=self.plazo_factura_compra))
                # print 'calculo: %s' % calculo
                if calculo < today:
                    # estado = OrdenCompraEstado.objects.get(estado_orden_compra='PEP')
                    estado_factura_compra = FacturaProveedorEstado.objects.get(estado_factura_proveedor='FPP')
                    # factura.save()
            elif self.tipo_factura_compra.tipo_factura_compra == 'CON':
                if self.fecha_factura_compra < today:
                    estado_factura_compra = FacturaProveedorEstado.objects.get(estado_factura_proveedor='FPP')
        return estado_factura_compra

    def __unicode__(self):
        return "Compra: %s - Factura: %s" % (self.compra, self.numero_factura_compra)


class ProductoProveedor(models.Model):
    """
    La intencion de este modelo o tabla es poder relacionar los Productos con los Proveedores y utilizar esta tabla
    resultante para filtrar los Productos en funcion del Proveedor seleccionado en la pantalla de Ordenes de Compras.
    """
    proveedor = models.ForeignKey('Proveedor', help_text='Seleccione el Proveedor al cual asignar un Producto.')
    producto = models.ForeignKey('stock.Producto', help_text='Seleccione el Producto a relacionar con el Proveedor.')

    class Meta:
        verbose_name = 'Proveedor - Producto'
        verbose_name_plural = 'Proveedores - Productos'

    # VALIDACIONES/FUNCIONALIDADES
    # ============================

    def __unicode__(self):
        return "%s - %s" % (self.proveedor, self.producto)


class Empresa(Proveedor):
    """
    Prueba de Multi-table Model inheritance.
    """
    logo_empresa = models.ImageField(upload_to='compras/empresa/', verbose_name='Archivo de Logo',
                                     help_text='Seleccione el archivo con el logo de la Empresa.')
    fecha_apertura = models.DateField(verbose_name='Fecha de Apertura',
                                      help_text='Indique la Fecha de Apertura de la Empresa.')
    timbrado = models.ForeignKey('bar.Timbrado', limit_choices_to={'estado_timbrado': "AC"})
    codigo_establecimiento = models.CharField(max_length=3, default="001",
                                              verbose_name='Codigo de Establecimiento',
                                              help_text='Ingrese el Codigo de Establecimiento.')
    actividad_economica = models.CharField(max_length=100, default="Compra/venta de productos gastronomicos",
                                           verbose_name='Actividad Economica',
                                           help_text='Ingrese la actividad economica a la que se dedica la Empresa.')
    salario_minimo_vigente = models.DecimalField(max_digits=18, decimal_places=0, default=1824055,
                                                 verbose_name='Salario Minimo Vigente',
                                                 help_text='Ingrese el Salario Minimo Vigente.')

    class Meta:
        verbose_name = 'Empresa'
        verbose_name_plural = 'Empresas'

    # VALIDACIONES/FUNCIONALIDADES
    # ============================

    def thumb(self):
        if self.logo_empresa:
            return mark_safe('<img src="%s" width=60 height=60 />' % self.logo_empresa.url)
        else:
            return u'Logo no disponible.'
    thumb.short_description = 'Vista de Logo'

    def clean(self):
        # Valida que la fecha_apertura NO sea mayor a la fecha actual
        if self.fecha_apertura > datetime.date.today():
            raise ValidationError({'fecha_apertura': _('La Fecha de Apertura de la Empresa no puede ser mayor que la '
                                                       'fecha actual.')})

    def __init__(self, *args, **kwargs):
        super(Empresa, self).__init__(*args, **kwargs)
        # self._meta.get_field('empresa_administrada').default = True
        self.empresa_administrada = True

    def __unicode__(self):
        return "%s" % self.proveedor


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
    # La recomendacion de JuanBer90 es definir las choices en el propio modelo sin utilizar una tabla auxiliar de
    # parametrizaciones
    # ESTADOS_ORDENES_COMPRAS = {'PEP': 'adsfasdfasdf '}
    # ESTADOS_ORDENES_COMPRAS['PEP']

    # id = models.AutoField(primary_key=True)
    numero_orden_compra = models.AutoField(primary_key=True,
                                           verbose_name='Nro. Orden Compra',
                                           help_text='Este dato se genera automaticamente cada vez que se va crear '
                                                     'una Orden de Compra.')
    # ===============================================================================================================
    # numero_orden_compra = models.AutoField(primary_key=True,
    # numero_orden_compra = SerialField(max_length=12, unique=True,
    # numero_orden_compra = models.UUIDField(default=uuid.uuid4, max_length=6
    # models.IntegerField(default=lambda: OrdenCompra.objects.latest('id').serial + 1,
    # models.AutoField(primary_key=False, editable=True,
    # models.CharField(default='XXXXXX', max_length=6, unique=True,
    # ===============================================================================================================

    fecha_orden_compra = models.DateTimeField(auto_now_add=True,  # editable=True, auto_now_add=True,
                                              verbose_name='Fecha/hora Orden de Compra',
                                              help_text='La fecha y hora de la Orden de Compra se asignan al momento '
                                                        'de guardar los datos del pedido. No se requiere el ingreso de '
                                                        'este dato.')
    fecha_ultima_modificacion_orden_compra = models.DateTimeField(auto_now=True,  # default=timezone.now(),
                                                                  verbose_name='Fecha/hora Ult. Modif.',
                                                                  help_text='Registra la fecha/hora de ultima '
                                                                            'modificacion de la Orden de Compra.')
    # Aumenta 1 dia la fecha_entrega a partir de la fecha actual
    fecha_entrega_orden_compra = models.DateTimeField(default=(timezone.now() + datetime.timedelta(days=1)),
                                                      verbose_name='Fecha/hora de Entrega',
                                                      help_text='Indique la fecha y hora en la que el proveedor debe '
                                                                'entregar la Orden de Compra.')
    proveedor_orden_compra = models.ForeignKey('Proveedor', verbose_name='Proveedor', on_delete=models.PROTECT,
                                               # limit_choices_to=LineaCreditoProveedor.objects.filter(estado_linea_credito_proveedor='DEL'),
                                               # limit_choices_to=Q(estado_orden_compra__estado_orden_compra="EPP") |
                                               #                  Q(estado_orden_compra__estado_orden_compra="PEP"),
                                               help_text='Seleccione el Proveedor al cual se le realizara la Orden de '
                                                         'Compra.')
    forma_pago_orden_compra = models.ForeignKey('bar.FormaPagoCompra', verbose_name='Forma de Pago',
                                                help_text='Seleccione la Forma de Pago para esta Orden de Compra.')

    # Se debe definir un metodo o funcion que compare OrdenCompra.fecha_entrega_orden_compra contra la fecha actual y
    # modificar si corresponde el ESTADO de la Orden de Compra.
    estado_orden_compra = models.ForeignKey('bar.OrdenCompraEstado', default=1,
                                            verbose_name='Estado',
                                            help_text='El estado de la Orden de Compra se establece automaticamente de '
                                                      'acuerdo a la Fecha de Entrega ingresada.')
    usuario_registro_orden_compra = models.ForeignKey('personal.Empleado',  # default=1,
                                                      related_name='usuario_registro',
                                                      # limit_choices_to='',
                                                      # to_field='usuario',
                                                      verbose_name='Preparado por?',
                                                      help_text='Usuario que registro la Orden de Compra.')
    usuario_modifica_orden_compra = models.ForeignKey('personal.Empleado', null=True, blank=True,  # default=17,
                                                      related_name='usuario_modifica',
                                                      # limit_choices_to='',
                                                      # to_field='usuario',
                                                      verbose_name='Modificado por?',
                                                      help_text='Usuario que modifico la Orden de Compra.')
    # Calcular la suma de todos los totales de compra de cada producto
    # Debe ir en la cabecera y no en el detalle
    total_orden_compra = models.DecimalField(max_digits=18, decimal_places=0, default=0,
                                             verbose_name='Total Ord. Compra')  # blank=False (Default is False)

    motivo_cancelacion = models.CharField(max_length=200, null=True, blank=True)
    observaciones_cancelacion = models.CharField(max_length=200, null=True, blank=True)
    usuario_cancelacion = models.ForeignKey('personal.Empleado', null=True, blank=True,
                                            related_name='usuario_cancelacion_orden_compra',
                                            # limit_choices_to='',
                                            #  to_field='usuario',
                                            verbose_name='Cancelado por?',
                                            help_text='Usuario que cancelo la Orden de Compra.')
    fecha_hora_cancelacion = models.DateTimeField(null=True, blank=True)

    class Meta:
        verbose_name = 'Orden de Compra'
        verbose_name_plural = 'Compras - Ordenes'

    # VALIDACIONES/FUNCIONALIDADES
    # ============================
    # 1) Validaciones sobre "fecha_entrega_orden_compra". OK!
    # 2) Validar que el Total de la Orden de Compra no sea 0. OK!
    # 3) Se debe definir un metodo o funcion que compare OrdenCompra.fecha_entrega_orden_compra contra la fecha actual y
    # modifique si corresponde el ESTADO de la Orden de Compra.
    # 4) Validar la LineaCreditoProveedor con el Proveedor de acuerdo a las Ordenes de Compra y Pagos realizados.
    # La suma de las Ordenes de Compra contra los Pagos realizados no debe superar la Linea de Credito habilitada con
    # el Proveedor.

    # Se debe definir un metodo o funcion que compare OrdenCompra.fecha_entrega_orden_compra contra la fecha actual y
    # modificar si corresponde el ESTADO de la Orden de Compra.
    # def verifica_estado_orden_compra(self):
    # def from_db(cls, db, field_names, values):
    #     verifica_estado_orden_compra

    # def __init__(self, *args, **kwargs):
    #     if self.estado_orden_compra.estado_orden_compra not in ('ENT', 'CAN') \
    #             and self.fecha_entrega_orden_compra < timezone.now():
    #         self.estado_orden_compra == OrdenCompraEstado.objects.get(estado_orden_compra='PEP')
    #         # self.estado_orden_compra.save()
    #     elif self.estado_orden_compra.estado_orden_compra not in ('ENT', 'CAN') \
    #             and self.fecha_entrega_orden_compra >= timezone.now():
    #         self.estado_orden_compra == OrdenCompraEstado.objects.get(estado_orden_compra='EPP')
    #         # self.estado_orden_compra.save()
    #     super(OrdenCompra, self).__init__(*args, **kwargs)

    def get_linea_credito(self):
        proveedor = Proveedor.objects.get(id=self.proveedor_orden_compra_id)
        # proveedor = Proveedor.objects.get(pk=self.proveedor_orden_compra)
        disponible_linea_credito = proveedor.lineacreditoproveedor.disponible_linea_credito_proveedor
        print 'proveedor: %s - linea_credito: %s' % (proveedor, disponible_linea_credito)
        return disponible_linea_credito

    def clean(self):
        # Valida que la fecha_entrega_orden_compra sea mayor o igual a la fecha_orden_compra
        # Esta condicion no se va dar si se valida que la fecha_entrega_orden_compra sea mayor que la fecha/hora actual
        # if self.fecha_orden_compra is None or self.fecha_entrega_orden_compra < self.fecha_orden_compra:
        #     raise ValidationError({'fecha_entrega_orden_compra': _('La Fecha/hora de Entrega no puede ser menor que '
        #                                                            'la Fecha/hora de la Orden de Compra.')})

        # Valida que la fecha_entrega_orden_compra sea mayor que la fecha/hora actual
        now = timezone.now()
        if self.fecha_entrega_orden_compra <= now:
            raise ValidationError({'fecha_entrega_orden_compra': _('La Fecha/Hora de Entrega no puede ser menor que la '
                                                                   'Fecha/Hora actual.')})

        # Valida que el Total de la Orden de Compra no sea 0
        if self.total_orden_compra == 0:
            raise ValidationError({'total_orden_compra': _('El Total de la Orden de Compra no puede ser 0.')})

    def __unicode__(self):
        # return "%d - %s" % (self.numero_orden_compra, self.proveedor_orden_compra.proveedor)
        return "%s" % self.numero_orden_compra

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
    # Finalmente se direcciono a la tabla de Productos.
    producto_orden_compra = models.ForeignKey('stock.Producto', related_name='orden_compra_productos',
                                              limit_choices_to={'compuesto': False},
                                              verbose_name='Producto',
                                              help_text='Seleccione un Producto a ordenar.')
    precio_producto_orden_compra = models.DecimalField(max_digits=18, decimal_places=0,
                                                       verbose_name='Precio Compra Producto',
                                                       help_text='Ingrese el precio de compra del producto definido '
                                                                 'por el proveedor.')

    # La Unidad de Medida del Producto ya esta definida en la clase Producto en la app de Stock.
    # Visualmente seria conveniente que el usuario vea la Unidad de Medida de Compra del Producto
    # en el detalle de la Orden de Compra.
    unidad_medida_orden_compra = models.ForeignKey('bar.UnidadMedidaProducto',  # default=1, # to_field='unidad_medida',
                                                   verbose_name='Un. Med. Compra Producto',
                                                   help_text='Debe ser la definida en los datos del Producto, no '
                                                             'debe ser seleccionada por el usuario.')

    cantidad_producto_orden_compra = models.DecimalField(max_digits=10, decimal_places=3,
                                                         verbose_name='Cantidad Producto',
                                                         help_text='Ingrese la cantidad a adquirir del producto.')
    # Calcular "cantidad_producto_orden_compra" x "precio_producto_orden_compra"
    total_producto_orden_compra = models.DecimalField(max_digits=18, decimal_places=0, default=0,
                                                      verbose_name='Total Producto',
                                                      help_text='Este valor se calcula automaticamente tomando el '
                                                                'Precio del Producto por la Cantidad del Producto.')

    # ===============================================================================================================
    # @property
    # def total_orden_compra_producto(self):
    #     """
    #     Calcula "cantidad_producto * precio_compra_producto" y retorna el valor para el campo total_compra_producto
    #     como una propiedad o atributo del modelo.
    #     """
    #     return self.cantidad_producto * self.precio_compra_producto

    # total_orden_compra_producto = property(_get_total_compra_producto())
    # ===============================================================================================================

    class Meta:
        verbose_name = 'Detalle de Orden de Compra'
        verbose_name_plural = 'Compras - Detalles de Ordenes'

    # def __unicode__(self):
    #     return self.compra + ' - ' + self.producto


# ======================================================================================================================
class Compra(models.Model):
    """
    21/06/2061: Registrar compras.
                Sumar los productos comprados al stock.
                Listar las Compras realizadas por unidad de tiempo y/o proveedor.

    Las Compras de los productos o insumos se realizan por dia. Se realiza un pedido al proveedor de lo que se va
    utilizar en ese dia. Esto es porque el Deposito en el cual se guardan los productos es muy limitado en cuando a
    espacio fisico. Ademas realizando de esta manera se mejora el control de Stock.

    Las Compras ingresan totalmente al Deposito Central y a partir de ahi se transfieren a los Depositos Operativos
    segun pedidos de transferencias: Deposito Barra Principal, Deposito Barra Arriba, Cocina y Barrita.
    """
    # id = models.AutoField(primary_key=True)
    numero_compra = models.AutoField(primary_key=True, verbose_name='ID de Compra',
                                     help_text='Este dato se genera automaticamente cada vez que se va a confirmar '
                                               'una Compra.')
    # Filtrar las Ordenes de Compras que tienen estado EPP y PEP.
    numero_orden_compra = models.OneToOneField('OrdenCompra', blank=True,
                                               # limit_choices_to=Q(estado_orden_compra__estado_orden_compra="EPP") |
                                               #                  Q(estado_orden_compra__estado_orden_compra="PEP"),
                                               verbose_name='Numero Orden de Compra',
                                               help_text='Numero Orden de Compra seleccionada.')
    proveedor = models.ForeignKey('Proveedor')  # default=9

    disponible_linea_credito_proveedor = models.DecimalField(max_digits=18, decimal_places=0, default=0,
                                                             verbose_name='Disponible Linea de Credito',
                                                             help_text='Este valor se calcula automaticamente como la '
                                                                       'diferencia entre el Monto de la Linea de '
                                                                       'Credito y el Monto Utilizado de la Linea de '
                                                                       'Credito.')

    # numero_factura_compra = models.DecimalField(max_digits=13, decimal_places=0, blank=True,  # default=1,
    # codigo_establecimiento = models.CharField(max_length=3, default="001",
    numero_factura_compra = models.CharField(max_length=15, blank=True,  # default=1,
                                             # validators=[numero_factura],
                                             verbose_name='Numero de Factura Compra',
                                             help_text='Ingrese el Numero de Factura que acompana la Compra.')
    tipo_factura_compra = models.ForeignKey('bar.TipoFacturaCompra', default=1,
                                            verbose_name='Tipo de Factura',
                                            help_text='Seleccione el Tipo de Factura para la Compra.')
    fecha_factura_compra = models.DateField(default=datetime.date.today,
                                            verbose_name='Fecha Factura Compra',
                                            help_text='Ingrese la fecha de la factura.')

    # No corresponde, la Nota de Credito nos entrega un proveedor cuando se realiza una devolucion y anula la factura
    # que ya emitieron.
    # numero_nota_credito_compra = models.IntegerField(verbose_name='Numero Nota de Credito',  # default=1,
    #                                                  help_text='Ingrese el Numero de la Nota de Credito que acompana '
    #                                                            'la Compra en caso de que la Forma de Pago de la '
    #                                                            'misma sea a Credito.')

    fecha_compra = models.DateTimeField(auto_now=True,  # editable=True, default=timezone.now(),
                                        verbose_name='Fecha/hora Compra',
                                        help_text='La fecha y hora se asignan al momento de guardar los datos de la '
                                                  'Compra. No se requiere el ingreso de este dato.')
    # Utilizar los Estados de la Orden de Compra
    estado_compra = models.ForeignKey('bar.OrdenCompraEstado',  # default=5,
                                      verbose_name='Estado Compra',
                                      # help_text='La Compra puede tener 3 estados: PENDIENTE, CONFIRMADA o CANCELADA. '
                                      #           'El estado se asigna de forma automatica de acuerdo a la accion '
                                      #           'realizada.',
                                      help_text='Se asignan los Estados de la Orden de Compra.')
    usuario_registro_compra = models.ForeignKey('personal.Empleado', default=17,
                                                related_name='usuario_registro_compra',
                                                # limit_choices_to='',
                                                # to_field='usuario',
                                                verbose_name='Confirmado por?',
                                                help_text='Usuario que registro la Compra.')
    total_compra = models.DecimalField(max_digits=18, decimal_places=0, default=0,
                                       verbose_name='Total Compra',
                                       help_text='Este campo se calcula en funcion al detalle de la Compra.')

    motivo_cancelacion = models.CharField(max_length=200, null=True, blank=True)
    observaciones_cancelacion = models.CharField(max_length=200, null=True, blank=True)
    usuario_cancelacion = models.ForeignKey('personal.Empleado', null=True, blank=True,
                                            related_name='usuario_cancelacion_compra',
                                            # limit_choices_to='',
                                            #  to_field='usuario',
                                            verbose_name='Cancelado por?',
                                            help_text='Usuario que cancelo la Compra.')
    fecha_hora_cancelacion = models.DateTimeField(null=True, blank=True)

    # Para el caso de posibilitar la anulacion de una Compra.
    # anulado = models.BooleanField(default=False)

    class Meta:
        # proxy = True
        verbose_name = 'Confirmacion de Orden de Compra'
        verbose_name_plural = 'Compras - Confirmaciones de Ordenes'

    # VALIDACIONES/FUNCIONALIDADES
    # ============================
    # 1) Sumar los productos comprados al stock. OK!
    # 2) Modificar el Estado de la Compra de acuerdo a las acciones que se realicen con la misma. OK!
    #       La Compra puede tener 3 estados: PENDIENTE, CONFIRMADA o CANCELADA.
    #       El estado se asigna de forma automatica de acuerdo a la accion realizada.
    #       Cuando la Compra llega a los estados de CON o CAN ya no puede volver a ser modificada. OK!
    # En el caso de que una Compra confirmada deba ser devuelta se debe registrar el proceso en el modelo de
    # Devoluciones. El estado PEN es necesario para poder realizar la copia de los datos de la OrdenCompra a la Compra.
    # 3) Al confirmar la Compra se debe generar un registro en FacturaProveedor con los datos de la factura a pagar. OK!
    # 4) fecha_factura_compra no debe ser superior a la fecha actual. OK!

    # def get_nro_orden_compra(self, numero_compra):
    #     # proveedor = Proveedor.objects.get(id=self.proveedor_orden_compra_id)
    #     # # proveedor = Proveedor.objects.get(pk=self.proveedor_orden_compra)
    #     # disponible_linea_credito = proveedor.lineacreditoproveedor.disponible_linea_credito_proveedor
    #     print '====> numero_compra.numero_orden_compra: ', numero_compra.numero_orden_compra
    #     return numero_compra.numero_orden_compra

    def clean(self):
        # Valida que la fecha_factura_compra no sea superior a la fecha actual
        # now = datetime.date.today()
        if self.fecha_factura_compra > datetime.date.today():
            raise ValidationError({'fecha_factura_compra': _('La Fecha de la Factura no puede ser mayor que la '
                                                             'fecha actual.')})

    # def unique_error_message(self, model_class, unique_check):
    #     if model_class == type(self) and unique_check == ('proveedor', 'numero_factura_compra'):
    #         return 'Your custom error message.'
    #     else:
    #         return super(Compra, self).unique_error_message(model_class, unique_check)

    def __unicode__(self):
        return str(self.numero_compra)


class CompraDetalle(models.Model):
    numero_compra = models.ForeignKey('Compra')
    producto_compra = models.ForeignKey('stock.Producto', related_name='compra_productos',  # default=1,
                                        limit_choices_to={'compuesto': False},
                                        verbose_name='Producto',
                                        help_text='Seleccione un producto a comprar.')
    precio_producto_compra = models.DecimalField(max_digits=18, decimal_places=0,
                                                 verbose_name='Precio Compra',
                                                 help_text='Ingrese el precio de compra del producto definido por el '
                                                           'proveedor.')

    # La Unidad de Medida del Producto ya esta definida en la clase Producto en la app de Stock.
    # Visualmente seria conveniente que el usuario vea la Unidad de Medida de Compra del Producto
    # en el detalle de la Orden de Compra.
    unidad_medida_compra = models.ForeignKey('bar.UnidadMedidaProducto', default=1,  # to_field='unidad_medida',
                                             verbose_name='Un. Med. Compra Producto',
                                             help_text='Debe ser la definida en los datos del Producto, no debe '
                                                       'ser seleccionada por el usuario.')

    cantidad_producto_compra = models.DecimalField(max_digits=10, decimal_places=3,
                                                   verbose_name='Cantidad Producto',
                                                   help_text='Ingrese la cantidad a adquirir del producto.')

    total_producto_compra = models.DecimalField(max_digits=18, decimal_places=0, default=0,
                                                verbose_name='Total Producto')

    # ===============================================================================================================
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
    # ===============================================================================================================

    class Meta:
        verbose_name = 'Detalle de Confirmacion de Orden de Compra'
        verbose_name_plural = 'Compras - Detalles de Confirmaciones de Ordenes'

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