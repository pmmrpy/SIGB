# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Mesa',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=20)),
                ('ubicacion', models.CharField(max_length=50)),
                ('estado', models.CharField(max_length=1, choices=[(b'A', b'Activa'), (b'I', b'Inactiva'), (b'O', b'Ocupada'), (b'D', b'Disponible')])),
            ],
        ),
    ]
