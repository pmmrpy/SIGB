# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('bar', '0106_auto_20160620_1159'),
    ]

    operations = [
        migrations.CreateModel(
            name='Deposito',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('deposito', models.CharField(max_length=3)),
                ('descripcion', models.CharField(max_length=100)),
                ('tipo_deposito', models.ForeignKey(to='bar.TipoDeposito')),
            ],
        ),
        migrations.AlterField(
            model_name='cotizacion',
            name='fecha_cotizacion',
            field=models.DateTimeField(default=datetime.datetime(2016, 6, 20, 17, 4, 4, 131000, tzinfo=utc), help_text=b'Registra la fecha en la que se definio la cotizacion. Corresponde a la fecha y hora actual.'),
        ),
    ]
