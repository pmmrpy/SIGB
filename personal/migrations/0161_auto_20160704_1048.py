# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('personal', '0160_auto_20160628_1534'),
    ]

    operations = [
        migrations.AlterField(
            model_name='empleado',
            name='fecha_nacimiento',
            field=models.DateField(default=datetime.datetime(2016, 7, 4, 14, 48, 34, 369000, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='empleadotelefono',
            name='codigo_operadora_telefono',
            field=models.ForeignKey(help_text=b'Seleccione el codigo de ciudad u operadora para el numero de telefono.', to='bar.CodigoOperadoraTelefono'),
        ),
        migrations.AlterField(
            model_name='empleadotelefono',
            name='codigo_pais_telefono',
            field=models.ForeignKey(help_text=b'Seleccione el codigo de pais para el numero de telefono.', to='bar.CodigoPaisTelefono'),
        ),
        migrations.AlterField(
            model_name='horario',
            name='horario_fin',
            field=models.TimeField(default=datetime.datetime(2016, 7, 4, 14, 48, 34, 371000, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='horario',
            name='horario_inicio',
            field=models.TimeField(default=datetime.datetime(2016, 7, 4, 14, 48, 34, 371000, tzinfo=utc)),
        ),
    ]
