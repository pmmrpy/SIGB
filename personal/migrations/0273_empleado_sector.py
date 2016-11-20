# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bar', '0321_auto_20161010_1547'),
        ('personal', '0272_auto_20160827_2010'),
    ]

    operations = [
        migrations.AddField(
            model_name='empleado',
            name='sector',
            field=models.ForeignKey(default=1, to='bar.Sector', help_text=b'Seleccione el sector en donde desempenara sus funciones el Empleado.'),
        ),
    ]
