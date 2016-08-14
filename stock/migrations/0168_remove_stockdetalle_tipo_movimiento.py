# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0167_auto_20160809_1019'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='stockdetalle',
            name='tipo_movimiento',
        ),
    ]
