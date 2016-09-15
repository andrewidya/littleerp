# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hrm', '0013_leaverecord'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='birth_date',
            field=models.DateField(verbose_name='Birth Date'),
        ),
        migrations.AlterField(
            model_name='maritalstatus',
            name='description',
            field=models.CharField(max_length=255, verbose_name='Description', blank=True),
        ),
    ]
