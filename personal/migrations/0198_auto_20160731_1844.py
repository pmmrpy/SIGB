# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('personal', '0197_auto_20160731_1130'),
    ]

    operations = [
        migrations.AddField(
            model_name='cargo',
            name='descripcion_cargo',
            field=models.CharField(default=b'cargo', help_text=b'Ingrese la descripcion del Cargo. (Hasta 50 caracteres)', max_length=50, verbose_name=b'Descripcion del Cargo'),
        ),
        migrations.AlterField(
            model_name='cargo',
            name='cargo',
            field=models.CharField(help_text=b'Ingrese el identificador del Cargo. (Hasta 2 caracteres)', max_length=2, verbose_name=b'Cargo', choices=[(b'MO', b'Moz@'), (b'BM', b'Barman/Barwoman'), (b'CA', b'Cajer@'), (b'CO', b'Cociner@'), (b'DE', b'Depositer@')]),
        ),
        migrations.AlterField(
            model_name='empleado',
            name='apellidos',
            field=models.CharField(help_text=b'Ingrese el/los apellido/s del Empleado. (Hasta 80 caracteres)', max_length=80, verbose_name=b'Apellido/s del Empleado'),
        ),
        migrations.AlterField(
            model_name='empleado',
            name='barrio',
            field=models.CharField(help_text=b'Ingrese el barrio.', max_length=100, blank=True),
        ),
        migrations.AlterField(
            model_name='empleado',
            name='cargo',
            field=models.ForeignKey(default=1, to='personal.Cargo', help_text=b'Seleccione el cargo.'),
        ),
        migrations.AlterField(
            model_name='empleado',
            name='ciudad',
            field=models.ForeignKey(default=1, to='bar.Ciudad', help_text=b'Seleccione la ciudad.'),
        ),
        migrations.AlterField(
            model_name='empleado',
            name='codigo_venta',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='empleado',
            name='direccion',
            field=models.CharField(help_text=b'Ingrese la direccion del Empleado.', max_length=200, verbose_name=b'Direccion del Empleado'),
        ),
        migrations.AlterField(
            model_name='empleado',
            name='email',
            field=models.EmailField(default=b'mail@ejemplo.com', help_text=b'Ingrese la direccion de email del Empleado.', max_length=254, blank=True),
        ),
        migrations.AlterField(
            model_name='empleado',
            name='fecha_nacimiento',
            field=models.DateField(help_text=b'Ingrese la fecha de nacimiento del Empleado.', verbose_name=b'Fecha de Nacimiento'),
        ),
        migrations.AlterField(
            model_name='empleado',
            name='horario',
            field=models.ForeignKey(default=1, to='personal.Horario', help_text=b'Seleccione el horario del Empleado.'),
        ),
        migrations.AlterField(
            model_name='empleado',
            name='nombres',
            field=models.CharField(help_text=b'Ingrese el/los nombre/s del Empleado. (Hasta 80 caracteres)', max_length=80, verbose_name=b'Nombre/s del Empleado'),
        ),
        migrations.AlterField(
            model_name='empleado',
            name='pais',
            field=models.ForeignKey(default=1, to='bar.Pais', help_text=b'Seleccione el pais.'),
        ),
        migrations.AlterField(
            model_name='empleado',
            name='salario',
            field=models.DecimalField(help_text=b'Ingrese el salario del Empleado.', max_digits=18, decimal_places=0),
        ),
        migrations.AlterField(
            model_name='empleado',
            name='sexo',
            field=models.CharField(help_text=b'Seleccione el sexo del Empleado.', max_length=1, choices=[(b'F', b'Femenino'), (b'M', b'Masculino')]),
        ),
        migrations.AlterField(
            model_name='empleadodocumento',
            name='numero_documento',
            field=models.CharField(help_text=b'Ingrese el documento del Empleado. El dato puede contener numeros y letras dependiendo de la nacionalidad y tipo de documento.', unique=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='empleadotelefono',
            name='codigo_operadora_telefono',
            field=models.ForeignKey(verbose_name=b'Codigo de Operadora - Telefono', to='bar.CodigoOperadoraTelefono', help_text=b'Seleccione el codigo de operadora para el numero de telefono.'),
        ),
        migrations.AlterField(
            model_name='empleadotelefono',
            name='codigo_pais_telefono',
            field=models.ForeignKey(verbose_name=b'Codigo de Pais - Telefono', to='bar.CodigoPaisTelefono', help_text=b'Seleccione el codigo de pais para el numero de telefono.'),
        ),
        migrations.AlterField(
            model_name='empleadotelefono',
            name='telefono',
            field=models.IntegerField(help_text=b'Ingrese el numero de telefono fijo o movil del Empleado. (El dato debe contener solo numeros)'),
        ),
        migrations.AlterField(
            model_name='horario',
            name='horario_fin',
            field=models.TimeField(default=datetime.datetime(2016, 7, 31, 22, 44, 25, 578000, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='horario',
            name='horario_inicio',
            field=models.TimeField(default=datetime.datetime(2016, 7, 31, 22, 44, 25, 578000, tzinfo=utc)),
        ),
    ]
