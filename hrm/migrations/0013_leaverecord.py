# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0012_auto_20160912_0509'),
        ('hrm', '0012_auto_20160911_1457'),
    ]

    operations = [
        migrations.CreateModel(
            name='LeaveRecord',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date_taken', models.DateField(verbose_name='Leave Date Taken')),
                ('description', models.TextField(blank=True)),
                ('branch', models.ForeignKey(to='crm.Branch')),
                ('customer', models.ForeignKey(to='crm.Customer')),
                ('employee', models.ForeignKey(to='hrm.Employee')),
            ],
        ),
    ]
