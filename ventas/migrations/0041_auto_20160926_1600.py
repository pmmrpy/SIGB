# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ventas', '0040_auto_20160817_1352'),
    ]

    operations = [
        migrations.DeleteModel(
            name='IngresoValorCaja',
        ),
        migrations.DeleteModel(
            name='RetiroValorCaja',
        ),
    ]
