# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-12 09:24
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20160712_1119'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='PostHasTags',
            new_name='Tag',
        ),
    ]
