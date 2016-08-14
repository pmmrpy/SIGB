# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('personal', '0217_auto_20160810_1136'),
    ]

    operations = [
        migrations.AlterField(
            model_name='horario',
            name='horario_fin',
            field=models.TimeField(default=datetime.datetime(2016, 8, 11, 14, 59, 18, 648000, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='horario',
            name='horario_inicio',
            field=models.TimeField(default=datetime.datetime(2016, 8, 11, 14, 59, 18, 648000, tzinfo=utc)),
        ),
    ]
