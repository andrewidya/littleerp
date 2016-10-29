# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hrm', '0028_auto_20161013_2149'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employeecontract',
            name='employee',
            field=models.ForeignKey(related_name='contract', verbose_name='Employee', to='hrm.Employee'),
        ),
        migrations.AlterField(
            model_name='employeecontract',
            name='service_related',
            field=models.ForeignKey(related_name='service_order', verbose_name='Customer Demand Related', to='crm.SalesOrderDetail', help_text='This info related to the service needed by customer as detail of                                                     sales order'),
        ),
        migrations.AlterField(
            model_name='salaryname',
            name='calculate_condition',
            field=models.CharField(help_text='Condition needed for calculate total salary', max_length=1, verbose_name='Calculating Condition', choices=[(b'+', b'Adding Total Salary'), (b'-', b'Decreasing Total Salary')]),
        ),
    ]
