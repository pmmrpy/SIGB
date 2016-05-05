# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('personal', '0010_auto_20151020_2154'),
    ]

    operations = [
        migrations.AddField(
            model_name='empleado',
            name='cargo_empleado',
            field=models.ForeignKey(default=1, to='personal.Cargo'),
        ),
        migrations.AlterField(
            model_name='empleado',
            name='fecha_nacimiento',
            field=models.DateField(default=datetime.datetime(2015, 10, 21, 1, 3, 41, 505000, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='horario',
            name='horario_fin',
            field=models.TimeField(default=datetime.datetime(2015, 10, 21, 1, 3, 41, 510000, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='horario',
            name='horario_inicio',
            field=models.TimeField(default=datetime.datetime(2015, 10, 21, 1, 3, 41, 510000, tzinfo=utc)),
        ),
    ]
