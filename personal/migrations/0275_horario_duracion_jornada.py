# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('personal', '0274_auto_20161010_1636'),
    ]

    operations = [
        migrations.AddField(
            model_name='horario',
            name='duracion_jornada',
            field=models.TimeField(default=datetime.time(10, 0), verbose_name=b'Duracion Jornada'),
        ),
    ]
