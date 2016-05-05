# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('personal', '0061_auto_20151211_1556'),
    ]

    operations = [
        migrations.AlterField(
            model_name='empleado',
            name='fecha_nacimiento',
            field=models.DateField(default=datetime.datetime(2015, 12, 15, 19, 23, 59, 728000, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='empleado',
            name='salario',
            field=models.DecimalField(max_digits=18, decimal_places=0),
        ),
        migrations.AlterField(
            model_name='horario',
            name='horario_fin',
            field=models.TimeField(default=datetime.datetime(2015, 12, 15, 19, 23, 59, 733000, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='horario',
            name='horario_inicio',
            field=models.TimeField(default=datetime.datetime(2015, 12, 15, 19, 23, 59, 733000, tzinfo=utc)),
        ),
    ]
