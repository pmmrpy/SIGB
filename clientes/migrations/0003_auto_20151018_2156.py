# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0002_auto_20151018_2152'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='fecha_nacimiento',
            field=models.DateField(default=datetime.datetime(2015, 10, 19, 0, 56, 40, 579000, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='reserva',
            name='fecha_hora',
            field=models.DateTimeField(default=datetime.datetime(2015, 10, 19, 0, 56, 40, 582000, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='reserva',
            name='usuario_registro',
            field=models.ForeignKey(default=b'1', to=settings.AUTH_USER_MODEL),
        ),
    ]
