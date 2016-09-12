# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
import django.core.validators
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('compras', '0174_auto_20160831_1242'),
    ]

    operations = [
        migrations.AlterField(
            model_name='empresa',
            name='logo_empresa',
            field=models.ImageField(help_text=b'Seleccione el archivo con el logo de la Empresa.', upload_to=b'compras/empresa/', verbose_name=b'Archivo de Logo'),
        ),
        migrations.AlterField(
            model_name='lineacreditoproveedor',
            name='estado_linea_credito_proveedor',
            field=models.CharField(help_text=b'Se asigna automaticamente de acuerdo a la utilizacion de la Linea de Credito.', max_length=3, verbose_name=b'Estado Linea de Credito', choices=[(b'DEL', b'Dentro de la Linea de Credito'), (b'SOB', b'Sobregirada')]),
        ),
        migrations.AlterField(
            model_name='ordencompra',
            name='fecha_entrega_orden_compra',
            field=models.DateTimeField(default=datetime.datetime(2016, 9, 5, 20, 47, 11, 192000, tzinfo=utc), help_text=b'Indique la fecha y hora en la que el proveedor debe entregar la Orden de Compra.', verbose_name=b'Fecha/hora de Entrega'),
        ),
        migrations.AlterField(
            model_name='proveedor',
            name='ruc',
            field=models.CharField(help_text=b'Ingrese el RUC del Proveedor.', unique=True, max_length=10, verbose_name=b'RUC', validators=[django.core.validators.RegexValidator(b'^[0-9]*$', b'Solo se permiten caracteres numericos.')]),
        ),
    ]
