# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='email',
            field=models.EmailField(default=b'mail@example.com', max_length=254),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='fecha_nacimiento',
            field=models.DateField(default=datetime.datetime(2015, 8, 23, 21, 35, 37, 429000, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='telefono',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='telefono_movil',
            field=models.IntegerField(),
        ),
    ]
