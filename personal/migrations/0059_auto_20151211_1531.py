# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('personal', '0058_auto_20151211_1329'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cargo',
            name='cargo',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='cargo',
            name='id',
            field=models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True),
        ),
        migrations.AlterField(
            model_name='empleado',
            name='email',
            field=models.EmailField(default=b'mail@example.com', max_length=254, blank=True),
        ),
        migrations.AlterField(
            model_name='empleado',
            name='fecha_nacimiento',
            field=models.DateField(default=datetime.datetime(2015, 12, 11, 18, 31, 41, 846000, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='horario',
            name='horario_fin',
            field=models.TimeField(default=datetime.datetime(2015, 12, 11, 18, 31, 41, 853000, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='horario',
            name='horario_inicio',
            field=models.TimeField(default=datetime.datetime(2015, 12, 11, 18, 31, 41, 853000, tzinfo=utc)),
        ),
    ]
