# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-12 09:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='tag',
            field=models.ManyToManyField(blank=True, to='blog.PostHasTags'),
        ),
    ]
