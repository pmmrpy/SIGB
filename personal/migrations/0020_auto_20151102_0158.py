# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('personal', '0019_auto_20151101_2104'),
    ]

    operations = [
        migrations.AlterField(
            model_name='empleado',
            name='fecha_nacimiento',
            field=models.DateField(default=datetime.datetime(2015, 11, 2, 4, 58, 53, 197000, tzinfo=utc)),
        ),
        # migrations.AlterField(
            # model_name='empleado',
            # name='horario',
            # field=models.ForeignKey(to='personal.Horario'),
        # ),
        migrations.AlterField(
            model_name='horario',
            name='horario_fin',
            field=models.TimeField(default=datetime.datetime(2015, 11, 2, 4, 58, 53, 203000, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='horario',
            name='horario_inicio',
            field=models.TimeField(default=datetime.datetime(2015, 11, 2, 4, 58, 53, 202000, tzinfo=utc)),
        ),
    ]
