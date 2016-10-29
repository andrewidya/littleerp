# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('operational', '0022_auto_20161029_1701'),
        ('finance', '0002_finalpayrollperiod'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProcessedPayroll',
            fields=[
            ],
            options={
                'verbose_name': 'Processed Payroll',
                'proxy': True,
                'verbose_name_plural': 'Processed Payroll',
            },
            bases=('operational.payroll',),
        ),
    ]
