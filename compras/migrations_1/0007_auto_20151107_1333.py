# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('bar', '0009_auto_20151107_1333'),
        ('compras', '0006_auto_20151107_1121'),
    ]

    operations = [
        migrations.CreateModel(
            name='TelefonoProveedor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('telefono', models.IntegerField(help_text=b'Ingrese el telefono del proveedor. El dato debe contener solo numeros.')),
                ('codigo_ciudad_operadora_telefono', models.ForeignKey(default=21, to='bar.CodigoCiudadOperadoraTelefono')),
                ('codigo_pais_telefono', models.ForeignKey(default=595, to='bar.CodigoPaisTelefono')),
            ],
        ),
        migrations.RemoveField(
            model_name='proveedor',
            name='codigo_ciudad_operadora_telefono',
        ),
        migrations.RemoveField(
            model_name='proveedor',
            name='codigo_pais_telefono',
        ),
        migrations.RemoveField(
            model_name='proveedor',
            name='telefono',
        ),
        migrations.AddField(
            model_name='proveedor',
            name='digito_verificador',
            field=models.IntegerField(default=1, help_text=b'Ingrese del digito verificado del RUC del proveedor.'),
        ),
        migrations.AlterField(
            model_name='compra',
            name='fecha_entrega',
            field=models.DateTimeField(default=datetime.datetime(2015, 11, 7, 16, 33, 30, 158000, tzinfo=utc), help_text=b'Indique la fecha en la que el proveedor debe entregar el pedido.'),
        ),
        migrations.AlterField(
            model_name='compra',
            name='fecha_pedido',
            field=models.DateTimeField(default=datetime.datetime(2015, 11, 7, 16, 33, 30, 158000, tzinfo=utc), help_text=b'Ingrese la fecha en la que se realiza el pedido.'),
        ),
        # migrations.AlterField(
            # model_name='proveedor',
            # name='ruc',
            # field=models.IntegerField(help_text=b'RUC del proveedor.', unique=True, verbose_name=b'RUC'),
        # ),
		migrations.RemoveField(
            model_name='proveedor',
            name='ruc',
        ),
        migrations.AddField(
            model_name='telefonoproveedor',
            name='proveedor',
            field=models.ForeignKey(to='compras.Proveedor'),
        ),
    ]
