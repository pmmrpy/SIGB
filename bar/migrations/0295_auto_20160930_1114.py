# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('bar', '0294_auto_20160928_0742'),
    ]

    operations = [
        migrations.CreateModel(
            name='FacturaProveedorEstado',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('estado_factura_proveedor', models.CharField(max_length=3, verbose_name=b'Estado de la Factura del Proveedor', choices=[(b'EPP', b'En Plazo de Pago'), (b'FPP', b'Fuera del Plazo de Pago'), (b'PAG', b'Pagada'), (b'CAN', b'Cancelada')])),
                ('descripcion', models.CharField(help_text=b'Ingrese la descripcion del Estado de la Factura del Proveedor. (Hasta 200 caracteres)', max_length=200, verbose_name=b'Descripcion del Estado de la Factura del Proveedor')),
            ],
            options={
                'verbose_name': 'Factura Proveedor - Estado',
                'verbose_name_plural': 'Facturas Proveedores - Estados',
            },
        ),
        migrations.CreateModel(
            name='OrdenPagoEstado',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('estado_orden_pago', models.CharField(max_length=3, verbose_name=b'Estado de la Orden de Pago', choices=[(b'PEN', b'Pendiente'), (b'CON', b'Confirmada'), (b'ANU', b'Anulada'), (b'CAN', b'Cancelada')])),
                ('descripcion', models.CharField(help_text=b'Ingrese la descripcion del Estado de la Orden de Pago. (Hasta 200 caracteres)', max_length=200, verbose_name=b'Descripcion del Estado de la Orden de Pago')),
            ],
            options={
                'verbose_name': 'Orden de Pago - Estado',
                'verbose_name_plural': 'Ordenes de Pagos - Estados',
            },
        ),
        migrations.AlterField(
            model_name='timbrado',
            name='fecha_limite_vigencia_timbrado',
            field=models.DateField(default=datetime.datetime(2017, 9, 30, 11, 14, 26, 411000), help_text=b'Ingrese la Fecha Limite de Vigencia del Timbrado', verbose_name=b'Fecha Limite de Vigencia del Timbrado'),
        ),
        migrations.AlterField(
            model_name='timbrado',
            name='timbrado',
            field=models.CharField(help_text=b'Ingrese el numero de Timbrado.', unique=True, max_length=8, verbose_name=b'Numero de Timbrado'),
        ),
    ]
