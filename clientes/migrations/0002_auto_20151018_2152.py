# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('clientes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='reserva',
            name='cantidad_personas',
            field=models.DecimalField(default=0, max_digits=5, decimal_places=0),
        ),
        migrations.AddField(
            model_name='reserva',
            name='pago',
            field=models.DecimalField(default=0, max_digits=20, decimal_places=2),
        ),
        migrations.AddField(
            model_name='reserva',
            name='usuario_registro',
            field=models.ForeignKey(default=1, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='fecha_nacimiento',
            field=models.DateField(default=datetime.datetime(2015, 10, 19, 0, 52, 45, 267000, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='reserva',
            name='fecha_hora',
            field=models.DateTimeField(default=datetime.datetime(2015, 10, 19, 0, 52, 45, 270000, tzinfo=utc)),
        ),
    ]
