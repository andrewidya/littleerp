# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('operational', '0020_auto_20161019_0039'),
    ]

    operations = [
        migrations.CreateModel(
            name='FinalPayrollDetail',
            fields=[
            ],
            options={
                'verbose_name': 'Finalized Payroll Detail',
                'proxy': True,
                'verbose_name_plural': 'Finalized Payroll Detail',
            },
            bases=('operational.payrolldetail',),
        ),
    ]
