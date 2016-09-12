# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hrm', '0007_auto_20160911_1405'),
    ]

    operations = [
        migrations.AlterField(
            model_name='education',
            name='address',
            field=models.CharField(max_length=100, verbose_name='Address', blank=True),
        ),
        migrations.AlterField(
            model_name='education',
            name='certificate_number',
            field=models.CharField(max_length=30, verbose_name='Certificate Number', blank=True),
        ),
        migrations.AlterField(
            model_name='education',
            name='city',
            field=models.CharField(max_length=25, verbose_name='City', blank=True),
        ),
        migrations.AlterField(
            model_name='education',
            name='description',
            field=models.CharField(max_length=255, verbose_name='Short Description', blank=True),
        ),
    ]
