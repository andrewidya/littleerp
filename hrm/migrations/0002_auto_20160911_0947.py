# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hrm', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='division',
            options={'verbose_name': 'Division', 'verbose_name_plural': 'Divisions'},
        ),
        migrations.AlterModelOptions(
            name='employee',
            options={'verbose_name': 'Employee', 'verbose_name_plural': 'Employee Lists'},
        ),
        migrations.AlterModelOptions(
            name='jobtitle',
            options={'verbose_name': 'Job Title', 'verbose_name_plural': 'Job Titles'},
        ),
        migrations.AlterModelOptions(
            name='maritalstatus',
            options={'verbose_name': 'Marital Status', 'verbose_name_plural': 'Marital Statuses'},
        ),
        migrations.AddField(
            model_name='maritalstatus',
            name='description',
            field=models.CharField(default='', max_length=255, verbose_name='Description'),
            preserve_default=False,
        ),
    ]
