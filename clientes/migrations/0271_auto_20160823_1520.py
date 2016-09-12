# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0270_auto_20160823_1510'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clientedocumento',
            name='tipo_documento',
            field=models.ForeignKey(verbose_name=b'Tipo de Documento', to='bar.Documento', help_text=b'Seleccione el Tipo de Documento del Cliente.'),
        ),
        migrations.AlterField(
            model_name='reserva',
            name='fecha_hora_reserva',
            field=models.DateTimeField(default=datetime.datetime(2016, 8, 23, 19, 20, 5, 998000, tzinfo=utc), help_text=b'Ingrese la fecha y hora de la Reserva.', verbose_name=b'Fecha y hora para la Reserva.'),
        ),
    ]
