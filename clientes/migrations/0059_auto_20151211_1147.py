# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('bar', '0034_auto_20151211_1147'),
        ('clientes', '0058_auto_20151211_1043'),
    ]

    operations = [
        migrations.AddField(
            model_name='cliente',
            name='ciudad',
            field=models.ForeignKey(default=1, to='bar.Ciudad'),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='fecha_nacimiento',
            field=models.DateField(default=datetime.datetime(2015, 12, 11, 14, 47, 4, 300000, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='clientetelefono',
            name='codigo_ciudad_operadora_telefono',
            field=models.ForeignKey(default=1, to='bar.CodigoCiudadOperadoraTelefono', help_text=b'Seleccione el codigo de ciudad u operadora para el numero de telefono.'),
        ),
        migrations.AlterField(
            model_name='clientetelefono',
            name='codigo_pais_telefono',
            field=models.ForeignKey(default=595, to='bar.CodigoPaisTelefono', help_text=b'Seleccione el codigo de pais para el numero de telefono.'),
        ),
        migrations.AlterField(
            model_name='reserva',
            name='fecha_hora',
            field=models.DateTimeField(default=datetime.datetime(2015, 12, 11, 14, 47, 4, 305000, tzinfo=utc)),
        ),
    ]
