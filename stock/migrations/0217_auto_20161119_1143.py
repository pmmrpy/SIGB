# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0216_auto_20161119_0900'),
    ]

    operations = [
        migrations.CreateModel(
            name='TransferenciaStockDetalle',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cantidad_producto_transferencia', models.DecimalField(help_text=b'Cantidad a transferir del Producto.', verbose_name=b'Cantidad a transferir', max_digits=10, decimal_places=3)),
                ('producto_transferencia', models.ForeignKey(related_name='producto_solicitado', verbose_name=b'Producto a transferir', to='stock.Producto', help_text=b'Seleccione el producto a transferir entre Depositos.')),
            ],
            options={
                'verbose_name': 'Detalle de Transferencia de Productos entre Depositos',
                'verbose_name_plural': 'Detalles de Transferencias de Productos entre Depositos',
            },
        ),
        migrations.AlterModelOptions(
            name='transferenciastock',
            options={'verbose_name': 'Transferencia de Productos entre Depositos', 'verbose_name_plural': 'Transferencias de Productos entre Depositos'},
        ),
        migrations.RemoveField(
            model_name='transferenciastock',
            name='cantidad_producto_transferencia',
        ),
        migrations.RemoveField(
            model_name='transferenciastock',
            name='producto_transferencia',
        ),
        migrations.AlterField(
            model_name='transferenciastock',
            name='fecha_hora_autorizacion_transferencia',
            field=models.DateTimeField(help_text=b'La fecha y hora se asignan al momento de autorizarse la Transferencia. No se requiere el ingreso de este dato.', null=True, verbose_name=b'Fecha/hora autorizacion Transferencia', blank=True),
        ),
        migrations.AddField(
            model_name='transferenciastockdetalle',
            name='transferencia',
            field=models.ForeignKey(to='stock.TransferenciaStock'),
        ),
    ]
