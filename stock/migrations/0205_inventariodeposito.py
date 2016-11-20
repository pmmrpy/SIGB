# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0204_productoventa'),
    ]

    operations = [
        migrations.CreateModel(
            name='InventarioDeposito',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('producto', models.CharField(max_length=50)),
                ('cant_exist_DCE', models.IntegerField()),
                ('cant_exist_DBP', models.IntegerField()),
                ('cant_exist_DBA', models.IntegerField()),
                ('cant_exist_DCO', models.IntegerField()),
                ('cant_exist_DBI', models.IntegerField()),
                ('cantidad_existente', models.IntegerField()),
            ],
            options={
                'verbose_name': 'Inventario por Deposito',
                'db_table': 'inventario_por_deposito',
                'managed': False,
                'verbose_name_plural': 'Stock - Inventarios por Depositos',
            },
        ),
    ]
