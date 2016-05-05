# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('personal', '0003_auto_20150928_1746'),
    ]

    operations = [
        migrations.AlterField(
            model_name='empleado',
            name='documentos',
            field=models.ManyToManyField(to='bar.Documento', through='personal.EmpleadoDocumento'),
        ),
        migrations.AlterField(
            model_name='empleado',
            name='fecha_nacimiento',
            field=models.DateField(default=datetime.datetime(2015, 9, 28, 23, 0, 58, 127000, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='empleadodocumento',
            name='tipo_documento',
            field=models.ForeignKey(default=b'CI', to='bar.Documento'),
        ),
        migrations.AlterField(
            model_name='horario',
            name='horario_fin',
            field=models.TimeField(default=datetime.datetime(2015, 9, 28, 23, 0, 58, 129000, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='horario',
            name='horario_inicio',
            field=models.TimeField(default=datetime.datetime(2015, 9, 28, 23, 0, 58, 129000, tzinfo=utc)),
        ),
    ]
