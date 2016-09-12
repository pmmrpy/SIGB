# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('personal', '0266_auto_20160823_1510'),
    ]

    operations = [
        migrations.AlterField(
            model_name='empleadodocumento',
            name='numero_documento',
            field=models.CharField(help_text=b'Ingrese el documento del Empleado. El dato puede contener numeros y letras dependiendo de la nacionalidad y tipo de documento.', max_length=50, verbose_name=b'Numero de Documento'),
        ),
        migrations.AlterField(
            model_name='empleadodocumento',
            name='tipo_documento',
            field=models.ForeignKey(verbose_name=b'Tipo de Documento', to='bar.Documento', help_text=b'Seleccione el Tipo de Documento para el Empleado.'),
        ),
        migrations.AlterField(
            model_name='horario',
            name='horario_fin',
            field=models.TimeField(default=datetime.datetime(2016, 8, 23, 19, 20, 5, 994000, tzinfo=utc), help_text=b'Ingrese la hora de finalizacion de la jornada de trabajo.', verbose_name=b'Hora de Finalizacion Jornada'),
        ),
        migrations.AlterField(
            model_name='horario',
            name='horario_inicio',
            field=models.TimeField(default=datetime.datetime(2016, 8, 23, 19, 20, 5, 994000, tzinfo=utc), help_text=b'Ingrese la hora de inicio de la jornada de trabajo.', verbose_name=b'Hora de Inicio Jornada'),
        ),
    ]
