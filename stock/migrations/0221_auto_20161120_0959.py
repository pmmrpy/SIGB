# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0220_auto_20161119_1921'),
    ]

    operations = [
        migrations.DeleteModel(
            name='StockAjuste',
        ),
        migrations.AlterField(
            model_name='movimientostock',
            name='tipo_movimiento',
            field=models.CharField(help_text=b'Seleccione el identificador del Tipo de Movimiento de Stock.', max_length=2, verbose_name=b'Tipo de Movimiento', choices=[(b'VE', b'Venta'), (b'CO', b'Compra'), (b'TR', b'Transferencias'), (b'AI', b'Ajustes de Inventario')]),
        ),
        migrations.AlterField(
            model_name='transferenciastockdetalle',
            name='unidad_medida',
            field=models.ForeignKey(related_name='un_med_transferencia', verbose_name=b'Unidad de Medida', to='bar.UnidadMedidaProducto', help_text=b'Corresponde a la Unidad de Medida de Compra si el Producto es para la Venta o a la Unidad de Medida del Contenido si el Producto es un Insumo.'),
        ),
    ]
