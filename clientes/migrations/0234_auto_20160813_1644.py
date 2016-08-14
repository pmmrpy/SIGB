# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0233_auto_20160813_1518'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='ciudad',
            field=models.ForeignKey(help_text=b'Seleccione la ciudad de residencia del Cliente.', to='bar.Ciudad'),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='fecha_nacimiento',
            field=models.DateField(help_text=b'Seleccione la fecha de nacimiento del Cliente.', verbose_name=b'Fecha de Nacimiento'),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='pais',
            field=models.ForeignKey(help_text=b'Seleccione el pais de residencia del Cliente.', to='bar.Pais'),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='sexo',
            field=models.CharField(help_text=b'Seleccione el genero del Cliente.', max_length=1, choices=[(b'F', b'Femenino'), (b'M', b'Masculino')]),
        ),
        migrations.AlterField(
            model_name='clientedocumento',
            name='numero_documento',
            field=models.CharField(help_text=b'Ingrese el documento del Cliente. (El dato puede contener numeros y letras dependiendo de la nacionalidad y tipo de documento)', max_length=50, verbose_name=b'Numero de Documento'),
        ),
        migrations.AlterField(
            model_name='reserva',
            name='cantidad_personas',
            field=models.DecimalField(default=0, help_text=b'Ingrese la cantidad de personas que utilizaran la Reserva.', verbose_name=b'Cantidad de Personas', max_digits=3, decimal_places=0),
        ),
        migrations.AlterField(
            model_name='reserva',
            name='fecha_hora_reserva',
            field=models.DateTimeField(default=datetime.datetime(2016, 8, 13, 20, 44, 53, 553000, tzinfo=utc), help_text=b'Ingrese la fecha y hora de la Reserva.', verbose_name=b'Fecha y hora para la Reserva.'),
        ),
        migrations.AlterUniqueTogether(
            name='clientedocumento',
            unique_together=set([('tipo_documento', 'numero_documento')]),
        ),
    ]
