# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-04-22 20:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('blog_text', models.CharField(max_length=10000)),
            ],
        ),
    ]
