# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('bar', '0138_auto_20160628_1456'),
        ('personal', '0158_auto_20160628_1354'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='empleadotelefono',
            name='codigo_ciudad_operadora_telefono',
        ),
        migrations.AddField(
            model_name='empleadotelefono',
            name='codigo_operadora_telefono',
            field=models.ForeignKey(default=21, to='bar.CodigoOperadoraTelefono', help_text=b'Seleccione el codigo de ciudad u operadora para el numero de telefono.'),
        ),
        migrations.AlterField(
            model_name='empleado',
            name='fecha_nacimiento',
            field=models.DateField(default=datetime.datetime(2016, 6, 28, 18, 56, 19, 327000, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='horario',
            name='horario_fin',
            field=models.TimeField(default=datetime.datetime(2016, 6, 28, 18, 56, 19, 330000, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='horario',
            name='horario_inicio',
            field=models.TimeField(default=datetime.datetime(2016, 6, 28, 18, 56, 19, 330000, tzinfo=utc)),
        ),
    ]
