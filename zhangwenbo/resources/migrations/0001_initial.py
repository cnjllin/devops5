# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-28 08:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Idc',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=10, unique=True, verbose_name='idc 字母简称')),
                ('idc_name', models.CharField(default='', max_length=100, verbose_name='idc 中文名字')),
                ('address', models.CharField(default='', max_length=255, verbose_name='具体的地址，阿里云')),
                ('phone', models.CharField(max_length=20, null=True, verbose_name='机房负责人联系电话')),
                ('email', models.EmailField(max_length=254, null=True, verbose_name='机房联系email')),
                ('username', models.CharField(max_length=32, null=True, verbose_name='机房联系人')),
            ],
        ),
    ]