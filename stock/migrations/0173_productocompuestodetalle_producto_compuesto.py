# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0172_auto_20160814_1133'),
    ]

    operations = [
        migrations.AddField(
            model_name='productocompuestodetalle',
            name='producto_compuesto',
            field=models.ForeignKey(related_name='producto_cabecera', to='stock.ProductoCompuesto', null=True),
        ),
    ]
