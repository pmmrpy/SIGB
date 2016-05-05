# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0005_precioproducto_activo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='precioproducto',
            name='activo',
            field=models.BooleanField(default=True),
        ),
    ]
