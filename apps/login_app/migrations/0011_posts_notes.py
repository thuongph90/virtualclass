# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-03-01 16:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login_app', '0010_auto_20190227_2141'),
    ]

    operations = [
        migrations.AddField(
            model_name='posts',
            name='notes',
            field=models.TextField(default=None, max_length=250, null=True),
        ),
    ]
