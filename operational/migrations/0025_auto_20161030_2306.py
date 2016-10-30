# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hrm', '0029_auto_20161028_2331'),
        ('operational', '0024_payroll_total'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255, verbose_name=b'Name')),
            ],
            options={
                'verbose_name': 'Course',
                'verbose_name_plural': 'Courses',
            },
        ),
        migrations.CreateModel(
            name='CourseType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255, verbose_name=b'Name')),
            ],
            options={
                'verbose_name': 'Courses Type',
                'verbose_name_plural': 'Courses Type',
            },
        ),
        migrations.CreateModel(
            name='TrainingClass',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('employee', models.ForeignKey(verbose_name=b'Employee', to='hrm.Employee')),
            ],
            options={
                'verbose_name': 'Training Class',
                'verbose_name_plural': 'Training Classes',
            },
        ),
        migrations.CreateModel(
            name='TrainingSchedule',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateField(verbose_name=b'Date')),
                ('has_certificate', models.BooleanField(default=True, verbose_name=b'Certificate')),
                ('presenter', models.CharField(max_length=45, verbose_name=b'Presenter')),
                ('course', models.ForeignKey(verbose_name=b'Courses', to='operational.Course')),
            ],
            options={
                'verbose_name': 'Training Schedule',
                'verbose_name_plural': 'Training Schedule',
            },
        ),
        migrations.AddField(
            model_name='trainingclass',
            name='schedule',
            field=models.ForeignKey(verbose_name=b'Schedule', to='operational.TrainingSchedule'),
        ),
        migrations.AddField(
            model_name='course',
            name='course_type',
            field=models.ForeignKey(verbose_name=b'Course Type', to='operational.CourseType'),
        ),
    ]
