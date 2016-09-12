# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hrm', '0008_auto_20160911_1415'),
    ]

    operations = [
        migrations.AlterField(
            model_name='education',
            name='name',
            field=models.CharField(max_length=50, verbose_name='Institution Name'),
        ),
    ]
