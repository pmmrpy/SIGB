# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('personal', '0020_auto_20151102_0158'),
    ]

    operations = [
        # migrations.RemoveField(
            # model_name='empleado',
            # name='horario',
        # ),
        migrations.AlterField(
            model_name='empleado',
            name='fecha_nacimiento',
            field=models.DateField(default=datetime.datetime(2015, 11, 2, 5, 4, 6, 75000, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='horario',
            name='horario_fin',
            field=models.TimeField(default=datetime.datetime(2015, 11, 2, 5, 4, 6, 78000, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='horario',
            name='horario_inicio',
            field=models.TimeField(default=datetime.datetime(2015, 11, 2, 5, 4, 6, 78000, tzinfo=utc)),
        ),
    ]
