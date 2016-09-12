# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0002_customer_phone_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='branch',
            name='phone_number',
            field=models.CharField(max_length=15, null=True, verbose_name='Phone Number', blank=True),
        ),
        migrations.AlterField(
            model_name='branch',
            name='address',
            field=models.CharField(max_length=100, verbose_name='Address', blank=True),
        ),
        migrations.AlterField(
            model_name='branch',
            name='city',
            field=models.CharField(max_length=50, verbose_name='City', blank=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='address',
            field=models.CharField(max_length=100, verbose_name='Address', blank=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='city',
            field=models.CharField(max_length=50, verbose_name='City', blank=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='tax_id_number',
            field=models.CharField(max_length=30, verbose_name='NPWP', blank=True),
        ),
    ]
