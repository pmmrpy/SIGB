# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ventas', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='caja',
            name='estado',
            field=models.ForeignKey(to='bar.CajaEstado'),
        ),
        migrations.AlterField(
            model_name='mesa',
            name='estado',
            field=models.ForeignKey(to='bar.MesaEstado'),
        ),
        migrations.DeleteModel(
            name='CajaEstado',
        ),
        migrations.DeleteModel(
            name='MesaEstado',
        ),
    ]
