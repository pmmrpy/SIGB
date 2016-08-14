# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('personal', '0222_auto_20160811_1218'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='empleado',
            name='codigo_venta',
        ),
        migrations.AddField(
            model_name='empleado',
            name='usuario',
            field=models.ForeignKey(default=1, to=settings.AUTH_USER_MODEL, help_text=b'Seleccione el usuario del Empleado.'),
        ),
        migrations.AlterField(
            model_name='empleado',
            name='email',
            field=models.EmailField(default=b'mail@ejemplo.com', help_text=b'Ingrese la direccion de correo electronico del Empleado.', max_length=254, blank=True),
        ),
        migrations.AlterField(
            model_name='empleadodocumento',
            name='numero_documento',
            field=models.CharField(help_text=b'Ingrese el documento del Empleado. El dato puede contener numeros y letras dependiendo de la nacionalidad y tipo de documento.', unique=True, max_length=50, verbose_name=b'Numero de Documento'),
        ),
        migrations.AlterField(
            model_name='empleadodocumento',
            name='tipo_documento',
            field=models.ForeignKey(help_text=b'Seleccione el Tipo de Documento para el Empleado.', to='bar.Documento'),
        ),
        migrations.AlterField(
            model_name='horario',
            name='horario',
            field=models.CharField(help_text=b'Ingrese el nombre o descripcion de la jornada laboral.', max_length=30, verbose_name=b'Horario'),
        ),
        migrations.AlterField(
            model_name='horario',
            name='horario_fin',
            field=models.TimeField(default=datetime.datetime(2016, 8, 13, 0, 39, 22, 230000, tzinfo=utc), help_text=b'Ingrese la hora de finalizacion de la jornada de trabajo.', verbose_name=b'Hora de Finalizacion Jornada'),
        ),
        migrations.AlterField(
            model_name='horario',
            name='horario_inicio',
            field=models.TimeField(default=datetime.datetime(2016, 8, 13, 0, 39, 22, 229000, tzinfo=utc), help_text=b'Ingrese la hora de inicio de la jornada de trabajo.', verbose_name=b'Hora de Inicio Jornada'),
        ),
    ]
