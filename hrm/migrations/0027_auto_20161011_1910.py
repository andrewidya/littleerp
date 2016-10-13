# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hrm', '0026_auto_20161001_0937'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employeecontract',
            name='service_related',
            field=models.ForeignKey(related_name='service_order', verbose_name='Customer Demand Related', to='crm.SalesOrderDetail', help_text='This info related to the \t\t\t\t\t\t\t\t\t   \t\t\t  service needed by customer \t\t\t\t\t\t\t\t\t   \t\t\t  as detail of sales order'),
        ),
        migrations.AlterField(
            model_name='salaryname',
            name='calculate_condition',
            field=models.CharField(help_text='Condition needed for \t\t\t\t\t\t\t\t\t\t  \t\t\t calculate total salary', max_length=1, verbose_name='Calculating Condition', choices=[(b'+', b'Adding Total Salary'), (b'-', b'Decreasing Total Salary')]),
        ),
    ]
