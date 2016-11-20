# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0211_producto_insumo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='insumo',
            name='costo_promedio',
        ),
    ]
