# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0204_productoventa'),
        ('ventas', '0074_auto_20161016_1054'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comanda',
            name='producto_a_elaborar',
        ),
        migrations.AddField(
            model_name='comanda',
            name='producto_a_entregar',
            field=models.ForeignKey(default=2, verbose_name=b'Producto Solicitado', to='stock.ProductoVenta'),
        ),
        migrations.AlterField(
            model_name='comanda',
            name='area_solicitante',
            field=models.ForeignKey(related_name='area_solicitante_comanda', verbose_name=b'Area Encargada', to='bar.Sector'),
        ),
    ]
