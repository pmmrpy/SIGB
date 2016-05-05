# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0003_auto_20151025_1533'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='producto',
            name='precio_venta',
        ),
    ]
