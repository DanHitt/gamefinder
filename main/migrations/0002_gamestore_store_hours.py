# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-08 22:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='gamestore',
            name='store_hours',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
