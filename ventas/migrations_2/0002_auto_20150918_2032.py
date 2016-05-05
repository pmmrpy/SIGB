# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ventas', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Caja',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('numero', models.IntegerField()),
                ('ubicacion', models.CharField(max_length=100)),
                ('estado', models.CharField(max_length=1)),
            ],
        ),
        migrations.AlterField(
            model_name='mesa',
            name='estado',
            field=models.CharField(max_length=1),
        ),
    ]
