# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-01-28 14:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shortener', '0002_auto_20170128_2220'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shortenedurl',
            name='shortCode',
            field=models.CharField(blank=True, max_length=30, unique=True),
        ),
    ]
