# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ventas', '0069_auto_20161016_1018'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='venta',
            name='cliente_documento_factura',
        ),
    ]
