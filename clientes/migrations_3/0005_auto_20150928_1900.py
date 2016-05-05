# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('personal', '0004_auto_20150928_1900'),
        ('clientes', '0004_auto_20150928_1745'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='documentos',
            field=models.ManyToManyField(to='bar.Documento', through='clientes.ClienteDocumento'),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='fecha_nacimiento',
            field=models.DateField(default=datetime.datetime(2015, 9, 28, 23, 0, 58, 112000, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='clientedocumento',
            name='tipo_documento',
            field=models.ForeignKey(to='bar.Documento'),
        ),
        migrations.AlterField(
            model_name='reserva',
            name='descripcion',
            field=models.CharField(default=b'Reserva de Mesa', max_length=50),
        ),
        migrations.AlterField(
            model_name='reserva',
            name='estado',
            field=models.ForeignKey(to='bar.ReservaEstado'),
        ),
        migrations.AlterField(
            model_name='reserva',
            name='fecha_hora',
            field=models.DateTimeField(default=datetime.datetime(2015, 9, 28, 23, 0, 58, 114000, tzinfo=utc)),
        ),
        migrations.DeleteModel(
            name='Documento',
        ),
        migrations.DeleteModel(
            name='ReservaEstado',
        ),
    ]
