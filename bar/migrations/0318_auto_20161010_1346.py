# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('bar', '0317_auto_20161008_2004'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sector',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('sector', models.CharField(help_text=b'Seleccione el identificador del Sector.', max_length=3, verbose_name=b'Sector', choices=[(b'DCE', b'Deposito Central'), (b'DBP', b'Deposito Barra Principal'), (b'DBA', b'Deposito Barra Arriba'), (b'DBI', b'Deposito Barrita'), (b'DCO', b'Deposito Cocina'), (b'BPR', b'Barra Principal'), (b'BAR', b'Barra Arriba'), (b'BAI', b'Barrita'), (b'COC', b'Cocina')])),
                ('descripcion', models.CharField(help_text=b'Ingrese la descripcion del Sector. (Hasta 100 caracteres)', max_length=100, verbose_name=b'Descripcion del Sector')),
            ],
            options={
                'verbose_name': 'Sector',
                'verbose_name_plural': 'Sectores',
            },
        ),
        migrations.RemoveField(
            model_name='caja',
            name='ubicacion',
        ),
        migrations.AlterField(
            model_name='facturaventa',
            name='numero_serie',
            field=models.PositiveIntegerField(unique=True, verbose_name=b'Numero de Serie'),
        ),
        migrations.AlterField(
            model_name='formapagoventa',
            name='forma_pago_venta',
            field=models.CharField(max_length=2, verbose_name=b'Forma de Pago Venta', choices=[(b'EF', b'Efectivo'), (b'TC', b'Tarjeta de Credito'), (b'TD', b'Tarjeta de Debito'), (b'OM', b'Otros medios')]),
        ),
        migrations.AlterField(
            model_name='timbrado',
            name='fecha_limite_vigencia_timbrado',
            field=models.DateField(default=datetime.datetime(2017, 10, 10, 13, 46, 52, 351000), help_text=b'Ingrese la Fecha Limite de Vigencia del Timbrado', verbose_name=b'Fecha Limite de Vigencia del Timbrado'),
        ),
        migrations.DeleteModel(
            name='CajaUbicacion',
        ),
    ]
