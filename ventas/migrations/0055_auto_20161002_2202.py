# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ventas', '0054_auto_20161002_1822'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pedido',
            old_name='fecha_pedido',
            new_name='fecha_hora_pedido',
        ),
    ]
