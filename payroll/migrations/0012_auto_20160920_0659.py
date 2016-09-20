# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('payroll', '0011_auto_20160915_1016'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payrolldecreasedetail',
            name='customer',
            field=models.ForeignKey(related_name='customer_payroll_decrease_detail', to='crm.Customer'),
        ),
        migrations.AlterField(
            model_name='payrolldecreasedetail',
            name='employee',
            field=models.ForeignKey(related_name='employee_payroll_decrease_detail', to='hrm.Employee'),
        ),
        migrations.AlterField(
            model_name='payrolldecreasedetail',
            name='item',
            field=models.ForeignKey(related_name='payroll_decrease_items', to='payroll.PayrollDecreaseItem'),
        ),
        migrations.AlterField(
            model_name='payrollincreasedetail',
            name='item',
            field=models.ForeignKey(related_name='payroll_increase_items', to='payroll.PayrollIncreaseItem'),
        ),
    ]
