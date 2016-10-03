# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('personal', '0272_auto_20160827_2010'),
        ('compras', '0194_auto_20160923_2121'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ordencompra',
            old_name='motivo_anulacion',
            new_name='motivo_cancelacion',
        ),
        migrations.RenameField(
            model_name='ordencompra',
            old_name='observaciones_anulacion',
            new_name='observaciones_cancelacion',
        ),
        migrations.AddField(
            model_name='compra',
            name='fecha_hora_cancelacion',
            field=models.DateTimeField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='compra',
            name='motivo_cancelacion',
            field=models.CharField(max_length=50, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='compra',
            name='observaciones_cancelacion',
            field=models.CharField(max_length=200, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='compra',
            name='usuario_cancelacion',
            field=models.ForeignKey(related_name='usuario_cancelacion_compra', blank=True, to='personal.Empleado', help_text=b'Usuario que cancelo la Compra.', null=True, verbose_name=b'Cancelado por?'),
        ),
        migrations.AddField(
            model_name='lineacreditoproveedordetalle',
            name='anulado',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='lineacreditoproveedordetalle',
            name='fecha_hora_anulacion',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='ordencompra',
            name='fecha_hora_cancelacion',
            field=models.DateTimeField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='ordencompra',
            name='usuario_cancelacion',
            field=models.ForeignKey(related_name='usuario_cancelacion_orden_compra', blank=True, to='personal.Empleado', help_text=b'Usuario que cancelo la Orden de Compra.', null=True, verbose_name=b'Cancelado por?'),
        ),
        migrations.AddField(
            model_name='ordenpago',
            name='fecha_hora_anulacion',
            field=models.DateTimeField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='ordenpago',
            name='motivo_anulacion',
            field=models.CharField(max_length=50, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='ordenpago',
            name='observaciones_anulacion',
            field=models.CharField(max_length=200, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='ordenpago',
            name='usuario_anulacion',
            field=models.ForeignKey(related_name='usuario_anulacion_orden_pago', blank=True, to='personal.Empleado', help_text=b'Usuario que anulo la Orden de Pago.', null=True, verbose_name=b'Anulado por?'),
        ),
        migrations.AddField(
            model_name='pagoproveedor',
            name='anulado',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='pagoproveedor',
            name='fecha_hora_anulacion',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='ordencompra',
            name='fecha_entrega_orden_compra',
            field=models.DateTimeField(default=datetime.datetime(2016, 9, 25, 19, 46, 19, 917000, tzinfo=utc), help_text=b'Indique la fecha y hora en la que el proveedor debe entregar la Orden de Compra.', verbose_name=b'Fecha/hora de Entrega'),
        ),
        migrations.AlterField(
            model_name='ordenpago',
            name='estado_orden_pago',
            field=models.CharField(blank=True, help_text=b'Se asigna automaticamente de acuerdo a la accion que se realicecon la Orden de Pago.', max_length=3, verbose_name=b'Estado Orden de Pago', choices=[(b'PEN', b'Pendiente'), (b'CON', b'Confirmada'), (b'ANU', b'Anulada'), (b'CAN', b'Cancelada')]),
        ),
    ]
