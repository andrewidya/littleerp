# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('operational', '0023_auto_20161029_2211'),
    ]

    operations = [
        migrations.AddField(
            model_name='payroll',
            name='total',
            field=models.DecimalField(null=True, verbose_name=b'Total', max_digits=12, decimal_places=2, blank=True),
        ),
    ]
