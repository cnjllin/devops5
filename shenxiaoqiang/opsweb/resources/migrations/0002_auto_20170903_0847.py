# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-09-03 08:47
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('resources', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='idc',
            options={'permissions': (('view_idc', 'can show idc list'),)},
        ),
    ]