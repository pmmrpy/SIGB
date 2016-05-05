# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('personal', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='empleado',
            name='email',
            field=models.EmailField(default=b'mail@example.com', max_length=254),
        ),
        migrations.AddField(
            model_name='empleado',
            name='fecha_nacimiento',
            field=models.DateField(default=datetime.datetime(2015, 8, 23, 21, 35, 37, 442000, tzinfo=utc)),
        ),
        migrations.AddField(
            model_name='horario',
            name='horario_fin',
            field=models.TimeField(default=datetime.datetime(2015, 8, 23, 21, 35, 37, 444000, tzinfo=utc)),
        ),
        migrations.AddField(
            model_name='horario',
            name='horario_inicio',
            field=models.TimeField(default=datetime.datetime(2015, 8, 23, 21, 35, 37, 444000, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='empleado',
            name='codigo_venta',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='empleado',
            name='telefono',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='empleado',
            name='telefono_movil',
            field=models.IntegerField(),
        ),
    ]
