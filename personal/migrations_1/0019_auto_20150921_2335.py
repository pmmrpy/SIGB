# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('personal', '0018_auto_20150921_2135'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='empleado',
            name='documentos',
        ),
        migrations.RemoveField(
            model_name='empleadodocumento',
            name='tipo_documento',
        ),
        migrations.AlterField(
            model_name='empleado',
            name='fecha_nacimiento',
            field=models.DateField(default=datetime.datetime(2015, 9, 22, 3, 35, 1, 741000, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='horario',
            name='horario_fin',
            field=models.TimeField(default=datetime.datetime(2015, 9, 22, 3, 35, 1, 742000, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='horario',
            name='horario_inicio',
            field=models.TimeField(default=datetime.datetime(2015, 9, 22, 3, 35, 1, 742000, tzinfo=utc)),
        ),
    ]
