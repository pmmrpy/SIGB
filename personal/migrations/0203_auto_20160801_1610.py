# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('personal', '0202_auto_20160731_2055'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cargo',
            name='descripcion_cargo',
            field=models.CharField(default=b'Cargo', help_text=b'Ingrese la descripcion del Cargo. (Hasta 50 caracteres)', max_length=50, verbose_name=b'Descripcion del Cargo'),
        ),
        migrations.AlterField(
            model_name='horario',
            name='horario_fin',
            field=models.TimeField(default=datetime.datetime(2016, 8, 1, 20, 10, 34, 868000, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='horario',
            name='horario_inicio',
            field=models.TimeField(default=datetime.datetime(2016, 8, 1, 20, 10, 34, 868000, tzinfo=utc)),
        ),
    ]
