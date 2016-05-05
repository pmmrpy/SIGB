# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0013_auto_20150918_2059'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='documento',
            name='id',
        ),
        migrations.AlterField(
            model_name='cliente',
            name='fecha_nacimiento',
            field=models.DateField(default=datetime.datetime(2015, 9, 19, 1, 1, 38, 159000, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='documento',
            name='documento',
            field=models.CharField(max_length=3, serialize=False, primary_key=True, choices=[(b'CI', b'Cedula de Identidad'), (b'RUC', b'Registro Unico del Contribuyente'), (b'P', b'Pasaporte'), (b'RC', b'Registro de Conducir')]),
        ),
    ]
