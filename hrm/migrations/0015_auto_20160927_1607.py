# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hrm', '0014_auto_20160927_1503'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bankname',
            options={'verbose_name': 'Bank', 'verbose_name_plural': 'Bank Name Lists'},
        ),
        migrations.AlterField(
            model_name='employee',
            name='division',
            field=models.ForeignKey(verbose_name='Division', blank=True, to='hrm.Division', null=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='job_title',
            field=models.ForeignKey(verbose_name='Job Tittle', blank=True, to='hrm.JobTitle', null=True),
        ),
    ]
