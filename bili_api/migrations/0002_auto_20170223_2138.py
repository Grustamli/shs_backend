# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2017-02-23 21:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bili_api', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='id',
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=15, primary_key=True, serialize=False),
        ),
    ]
