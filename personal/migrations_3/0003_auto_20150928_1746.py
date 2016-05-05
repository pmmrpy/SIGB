# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('personal', '0002_auto_20150928_1701'),
    ]

    operations = [
        migrations.AlterField(
            model_name='empleado',
            name='fecha_nacimiento',
            field=models.DateField(default=datetime.datetime(2015, 9, 28, 21, 46, 7, 593000, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='empleado',
            name='telefono',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='empleado',
            name='telefono_movil',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='horario',
            name='horario_fin',
            field=models.TimeField(default=datetime.datetime(2015, 9, 28, 21, 46, 7, 596000, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='horario',
            name='horario_inicio',
            field=models.TimeField(default=datetime.datetime(2015, 9, 28, 21, 46, 7, 596000, tzinfo=utc)),
        ),
    ]
