# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bar', '0188_auto_20160808_0946'),
        ('stock', '0163_auto_20160804_1619'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='stockdetalle',
            options={'verbose_name': 'Detalle de Inventario de Productos', 'verbose_name_plural': 'Detalles del Inventario de Productos'},
        ),
        migrations.AddField(
            model_name='stockdetalle',
            name='ubicacion',
            field=models.ForeignKey(default=1, to='bar.Deposito', help_text=b'Ubicacion del Stock.'),
        ),
        migrations.AlterField(
            model_name='stock',
            name='producto_stock',
            field=models.ForeignKey(related_name='producto_stock', verbose_name=b'Producto', to='stock.Producto', help_text=b'Seleccione el Producto a registrar en el Stock.', unique=True),
        ),
        migrations.AlterField(
            model_name='stockdetalle',
            name='fecha_hora_registro_stock',
            field=models.DateTimeField(help_text=b'Fecha y hora de registro en el Stock.', verbose_name=b'Fecha y hora registro movimiento', auto_now_add=True),
        ),
        migrations.AlterUniqueTogether(
            name='stock',
            unique_together=set([]),
        ),
        migrations.RemoveField(
            model_name='stock',
            name='ubicacion',
        ),
    ]
