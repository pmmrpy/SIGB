# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('bar', '0297_auto_20160930_1145'),
    ]

    operations = [
        migrations.CreateModel(
            name='LineaCreditoProveedorEstado',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('estado_linea_credito', models.CharField(max_length=3, verbose_name=b'Estado de la Linea de Credito con el Proveedor', choices=[(b'DEL', b'Dentro de la Linea de Credito'), (b'LIM', b'En el Limite'), (b'SOB', b'Sobregirada')])),
                ('descripcion', models.CharField(help_text=b'Ingrese la descripcion del Estado de la Linea de Credito con el Proveedor. (Hasta 200 caracteres)', max_length=200, verbose_name=b'Descripcion del Estado de la Linea de Credito con el Proveedor')),
            ],
            options={
                'verbose_name': 'Linea de Credito Proveedor - Estado',
                'verbose_name_plural': 'Linea de Credito Proveedores - Estados',
            },
        ),
        migrations.AlterField(
            model_name='timbrado',
            name='fecha_limite_vigencia_timbrado',
            field=models.DateField(default=datetime.datetime(2017, 10, 1, 15, 52, 46, 635000), help_text=b'Ingrese la Fecha Limite de Vigencia del Timbrado', verbose_name=b'Fecha Limite de Vigencia del Timbrado'),
        ),
    ]
