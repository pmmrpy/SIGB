# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0054_auto_20151112_2256'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='telefonomovilcliente',
            name='cliente',
        ),
        migrations.RemoveField(
            model_name='telefonomovilcliente',
            name='codigo_ciudad_operadora_telefono',
        ),
        migrations.RemoveField(
            model_name='telefonomovilcliente',
            name='codigo_pais_telefono',
        ),
        migrations.AlterField(
            model_name='cliente',
            name='fecha_nacimiento',
            field=models.DateField(default=datetime.datetime(2015, 12, 10, 19, 56, 49, 608000, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='reserva',
            name='fecha_hora',
            field=models.DateTimeField(default=datetime.datetime(2015, 12, 10, 19, 56, 49, 615000, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='telefonocliente',
            name='telefono',
            field=models.IntegerField(help_text=b'Ingrese el telefono fijo o movil del cliente. El dato debe contener solo numeros.'),
        ),
        migrations.DeleteModel(
            name='TelefonoMovilCliente',
        ),
    ]
