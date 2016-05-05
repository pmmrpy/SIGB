# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0010_auto_20150918_2051'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='fecha_nacimiento',
            field=models.DateField(default=datetime.datetime(2015, 9, 19, 0, 54, 14, 737000, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='documento',
            name='documento',
            field=models.CharField(max_length=3),
        ),
    ]
