# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bar', '0004_tipodeposito_tipoproducto'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cotizacion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fecha_cotizacion', models.DateTimeField(help_text=b'Registra la fecha en la que se definio la cotizacion. Corresponde a la fecha y hora actual', auto_now=True)),
                ('cotizacion', models.DecimalField(help_text=b'Ingrese cotizacion.', max_digits=20, decimal_places=2)),
            ],
        ),
        migrations.CreateModel(
            name='Moneda',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('codigo_moneda', models.IntegerField(help_text=b'Corresponde al codigo internacional de la moneda. Ej: Gs - 6900')),
                ('moneda', models.CharField(help_text=b'Nombre de la moneda.', max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='cotizacion',
            name='moneda',
            field=models.ForeignKey(help_text=b'Seleccione la moneda para la cual definir su cotizacion.', to='bar.Moneda'),
        ),
    ]
