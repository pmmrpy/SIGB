# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('personal', '0004_auto_20150928_1900'),
    ]

    operations = [
        migrations.AlterField(
            model_name='empleado',
            name='fecha_nacimiento',
            field=models.DateField(default=datetime.datetime(2015, 9, 28, 23, 3, 15, 24000, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='empleadodocumento',
            name='tipo_documento',
            field=models.ForeignKey(to='bar.Documento'),
        ),
        migrations.AlterField(
            model_name='horario',
            name='horario_fin',
            field=models.TimeField(default=datetime.datetime(2015, 9, 28, 23, 3, 15, 26000, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='horario',
            name='horario_inicio',
            field=models.TimeField(default=datetime.datetime(2015, 9, 28, 23, 3, 15, 26000, tzinfo=utc)),
        ),
    ]
