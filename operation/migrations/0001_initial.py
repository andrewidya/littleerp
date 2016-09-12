# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hrm', '0012_auto_20160911_1457'),
        ('crm', '0012_auto_20160912_0509'),
    ]

    operations = [
        migrations.CreateModel(
            name='Training',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateField()),
                ('subject', models.CharField(max_length=75, verbose_name='Training Subject')),
                ('author', models.CharField(max_length=50, verbose_name='Trainer', blank=True)),
                ('is_certificate', models.BooleanField()),
                ('report', models.TextField(blank=True)),
                ('branch', models.ForeignKey(to='crm.Branch')),
                ('customer', models.ForeignKey(to='crm.Customer')),
                ('employee', models.ForeignKey(verbose_name='Attendance Person', to='hrm.Employee')),
            ],
            options={
                'verbose_name': 'Training',
            },
        ),
        migrations.CreateModel(
            name='TrainingType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50, verbose_name='Training Name')),
                ('description', models.TextField(blank=True)),
            ],
        ),
    ]
