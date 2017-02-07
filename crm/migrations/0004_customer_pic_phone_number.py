# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0003_auto_20170207_1125'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='pic_phone_number',
            field=models.CharField(max_length=15, null=True, verbose_name='PIC Phone Number', blank=True),
        ),
    ]
