# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Proveedor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('proveedor', models.CharField(help_text=b'Ingrese la Razon Social o el Nombre del Proveedor. (Hasta 100 caracteres)', max_length=100, verbose_name=b'Razon Social o Nombre')),
                ('ruc', models.CharField(help_text=b'Ingrese el RUC del Proveedor.', unique=True, max_length=15, verbose_name=b'RUC')),
                ('digito_verificador', models.IntegerField(default=1, help_text=b'Ingrese el digito verificador del RUC del Proveedor.')),
                ('direccion', models.CharField(help_text=b'Ingrese la Direccion del Proveedor. (Hasta 200 caracteres)', max_length=200, null=True)),
                ('pagina_web', models.URLField(null=True, blank=True)),
                ('fecha_alta_proveedor', models.DateTimeField(default=datetime.datetime(2016, 6, 1, 15, 26, 40, 809000, tzinfo=utc), help_text=b'La Fecha de Alta se asigna al momento de guardar los datos del Proveedor. No se requiere el ingreso de este dato.', verbose_name=b'Fecha de Alta')),
            ],
            options={
                'verbose_name': 'Proveedor',
                'verbose_name_plural': 'Proveedores',
            },
        ),
    ]
