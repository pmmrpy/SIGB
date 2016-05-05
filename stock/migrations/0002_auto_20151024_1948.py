# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='contenido',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='producto',
            name='imagen',
            field=models.ImageField(default=1, upload_to=b''),
        ),
    ]
