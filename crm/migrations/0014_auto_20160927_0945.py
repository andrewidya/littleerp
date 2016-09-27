# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0013_auto_20160926_1437'),
    ]

    operations = [
        migrations.CreateModel(
            name='Satisfication',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('create_date', models.DateField(verbose_name='Date Created')),
                ('name', models.CharField(max_length=255, verbose_name='Subject')),
                ('respondent', models.CharField(max_length=50, verbose_name='Person Interviewed', blank=True)),
                ('sales_order', models.ForeignKey(verbose_name='Related Sales Order', to='crm.SalesOrder')),
            ],
            options={
                'verbose_name': 'Satisfication Interview',
                'verbose_name_plural': 'Satisfication Interview',
            },
        ),
        migrations.CreateModel(
            name='SatisficationDetail',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('value', models.CharField(max_length=255, verbose_name='Value')),
            ],
            options={
                'verbose_name': 'Satisfication Interview Detail',
                'verbose_name_plural': 'Satisfication Interview Details',
            },
        ),
        migrations.CreateModel(
            name='SatisficationPointRateItem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(help_text='Point rate question for polling', max_length=255, verbose_name='Satisfication Point Rate')),
                ('description', models.CharField(max_length=255, verbose_name='Description', blank=True)),
            ],
            options={
                'verbose_name': 'Satisfication Point Rate Item',
                'verbose_name_plural': 'Satisfication Point Rate Item',
            },
        ),
        migrations.AddField(
            model_name='satisficationdetail',
            name='point_rate_item',
            field=models.ForeignKey(verbose_name='Point Rate Item', to='crm.SatisficationPointRateItem'),
        ),
        migrations.AddField(
            model_name='satisficationdetail',
            name='satisfication',
            field=models.ForeignKey(verbose_name='Satisfication Subject', to='crm.Satisfication'),
        ),
    ]
