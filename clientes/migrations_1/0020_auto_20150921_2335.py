# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('personal', '0019_auto_20150921_2335'),
        ('clientes', '0019_auto_20150921_2137'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cliente',
            name='documentos',
        ),
        migrations.RemoveField(
            model_name='clientedocumento',
            name='tipo_documento',
        ),
        migrations.AlterField(
            model_name='cliente',
            name='fecha_nacimiento',
            field=models.DateField(default=datetime.datetime(2015, 9, 22, 3, 35, 1, 689000, tzinfo=utc)),
        ),
        migrations.DeleteModel(
            name='Documento',
        ),
    ]
