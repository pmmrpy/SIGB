# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0194_auto_20160828_2031'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='tipo_producto',
            field=models.CharField(default=b'VE', help_text=b'Seleccione el Tipo de Producto.', max_length=2, verbose_name=b'Tipo de Producto', choices=[(b'VE', b'Para la Venta'), (b'IN', b'Insumo')]),
        ),
    ]
