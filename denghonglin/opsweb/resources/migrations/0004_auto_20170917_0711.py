# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-17 07:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resources', '0003_server'),
    ]

    operations = [
        migrations.AlterField(
            model_name='server',
            name='check_update_time',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]