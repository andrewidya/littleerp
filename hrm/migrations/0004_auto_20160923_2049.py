# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hrm', '0003_auto_20160923_2041'),
    ]

    operations = [
        migrations.AlterField(
            model_name='leavetaken',
            name='day',
            field=models.SmallIntegerField(null=True, blank=True),
        ),
    ]
