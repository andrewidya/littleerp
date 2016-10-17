# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django_fsm


class Migration(migrations.Migration):

    dependencies = [
        ('operational', '0016_auto_20161013_2301'),
    ]

    operations = [
        migrations.AddField(
            model_name='payroll',
            name='state',
            field=django_fsm.FSMField(default=b'Draft', max_length=50),
        ),
        migrations.AlterField(
            model_name='payroll',
            name='contract',
            field=models.ForeignKey(verbose_name=b'Employee \t\t\t\t\t\t\t\tContract', to='hrm.EmployeeContract'),
        ),
        migrations.AlterField(
            model_name='payrollperiod',
            name='date_create',
            field=models.DateField(auto_now_add=True, verbose_name=b'Date Created'),
        ),
        migrations.AlterField(
            model_name='payrollperiod',
            name='end_date',
            field=models.DateField(verbose_name=b'End Date'),
        ),
        migrations.AlterField(
            model_name='payrollperiod',
            name='start_date',
            field=models.DateField(verbose_name=b'Start Date'),
        ),
    ]
