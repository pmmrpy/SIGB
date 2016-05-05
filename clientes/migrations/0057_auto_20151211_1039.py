# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('bar', '0032_auto_20151211_1039'),
        ('clientes', '0056_auto_20151210_1746'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='email',
            field=models.EmailField(default=b'mail@example.com', max_length=254, blank=True),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='fecha_nacimiento',
            field=models.DateField(default=datetime.datetime(2015, 12, 11, 13, 39, 8, 767000, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='clientedocumento',
            name='numero_documento',
            field=models.CharField(help_text=b'Ingrese el documento del cliente. El dato puede contener numeros y letras dependiendo de la nacionalidad y tipo de documento.', unique=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='clientedocumento',
            name='tipo_documento',
            field=models.ForeignKey(help_text=b'Seleccione el tipo de documento del cliente.', to='bar.Documento'),
        ),
        migrations.AlterField(
            model_name='reserva',
            name='fecha_hora',
            field=models.DateTimeField(default=datetime.datetime(2015, 12, 11, 13, 39, 8, 773000, tzinfo=utc)),
        ),
    ]
