# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0206_auto_20160731_2055'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reserva',
            name='fecha_hora',
        ),
        migrations.AddField(
            model_name='reserva',
            name='fecha_hora_registro_reserva',
            field=models.DateTimeField(default=datetime.datetime(2016, 8, 1, 20, 10, 34, 851000, tzinfo=utc), help_text=b'Este dato se completara automaticamente cuando la Reserva sea guardada.', verbose_name=b'Fecha y hora del registro de la Reserva'),
        ),
        migrations.AddField(
            model_name='reserva',
            name='fecha_hora_reserva',
            field=models.DateTimeField(default=datetime.datetime(2016, 8, 1, 20, 10, 34, 851000, tzinfo=utc), help_text=b'Ingrese la fecha y hora de la Reserva.', verbose_name=b'Fecha y hora para la Reserva.'),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='fecha_nacimiento',
            field=models.DateField(default=datetime.datetime(2016, 8, 1, 20, 10, 34, 849000, tzinfo=utc), help_text=b'Seleccione la fecha de nacimiento del Cliente.', verbose_name=b'Fecha de Nacimiento'),
        ),
        migrations.AlterField(
            model_name='reserva',
            name='cantidad_personas',
            field=models.DecimalField(default=0, help_text=b'Ingrese la cantidad de personas que utilizaran la Reserva.', verbose_name=b'Cantidad de Personas', max_digits=5, decimal_places=0),
        ),
        migrations.AlterField(
            model_name='reserva',
            name='cliente',
            field=models.ForeignKey(help_text=b'Seleccione los datos del Cliente si ya se encuentra registrado, de lo contrario realice el alta del Cliente.', to='clientes.Cliente'),
        ),
        migrations.AlterField(
            model_name='reserva',
            name='descripcion',
            field=models.CharField(default=b'Reserva de Mesa', help_text=b'Puede ingresar alguna descripcion que identifique a la Reserva.', max_length=50),
        ),
        migrations.AlterField(
            model_name='reserva',
            name='estado',
            field=models.ForeignKey(default=1, to='bar.ReservaEstado'),
        ),
        migrations.AlterField(
            model_name='reserva',
            name='mesas',
            field=models.ManyToManyField(help_text=b'Seleccione las Mesas que seran reservadas.', to='bar.Mesa', verbose_name=b'Mesas a Reservar'),
        ),
        migrations.AlterField(
            model_name='reserva',
            name='pago',
            field=models.DecimalField(default=0, help_text=b'Ingrese el monto a pagar por la Reserva. Este monto luego se acredita en consumision.', verbose_name=b'Entrega', max_digits=18, decimal_places=0),
        ),
        migrations.AlterField(
            model_name='reserva',
            name='usuario_registro',
            field=models.ForeignKey(default=1, verbose_name=b'Usuario que registra Reserva', to=settings.AUTH_USER_MODEL),
        ),
    ]
