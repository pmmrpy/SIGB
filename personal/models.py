# -*- coding: utf-8 -*-

from django.db import models
# from django.contrib.auth.models import User
import datetime
from django.utils import timezone
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
# from random import randint
from compras.models import Empresa

# Create your models here.


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


def get_salario_minimo_vigente():
    empresa = Empresa.objects.get(pk=9)
    salario = empresa.salario_minimo_vigente
    return salario


class Empleado(models.Model):
#    id = models.AutoField(primary_key=True)
    nombres = models.CharField(max_length=80, verbose_name='Nombre/s del Empleado',
                               help_text='Ingrese el/los nombre/s del Empleado. (Hasta 80 caracteres)')
    apellidos = models.CharField(max_length=80, verbose_name='Apellido/s del Empleado',
                                 help_text='Ingrese el/los apellido/s del Empleado. (Hasta 80 caracteres)')
    fecha_nacimiento = models.DateField(verbose_name='Fecha de Nacimiento',
                                        help_text='Ingrese la fecha de nacimiento del Empleado.')
    sexo = models.CharField(max_length=1, verbose_name='Genero', choices=(
        ('F', 'Femenino'),
        ('M', 'Masculino'),
        ('O', 'Otros'),
    ), help_text='Seleccione el sexo del Empleado.'
    )
    direccion = models.CharField(max_length=200, verbose_name='Direccion del Empleado',
                                 help_text='Ingrese la direccion del Empleado.')
    pais = models.ForeignKey('bar.Pais', help_text='Seleccione el pais.')  # default=1,
    ciudad = models.ForeignKey('bar.Ciudad', help_text='Seleccione la ciudad.')  # default=1,
    barrio = models.CharField(max_length=100, blank=True, help_text='Ingrese el barrio.')
    email = models.EmailField(default='mail@ejemplo.com', blank=True,
                              help_text='Ingrese la direccion de correo electronico del Empleado.')
    cargo = models.ForeignKey('Cargo', help_text='Seleccione el cargo.')  # default=1,
    salario = models.DecimalField(max_digits=18, decimal_places=0, default=1824055,
                                  # default=get_salario_minimo_vigente(),
                                  help_text='Ingrese el salario del Empleado.')
    horario = models.ForeignKey('Horario',  # default=1,
                                help_text='Seleccione el horario del Empleado.')
    # Generar de forma automatica un Codigo de Venta de 4 digitos numerico
    usuario = models.OneToOneField('auth.User', help_text='Seleccione el usuario del Empleado.')  # default=1
    _codigo_venta = models.PositiveIntegerField(db_column="codigo_venta", null=True, verbose_name='Codigo de Venta')  # default=100
    documentos = models.ManyToManyField('bar.Documento', through='EmpleadoDocumento')

    # @property
    # def codigo_venta(self):
    #     return self._codigo_venta
    # # codigo_venta.short_description = 'Codigo de Venta'
    #
    # @codigo_venta.setter
    # def codigo_venta(self, value):
    #     # if value > 0:
    #     #     logger.warning("Ya fue asignado un Codigo de Venta al usuario.")
    #     value = randint(001, 999)
    #     self._codigo_venta = value

    def __init__(self, *args, **kwargs):
        super(Empleado, self).__init__(*args, **kwargs)
        if not self.id:
            # empresa = Empresa.objects.get(pk=9)
            # self.salario = empresa.salario_minimo_vigente
            self.salario = get_salario_minimo_vigente()

    def clean(self):
        # Validar si el Cliente es mayor de edad.
        # edad = datetime.date.today() - self.fecha_nacimiento
        edad = calcular_edad(self.fecha_nacimiento)
        if edad < 18:  # datetime.timedelta(days=365 * 18):
            raise ValidationError({'fecha_nacimiento': _(u"El Empleado debe ser mayor de edad. Su edad es de %s años."
                                                         % edad)})

    def __unicode__(self):
        # return "%s - %s" % (("%s %s" % (self.nombres, self.apellidos)).upper(), self.cargo)
        return "%s" % self.usuario


class EmpleadoDocumento(models.Model):
    empleado = models.ForeignKey('Empleado')
    tipo_documento = models.ForeignKey('bar.Documento', verbose_name='Tipo de Documento',
                                       help_text='Seleccione el Tipo de Documento para el Empleado.')
    numero_documento = models.CharField(max_length=50, verbose_name='Numero de Documento',  # unique=True,
                                        help_text='Ingrese el documento del Empleado. El dato puede contener numeros y '
                                                  'letras dependiendo de la nacionalidad y tipo de documento.')

    class Meta:
        unique_together = ['tipo_documento', 'numero_documento']
        verbose_name = 'Empleado - Documento'
        verbose_name_plural = 'Empleados - Documentos'

    @property
    def digito_verificador(self):
        if self.tipo_documento.documento == 'RUC':
            return calcular_dv(self.numero_documento, 11)
        else:
            return u'N/A'

    def __unicode__(self):
        return "%s - %s - %s" % (self.empleado, self.tipo_documento, self.numero_documento)


class EmpleadoTelefono(models.Model):
    empleado = models.ForeignKey('Empleado')
    codigo_pais_telefono = models.ForeignKey('bar.CodigoPaisTelefono',
                                             verbose_name='Codigo de Pais - Telefono',  # default=595,
                                             help_text='Seleccione el codigo de pais para el numero de telefono.')
    codigo_operadora_telefono = models.ForeignKey('bar.CodigoOperadoraTelefono',
                                                  verbose_name='Codigo de Operadora - Telefono',  # default=21,
                                                  help_text='Seleccione el codigo de operadora para el numero de '
                                                            'telefono.')
    telefono = models.IntegerField(help_text='Ingrese el numero de telefono fijo o movil del Empleado. (El dato debe '
                                             'contener solo numeros)')

    class Meta:
        verbose_name = 'Empleado - Telefono'
        verbose_name_plural = 'Empleados - Telefonos'

    def __unicode__(self):
        return "%s - %s - %s - %s" % (self.empleado, self.codigo_pais_telefono, self.codigo_operadora_telefono,
                                      self.telefono)


class Cargo(models.Model):
    CARGOS = (
        ('MO', 'Moz@'),
        ('BM', 'Barman/Barwoman'),
        ('CA', 'Cajer@'),
        ('CO', 'Cociner@'),
        ('DE', 'Depositer@'),
        ('EI', 'Encargado Informatica'),
        ('RP', 'Relaciones Publicas'),
    )
    # id = models.AutoField(primary_key=True)
    cargo = models.CharField(max_length=2, choices=CARGOS, verbose_name='Cargo',
                             help_text='Ingrese el identificador del Cargo. (Hasta 2 caracteres)')
    descripcion_cargo = models.CharField(max_length=50, verbose_name='Descripcion del Cargo', default='Cargo',
                                         help_text='Ingrese la descripcion del Cargo. (Hasta 50 caracteres)')

    def __unicode__(self):
        return "%s - %s" % (self.cargo, self.descripcion_cargo)


class Horario(models.Model):
    HORARIOS = (
        ('NO', 'Nocturno'),
        ('MA', 'Matinal'),
        ('TA', 'Tarde'),
        ('CO', 'Completo'),
    )
    horario = models.CharField(max_length=30, verbose_name='Horario',
                               help_text='Ingrese el nombre o descripcion de la jornada laboral.')
    horario_inicio = models.TimeField(default=timezone.now(), verbose_name='Hora de Inicio Jornada',
                                      help_text='Ingrese la hora de inicio de la jornada de trabajo.')
    horario_fin = models.TimeField(default=timezone.now(), verbose_name='Hora de Finalizacion Jornada',
                                   help_text='Ingrese la hora de finalizacion de la jornada de trabajo.')

    def __unicode__(self):
        return "%s" % self.horario