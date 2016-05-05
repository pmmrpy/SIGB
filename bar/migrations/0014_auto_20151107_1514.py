# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('bar', '0013_auto_20151107_1436'),
    ]

    operations = [
        migrations.CreateModel(
            name='FormaPagoCompra',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('forma_pago_compra', models.CharField(help_text=b'Contado / Credito', max_length=50)),
                ('plazo_compra', models.IntegerField(help_text=b'En caso de Credito establecer el plazo de tiempo para el pago')),
            ],
        ),
        migrations.CreateModel(
            name='FormaPagoVenta',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('forma_pago_venta', models.CharField(help_text=b'Contado / TC / TD', max_length=50)),
            ],
        ),
        migrations.DeleteModel(
            name='FormaPago',
        ),
        migrations.AlterField(
            model_name='cotizacion',
            name='fecha_cotizacion',
            field=models.DateTimeField(default=datetime.datetime(2015, 11, 7, 18, 14, 12, 439000, tzinfo=utc), help_text=b'Registra la fecha en la que se definio la cotizacion. Corresponde a la fecha y hora actual'),
        ),
    ]
