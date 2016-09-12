# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hrm', '0009_auto_20160911_1416'),
    ]

    operations = [
        migrations.CreateModel(
            name='Evaluation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('value', models.CharField(max_length=3, verbose_name='Value')),
                ('employee', models.ForeignKey(to='hrm.Employee')),
            ],
        ),
        migrations.CreateModel(
            name='EvaluationItem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50, verbose_name='Name')),
                ('description', models.TextField()),
                ('evaluation', models.ManyToManyField(to='hrm.Employee', through='hrm.Evaluation')),
            ],
        ),
        migrations.CreateModel(
            name='EvaluationPeriod',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('evaluation_date', models.DateField()),
                ('period', models.CharField(max_length=50, null=True, blank=True)),
            ],
            options={
                'verbose_name': 'Evaluation Period',
            },
        ),
        migrations.AddField(
            model_name='evaluation',
            name='item',
            field=models.ForeignKey(related_name='evaluated_item', to='hrm.EvaluationItem'),
        ),
    ]
