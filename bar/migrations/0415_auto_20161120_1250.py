# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('bar', '0414_auto_20161120_0959'),
    ]

    operations = [
        migrations.CreateModel(
            name='AjusteStockEstado',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('estado_ajuste_stock', models.CharField(help_text=b'Ingrese el identificador del Estado del Ajuste de Stock. (Hasta 3 caracteres)', max_length=3, verbose_name=b'Estado del Ajuste de Stock', choices=[(b'PEN', b'Pendiente'), (b'PRO', b'Procesada'), (b'CAN', b'Cancelada')])),
                ('descripcion', models.CharField(help_text=b'Ingrese la descripcion del Estado del Ajuste de Stock. (Hasta 200 caracteres)', max_length=200, verbose_name=b'Descripcion del Estado')),
            ],
            options={
                'ordering': ('id',),
                'verbose_name': 'Stock - Ajuste de Inventario - Estado',
                'verbose_name_plural': 'Stock - Ajustes de Inventario - Estados',
            },
        ),
        migrations.AlterField(
            model_name='timbrado',
            name='fecha_limite_vigencia_timbrado',
            field=models.DateField(default=datetime.datetime(2017, 11, 20, 12, 50, 9, 452000), help_text=b'Ingrese la Fecha Limite de Vigencia del Timbrado', verbose_name=b'Fecha Limite de Vigencia del Timbrado'),
        ),
        migrations.AlterField(
            model_name='transferenciastockestado',
            name='descripcion',
            field=models.CharField(help_text=b'Ingrese la descripcion del Estado de la Transferencia entre Depositos. (Hasta 200 caracteres)', max_length=200, verbose_name=b'Descripcion del Estado'),
        ),
    ]
