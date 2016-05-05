# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('bar', '0035_auto_20151211_1158'),
        ('clientes', '0059_auto_20151211_1147'),
    ]

    operations = [
        migrations.AddField(
            model_name='cliente',
            name='pais',
            field=models.ForeignKey(default=1, to='bar.Pais'),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='fecha_nacimiento',
            field=models.DateField(default=datetime.datetime(2015, 12, 11, 14, 58, 42, 990000, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='reserva',
            name='fecha_hora',
            field=models.DateTimeField(default=datetime.datetime(2015, 12, 11, 14, 58, 42, 993000, tzinfo=utc)),
        ),
    ]
