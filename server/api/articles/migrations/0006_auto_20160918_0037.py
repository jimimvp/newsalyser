# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-18 00:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0005_article_tags'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='brand',
            field=models.CharField(max_length=300),
        ),
        migrations.AlterField(
            model_name='article',
            name='title',
            field=models.CharField(max_length=300),
        ),
        migrations.AlterField(
            model_name='article',
            name='url',
            field=models.CharField(max_length=300, unique=True),
        ),
    ]
