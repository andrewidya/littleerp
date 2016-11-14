# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='salesorder',
            name='number',
            field=models.IntegerField(verbose_name='SO Number'),
        ),
        migrations.AlterField(
            model_name='salesorderdetail',
            name='basic_salary',
            field=models.DecimalField(null=True, verbose_name='Base Salary', max_digits=12, decimal_places=2, blank=True),
        ),
    ]
