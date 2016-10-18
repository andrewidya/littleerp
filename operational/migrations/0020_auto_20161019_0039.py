# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('operational', '0019_auto_20161016_2339'),
    ]

    operations = [
        migrations.DeleteModel(
            name='PostProcessedPayroll',
        ),
        migrations.CreateModel(
            name='FinalPayroll',
            fields=[
            ],
            options={
                'verbose_name': 'Finalized Payroll',
                'proxy': True,
                'verbose_name_plural': 'Finalized Payroll',
            },
            bases=('operational.payroll',),
        ),
    ]
