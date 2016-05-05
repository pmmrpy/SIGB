# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('personal', '0060_auto_20151211_1536'),
    ]

    operations = [
        migrations.AddField(
            model_name='empleado',
            name='barrio',
            field=models.CharField(max_length=100, blank=True),
        ),
        migrations.AlterField(
            model_name='empleado',
            name='email',
            field=models.EmailField(default=b'mail@ejemplo.com', max_length=254, blank=True),
        ),
        migrations.AlterField(
            model_name='empleado',
            name='fecha_nacimiento',
            field=models.DateField(default=datetime.datetime(2015, 12, 11, 18, 56, 27, 279000, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='horario',
            name='horario_fin',
            field=models.TimeField(default=datetime.datetime(2015, 12, 11, 18, 56, 27, 294000, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='horario',
            name='horario_inicio',
            field=models.TimeField(default=datetime.datetime(2015, 12, 11, 18, 56, 27, 294000, tzinfo=utc)),
        ),
    ]
