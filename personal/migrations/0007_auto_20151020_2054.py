# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('personal', '0006_auto_20151019_0021'),
    ]

    operations = [
        # migrations.AlterField(
            # model_name='empleado',
            # name='cargo',
            # field=models.ForeignKey(to='personal.Cargo'),
        # ),
        migrations.AlterField(
            model_name='empleado',
            name='fecha_nacimiento',
            field=models.DateField(default=datetime.datetime(2015, 10, 20, 23, 54, 10, 401000, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='horario',
            name='horario_fin',
            field=models.TimeField(default=datetime.datetime(2015, 10, 20, 23, 54, 10, 407000, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='horario',
            name='horario_inicio',
            field=models.TimeField(default=datetime.datetime(2015, 10, 20, 23, 54, 10, 407000, tzinfo=utc)),
        ),
    ]
