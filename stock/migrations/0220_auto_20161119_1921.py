# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bar', '0413_auto_20161119_1921'),
        ('stock', '0219_auto_20161119_1451'),
    ]

    operations = [
        migrations.AddField(
            model_name='transferenciastockdetalle',
            name='unidad_medida',
            field=models.ForeignKey(related_name='un_med_transferencia', default=3, verbose_name=b'Unidad de Medida', to='bar.UnidadMedidaProducto', help_text=b'Corresponde a la Unidad de Medida del contenido del Producto.'),
        ),
        migrations.AlterField(
            model_name='transferenciastockdetalle',
            name='cantidad_producto_transferencia',
            field=models.DecimalField(help_text=b'Ingrese la cantidad a transferir del Producto.', verbose_name=b'Cantidad a transferir', max_digits=10, decimal_places=3),
        ),
    ]
