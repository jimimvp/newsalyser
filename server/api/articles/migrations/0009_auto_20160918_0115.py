# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-18 01:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0008_auto_20160918_0039'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Sources',
        ),
        migrations.AddField(
            model_name='cluster',
            name='category',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
