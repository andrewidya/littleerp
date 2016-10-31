# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('operational', '0030_auto_20161101_0016'),
    ]

    operations = [
        migrations.AddField(
            model_name='payroll',
            name='base_salary_per_day',
            field=models.DecimalField(null=True, verbose_name=b'Salary/Day', max_digits=12, decimal_places=2, blank=True),
        ),
        migrations.AddField(
            model_name='payroll',
            name='normal_overtime',
            field=models.DecimalField(null=True, verbose_name=b'LN', max_digits=12, decimal_places=2, blank=True),
        ),
    ]
