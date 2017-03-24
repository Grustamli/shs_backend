# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2017-03-24 22:58
from __future__ import unicode_literals

import bili_api.models.user
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('bili_api', '0003_address_phonenumber'),
    ]

    operations = [
        migrations.CreateModel(
            name='PrivacySetting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_visible', models.BooleanField(default=False)),
                ('email_visible', models.BooleanField(default=False)),
                ('address_visible', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_pic', models.ImageField(upload_to=bili_api.models.user.Profile.profile_pic_directory_path)),
                ('owner', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RenameField(
            model_name='addontype',
            old_name='az',
            new_name='lang_az',
        ),
        migrations.RenameField(
            model_name='addontype',
            old_name='en',
            new_name='lang_en',
        ),
        migrations.RenameField(
            model_name='addontype',
            old_name='ru',
            new_name='lang_ru',
        ),
        migrations.RenameField(
            model_name='addontype',
            old_name='tr',
            new_name='lang_tr',
        ),
        migrations.AlterUniqueTogether(
            name='address',
            unique_together=set([('content_type', 'object_id')]),
        ),
        migrations.AlterUniqueTogether(
            name='phonenumber',
            unique_together=set([('content_type', 'object_id')]),
        ),
        migrations.AddField(
            model_name='privacysetting',
            name='profile',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='privacy_setting', to='bili_api.Profile'),
        ),
    ]
