# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('compras', '0155_auto_20160817_1352'),
        ('ventas', '0040_auto_20160817_1352'),
        ('bar', '0237_auto_20160817_0947'),
    ]

    operations = [
        migrations.CreateModel(
            name='FacturaVenta',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('estado', models.CharField(default=b'AC', help_text=b'Seleccione el estado de la Factura.', max_length=2, choices=[(b'AC', b'Activo'), (b'IN', b'Inactivo')])),
                ('numero_factura_inicial', models.DecimalField(default=1, max_digits=7, decimal_places=0)),
                ('numero_factura_final', models.DecimalField(default=9999999, max_digits=7, decimal_places=0)),
                ('numero_factura_actual', models.DecimalField(default=1, max_digits=7, decimal_places=0)),
            ],
        ),
        migrations.RemoveField(
            model_name='factura',
            name='caja',
        ),
        migrations.AddField(
            model_name='caja',
            name='punto_expedicion',
            field=models.CharField(default=b'001', help_text=b'Ingrese el Punto de Expedicion.', max_length=3, verbose_name=b'Punto de Expedicion'),
        ),
        migrations.AlterField(
            model_name='timbrado',
            name='fecha_autorizacion_timbrado',
            field=models.DateField(default=datetime.datetime(2016, 8, 17, 13, 52, 49, 390000), help_text=b'Ingrese la Fecha de Autorizacion del Timbrado', verbose_name=b'Fecha de Autorizacion del Timbrado'),
        ),
        migrations.AlterField(
            model_name='timbrado',
            name='fecha_limite_vigencia_timbrado',
            field=models.DateField(default=datetime.datetime(2017, 8, 17, 13, 52, 49, 390000), help_text=b'Ingrese la Fecha Limite de Vigencia del Timbrado', verbose_name=b'Fecha Limite de Vigencia del Timbrado'),
        ),
        migrations.DeleteModel(
            name='Factura',
        ),
        migrations.AddField(
            model_name='facturaventa',
            name='caja',
            field=models.ForeignKey(to='bar.Caja'),
        ),
        migrations.AddField(
            model_name='facturaventa',
            name='empresa',
            field=models.ForeignKey(default=1, to='compras.Empresa'),
        ),
    ]
