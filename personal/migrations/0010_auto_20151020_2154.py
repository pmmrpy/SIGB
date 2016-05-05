# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('personal', '0009_auto_20151020_2114'),
    ]

    operations = [
        # migrations.AddField(
            # model_name='empleado',
            # name='cargo',
            # field=models.ForeignKey(default=b'Mozo', to='personal.Cargo'),
        # ),
        migrations.AlterField(
            model_name='cargo',
            name='cargo',
            field=models.CharField(default=b'Mozo', max_length=50),
        ),
        migrations.AlterField(
            model_name='empleado',
            name='fecha_nacimiento',
            field=models.DateField(default=datetime.datetime(2015, 10, 21, 0, 54, 26, 306000, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='horario',
            name='horario_fin',
            field=models.TimeField(default=datetime.datetime(2015, 10, 21, 0, 54, 26, 313000, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='horario',
            name='horario_inicio',
            field=models.TimeField(default=datetime.datetime(2015, 10, 21, 0, 54, 26, 313000, tzinfo=utc)),
        ),
    ]
