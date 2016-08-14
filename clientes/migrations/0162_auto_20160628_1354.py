# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0161_auto_20160626_2022'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='apellidos',
            field=models.CharField(help_text=b'Ingrese el o los apellidos del Cliente. (Hasta 80 caracteres)', max_length=80),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='ciudad',
            field=models.ForeignKey(default=1, to='bar.Ciudad', help_text=b'Seleccione la ciudad de residencia del Cliente.'),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='direccion',
            field=models.CharField(help_text=b'Ingrese la direccion del Cliente. (Hasta 200 caracteres)', max_length=200),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='email',
            field=models.EmailField(default=b'mail@ejemplo.com', help_text=b'Ingrese la direccion de email del Cliente.', max_length=254, blank=True),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='fecha_nacimiento',
            field=models.DateField(default=datetime.datetime(2016, 6, 28, 17, 54, 4, 313000, tzinfo=utc), help_text=b'Seleccione la fecha de nacimiento del Cliente.', verbose_name=b'Fecha de Nacimiento'),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='nombres',
            field=models.CharField(help_text=b'Ingrese el o los nombres del Cliente. (Hasta 80 caracteres)', max_length=80),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='pais',
            field=models.ForeignKey(default=1, to='bar.Pais', help_text=b'Seleccione el pais de residencia del Cliente.'),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='sexo',
            field=models.CharField(default=b'F', help_text=b'Seleccione el genero del Cliente.', max_length=1, choices=[(b'F', b'Femenino'), (b'M', b'Masculino')]),
        ),
        migrations.AlterField(
            model_name='clientedocumento',
            name='numero_documento',
            field=models.CharField(help_text=b'Ingrese el documento del Cliente. (El dato puede contener numeros y letras dependiendo de la nacionalidad y tipo de documento)', unique=True, max_length=50, verbose_name=b'Numero de Documento'),
        ),
        migrations.AlterField(
            model_name='clientedocumento',
            name='tipo_documento',
            field=models.ForeignKey(verbose_name=b'Tipo de Documento', to='bar.Documento', help_text=b'Seleccione el tipo de documento del Cliente.'),
        ),
        migrations.AlterField(
            model_name='clientetelefono',
            name='codigo_ciudad_operadora_telefono',
            field=models.ForeignKey(default=1, verbose_name=b'Codigo de Ciudad/Operadora - Telefono', to='bar.CodigoCiudadOperadoraTelefono', help_text=b'Seleccione el codigo de ciudad u operadora para el numero de telefono.'),
        ),
        migrations.AlterField(
            model_name='clientetelefono',
            name='codigo_pais_telefono',
            field=models.ForeignKey(default=595, verbose_name=b'Codigo de Pais - Telefono', to='bar.CodigoPaisTelefono', help_text=b'Seleccione el codigo de pais para el numero de telefono.'),
        ),
        migrations.AlterField(
            model_name='clientetelefono',
            name='telefono',
            field=models.IntegerField(help_text=b'Ingrese el numero de telefono fijo o movil del Cliente. (El dato debe contener solo numeros)'),
        ),
        migrations.AlterField(
            model_name='reserva',
            name='fecha_hora',
            field=models.DateTimeField(default=datetime.datetime(2016, 6, 28, 17, 54, 4, 315000, tzinfo=utc), help_text=b'Ingrese la fecha y hora de la Reserva.'),
        ),
    ]
