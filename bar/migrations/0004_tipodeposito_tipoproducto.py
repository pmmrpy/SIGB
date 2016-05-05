# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bar', '0003_auto_20151025_1138'),
    ]

    operations = [
        migrations.CreateModel(
            name='TipoDeposito',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tipo_deposito', models.CharField(max_length=2)),
                ('descripcion', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='TipoProducto',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tipo_producto', models.CharField(max_length=2)),
                ('descripcion', models.CharField(max_length=100)),
            ],
        ),
    ]
