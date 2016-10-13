# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hrm', '0027_auto_20161011_1910'),
        ('operational', '0012_payroll_overtime'),
    ]

    operations = [
        migrations.CreateModel(
            name='PayrollDetail',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('value', models.DecimalField(null=True, verbose_name=b'Value', max_digits=12, decimal_places=2, blank=True)),
                ('note', models.CharField(max_length=255, verbose_name=b'Note', blank=True)),
            ],
            options={
                'verbose_name': 'Payroll Detail',
                'verbose_name_plural': 'Payroll Details',
            },
        ),
        migrations.AlterModelOptions(
            name='payroll',
            options={'verbose_name': 'Payroll', 'verbose_name_plural': 'Payroll'},
        ),
        migrations.AlterUniqueTogether(
            name='payroll',
            unique_together=set([('contract', 'period')]),
        ),
        migrations.AddField(
            model_name='payrolldetail',
            name='payroll',
            field=models.ForeignKey(verbose_name=b'Payroll', to='operational.Payroll'),
        ),
        migrations.AddField(
            model_name='payrolldetail',
            name='salary',
            field=models.ForeignKey(verbose_name=b'Component', to='hrm.SalaryName'),
        ),
        migrations.AlterUniqueTogether(
            name='payrolldetail',
            unique_together=set([('payroll', 'salary')]),
        ),
    ]
