# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hrm', '0016_auto_20160914_1504'),
    ]

    operations = [
        migrations.CreateModel(
            name='SalaryInformation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('value', models.DecimalField(max_digits=15, decimal_places=2)),
                ('employee', models.OneToOneField(to='hrm.Employee')),
            ],
        ),
        migrations.CreateModel(
            name='SalaryItem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=25, verbose_name='Salary Component Name')),
                ('description', models.CharField(max_length=255)),
            ],
        ),
        migrations.AddField(
            model_name='salaryinformation',
            name='salary_item',
            field=models.OneToOneField(to='hrm.SalaryItem'),
        ),
        migrations.AddField(
            model_name='employee',
            name='salary_information',
            field=models.ManyToManyField(to='hrm.SalaryItem', through='hrm.SalaryInformation'),
        ),
    ]
