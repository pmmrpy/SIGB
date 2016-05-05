# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0002_auto_20150823_1735'),
    ]

    operations = [
        migrations.AddField(
            model_name='documento',
            name='descripcion',
            field=models.CharField(default=b'documento', max_length=50),
        ),
        migrations.AddField(
            model_name='documento',
            name='id',
            field=models.AutoField(serialize=False),
        ),
        migrations.AddField(
            model_name='reserva',
            name='reserva_descripcion',
            field=models.CharField(default=b'Reserva', max_length=50),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='fecha_nacimiento',
            field=models.DateField(default=datetime.datetime(2015, 9, 19, 0, 32, 42, 704000, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='documento',
            name='documento',
            field=models.CharField(max_length=3),
        ),
        migrations.AlterField(
            model_name='reserva',
            name='reserva_estado',
            field=models.CharField(max_length=1),
        ),
    ]
