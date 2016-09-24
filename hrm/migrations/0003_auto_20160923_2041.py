# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hrm', '0002_auto_20160923_2038'),
    ]

    operations = [
        migrations.AlterField(
            model_name='education',
            name='certificate',
            field=models.BooleanField(default=False),
        ),
    ]
