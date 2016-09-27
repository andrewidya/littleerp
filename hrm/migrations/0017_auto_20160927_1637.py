# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hrm', '0016_auto_20160927_1622'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='employee',
            options={'verbose_name': 'Employee', 'verbose_name_plural': 'Employee Lists', 'permissions': (('hrm_employee_view', 'Can view only'),)},
        ),
        migrations.AlterModelOptions(
            name='employeecontract',
            options={'verbose_name': 'Contract', 'verbose_name_plural': 'Employee Contracts List'},
        ),
        migrations.AlterField(
            model_name='employee',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='Active'),
        ),
    ]
