# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-22 18:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LikeSeries', '0005_auto_20171122_1917'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userlikes',
            name='tv_id_liked',
            field=models.CharField(max_length=100),
        ),
    ]
