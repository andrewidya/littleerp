# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hrm', '0006_familyofemployee'),
    ]

    operations = [
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('grade', models.CharField(max_length=2, verbose_name='Grade', choices=[(b'1', b'SD'), (b'2', b'SMP'), (b'3', b'SMA/SMK Sederajat'), (b'4', b'D1'), (b'5', b'D2'), (b'6', b'D3'), (b'7', b'D4/S1'), (b'8', b'S2/Magister Sederajat'), (b'9', b'S3/Doktoral'), (b'10', b'Akademi/Pelatihan')])),
                ('name', models.CharField(max_length=15, verbose_name='Institution Name')),
                ('address', models.CharField(max_length=100, verbose_name='Address')),
                ('city', models.CharField(max_length=25, verbose_name='City')),
                ('graduation_date', models.DateField()),
                ('certificate_number', models.CharField(max_length=30, verbose_name='Certificate Number')),
                ('description', models.CharField(max_length=255, verbose_name='Short Description')),
                ('employee', models.ForeignKey(to='hrm.Employee')),
            ],
            options={
                'verbose_name': 'Education',
            },
        ),
        migrations.AlterModelOptions(
            name='familyofemployee',
            options={'verbose_name': 'Family Information', 'verbose_name_plural': 'Familiy Informations'},
        ),
    ]
