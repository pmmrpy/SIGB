from django.db import models
# from ventas.models import Mesa
# import datetime
from django.utils import timezone

# Create your models here.


class Cliente(models.Model):
    """
    07/07/2016: Registro de Clientes.

    * Listar Clientes por frecuencia, por facturacion, por edad, por sexo.
    """
#    id = models.AutoField(primary_key=True)
    nombres = models.CharField(max_length=80, help_text='Ingrese el o los nombres del Cliente. (Hasta 80 caracteres)')
    apellidos = models.CharField(max_length=80, help_text='Ingrese el o los apellidos del Cliente. '
                                                          '(Hasta 80 caracteres)')
    fecha_nacimiento = models.DateField(default=timezone.now(), verbose_name='Fecha de Nacimiento',
                                        help_text='Seleccione la fecha de nacimiento del Cliente.')
    sexo = models.CharField(max_length=1, default='F', choices=(
        ('F', 'Femenino'),
        ('M', 'Masculino'),
    ), help_text='Seleccione el genero del Cliente.')
    direccion = models.CharField(max_length=200, help_text='Ingrese la direccion del Cliente. (Hasta 200 caracteres)')
    pais = models.ForeignKey('bar.Pais', default=1, help_text='Seleccione el pais de residencia del Cliente.')
    ciudad = models.ForeignKey('bar.Ciudad', default=1, help_text='Seleccione la ciudad de residencia del Cliente.')
    email = models.EmailField(default='mail@ejemplo.com', blank=True,
                              help_text='Ingrese la direccion de email del Cliente.')
    documentos = models.ManyToManyField('bar.Documento', through='ClienteDocumento')

    # def _get_full_name(self):
    #     "Returns the person's full name."
    #     return '%s %s' % (self.nombres, self.apellidos)
    # full_name = property(_get_full_name)

    def __unicode__(self):
        # return self.nombres + ' ' + self.apellidos
        return '%s %s' % (self.nombres, self.apellidos)


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


# class TelefonoMovilCliente(models.Model):
#     cliente = models.ForeignKey('Cliente')
#     codigo_pais_telefono = models.ForeignKey('bar.CodigoPaisTelefono', default=595)
#     codigo_ciudad_operadora_telefono = models.ForeignKey('bar.CodigoCiudadOperadoraTelefono', default=21)
#     telefono_movil = models.IntegerField(help_text='Ingrese el telefono movil del cliente. El dato debe '
#                                                    'contener solo numeros.')


class Reserva(models.Model):
    """
    07/07/2016: Registro de Reservas.
                Anular Reservas.
    * Emitir comprobantes. Anticipo de Reserva.
    """
#    id = models.AutoField(primary_key=True)
    descripcion = models.CharField(max_length=50, default='Reserva de Mesa',
                                   help_text='Puede indicar alguna descripcion que identifique a la Reserva.')
    cliente = models.ForeignKey('Cliente')
    fecha_hora = models.DateTimeField(default=timezone.now(), help_text='Ingrese la fecha y hora de la Reserva.')
    cantidad_personas = models.DecimalField(max_digits=5, decimal_places=0, default=0)
    mesas = models.ManyToManyField('bar.Mesa')
    estado = models.ForeignKey('bar.ReservaEstado')
    pago = models.DecimalField(max_digits=18, decimal_places=0, default=0)
    usuario_registro = models.ForeignKey('auth.User', default=1)

    def __unicode__(self):
        return "%s" % self.descripcion


class ClienteDocumento(models.Model):
    cliente = models.ForeignKey('Cliente')
    tipo_documento = models.ForeignKey('bar.Documento', verbose_name='Tipo de Documento',
                                       help_text='Seleccione el tipo de documento del Cliente.')
    numero_documento = models.CharField(unique=True, max_length=50, verbose_name='Numero de Documento',
                                        help_text='Ingrese el documento del Cliente. (El dato puede contener numeros '
                                                  'y letras dependiendo de la nacionalidad y tipo de documento)')
    #  El atributo "unique" fuerza a que el dato sea unico en la tabla

    class Meta:
        verbose_name = 'Cliente - Documento'
        verbose_name_plural = 'Clientes - Documentos'

    def __unicode__(self):
        return "%s - %s" % (self.tipo_documento, self.numero_documento)