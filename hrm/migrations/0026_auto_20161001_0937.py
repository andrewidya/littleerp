# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hrm', '0025_auto_20161001_0612'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='annualleave',
            options={'verbose_name': 'Annual Leave', 'verbose_name_plural': 'Annual Leaves'},
        ),
        migrations.AlterModelOptions(
            name='bankname',
            options={'verbose_name': 'Bank', 'verbose_name_plural': 'Banks'},
        ),
        migrations.AlterModelOptions(
            name='employee',
            options={'verbose_name': 'Employee', 'verbose_name_plural': 'Employees', 'permissions': (('hrm_employee_view', 'Can view only'),)},
        ),
        migrations.AlterModelOptions(
            name='employeecontract',
            options={'verbose_name': 'Contract', 'verbose_name_plural': 'Contracts'},
        ),
        migrations.AlterModelOptions(
            name='evaluation',
            options={'verbose_name': 'Evaluation', 'verbose_name_plural': 'Evaluations'},
        ),
        migrations.AlterModelOptions(
            name='evaluationitem',
            options={'verbose_name': 'Evaluating Item', 'verbose_name_plural': 'Evaluating Items'},
        ),
        migrations.AlterModelOptions(
            name='leavetaken',
            options={'verbose_name': 'Leave Check List', 'verbose_name_plural': 'Leave Check Lists'},
        ),
        migrations.AlterField(
            model_name='employeecontract',
            name='contract_status',
            field=models.CharField(default=b'ACTIVE', max_length=8, blank=True),
        ),
    ]
