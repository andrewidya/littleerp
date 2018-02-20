# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0004_customer_pic_phone_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='pic_phone_number',
            field=models.CharField(max_length=15, null=True, verbose_name='Phone Number', blank=True),
        ),
        migrations.AlterField(
            model_name='salesorder',
            name='contract',
            field=models.CharField(max_length=255, verbose_name='Contract Ref (PKS)', blank=True),
        ),
    ]
