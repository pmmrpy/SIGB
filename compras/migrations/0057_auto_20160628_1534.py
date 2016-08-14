# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('bar', '0140_auto_20160628_1534'),
        ('compras', '0056_auto_20160628_1456'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProveedorTelefono',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('telefono', models.IntegerField(help_text=b'Ingrese el telefono fijo o movil del proveedor. El dato debe contener solo numeros.')),
                ('interno', models.IntegerField(help_text=b'Ingrese el numero de interno.', null=True, blank=True)),
                ('contacto', models.CharField(help_text=b'Nombre de la persona a la cual contactar en este numero. (Hasta 100 caracteres)', max_length=100, null=True, blank=True)),
                ('codigo_operadora_telefono', models.ForeignKey(default=21, to='bar.CodigoOperadoraTelefono', help_text=b'Seleccione o ingrese el codigo de ciudad u operadora de telefonia movil.')),
                ('codigo_pais_telefono', models.ForeignKey(default=595, to='bar.CodigoPaisTelefono')),
            ],
            options={
                'verbose_name': 'Proveedor - Telefono',
                'verbose_name_plural': 'Proveedores - Telefonos',
            },
        ),
        migrations.RemoveField(
            model_name='telefonoproveedor',
            name='codigo_operadora_telefono',
        ),
        migrations.RemoveField(
            model_name='telefonoproveedor',
            name='codigo_pais_telefono',
        ),
        migrations.RemoveField(
            model_name='telefonoproveedor',
            name='proveedor',
        ),
        migrations.AlterField(
            model_name='compra',
            name='fecha_compra',
            field=models.DateTimeField(default=datetime.datetime(2016, 6, 28, 19, 34, 55, 319000, tzinfo=utc), help_text=b'La fecha y hora se asignan al momento de guardar los datos de la Compra. No se requiere el ingreso de este dato.', verbose_name=b'Fecha y hora de la Compra'),
        ),
        migrations.AlterField(
            model_name='compra',
            name='fecha_factura_compra',
            field=models.DateField(default=datetime.datetime(2016, 6, 28, 19, 34, 55, 319000, tzinfo=utc), help_text=b'Ingrese la fecha de la factura.', verbose_name=b'Fecha de la Factura de la Compra'),
        ),
        migrations.AlterField(
            model_name='lineacreditoproveedor',
            name='fecha_linea_credito_proveedor',
            field=models.DateTimeField(default=datetime.datetime(2016, 6, 28, 19, 34, 55, 315000, tzinfo=utc), help_text=b'Ingrese la fecha en la que se registra la Linea de Credito ofrecida por el Proveedor.', verbose_name=b'Fecha de registro'),
        ),
        migrations.AlterField(
            model_name='ordencompra',
            name='fecha_entrega_orden_compra',
            field=models.DateTimeField(default=datetime.datetime(2016, 6, 29, 19, 34, 55, 317000, tzinfo=utc), help_text=b'Indique la fecha y hora en la que el proveedor debe entregar la Orden de Compra.', verbose_name=b'Fecha de Entrega'),
        ),
        migrations.AlterField(
            model_name='ordencompra',
            name='fecha_orden_compra',
            field=models.DateTimeField(default=datetime.datetime(2016, 6, 28, 19, 34, 55, 317000, tzinfo=utc), help_text=b'La fecha y hora de la Orden de Compra se asignan al momento de guardar los datos del pedido. No se requiere el ingreso de este dato.', verbose_name=b'Fecha de la Orden de Compra'),
        ),
        migrations.AlterField(
            model_name='proveedor',
            name='fecha_alta_proveedor',
            field=models.DateTimeField(default=datetime.datetime(2016, 6, 28, 19, 34, 55, 314000, tzinfo=utc), help_text=b'La Fecha de Alta se asigna al momento de guardar los datos del Proveedor. No se requiere el ingreso de este dato.', verbose_name=b'Fecha de Alta'),
        ),
        migrations.DeleteModel(
            name='TelefonoProveedor',
        ),
        migrations.AddField(
            model_name='proveedortelefono',
            name='proveedor',
            field=models.ForeignKey(to='compras.Proveedor'),
        ),
    ]
