# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('operational', '0015_auto_20161013_2137'),
    ]

    operations = [
        migrations.AddField(
            model_name='payroll',
            name='back_pay',
            field=models.DecimalField(null=True, verbose_name=b'Back Pay', max_digits=12, decimal_places=2, blank=True),
        ),
        migrations.AlterField(
            model_name='payroll',
            name='overtime',
            field=models.DecimalField(null=True, verbose_name=b'Overtime/Hrs', max_digits=12, decimal_places=2, blank=True),
        ),
    ]
