# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0171_auto_20160814_1120'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productocompuestodetalle',
            name='producto_compuesto',
        ),
        migrations.AddField(
            model_name='productocompuestodetalle',
            name='producto',
            field=models.ForeignKey(related_name='producto_detalle', verbose_name=b'Nombre del Producto', to='stock.Producto', help_text=b'Seleccione el o los Productos que componen este Producto Compuesto.', null=True),
        ),
    ]
