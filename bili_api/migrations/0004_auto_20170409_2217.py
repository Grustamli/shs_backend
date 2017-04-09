# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2017-04-09 22:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bili_api', '0003_auto_20170403_0012'),
    ]

    operations = [
        migrations.AddField(
            model_name='searchalert',
            name='search_term',
            field=models.CharField(default='something', max_length=150),
            preserve_default=False,
        ),
        migrations.RemoveField(
            model_name='searchalert',
            name='name',
        ),
        migrations.AlterUniqueTogether(
            name='searchalert',
            unique_together=set([('owner', 'search_term')]),
        ),
    ]
