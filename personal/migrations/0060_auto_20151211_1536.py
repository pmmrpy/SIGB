# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('personal', '0059_auto_20151211_1531'),
    ]

    operations = [
        migrations.AddField(
            model_name='empleado',
            name='cargo',
            field=models.ForeignKey(default=1, to='personal.Cargo'),
        ),
        migrations.AlterField(
            model_name='empleado',
            name='fecha_nacimiento',
            field=models.DateField(default=datetime.datetime(2015, 12, 11, 18, 36, 53, 206000, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='horario',
            name='horario_fin',
            field=models.TimeField(default=datetime.datetime(2015, 12, 11, 18, 36, 53, 213000, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='horario',
            name='horario_inicio',
            field=models.TimeField(default=datetime.datetime(2015, 12, 11, 18, 36, 53, 213000, tzinfo=utc)),
        ),
    ]
