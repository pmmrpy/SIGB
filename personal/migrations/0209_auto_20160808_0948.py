# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('personal', '0208_auto_20160808_0946'),
    ]

    operations = [
        migrations.AlterField(
            model_name='horario',
            name='horario_fin',
            field=models.TimeField(default=datetime.datetime(2016, 8, 8, 13, 48, 17, 630000, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='horario',
            name='horario_inicio',
            field=models.TimeField(default=datetime.datetime(2016, 8, 8, 13, 48, 17, 630000, tzinfo=utc)),
        ),
    ]
