# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('personal', '0226_auto_20160813_1050'),
    ]

    operations = [
        migrations.AlterField(
            model_name='empleado',
            name='_codigo_venta',
            field=models.PositiveIntegerField(null=True, verbose_name=b'Codigo de Venta', db_column=b'codigo_venta'),
        ),
        migrations.AlterField(
            model_name='empleado',
            name='cargo',
            field=models.ForeignKey(help_text=b'Seleccione el cargo.', to='personal.Cargo'),
        ),
        migrations.AlterField(
            model_name='empleado',
            name='ciudad',
            field=models.ForeignKey(help_text=b'Seleccione la ciudad.', to='bar.Ciudad'),
        ),
        migrations.AlterField(
            model_name='empleado',
            name='horario',
            field=models.ForeignKey(help_text=b'Seleccione el horario del Empleado.', to='personal.Horario'),
        ),
        migrations.AlterField(
            model_name='empleado',
            name='pais',
            field=models.ForeignKey(help_text=b'Seleccione el pais.', to='bar.Pais'),
        ),
        migrations.AlterField(
            model_name='empleado',
            name='usuario',
            field=models.ForeignKey(help_text=b'Seleccione el usuario del Empleado.', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='horario',
            name='horario_fin',
            field=models.TimeField(default=datetime.datetime(2016, 8, 13, 15, 13, 57, 511000, tzinfo=utc), help_text=b'Ingrese la hora de finalizacion de la jornada de trabajo.', verbose_name=b'Hora de Finalizacion Jornada'),
        ),
        migrations.AlterField(
            model_name='horario',
            name='horario_inicio',
            field=models.TimeField(default=datetime.datetime(2016, 8, 13, 15, 13, 57, 511000, tzinfo=utc), help_text=b'Ingrese la hora de inicio de la jornada de trabajo.', verbose_name=b'Hora de Inicio Jornada'),
        ),
    ]
