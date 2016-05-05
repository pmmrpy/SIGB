# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('bar', '0031_auto_20151210_1746'),
        ('personal', '0051_auto_20151210_1657'),
    ]

    operations = [
        migrations.CreateModel(
            name='EmpleadoTelefono',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('telefono', models.IntegerField(help_text=b'Ingrese el telefono fijo o movil del cliente. El dato debe contener solo numeros.')),
                ('codigo_ciudad_operadora_telefono', models.ForeignKey(default=21, to='bar.CodigoCiudadOperadoraTelefono')),
                ('codigo_pais_telefono', models.ForeignKey(default=595, to='bar.CodigoPaisTelefono')),
            ],
        ),
        migrations.RemoveField(
            model_name='empleado',
            name='telefono',
        ),
        migrations.RemoveField(
            model_name='empleado',
            name='telefono_movil',
        ),
        migrations.AddField(
            model_name='empleado',
            name='sexo',
            field=models.CharField(default=b'F', max_length=1, choices=[(b'F', b'Femenino'), (b'M', b'Masculino')]),
        ),
        migrations.AlterField(
            model_name='empleado',
            name='fecha_nacimiento',
            field=models.DateField(default=datetime.datetime(2015, 12, 10, 20, 46, 43, 529000, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='horario',
            name='horario_fin',
            field=models.TimeField(default=datetime.datetime(2015, 12, 10, 20, 46, 43, 539000, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='horario',
            name='horario_inicio',
            field=models.TimeField(default=datetime.datetime(2015, 12, 10, 20, 46, 43, 538000, tzinfo=utc)),
        ),
        migrations.AddField(
            model_name='empleadotelefono',
            name='empleado',
            field=models.ForeignKey(to='personal.Empleado'),
        ),
    ]
