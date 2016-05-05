# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0021_auto_20151025_1834'),
    ]

    operations = [
        migrations.AddField(
            model_name='cliente',
            name='sexo',
            field=models.CharField(default=b'F', max_length=1, choices=[(b'F', b'Femenino'), (b'M', b'Masculino')]),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='fecha_nacimiento',
            field=models.DateField(default=datetime.datetime(2015, 10, 26, 1, 38, 42, 93000, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='reserva',
            name='fecha_hora',
            field=models.DateTimeField(default=datetime.datetime(2015, 10, 26, 1, 38, 42, 95000, tzinfo=utc)),
        ),
    ]
