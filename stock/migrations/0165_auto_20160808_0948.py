# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0164_auto_20160808_0946'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stock',
            name='producto_stock',
            field=models.ForeignKey(related_name='producto_stock', verbose_name=b'Producto', to='stock.Producto', help_text=b'Seleccione el Producto a registrar en el Stock.'),
        ),
    ]
