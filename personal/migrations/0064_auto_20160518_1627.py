# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('personal', '0063_auto_20151215_1641'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='empleadodocumento',
            options={'verbose_name': 'Empleado - Documento', 'verbose_name_plural': 'Empleados - Documentos'},
        ),
        migrations.AlterModelOptions(
            name='empleadotelefono',
            options={'verbose_name': 'Empleado - Telefono', 'verbose_name_plural': 'Empleados - Telefonos'},
        ),
        migrations.AlterField(
            model_name='empleado',
            name='fecha_nacimiento',
            field=models.DateField(default=datetime.datetime(2016, 5, 18, 20, 27, 48, 111000, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='horario',
            name='horario_fin',
            field=models.TimeField(default=datetime.datetime(2016, 5, 18, 20, 27, 48, 114000, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='horario',
            name='horario_inicio',
            field=models.TimeField(default=datetime.datetime(2016, 5, 18, 20, 27, 48, 113000, tzinfo=utc)),
        ),
    ]
