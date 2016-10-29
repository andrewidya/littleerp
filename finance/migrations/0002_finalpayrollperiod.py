# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('operational', '0022_auto_20161029_1701'),
        ('finance', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FinalPayrollPeriod',
            fields=[
            ],
            options={
                'verbose_name': 'Payroll Period',
                'proxy': True,
                'verbose_name_plural': 'Payroll Period',
            },
            bases=('operational.payrollperiod',),
        ),
    ]
