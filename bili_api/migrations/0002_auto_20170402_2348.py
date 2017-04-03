# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2017-04-02 23:48
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bili_api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adthumbnail',
            name='ad',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='thumbnail', to='bili_api.Ad'),
        ),
    ]
