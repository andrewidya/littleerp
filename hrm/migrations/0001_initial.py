# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Division',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=20, verbose_name='Division Name')),
                ('description', models.CharField(max_length=255, verbose_name='Description')),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('reg_number', models.CharField(unique=True, max_length=6, verbose_name='Registration Number')),
                ('id_number', models.CharField(max_length=15, verbose_name='ID Number')),
                ('name', models.CharField(max_length=50, verbose_name='Name')),
                ('birth_place', models.CharField(max_length=25, verbose_name='Birth Place')),
                ('birth_date', models.DateField()),
                ('gender', models.CharField(max_length=1, verbose_name='Gender', choices=[(b'P', b'Perempuan'), (b'L', b'Laki-laki')])),
                ('mother_name', models.CharField(max_length=30, verbose_name='Mother Name')),
                ('date_of_hire', models.DateField(verbose_name='Date of Hire')),
                ('account_number', models.CharField(max_length=20, verbose_name='Account Number')),
                ('phone_number', models.CharField(max_length=15, verbose_name='Phone Number')),
                ('is_active', models.BooleanField()),
                ('divison', models.ForeignKey(to='hrm.Division')),
            ],
        ),
        migrations.CreateModel(
            name='JobTitle',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=20, verbose_name='Job Title')),
                ('description', models.CharField(max_length=255, verbose_name='Description')),
            ],
        ),
        migrations.CreateModel(
            name='MaritalStatus',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('code', models.CharField(max_length=4, verbose_name='Marital Code')),
            ],
        ),
        migrations.AddField(
            model_name='employee',
            name='job_title',
            field=models.ForeignKey(to='hrm.JobTitle'),
        ),
        migrations.AddField(
            model_name='employee',
            name='marital_status',
            field=models.ForeignKey(to='hrm.MaritalStatus'),
        ),
    ]
