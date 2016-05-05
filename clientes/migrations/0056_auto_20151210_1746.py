# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('bar', '0031_auto_20151210_1746'),
        ('clientes', '0055_auto_20151210_1657'),
    ]

    operations = [
        migrations.CreateModel(
            name='ClienteTelefono',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('telefono', models.IntegerField(help_text=b'Ingrese el telefono fijo o movil del cliente. El dato debe contener solo numeros.')),
            ],
        ),
        migrations.RemoveField(
            model_name='telefonocliente',
            name='cliente',
        ),
        migrations.RemoveField(
            model_name='telefonocliente',
            name='codigo_ciudad_operadora_telefono',
        ),
        migrations.RemoveField(
            model_name='telefonocliente',
            name='codigo_pais_telefono',
        ),
        migrations.AlterField(
            model_name='cliente',
            name='fecha_nacimiento',
            field=models.DateField(default=datetime.datetime(2015, 12, 10, 20, 46, 43, 476000, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='reserva',
            name='fecha_hora',
            field=models.DateTimeField(default=datetime.datetime(2015, 12, 10, 20, 46, 43, 483000, tzinfo=utc)),
        ),
        migrations.DeleteModel(
            name='TelefonoCliente',
        ),
        migrations.AddField(
            model_name='clientetelefono',
            name='cliente',
            field=models.ForeignKey(to='clientes.Cliente'),
        ),
        migrations.AddField(
            model_name='clientetelefono',
            name='codigo_ciudad_operadora_telefono',
            field=models.ForeignKey(default=21, to='bar.CodigoCiudadOperadoraTelefono'),
        ),
        migrations.AddField(
            model_name='clientetelefono',
            name='codigo_pais_telefono',
            field=models.ForeignKey(default=595, to='bar.CodigoPaisTelefono'),
        ),
    ]
