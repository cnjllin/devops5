# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-09-18 14:01
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('resources', '0008_delete_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='Serstatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=20, verbose_name='服务器状态')),
            ],
        ),
        migrations.AddField(
            model_name='server',
            name='ser_status',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Serstatus', to='resources.Serstatus'),
        ),
    ]
