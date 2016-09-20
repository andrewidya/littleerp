# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('address_data', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Districts',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255, verbose_name='District')),
            ],
        ),
        migrations.CreateModel(
            name='Regencies',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255, verbose_name='Address')),
                ('province', models.ForeignKey(verbose_name='Province', to='address_data.Provinces')),
            ],
        ),
        migrations.CreateModel(
            name='Villages',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255, verbose_name='Village')),
                ('district', models.ForeignKey(verbose_name='District', to='address_data.Districts')),
            ],
        ),
        migrations.AddField(
            model_name='districts',
            name='regency',
            field=models.ForeignKey(verbose_name='Regency', to='address_data.Regencies'),
        ),
    ]
