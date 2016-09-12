# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0185_auto_20160817_0947'),
    ]

    operations = [
        migrations.CreateModel(
            name='StockDeposito',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
            options={
                'verbose_name': 'Inventario por Deposito',
                'verbose_name_plural': 'Stock - Inventarios por Depositos',
            },
        ),
        migrations.CreateModel(
            name='StockProducto',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
            options={
                'verbose_name': 'Inventario por Producto',
                'verbose_name_plural': 'Stock - Inventarios por Productos',
            },
        ),
        migrations.AlterModelOptions(
            name='confirmatransferenciastock',
            options={'verbose_name': 'Confirmacion de Transferencia de Producto entre Deposito', 'verbose_name_plural': 'Stock - Transferencias de Productos entre Depositos - Confirmaciones'},
        ),
        migrations.AlterModelOptions(
            name='solicitatransferenciastock',
            options={'verbose_name': 'Solicitud de Transferencia de Producto entre Deposito', 'verbose_name_plural': 'Stock - Transferencias de Productos entre Depositos - Solicitudes'},
        ),
        migrations.AlterField(
            model_name='stockdetalle',
            name='id_movimiento',
            field=models.PositiveIntegerField(help_text=b'Identificador del movimiento en el Stock.', verbose_name=b'ID Movimiento'),
        ),
        migrations.AlterField(
            model_name='stockdetalle',
            name='ubicacion_destino',
            field=models.ForeignKey(related_name='ubicacion_destino', verbose_name=b'Ubicacion Destino', to='bar.Deposito', help_text=b'Ubicacion a donde se dirige el movimiento de Stock.'),
        ),
        migrations.AlterField(
            model_name='stockdetalle',
            name='ubicacion_origen',
            field=models.ForeignKey(related_name='ubicacion_origen', verbose_name=b'Ubicacion Origen', to='bar.Deposito', help_text=b'Ubicacion desde donde se origina el movimiento de Stock.'),
        ),
    ]
