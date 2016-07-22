from django.db import models
from django.utils import timezone

# Create your models here.


class Empleado(models.Model):
#    id = models.AutoField(primary_key=True)
    nombres = models.CharField(max_length=80)
    apellidos = models.CharField(max_length=80)
#    telefono = models.CharField(max_length=50)
#    telefono_movil = models.CharField(max_length=50)
    fecha_nacimiento = models.DateField(default=timezone.now())
    sexo = models.CharField(max_length=1, default='F', choices=(
        ('F', 'Femenino'),
        ('M', 'Masculino'),
    )
    )
    direccion = models.CharField(max_length=200)
    pais = models.ForeignKey('bar.Pais', default=1)
    ciudad = models.ForeignKey('bar.Ciudad', default=1)
    barrio = models.CharField(max_length=100, blank=True)
    email = models.EmailField(default='mail@ejemplo.com', blank=True)
    cargo = models.ForeignKey('Cargo', default=1)
    salario = models.DecimalField(max_digits=18, decimal_places=0)
    horario = models.ForeignKey('Horario', default=1)
    codigo_venta = models.IntegerField()
    documentos = models.ManyToManyField('bar.Documento', through='EmpleadoDocumento')

    def __unicode__(self):
        return self.nombres + ' ' + self.apellidos


class EmpleadoTelefono(models.Model):
    empleado = models.ForeignKey('Empleado')
    codigo_pais_telefono = models.ForeignKey('bar.CodigoPaisTelefono',  # default=595,
                                             help_text='Seleccione el codigo de pais para el numero de telefono.')
    codigo_operadora_telefono = models.ForeignKey('bar.CodigoOperadoraTelefono',  # default=21,
                                                  help_text='Seleccione el codigo de ciudad u operadora para '
                                                            'el numero de telefono.')
    telefono = models.IntegerField(help_text='Ingrese el telefono fijo o movil del empleado. El dato debe '
                                             'contener solo numeros.')

    class Meta:
        verbose_name = 'Empleado - Telefono'
        verbose_name_plural = 'Empleados - Telefonos'

    def __unicode__(self):
        return "%s - %s - %s - %s" % (self.empleado, self.codigo_pais_telefono, self.codigo_operadora_telefono,
                                      self.telefono)


class Cargo(models.Model):
    # id = models.AutoField(primary_key=True)
    cargo = models.CharField(max_length=50)

    def __unicode__(self):
        return self.cargo


class Horario(models.Model):
    horario = models.CharField(max_length=30)
    horario_inicio = models.TimeField(default=timezone.now())
    horario_fin = models.TimeField(default=timezone.now())

    def __unicode__(self):
        return self.horario


class EmpleadoDocumento(models.Model):
    empleado = models.ForeignKey('Empleado')
    tipo_documento = models.ForeignKey('bar.Documento')
    numero_documento = models.CharField(unique=True, max_length=50, help_text='Ingrese el documento del empleado. El '
                                                                              'dato puede contener numeros y letras '
                                                                              'dependiendo de la nacionalidad y tipo '
                                                                              'de documento.')

    class Meta:
        verbose_name = 'Empleado - Documento'
        verbose_name_plural = 'Empleados - Documentos'

    def __unicode__(self):
        return str(self.tipo_documento) + ' - ' + str(self.numero_documento)