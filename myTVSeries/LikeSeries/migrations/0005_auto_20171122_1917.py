# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-22 18:17
from __future__ import unicode_literals

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LikeSeries', '0004_auto_20171122_1851'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userlikes',
            name='tv_id_liked',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=1000), size=None),
        ),
    ]
