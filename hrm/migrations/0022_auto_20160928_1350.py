# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hrm', '0021_auto_20160928_1320'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='evaluation',
            options={'verbose_name': 'Evaluation', 'verbose_name_plural': 'Evaluation Lists'},
        ),
        migrations.AlterModelOptions(
            name='evaluationdetail',
            options={'verbose_name': 'Evaluation Detail', 'verbose_name_plural': 'Evaluation Details'},
        ),
        migrations.AlterField(
            model_name='evaluationdetail',
            name='eval_value',
            field=models.PositiveIntegerField(verbose_name='Point Value'),
        ),
        migrations.AlterUniqueTogether(
            name='othersalary',
            unique_together=set([('employee_contract', 'salary_name')]),
        ),
    ]
