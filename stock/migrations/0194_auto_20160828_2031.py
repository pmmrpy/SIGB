# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0193_auto_20160828_2010'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='tipo_producto',
            field=models.CharField(default=b'VE', max_length=2, choices=[(b'VE', b'Para la venta'), (b'IN', b'Insumos')]),
        ),
    ]
