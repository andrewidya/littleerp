# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hrm', '0005_auto_20160924_1404'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employeecontract',
            name='calculate_condition',
        ),
        migrations.AddField(
            model_name='salaryname',
            name='calculate_condition',
            field=models.CharField(default='', help_text='Condition needed for calculate total salary', max_length=1, verbose_name='Calculating Condition', choices=[(b'+', b'Adding Total Salary'), (b'-', b'Decreasing Total Salary')]),
            preserve_default=False,
        ),
    ]
