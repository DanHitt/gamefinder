# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-19 21:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20160308_2238'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='contact_info',
            field=models.CharField(blank=True, max_length=70, null=True),
        ),
    ]
