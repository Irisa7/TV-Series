# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-17 10:08
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('LikeSeries', '0002_auto_20171117_1033'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user_likes',
            name='like_action',
        ),
    ]