# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('bar', '0036_auto_20151211_1322'),
        ('personal', '0056_auto_20151211_1158'),
    ]

    operations = [
        migrations.AddField(
            model_name='empleado',
            name='ciudad',
            field=models.ForeignKey(default=1, to='bar.Ciudad'),
        ),
        migrations.AddField(
            model_name='empleado',
            name='pais',
            field=models.ForeignKey(default=1, to='bar.Pais'),
        ),
        migrations.AlterField(
            model_name='empleado',
            name='fecha_nacimiento',
            field=models.DateField(default=datetime.datetime(2015, 12, 11, 16, 22, 5, 920000, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='empleadotelefono',
            name='codigo_ciudad_operadora_telefono',
            field=models.ForeignKey(default=21, to='bar.CodigoCiudadOperadoraTelefono', help_text=b'Seleccione el codigo de ciudad u operadora para el numero de telefono.'),
        ),
        migrations.AlterField(
            model_name='empleadotelefono',
            name='codigo_pais_telefono',
            field=models.ForeignKey(default=595, to='bar.CodigoPaisTelefono', help_text=b'Seleccione el codigo de pais para el numero de telefono.'),
        ),
        migrations.AlterField(
            model_name='empleadotelefono',
            name='telefono',
            field=models.IntegerField(help_text=b'Ingrese el telefono fijo o movil del empleado. El dato debe contener solo numeros.'),
        ),
        migrations.AlterField(
            model_name='horario',
            name='horario_fin',
            field=models.TimeField(default=datetime.datetime(2015, 12, 11, 16, 22, 5, 924000, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='horario',
            name='horario_inicio',
            field=models.TimeField(default=datetime.datetime(2015, 12, 11, 16, 22, 5, 924000, tzinfo=utc)),
        ),
    ]
