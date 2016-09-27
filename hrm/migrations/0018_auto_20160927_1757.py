# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hrm', '0017_auto_20160927_1637'),
    ]

    operations = [
        migrations.AlterField(
            model_name='othersalary',
            name='employee_contract',
            field=models.ForeignKey(related_name='other_salary', verbose_name='Employee Contract', to='hrm.EmployeeContract'),
        ),
    ]
