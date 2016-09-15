# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0014_auto_20160914_1648'),
        ('hrm', '0018_auto_20160914_1524'),
        ('operation', '0003_auto_20160914_1504'),
    ]

    operations = [
        migrations.CreateModel(
            name='TrainingAttendance',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('customer', models.ForeignKey(to='crm.Customer')),
                ('employee', models.ForeignKey(to='hrm.Employee')),
            ],
        ),
        migrations.AddField(
            model_name='training',
            name='train_type',
            field=models.ForeignKey(default='', verbose_name='Type of Training', to='operation.TrainingType'),
            preserve_default=False,
        ),
        migrations.RemoveField(
            model_name='training',
            name='customer',
        ),
        migrations.RemoveField(
            model_name='training',
            name='employee',
        ),
        migrations.AddField(
            model_name='trainingattendance',
            name='training',
            field=models.ForeignKey(related_name='training_attendance', to='operation.Training'),
        ),
        migrations.AddField(
            model_name='training',
            name='customer',
            field=models.ManyToManyField(to='crm.Customer', through='operation.TrainingAttendance'),
        ),
        migrations.AddField(
            model_name='training',
            name='employee',
            field=models.ManyToManyField(to='hrm.Employee', through='operation.TrainingAttendance'),
        ),
    ]
