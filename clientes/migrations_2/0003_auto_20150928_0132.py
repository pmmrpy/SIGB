# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0002_auto_20150927_2202'),
    ]

    operations = [
        migrations.CreateModel(
            name='ReservaEstado',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('reserva_estado', models.CharField(max_length=1)),
                ('descripcion', models.CharField(max_length=50)),
            ],
        ),
        migrations.RenameField(
            model_name='reserva',
            old_name='reserva_descripcion',
            new_name='descripcion',
        ),
        migrations.RenameField(
            model_name='reserva',
            old_name='reserva_fecha_hora',
            new_name='fecha_hora',
        ),
        migrations.RemoveField(
            model_name='reserva',
            name='reserva_estado',
        ),
        migrations.AlterField(
            model_name='cliente',
            name='fecha_nacimiento',
            field=models.DateField(default=datetime.datetime(2015, 9, 28, 5, 32, 10, 889000, tzinfo=utc)),
        ),
        migrations.AddField(
            model_name='reserva',
            name='estado',
            field=models.ForeignKey(default=b'V', to='clientes.ReservaEstado'),
        ),
    ]
