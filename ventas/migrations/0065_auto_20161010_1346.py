# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ventas', '0064_auto_20161008_1922'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comanda',
            name='area_encargada',
        ),
        migrations.RemoveField(
            model_name='pedidodetalle',
            name='anulado',
        ),
        migrations.AddField(
            model_name='pedidodetalle',
            name='cancelado',
            field=models.BooleanField(default=False, help_text=b'Seleccione esta casilla si desea cancelar el Producto solicitado.', verbose_name=b'Cancelar?'),
        ),
        migrations.AlterField(
            model_name='venta',
            name='estado_venta',
            field=models.ForeignKey(default=1, verbose_name=b'Estado Venta', to='bar.VentaEstado', help_text=b'El estado de la Venta se establece automaticamente una vez que es confirmada la misma.'),
        ),
        migrations.AlterField(
            model_name='venta',
            name='total_venta',
            field=models.DecimalField(default=0, verbose_name=b'Total Venta', max_digits=18, decimal_places=0),
        ),
    ]
