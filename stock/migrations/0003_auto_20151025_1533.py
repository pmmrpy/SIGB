# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bar', '0004_tipodeposito_tipoproducto'),
        ('stock', '0002_auto_20151024_1948'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='tipo_producto',
            field=models.ForeignKey(default=1, to='bar.TipoProducto'),
        ),
        migrations.AlterField(
            model_name='deposito',
            name='tipo_deposito',
            field=models.ForeignKey(to='bar.TipoDeposito'),
        ),
        migrations.RemoveField(
            model_name='producto',
            name='precio_venta',
        ),
        migrations.AddField(
            model_name='producto',
            name='precio_venta',
            field=models.ManyToManyField(related_name='precio', to='stock.PrecioProducto'),
        ),
        migrations.DeleteModel(
            name='TipoDeposito',
        ),
    ]
