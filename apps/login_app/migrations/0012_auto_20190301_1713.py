# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-03-01 17:13
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('login_app', '0011_posts_notes'),
    ]

    operations = [
        migrations.CreateModel(
            name='Notes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('notes', models.TextField(default=None, max_length=250, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='to_note', to='login_app.register')),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='from_note', to='login_app.register')),
            ],
        ),
        migrations.RemoveField(
            model_name='posts',
            name='notes',
        ),
    ]
