# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hrm', '0002_auto_20161128_0036'),
        ('general_affair', '0002_auto_20161208_2154'),
    ]

    operations = [
        migrations.CreateModel(
            name='IDCard',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date_created', models.DateField(verbose_name='Date Created')),
                ('date_expired', models.DateField(verbose_name='Expired')),
                ('status', models.BooleanField(default=False, verbose_name='Is Active')),
                ('employee', models.ForeignKey(verbose_name='Employee', to='hrm.Employee')),
            ],
            options={
                'verbose_name': 'ID Card',
                'verbose_name_plural': 'ID Cards',
            },
        ),
        migrations.CreateModel(
            name='IDReleaseType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50, verbose_name='Name')),
            ],
            options={
                'verbose_name': 'Release Type',
                'verbose_name_plural': 'Release Types',
            },
        ),
        migrations.AddField(
            model_name='idcard',
            name='release_type',
            field=models.ForeignKey(verbose_name='Release Type', to='general_affair.IDReleaseType'),
        ),
    ]
