# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('ventas', '0029_auto_20160809_1019'),
        ('bar', '0190_auto_20160808_1006'),
    ]

    operations = [
        migrations.CreateModel(
            name='Factura',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('numero_factura_inicial', models.PositiveIntegerField()),
                ('numero_factura_final', models.PositiveIntegerField()),
                ('numero_factura_actual', models.PositiveIntegerField()),
                ('caja', models.OneToOneField(to='bar.Caja')),
            ],
        ),
        migrations.CreateModel(
            name='TipoMovimientoStock',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tipo_movimiento_stock', models.CharField(help_text=b'Ingrese el identificador del Tipo de Movimiento de Stock. (Hasta 2 caracteres)', max_length=2, verbose_name=b'Tipo de Movimiento de Stock', choices=[(b'VE', b'Venta'), (b'CO', b'Compra'), (b'ME', b'Mermas'), (b'TR', b'Transferencias'), (b'DE', b'Devoluciones')])),
                ('descripcion', models.CharField(help_text=b'Ingrese la descripcion del Tipo de Movimiento de Stock. (Hasta 200 caracteres)', max_length=200, verbose_name=b'Descripcion del Tipo de Movimiento de Stock')),
            ],
            options={
                'ordering': ('id',),
                'verbose_name': 'Stock - Tipo de Movimiento',
                'verbose_name_plural': 'Stock - Tipos de Movimientos',
            },
        ),
        migrations.CreateModel(
            name='TransferenciaStockEstado',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('estado_transferencia_stock', models.CharField(help_text=b'Ingrese el identificador del Estado de la Transferencia de Stock entre depositos. (Hasta 3 caracteres)', max_length=3, verbose_name=b'Estado de la Transferencia de Stock', choices=[(b'PEN', b'Pendiente'), (b'PRO', b'Procesada'), (b'CAN', b'Cancelada')])),
                ('descripcion', models.CharField(help_text=b'Ingrese la descripcion del Estado del Pedido. (Hasta 200 caracteres)', max_length=200, verbose_name=b'Descripcion del Estado')),
            ],
            options={
                'ordering': ('id',),
                'verbose_name': 'Stock - Transferencia - Estado',
                'verbose_name_plural': 'Stock - Transferencias - Estados',
            },
        ),
        migrations.RemoveField(
            model_name='facturas',
            name='caja',
        ),
        migrations.AlterField(
            model_name='timbrado',
            name='fecha_autorizacion_timbrado',
            field=models.DateField(default=datetime.datetime(2016, 8, 9, 10, 19, 29, 2000), help_text=b'Ingrese la Fecha de Autorizacion del Timbrado', verbose_name=b'Fecha de Autorizacion del Timbrado'),
        ),
        migrations.AlterField(
            model_name='timbrado',
            name='fecha_limite_vigencia_timbrado',
            field=models.DateField(default=datetime.datetime(2017, 8, 9, 10, 19, 29, 2000), help_text=b'Ingrese la Fecha Limite de Vigencia del Timbrado', verbose_name=b'Fecha Limite de Vigencia del Timbrado'),
        ),
        migrations.DeleteModel(
            name='Facturas',
        ),
    ]
