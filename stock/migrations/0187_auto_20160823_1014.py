# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0186_auto_20160817_1352'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='producto',
            name='precio_venta',
        ),
        migrations.AddField(
            model_name='producto',
            name='porcentaje_ganancia',
            field=models.DecimalField(default=30, help_text=b'Ingrese el Margen de Utilidad o Porcentaje de Ganancia que desea obtener de la venta del Producto.', verbose_name=b'Porcentaje de Ganancia', max_digits=18, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='producto',
            name='compuesto',
            field=models.BooleanField(help_text=b'La casilla se marca automicamente si el Producto a ser registrado es Compuesto o no.', verbose_name=b'Es compuesto?'),
        ),
    ]
