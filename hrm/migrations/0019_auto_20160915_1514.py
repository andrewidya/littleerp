# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hrm', '0018_auto_20160914_1524'),
    ]

    operations = [
        migrations.AlterField(
            model_name='salaryinformation',
            name='employee',
            field=models.ForeignKey(to='hrm.Employee'),
        ),
        migrations.AlterField(
            model_name='salaryinformation',
            name='salary_item',
            field=models.ForeignKey(to='hrm.SalaryItem'),
        ),
        migrations.AlterUniqueTogether(
            name='salaryinformation',
            unique_together=set([('salary_item', 'employee')]),
        ),
    ]
