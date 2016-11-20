# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('bar', '0311_auto_20161007_1626'),
    ]

    operations = [
        migrations.CreateModel(
            name='FormaPagoVenta',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('forma_pago_venta', models.CharField(max_length=2, verbose_name=b'Forma de Pago Venta', choices=[(b'CO', b'Contado'), (b'TC', b'Tarjeta de Credito'), (b'TD', b'Tarjeta de Debito'), (b'OM', b'Otros medios')])),
            ],
            options={
                'verbose_name': 'Forma de Pago - Venta',
                'verbose_name_plural': 'Formas de Pago - Venta',
            },
        ),
        migrations.AlterField(
            model_name='timbrado',
            name='fecha_limite_vigencia_timbrado',
            field=models.DateField(default=datetime.datetime(2017, 10, 7, 18, 17, 57, 70000), help_text=b'Ingrese la Fecha Limite de Vigencia del Timbrado', verbose_name=b'Fecha Limite de Vigencia del Timbrado'),
        ),
    ]
