# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ventas', '0045_auto_20160927_1414'),
    ]

    operations = [
        migrations.AddField(
            model_name='venta',
            name='posee_reserva',
            field=models.BooleanField(default=False),
        ),
    ]
