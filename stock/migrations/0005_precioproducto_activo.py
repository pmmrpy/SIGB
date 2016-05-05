# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0004_remove_producto_precio_venta'),
    ]

    operations = [
        migrations.AddField(
            model_name='precioproducto',
            name='activo',
            field=models.BooleanField(default=True, unique=True),
        ),
    ]
