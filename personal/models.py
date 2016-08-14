from django.db import models
# from django.contrib.auth.models import User
from django.utils import timezone
from random import randint

# Create your models here.


class Empleado(models.Model):
#    id = models.AutoField(primary_key=True)
    nombres = models.CharField(max_length=80, verbose_name='Nombre/s del Empleado',
                               help_text='Ingrese el/los nombre/s del Empleado. (Hasta 80 caracteres)')
    apellidos = models.CharField(max_length=80, verbose_name='Apellido/s del Empleado',
                                 help_text='Ingrese el/los apellido/s del Empleado. (Hasta 80 caracteres)')
    fecha_nacimiento = models.DateField(verbose_name='Fecha de Nacimiento',
                                        help_text='Ingrese la fecha de nacimiento del Empleado.')
    sexo = models.CharField(max_length=1, choices=(
        ('F', 'Femenino'),
        ('M', 'Masculino'),
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
    salario = models.DecimalField(max_digits=18, decimal_places=0,
                                  help_text='Ingrese el salario del Empleado.')
    horario = models.ForeignKey('Horario',  # default=1,
                                help_text='Seleccione el horario del Empleado.')
    # Generar de forma automatica un Codigo de Venta de 4 digitos numerico
    usuario = models.ForeignKey('auth.User', help_text='Seleccione el usuario del Empleado.')  # default=1
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

    def __unicode__(self):
        return "%s - %s" % (("%s %s" % (self.nombres, self.apellidos)).upper(), self.cargo)


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


class EmpleadoDocumento(models.Model):
    empleado = models.ForeignKey('Empleado')
    tipo_documento = models.ForeignKey('bar.Documento', help_text='Seleccione el Tipo de Documento para el Empleado.')
    numero_documento = models.CharField(unique=True, max_length=50, verbose_name='Numero de Documento',
                                        help_text='Ingrese el documento del Empleado. El dato puede contener numeros y '
                                                  'letras dependiendo de la nacionalidad y tipo de documento.')

    class Meta:
        verbose_name = 'Empleado - Documento'
        verbose_name_plural = 'Empleados - Documentos'

    def __unicode__(self):
        return "%s - %s - %s" % (self.empleado, self.tipo_documento, self.numero_documento)