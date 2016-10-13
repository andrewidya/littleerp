# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('operational', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PayrollPeriod',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date_create', models.DateField(auto_now_add=True)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
            ],
        ),
        migrations.AlterField(
            model_name='visitcustomer',
            name='employee',
            field=models.ManyToManyField(help_text='Personnels in the field when\t\t\t\t\t\t\t\t\t \t\t\tthese visits', to='hrm.Employee', verbose_name='Personnels at Location'),
        ),
        migrations.AlterField(
            model_name='visitcustomer',
            name='sales_order_reference',
            field=models.ForeignKey(verbose_name='Sales Order', to='crm.SalesOrder', help_text='Sales Order number \t\t\t\t\t\t\t\t\t\t\t \tfor referencing to customer'),
        ),
    ]
