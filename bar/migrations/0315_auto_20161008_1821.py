# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('bar', '0314_auto_20161007_1830'),
    ]

    operations = [
        migrations.CreateModel(
            name='NumeroFacturaVenta',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('numero_factura', models.DecimalField(default=1, max_digits=7, decimal_places=0)),
                ('venta_asociada', models.PositiveIntegerField()),
                ('fecha_hora_uso', models.DateTimeField()),
            ],
        ),
        migrations.AlterModelOptions(
            name='facturaventa',
            options={'verbose_name': 'Venta - Serie de Factura', 'verbose_name_plural': 'Ventas - Series de Facturas'},
        ),
        migrations.AlterModelOptions(
            name='timbrado',
            options={'verbose_name': 'Venta - Timbrado', 'verbose_name_plural': 'Ventas - Timbrados'},
        ),
        migrations.RemoveField(
            model_name='facturaventa',
            name='numero_factura_actual',
        ),
        migrations.RemoveField(
            model_name='facturaventa',
            name='venta',
        ),
        migrations.AddField(
            model_name='facturaventa',
            name='numero_serie',
            field=models.PositiveIntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='facturaventa',
            name='estado',
            field=models.CharField(default=b'ACT', help_text=b'Seleccione el estado de la Factura.', max_length=3, choices=[(b'ACT', b'Activa'), (b'INA', b'Inactiva')]),
        ),
        migrations.AlterField(
            model_name='timbrado',
            name='fecha_limite_vigencia_timbrado',
            field=models.DateField(default=datetime.datetime(2017, 10, 8, 18, 21, 6, 856000), help_text=b'Ingrese la Fecha Limite de Vigencia del Timbrado', verbose_name=b'Fecha Limite de Vigencia del Timbrado'),
        ),
        migrations.AlterField(
            model_name='ventaestado',
            name='venta_estado',
            field=models.CharField(help_text=b'Ingrese el identificador del Estado de la Venta. (Hasta 3 caracteres)', max_length=3, verbose_name=b'Estado de la Venta', choices=[(b'CON', b'Confirmada'), (b'ANU', b'Anulada')]),
        ),
        migrations.AddField(
            model_name='numerofacturaventa',
            name='serie',
            field=models.ForeignKey(to='bar.FacturaVenta'),
        ),
    ]
