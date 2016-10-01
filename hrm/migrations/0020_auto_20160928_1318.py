# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hrm', '0019_auto_20160927_1833'),
    ]

    operations = [
        migrations.AlterField(
            model_name='evaluation',
            name='date_created',
            field=models.DateField(verbose_name='Date Created'),
        ),
        migrations.AlterField(
            model_name='evaluation',
            name='employee',
            field=models.ForeignKey(verbose_name='Employee Name', to='hrm.Employee'),
        ),
        migrations.AlterField(
            model_name='evaluation',
            name='eval_period',
            field=models.ForeignKey(verbose_name='Period', to='hrm.EvaluationPeriod'),
        ),
        migrations.AlterField(
            model_name='evaluationdetail',
            name='eval_item',
            field=models.ForeignKey(verbose_name='Point Item', to='hrm.EvaluationItem'),
        ),
    ]
