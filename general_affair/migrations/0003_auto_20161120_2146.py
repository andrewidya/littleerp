# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('general_affair', '0002_auto_20161120_2138'),
    ]

    operations = [
        migrations.AddField(
            model_name='supplier',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='supplier',
            name='end_date',
            field=models.DateField(null=True, verbose_name='End Date', blank=True),
        ),
        migrations.AddField(
            model_name='supplier',
            name='join_date',
            field=models.DateField(null=True, verbose_name='Join Date', blank=True),
        ),
        migrations.AddField(
            model_name='supplier',
            name='owner',
            field=models.CharField(max_length=50, verbose_name='Owner', blank=True),
        ),
        migrations.AddField(
            model_name='supplier',
            name='owner_id_number',
            field=models.CharField(max_length=15, null=True, verbose_name='ID Number', blank=True),
        ),
        migrations.AddField(
            model_name='supplier',
            name='siup_number',
            field=models.CharField(max_length=30, verbose_name='SIUP', blank=True),
        ),
        migrations.AddField(
            model_name='supplier',
            name='start_date',
            field=models.DateField(null=True, verbose_name='Start Date', blank=True),
        ),
        migrations.AddField(
            model_name='supplier',
            name='tax_id_number',
            field=models.CharField(max_length=30, verbose_name='NPWP', blank=True),
        ),
        migrations.AddField(
            model_name='supplier',
            name='tdp_number',
            field=models.CharField(max_length=30, verbose_name='TDP', blank=True),
        ),
    ]
