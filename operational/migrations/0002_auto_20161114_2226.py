# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('operational', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='payroll',
            options={'verbose_name': 'Payroll', 'verbose_name_plural': 'Payroll', 'permissions': (('audit_payroll', 'Can audit payroll'), ('pay_payroll', 'Can pay payroll'))},
        ),
    ]
