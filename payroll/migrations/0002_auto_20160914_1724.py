# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('payroll', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payroll',
            name='customer',
            field=models.ForeignKey(verbose_name='Customer', to='crm.Customer'),
        ),
        migrations.AlterField(
            model_name='payroll',
            name='employee',
            field=models.ForeignKey(verbose_name='Employee Name', to='hrm.Employee'),
        ),
        migrations.AlterField(
            model_name='payroll',
            name='period',
            field=models.ForeignKey(verbose_name='Payrolling Period', to='payroll.PayrollPeriod'),
        ),
    ]
