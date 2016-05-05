from django.db import models
# from ventas.models import Mesa
# import datetime
from django.utils import timezone

# Create your models here.


class Cliente(models.Model):
#    id = models.AutoField(primary_key=True)
    nombres = models.CharField(max_length=80)
    apellidos = models.CharField(max_length=80)
    fecha_nacimiento = models.DateField(default=timezone.now())
    sexo = models.CharField(max_length=1, default='F', choices=(
        ('F', 'Femenino'),
        ('M', 'Masculino'),
    )
    )
    direccion = models.CharField(max_length=200)
    pais = models.ForeignKey('bar.Pais', default=1)
    ciudad = models.ForeignKey('bar.Ciudad', default=1)
    email = models.EmailField(default='mail@ejemplo.com', blank=True)
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
    codigo_pais_telefono = models.ForeignKey('bar.CodigoPaisTelefono', default=595, help_text='Seleccione el codigo '
                                                                                              'de pais para el numero '
                                                                                              'de telefono.')
    codigo_ciudad_operadora_telefono = models.ForeignKey('bar.CodigoCiudadOperadoraTelefono',
                                                         default=1, help_text='Seleccione el codigo de ciudad u '
                                                                              'operadora para el numero de telefono.')
    telefono = models.IntegerField(help_text='Ingrese el telefono fijo o movil del cliente. El dato debe '
                                             'contener solo numeros.')

    class Meta:
        verbose_name = 'Cliente - Telefono'
        verbose_name_plural = 'Clientes - Telefonos'

    def __unicode__(self):
        return str(self.cliente) + ' - ' + str(self.codigo_pais_telefono) + ' - ' + \
            str(self.codigo_ciudad_operadora_telefono) + ' - ' + str(self.telefono)


# class TelefonoMovilCliente(models.Model):
#     cliente = models.ForeignKey('Cliente')
#     codigo_pais_telefono = models.ForeignKey('bar.CodigoPaisTelefono', default=595)
#     codigo_ciudad_operadora_telefono = models.ForeignKey('bar.CodigoCiudadOperadoraTelefono', default=21)
#     telefono_movil = models.IntegerField(help_text='Ingrese el telefono movil del cliente. El dato debe '
#                                                    'contener solo numeros.')


class Reserva(models.Model):
#    id = models.AutoField(primary_key=True)
    descripcion = models.CharField(max_length=50, default='Reserva de Mesa')
    cliente = models.ForeignKey('Cliente')
    fecha_hora = models.DateTimeField(default=timezone.now())
    cantidad_personas = models.DecimalField(max_digits=5, decimal_places=0, default=0)
    mesas = models.ManyToManyField('bar.Mesa')
    estado = models.ForeignKey('bar.ReservaEstado')
    pago = models.DecimalField(max_digits=18, decimal_places=0, default=0)
    usuario_registro = models.ForeignKey('auth.User', default=1)

    def __unicode__(self):
        return self.descripcion


class ClienteDocumento(models.Model):
    cliente = models.ForeignKey('Cliente')
    tipo_documento = models.ForeignKey('bar.Documento', help_text='Seleccione el tipo de documento del cliente.')
    numero_documento = models.CharField(unique=True, max_length=50, help_text='Ingrese el documento del cliente. El '
                                                                              'dato puede contener numeros y letras '
                                                                              'dependiendo de la nacionalidad y tipo '
                                                                              'de documento.')
    #  El atributo "unique" fuerza a que el dato sea unico en la tabla

    class Meta:
        verbose_name = 'Cliente - Documento'
        verbose_name_plural = 'Clientes - Documentos'

    def __unicode__(self):
        return str(self.tipo_documento) + ' - ' + str(self.numero_documento)