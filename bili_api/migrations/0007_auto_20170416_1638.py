# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2017-04-16 16:38
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bili_api', '0006_auto_20170409_2330'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='address',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='bili_api.Address'),
        ),
    ]