# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('personal', '0095_auto_20160601_0056'),
    ]

    operations = [
        migrations.AlterField(
            model_name='empleado',
            name='fecha_nacimiento',
            field=models.DateField(default=datetime.datetime(2016, 6, 1, 4, 57, 40, 344000, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='horario',
            name='horario_fin',
            field=models.TimeField(default=datetime.datetime(2016, 6, 1, 4, 57, 40, 347000, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='horario',
            name='horario_inicio',
            field=models.TimeField(default=datetime.datetime(2016, 6, 1, 4, 57, 40, 347000, tzinfo=utc)),
        ),
    ]
