# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('bar', '0193_auto_20160809_1031'),
    ]

    operations = [
        migrations.CreateModel(
            name='TipoFacturaCompra',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tipo_factura_compra', models.CharField(help_text=b'Ingrese el identificador del Tipo de Factura de Compra. (Hasta 3 caracteres)', max_length=3, verbose_name=b'Tipo de Factura Compra', choices=[(b'CON', b'Contado'), (b'CRE', b'Credito')])),
                ('descripcion', models.CharField(help_text=b'Ingrese la descripcion del Tipo de Factura Compra. (Hasta 200 caracteres)', max_length=200, verbose_name=b'Descripcion del Tipo de Factura Compra')),
            ],
            options={
                'verbose_name': 'Compra - Tipo de Factura',
                'verbose_name_plural': 'Compra - Tipo de Factura',
            },
        ),
        migrations.AlterField(
            model_name='timbrado',
            name='fecha_autorizacion_timbrado',
            field=models.DateField(default=datetime.datetime(2016, 8, 10, 11, 26, 49, 332000), help_text=b'Ingrese la Fecha de Autorizacion del Timbrado', verbose_name=b'Fecha de Autorizacion del Timbrado'),
        ),
        migrations.AlterField(
            model_name='timbrado',
            name='fecha_limite_vigencia_timbrado',
            field=models.DateField(default=datetime.datetime(2017, 8, 10, 11, 26, 49, 332000), help_text=b'Ingrese la Fecha Limite de Vigencia del Timbrado', verbose_name=b'Fecha Limite de Vigencia del Timbrado'),
        ),
    ]
