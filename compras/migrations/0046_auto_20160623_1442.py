# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('compras', '0045_auto_20160623_1421'),
    ]

    operations = [
        migrations.CreateModel(
            name='ModelA',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('field1', models.CharField(max_length=10)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AlterField(
            model_name='lineacreditoproveedor',
            name='fecha_linea_credito_proveedor',
            field=models.DateTimeField(default=datetime.datetime(2016, 6, 23, 18, 42, 25, 620000, tzinfo=utc), help_text=b'Ingrese la fecha en la que se registra la Linea de Credito ofrecida por el Proveedor.', verbose_name=b'Fecha de registro'),
        ),
        migrations.AlterField(
            model_name='ordencompra',
            name='fecha_entrega_orden_compra',
            field=models.DateTimeField(default=datetime.datetime(2016, 6, 24, 18, 42, 25, 623000, tzinfo=utc), help_text=b'Indique la fecha y hora en la que el proveedor debe entregar la Orden de Compra.', verbose_name=b'Fecha de Entrega'),
        ),
        migrations.AlterField(
            model_name='ordencompra',
            name='fecha_orden_compra',
            field=models.DateTimeField(default=datetime.datetime(2016, 6, 23, 18, 42, 25, 623000, tzinfo=utc), help_text=b'La fecha y hora de la Orden de Compra se asignan al momento de guardar los datos del pedido. No se requiere el ingreso de este dato.', verbose_name=b'Fecha de la Orden de Compra'),
        ),
        migrations.AlterField(
            model_name='proveedor',
            name='fecha_alta_proveedor',
            field=models.DateTimeField(default=datetime.datetime(2016, 6, 23, 18, 42, 25, 619000, tzinfo=utc), help_text=b'La Fecha de Alta se asigna al momento de guardar los datos del Proveedor. No se requiere el ingreso de este dato.', verbose_name=b'Fecha de Alta'),
        ),
        migrations.CreateModel(
            name='ModelB',
            fields=[
                ('modela_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='compras.ModelA')),
                ('field2', models.CharField(max_length=10)),
            ],
            options={
                'abstract': False,
            },
            bases=('compras.modela',),
        ),
        migrations.AddField(
            model_name='modela',
            name='polymorphic_ctype',
            field=models.ForeignKey(related_name='polymorphic_compras.modela_set+', editable=False, to='contenttypes.ContentType', null=True),
        ),
        migrations.CreateModel(
            name='ModelC',
            fields=[
                ('modelb_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='compras.ModelB')),
                ('field3', models.CharField(max_length=10)),
            ],
            options={
                'abstract': False,
            },
            bases=('compras.modelb',),
        ),
    ]
