# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('compras', '0095_auto_20160731_1844'),
        ('bar', '0177_auto_20160731_1130'),
    ]

    operations = [
        migrations.CreateModel(
            name='Empresa',
            fields=[
                ('proveedor_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='compras.Proveedor')),
                ('logo_empresa', models.ImageField(default=1, help_text=b'Seleccione el archivo con el logo de la Empresa.', verbose_name=b'Archivo de Logo', upload_to=b'compras/empresa/')),
                ('fecha_apertura', models.DateTimeField()),
            ],
            options={
                'verbose_name': 'Empresa',
                'verbose_name_plural': 'Empresas',
            },
            bases=('compras.proveedor',),
        ),
        migrations.AlterField(
            model_name='cotizacion',
            name='fecha_cotizacion',
            field=models.DateTimeField(default=datetime.datetime(2016, 7, 31, 22, 44, 25, 549000, tzinfo=utc), help_text=b'Registra la fecha y hora en la que se definio la Cotizacion. Corresponde a la fecha y hora actual.', verbose_name=b'Fecha de Cotizacion'),
        ),
        migrations.AddField(
            model_name='timbrado',
            name='empresa',
            field=models.ForeignKey(default=1, to='bar.Empresa'),
        ),
    ]
