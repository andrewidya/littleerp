# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0014_auto_20160914_1648'),
        ('hrm', '0018_auto_20160914_1524'),
        ('payroll', '0007_auto_20160914_1744'),
    ]

    operations = [
        migrations.AddField(
            model_name='payroll',
            name='customer',
            field=models.ForeignKey(default=1, verbose_name='Customer', to='crm.Customer'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='payroll',
            name='employee',
            field=models.ForeignKey(default=1, verbose_name='Employee Name', to='hrm.Employee'),
            preserve_default=False,
        ),
        migrations.AlterUniqueTogether(
            name='payroll',
            unique_together=set([('employee', 'customer')]),
        ),
    ]
