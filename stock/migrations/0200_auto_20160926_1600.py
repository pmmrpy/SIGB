# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bar', '0285_auto_20160926_1600'),
        ('stock', '0199_auto_20160925_1248'),
    ]

    operations = [
        migrations.CreateModel(
            name='MovimientoStock',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('id_movimiento', models.PositiveIntegerField(help_text=b'Identificador del movimiento en el Stock.', verbose_name=b'ID Movimiento')),
                ('cantidad_entrante', models.DecimalField(help_text=b'Cantidad entrante al Stock del producto.', verbose_name=b'Cantidad Entrante', max_digits=10, decimal_places=3)),
                ('cantidad_saliente', models.DecimalField(help_text=b'Cantidad saliente del Stock del producto.', verbose_name=b'Cantidad Saliente', max_digits=10, decimal_places=3)),
                ('fecha_hora_registro_stock', models.DateTimeField(help_text=b'La fecha y hora se asignan al momento de guardar los datos del Detalle del Stock. No se requiere el ingreso de este dato.', verbose_name=b'Fecha/hora registro movimiento', auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Movimientos de Stock',
                'verbose_name_plural': 'Movimientos de Stock',
            },
        ),
        migrations.RemoveField(
            model_name='ingresodeposito',
            name='producto',
        ),
        migrations.RemoveField(
            model_name='stock',
            name='producto_stock',
        ),
        migrations.RemoveField(
            model_name='stockdetalle',
            name='stock',
        ),
        migrations.RemoveField(
            model_name='stockdetalle',
            name='tipo_movimiento',
        ),
        migrations.RemoveField(
            model_name='stockdetalle',
            name='ubicacion_destino',
        ),
        migrations.RemoveField(
            model_name='stockdetalle',
            name='ubicacion_origen',
        ),
        migrations.RemoveField(
            model_name='producto',
            name='cantidad_existente_stock',
        ),
        migrations.AddField(
            model_name='producto',
            name='stock_minimo',
            field=models.DecimalField(default=0, help_text=b'Cantidad minima del Producto a mantener en Stock.', verbose_name=b'Stock Minimo', max_digits=10, decimal_places=3),
        ),
        migrations.AlterField(
            model_name='transferenciastock',
            name='producto_transferencia',
            field=models.ForeignKey(related_name='producto_solicitado', verbose_name=b'Producto a Transferir', to='stock.Producto', help_text=b'Seleccione el producto a Transferir entre depositos.'),
        ),
        migrations.DeleteModel(
            name='IngresoDeposito',
        ),
        migrations.DeleteModel(
            name='Stock',
        ),
        migrations.DeleteModel(
            name='StockDetalle',
        ),
        migrations.AddField(
            model_name='movimientostock',
            name='producto_stock',
            field=models.ForeignKey(related_name='producto_stock', default=2, verbose_name=b'Producto', to='stock.Producto', help_text=b'Seleccione el Producto a registrar en el Stock.'),
        ),
        migrations.AddField(
            model_name='movimientostock',
            name='tipo_movimiento',
            field=models.ForeignKey(default=1, verbose_name=b'Tipo de Movimiento', to='bar.TipoMovimientoStock', help_text=b'Seleccione el identificador del Tipo de Movimiento de Stock.'),
        ),
        migrations.AddField(
            model_name='movimientostock',
            name='ubicacion_destino',
            field=models.ForeignKey(related_name='ubicacion_destino', verbose_name=b'Ubicacion Destino', to='bar.Deposito', help_text=b'Ubicacion a donde se dirige el movimiento de Stock.'),
        ),
        migrations.AddField(
            model_name='movimientostock',
            name='ubicacion_origen',
            field=models.ForeignKey(related_name='ubicacion_origen', verbose_name=b'Ubicacion Origen', to='bar.Deposito', help_text=b'Ubicacion desde donde se origina el movimiento de Stock.'),
        ),
    ]
