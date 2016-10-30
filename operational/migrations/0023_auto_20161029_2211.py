# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('operational', '0022_auto_20161029_1701'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendance',
            name='period',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, verbose_name=b'Period', to='operational.PayrollPeriod'),
        ),
        migrations.AlterField(
            model_name='payroll',
            name='contract',
            field=models.ForeignKey(verbose_name=b'Employee Contract', to='hrm.EmployeeContract'),
        ),
        migrations.AlterField(
            model_name='payroll',
            name='period',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, verbose_name=b'Period', to='operational.PayrollPeriod'),
        ),
        migrations.AlterField(
            model_name='payroll',
            name='staff',
            field=models.ForeignKey(verbose_name=b'User Staff', blank=True, to=settings.AUTH_USER_MODEL, null=True),
        ),
        migrations.AlterField(
            model_name='visitcustomer',
            name='employee',
            field=models.ManyToManyField(help_text='Personnels in \t\t\t\t\t\t\t\t\t\t\t\t\t\t\t  the field when these visits', to='hrm.Employee', verbose_name='Personnels at Location'),
        ),
        migrations.AlterField(
            model_name='visitcustomer',
            name='sales_order_reference',
            field=models.ForeignKey(verbose_name='Sales Order', to='crm.SalesOrder', help_text='Sales Order number for referencing to customer'),
        ),
    ]
