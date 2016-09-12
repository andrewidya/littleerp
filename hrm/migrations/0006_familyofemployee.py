# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hrm', '0005_auto_20160911_1107'),
    ]

    operations = [
        migrations.CreateModel(
            name='FamilyOfEmployee',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50, verbose_name='Name')),
                ('birth_place', models.CharField(max_length=25, verbose_name='Birth Place')),
                ('birth_date', models.DateField()),
                ('gender', models.CharField(max_length=1, verbose_name='Gender', choices=[(b'P', b'Perempuan'), (b'L', b'Laki-laki')])),
                ('relationship', models.CharField(max_length=1, verbose_name='Relationship', choices=[(b'I', b'Istri'), (b'S', b'Suami'), (b'A', b'Anak')])),
                ('current_activity', models.CharField(max_length=50, null=True, verbose_name='Current Activity', blank=True)),
                ('employee', models.ForeignKey(to='hrm.Employee')),
            ],
        ),
    ]
