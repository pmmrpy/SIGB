# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ventas', '0027_auto_20160807_2113'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aperturacaja',
            name='caja',
            field=models.ForeignKey(verbose_name=b'Caja a Aperturar', to='bar.Caja', help_text=b'Seleccione la Caja a aperturar.'),
        ),
        migrations.AlterField(
            model_name='aperturacaja',
            name='cajero',
            field=models.ForeignKey(verbose_name=b'Cajero', to='personal.Empleado', help_text=b'Seleccione el Cajero que realizara movimientos en esta Caja.'),
        ),
        migrations.AlterField(
            model_name='ventadetalle',
            name='total_producto_venta',
            field=models.DecimalField(default=0, help_text=b'Este valor se calcula automaticamente tomando el Precio del Producto por la Cantidad del Producto.', verbose_name=b'Total del Producto ordenado por el Cliente.', max_digits=18, decimal_places=0),
        ),
    ]
