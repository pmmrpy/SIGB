# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('bar', '0050_auto_20160528_1141'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrdenCompraEstado',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('estado_orden_compra', models.CharField(max_length=3)),
                ('descripcion', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'Orden de Compra - Estado',
                'verbose_name_plural': 'Ordenes de Compras - Estados',
            },
        ),
        migrations.AlterField(
            model_name='cotizacion',
            name='fecha_cotizacion',
            field=models.DateTimeField(default=datetime.datetime(2016, 5, 30, 18, 55, 19, 869000, tzinfo=utc), help_text=b'Registra la fecha en la que se definio la cotizacion. Corresponde a la fecha y hora actual.'),
        ),
    ]
