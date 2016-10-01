# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hrm', '0018_auto_20160927_1757'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='employeecontract',
            options={'verbose_name': 'Contract', 'verbose_name_plural': 'Contracts List'},
        ),
        migrations.AlterField(
            model_name='salaryname',
            name='salary_category',
            field=models.ForeignKey(related_name='salary_category', on_delete=django.db.models.deletion.PROTECT, to='hrm.SalaryCategory'),
        ),
    ]
