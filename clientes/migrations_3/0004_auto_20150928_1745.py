# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0003_auto_20150928_1701'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='fecha_nacimiento',
            field=models.DateField(default=datetime.datetime(2015, 9, 28, 21, 45, 49, 131000, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='telefono',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='telefono_movil',
            field=models.CharField(max_length=50),
        ),
    ]
