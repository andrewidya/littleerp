# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('payroll', '0010_auto_20160914_1805'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payrollincreasedetail',
            name='customer',
            field=models.ForeignKey(related_name='customer_payroll_increase_detail', to='crm.Customer'),
        ),
        migrations.AlterField(
            model_name='payrollincreasedetail',
            name='employee',
            field=models.ForeignKey(related_name='employee_payroll_increase_detail', to='hrm.Employee'),
        ),
    ]
