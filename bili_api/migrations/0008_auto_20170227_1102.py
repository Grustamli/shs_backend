# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2017-02-27 11:02
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bili_api', '0007_auto_20170227_0038'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adimage',
            name='ad',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='bili_api.Ad'),
        ),
    ]
