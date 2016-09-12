# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0012_auto_20160912_0509'),
        ('operation', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Visit',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateField()),
                ('visitor', models.CharField(max_length=20, verbose_name='Visitor')),
                ('branch', models.ForeignKey(to='crm.Branch')),
                ('customer', models.ForeignKey(to='crm.Customer')),
            ],
        ),
        migrations.CreateModel(
            name='VisitEvaluationSubject',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50, verbose_name='Evaluation Subject')),
            ],
            options={
                'verbose_name': 'Visit Evaluation Subject',
            },
        ),
        migrations.CreateModel(
            name='VisitRecord',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('report', models.TextField(verbose_name='Visit Report', blank=True)),
                ('visit', models.ForeignKey(to='operation.Visit')),
                ('visit_evaluation_subject', models.ForeignKey(to='operation.VisitEvaluationSubject')),
            ],
        ),
        migrations.AddField(
            model_name='visit',
            name='visit_record',
            field=models.ManyToManyField(to='operation.VisitEvaluationSubject', through='operation.VisitRecord'),
        ),
    ]
