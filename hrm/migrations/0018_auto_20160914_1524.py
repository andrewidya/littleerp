# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hrm', '0017_auto_20160914_1519'),
    ]

    operations = [
        migrations.AlterField(
            model_name='salaryitem',
            name='description',
            field=models.CharField(max_length=255, blank=True),
        ),
    ]
