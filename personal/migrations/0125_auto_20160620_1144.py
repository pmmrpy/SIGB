# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('personal', '0124_auto_20160619_1909'),
    ]

    operations = [
        migrations.AlterField(
            model_name='empleado',
            name='fecha_nacimiento',
            field=models.DateField(default=datetime.datetime(2016, 6, 20, 15, 44, 48, 637000, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='horario',
            name='horario_fin',
            field=models.TimeField(default=datetime.datetime(2016, 6, 20, 15, 44, 48, 639000, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='horario',
            name='horario_inicio',
            field=models.TimeField(default=datetime.datetime(2016, 6, 20, 15, 44, 48, 639000, tzinfo=utc)),
        ),
    ]
