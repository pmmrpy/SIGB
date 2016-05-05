# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0014_auto_20150918_2101'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='fecha_nacimiento',
            field=models.DateField(default=datetime.datetime(2015, 9, 19, 1, 14, 18, 83000, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='documento',
            name='documento',
            field=models.CharField(default=b'CI', max_length=3, serialize=False, primary_key=True),
        ),
    ]
