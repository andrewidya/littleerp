# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hrm', '0027_auto_20161011_1910'),
        ('operational', '0005_auto_20161010_2207'),
    ]

    operations = [
        migrations.CreateModel(
            name='Attendance',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('work_day', models.PositiveIntegerField(verbose_name=b'Day Work')),
                ('sick_day', models.PositiveIntegerField(verbose_name=b'Day Sick')),
                ('alpha_day', models.PositiveIntegerField(verbose_name=b'Day Alpha')),
                ('leave_day', models.PositiveIntegerField(verbose_name=b'Leave Taken')),
                ('leave_left', models.PositiveIntegerField(verbose_name=b'Leave Left')),
                ('employee', models.ForeignKey(verbose_name=b'Employee', to='hrm.Employee')),
                ('period', models.ForeignKey(verbose_name=b'Period', to='operational.PayrollPeriod')),
            ],
            options={
                'verbose_name': 'Attendance Summary',
                'verbose_name_plural': 'Attendance Summary',
            },
        ),
        migrations.AlterUniqueTogether(
            name='attendance',
            unique_together=set([('employee', 'period')]),
        ),
    ]
