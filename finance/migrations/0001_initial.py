# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('operational', '0020_auto_20161019_0039'),
    ]

    operations = [
        migrations.CreateModel(
            name='PaidPayroll',
            fields=[
            ],
            options={
                'verbose_name': 'Payroll Payments History',
                'proxy': True,
                'verbose_name_plural': 'Payroll Payments History',
            },
            bases=('operational.payroll',),
        ),
    ]
