# -*- coding: utf-8 -*-
from django.db import models
# from ventas.models import Mesa
import datetime
# from dateutil.relativedelta import *
from django.db.models.query_utils import Q
from django.utils import timezone
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
import re
from personal.models import Empleado
from django.core.validators import RegexValidator

# Create your models here.

# numeric = RegexValidator(r'^[0-9]*$', 'Solo se permiten caracteres numericos.')


def calcular_dv(numero, base=11):
    total = 0
    k = 2
    for i in range(len(numero) - 1, - 1, - 1):
        k = 2 if k > base else k
        total += int(numero[i]) * k
        k += 1
    resto = total % 11
    return (11 - resto) if resto > 1 else 0


def calcular_edad(nacimiento):
    # nacimiento = self.fecha_nacimiento
    hoy = datetime.date.today()
    return hoy.year - nacimiento.year - ((hoy.month, hoy.day) < (nacimiento.month, nacimiento.day))
    # edad = relativedelta(hoy, nacimiento)
    # edad = edad.years
    # return edad


class Cliente(models.Model):
    """
    07/07/2016: Registro de Clientes.

    * Listar Clientes por frecuencia, por facturacion, por edad, por sexo.
    """
#    id = models.AutoField(primary_key=True)
    nombres = models.CharField(max_length=80, help_text='Ingrese el/los nombre/s del Cliente. (Hasta 80 caracteres)')
    apellidos = models.CharField(max_length=80, help_text='Ingrese el/los apellido/s del Cliente. '
                                                          '(Hasta 80 caracteres)')
    fecha_nacimiento = models.DateField(verbose_name='Fecha de Nacimiento',  # default=timezone.now(),
                                        help_text='Seleccione la fecha de nacimiento del Cliente.')
    sexo = models.CharField(max_length=1, verbose_name='Genero', choices=(  # default='F',
        ('F', 'Femenino'),
        ('M', 'Masculino'),
        ('O', 'Otros'),
    ), help_text='Seleccione el genero del Cliente.')
    direccion = models.CharField(max_length=200, help_text='Ingrese la direccion del Cliente. (Hasta 200 caracteres)')
    pais = models.ForeignKey('bar.Pais', help_text='Seleccione el pais de residencia del Cliente.')  # default=1,
    ciudad = models.ForeignKey('bar.Ciudad', help_text='Seleccione la ciudad de residencia del Cliente.')  # default=1,
    email = models.EmailField(default='mail@ejemplo.com', blank=True,
                              help_text='Ingrese la direccion de email del Cliente.')
    documentos = models.ManyToManyField('bar.Documento', through='ClienteDocumento')

    @property
    def nombre_completo(self):
        """Returns the person's full name."""
        return '%s %s' % (self.nombres, self.apellidos)
    # nombre_completo = property(get_nombre_completo)

    def clean(self):

        # import pdb
        # pdb.set_trace()

        # Validar si el Cliente es mayor de edad.
        # edad = datetime.date.today() - self.fecha_nacimiento
        if hasattr(self, 'fecha_nacimiento') and self.fecha_nacimiento is not None:
            edad = calcular_edad(self.fecha_nacimiento)
            if edad < 18:  # datetime.timedelta(days=365 * 18):
                raise ValidationError({'fecha_nacimiento': _(u"El Cliente debe ser mayor de edad. Su edad es de %s años."
                                                             % edad)})

    def __unicode__(self):
        # return self.nombres + ' ' + self.apellidos
        return '%s %s' % (self.nombres, self.apellidos)


class ClienteDocumento(models.Model):
    cliente = models.ForeignKey('Cliente')
    tipo_documento = models.ForeignKey('bar.Documento', verbose_name='Tipo de Documento',
                                       help_text='Seleccione el Tipo de Documento del Cliente.')
    numero_documento = models.CharField(max_length=50, verbose_name='Numero de Documento',  # unique=True,
                                        help_text='Ingrese el documento del Cliente. (El dato puede contener numeros '
                                                  'y letras dependiendo de la nacionalidad y tipo de documento)')
    #  El atributo "unique" fuerza a que el dato sea unico en la tabla

    class Meta:
        unique_together = ['tipo_documento', 'numero_documento']
        verbose_name = 'Cliente - Documento'
        verbose_name_plural = 'Clientes - Documentos'

    @property
    def digito_verificador(self):
        if self.tipo_documento.documento == 'RUC':
            # numero_documento = self.numero_documento
            # if not re.match(r'^[0-9]*$', self.numero_documento):
            #     # raise ValidationError({'self.numero_documento': _('Solo se permiten caracteres numericos.')})
            #     raise ValidationError(_('Solo se permiten caracteres numericos.'))
            # else:
            return calcular_dv(self.numero_documento, 11)
        else:
            return u'N/A'

    def __unicode__(self):
        return "%s: %s" % (self.tipo_documento.documento, self.numero_documento)


class ClienteTelefono(models.Model):
    cliente = models.ForeignKey('Cliente')
    codigo_pais_telefono = models.ForeignKey('bar.CodigoPaisTelefono',  # default='595',
                                             verbose_name='Codigo de Pais - Telefono',
                                             help_text='Seleccione el codigo de pais para el numero de telefono.')
    codigo_operadora_telefono = models.ForeignKey('bar.CodigoOperadoraTelefono',  # default='21',
                                                  verbose_name='Codigo de Operadora - Telefono',
                                                  help_text='Seleccione el codigo de operadora para el numero de '
                                                            'telefono.')
    telefono = models.IntegerField(help_text='Ingrese el numero de telefono fijo o movil del Cliente. (El dato debe '
                                             'contener solo numeros)')

    class Meta:
        verbose_name = 'Cliente - Telefono'
        verbose_name_plural = 'Clientes - Telefonos'

    def __unicode__(self):
        return "%s - %s%s%s" % (self.cliente, self.codigo_pais_telefono, self.codigo_operadora_telefono, self.telefono)


class Reserva(models.Model):
    """
    07/07/2016: Registro de Reservas.
                Anular Reservas.
    * Emitir comprobantes. Anticipo de Reserva.

    25/10/2016:
    * VALIDACIONES:
        1) Se pueden realizar Reservas de Mesas desde las 18 hasta las 21 hs, pasada las 21 hs se deben liberar las
        Mesas Reservadas y cambiar el Estado de la Reserva a CADUCADA.
        2) Una Mesa puede ser reservada solo una vez por jornada.
        3) Validar que las Mesas seleccionadas ya no se encuentran Reservadas para la fecha/hora indicada.
        4) El monto de la Entrega no puede ser menor a 100.000 Gs. OK!
    """
#    id = models.AutoField(primary_key=True)
    descripcion = models.CharField(max_length=300, default='Reserva de Mesa',
                                   verbose_name='Descripcion Reserva',
                                   help_text='Puede ingresar alguna descripcion que identifique a la Reserva.')
    descripcion_reserva = models.CharField(max_length=300, null=True, blank=True,  # default='Reserva de Mesa',
                                           verbose_name='Descripcion Reserva',
                                           help_text='Puede ingresar alguna descripcion que identifique a la Reserva.')
    cliente = models.ForeignKey('Cliente', help_text='Seleccione los datos del Cliente si ya se encuentra registrado, '
                                                     'de lo contrario realice el alta del Cliente.')
    cliente_documento_reserva = models.CharField(max_length=50,  # default='1234569',  # null=True, blank=True,
                                                 verbose_name='Documento',
                                                 help_text='Seleccione el Documento del Cliente el cual se registrara '
                                                           'en la Reserva.')
    fecha_hora_reserva = models.DateTimeField(default=timezone.now,
                                              verbose_name='Fecha y hora para la Reserva.',
                                              help_text='Ingrese la fecha y hora de la Reserva. Se pueden realizar '
                                                        'Reservas de Mesas desde las 18:00 hs hasta las 21:00 hs.')
    cantidad_personas = models.PositiveIntegerField(default=0, verbose_name='Cantidad de Personas',
                                                    help_text='Ingrese la cantidad de personas que utilizaran la '
                                                              'Reserva.')
    mesas = models.ManyToManyField('bar.Mesa', verbose_name='Mesas a Reservar',
                                   limit_choices_to=(~Q(numero_mesa=9999)),
                                   help_text='Seleccione las Mesas que seran reservadas.')
    pago = models.DecimalField(max_digits=18, decimal_places=0, default=0, verbose_name='Entrega',
                               help_text='Ingrese el monto a pagar por la Reserva. Este monto luego se acredita en '
                                         'consumision.')
    estado = models.ForeignKey('bar.ReservaEstado')  # default=1
    # Debe ser el usuario con el cual se esta realizando la carga de la Reserva, no se debe poder seleccionar el usuario
    usuario_registro = models.ForeignKey('personal.Empleado', limit_choices_to={'cargo__cargo': "RP"},
                                         # to_field='usuario',  # 'auth.User', default=1,
                                         verbose_name='Usuario que registra Reserva',
                                         help_text='Este dato se completara automaticamente cuando la Reserva sea '
                                                   'guardada.')
    fecha_hora_registro_reserva = models.DateTimeField(auto_now_add=True,  # default=timezone.now(),
                                                       verbose_name='Fecha y hora del registro de la Reserva',
                                                       help_text='Este dato se completara automaticamente cuando la '
                                                                 'Reserva sea guardada.')
    hora_inicio_reservas = models.TimeField(default=datetime.time(hour=18, minute=0))
    hora_fin_reservas = models.TimeField(default=datetime.time(hour=21, minute=0))
    evento_id = models.ForeignKey('calendarium.Event', null=True, blank=True)  # default=1

    motivo_cancelacion = models.CharField(max_length=200, null=True, blank=True)
    observaciones_cancelacion = models.CharField(max_length=200, null=True, blank=True)
    usuario_cancelacion = models.ForeignKey('personal.Empleado', null=True, blank=True,
                                            related_name='usuario_cancelacion_reserva',
                                            # limit_choices_to='',
                                            #  to_field='usuario',
                                            verbose_name='Cancelado por?',
                                            help_text='Usuario que cancelo la Reserva.')
    fecha_hora_cancelacion = models.DateTimeField(null=True, blank=True)

    # @property
    def set_descripcion_reserva(self):
        # fecha_hora_reserva = (obj.fecha_hora_reserva).astimezone(timezone.utc)
        return ("%s - %s - %s" % (self.descripcion, self.cliente,
                                  datetime.datetime.strftime(timezone.localtime(self.fecha_hora_reserva),
                                                             '%d/%m/%Y %H:%M:%S'))).upper()
    set_descripcion_reserva.short_description = 'Descripcion Reserva'

    class Meta:
        # 2) Validar que las Mesas seleccionadas ya no se encuentran Reservadas para la fecha/hora indicada.
        # ManyToManyFields are not permitted in 'unique_together'
        # unique_together = ['fecha_hora_reserva', 'mesas']
        verbose_name = 'Reserva de Mesa'
        verbose_name_plural = 'Reservas de Mesas'

    # VALIDACIONES/FUNCIONALIDADES
    # 1) usuario_registro: Debe ser el usuario con el cual se esta realizando la carga de la Reserva. OK!
    # 2) Validar que las Mesas seleccionadas ya no se encuentran Reservadas para la fecha/hora indicada.
    # 3) Modificar el Estado de la Reserva de acuerdo a las acciones que se realicen con la misma. Se debe permitir
    # CANCELAR la Reserva y se debe crear una funcion o metodo que controle la "fecha_hora_reserva" de cada Reserva
    # con la fecha/hora actual de modo a asignar el estado CADUCADA a las Reservas que no fueron utilizadas.

    def clean(self):
        # cleaned_data = super(Reserva, self).clean()

        # import pdb
        # pdb.set_trace()

        if self.cantidad_personas == 0:
            raise ValidationError({'cantidad_personas': _('La Cantidad de Personas no puede ser 0.')})

        if self.pago < 100000:
            raise ValidationError({'pago': _('El monto de la Entrega no puede ser menor a 100.000 Gs.')})

        if timezone.localtime(self.fecha_hora_reserva) < timezone.localtime(timezone.now()):
            raise ValidationError({'fecha_hora_reserva': 'La fecha/hora de la Reserva debe ser superior a la '
                                                         'fecha/hora actual.'})

        hora_inicio_reservas = datetime.time(hour=18, minute=0)
        hora_fin_reservas = datetime.time(hour=21, minute=0)
        hora_reserva = self.fecha_hora_reserva.time()
        if hora_fin_reservas < hora_reserva or hora_reserva < hora_inicio_reservas:
            raise ValidationError({'fecha_hora_reserva': 'La hora de la Reserva debe estar comprendida entre las '
                                                         '%s y %s horas.' % (hora_inicio_reservas, hora_fin_reservas)})

        self.descripcion_reserva = self.set_descripcion_reserva()

        # return cleaned_data

    def __unicode__(self):
        return "%s - %s - %s" % (self.descripcion, self.cliente, datetime.datetime.strftime(timezone.localtime(self.fecha_hora_reserva), '%d/%m/%Y %H:%M'))


# class CalendarioReserva(models.Model):
#
#     class Meta:
#         verbose_name = 'Calendario de Reservas'
#         verbose_name_plural = 'Calendario de Reservas'