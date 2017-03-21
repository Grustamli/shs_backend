# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2017-03-21 17:23
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bili_api', '0006_auto_20170321_1707'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='useraddress',
            name='address',
        ),
        migrations.RemoveField(
            model_name='useraddress',
            name='region',
        ),
        migrations.AlterField(
            model_name='adaddress',
            name='city',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='ad_addresses', to='bili_api.City'),
        ),
        migrations.AlterField(
            model_name='useraddress',
            name='city',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_addresses', to='bili_api.City'),
        ),
    ]