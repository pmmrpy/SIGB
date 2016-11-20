# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ventas', '0071_venta_cliente_documento_factura'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='venta',
            name='cliente_documento_factura',
        ),
    ]
