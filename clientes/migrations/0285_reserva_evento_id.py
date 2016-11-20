# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('calendarium', '0001_initial'),
        ('clientes', '0284_auto_20161111_1123'),
    ]

    operations = [
        migrations.AddField(
            model_name='reserva',
            name='evento_id',
            field=models.ForeignKey(default=1, to='calendarium.Event'),
        ),
    ]
