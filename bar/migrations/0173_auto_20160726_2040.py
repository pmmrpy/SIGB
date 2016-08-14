# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('bar', '0172_auto_20160722_1515'),
    ]

    operations = [
        migrations.CreateModel(
            name='Facturas',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('numero_factura_inicial', models.PositiveIntegerField()),
                ('numero_factura_final', models.PositiveIntegerField()),
                ('numero_factura_actual', models.PositiveIntegerField()),
                ('caja', models.OneToOneField(to='bar.Caja')),
            ],
        ),
        migrations.CreateModel(
            name='Timbrado',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('descripcion_timbrado', models.CharField(help_text=b'Ingrese la descripcion del Timbrado. (Hasta 200 caracteres)', max_length=200, verbose_name=b'Descripcion del Timbrado')),
                ('fecha_inicio_timbrado', models.DateTimeField()),
                ('fecha_fin_timbrado', models.DateTimeField()),
                ('estado_timbrado', models.CharField(help_text=b'Seleccione el Estado del Timbrado (Solo un Timbrado puede tener el estado ACTIVO.)', max_length=2, verbose_name=b'Estado del Timbrado', choices=[(b'AC', b'Activo'), (b'IN', b'Inactivo')])),
            ],
        ),
        migrations.AlterField(
            model_name='cotizacion',
            name='fecha_cotizacion',
            field=models.DateTimeField(default=datetime.datetime(2016, 7, 27, 0, 39, 58, 133000, tzinfo=utc), help_text=b'Registra la fecha y hora en la que se definio la Cotizacion. Corresponde a la fecha y hora actual.', verbose_name=b'Fecha de Cotizacion'),
        ),
    ]
