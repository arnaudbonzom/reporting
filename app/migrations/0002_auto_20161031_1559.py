# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-31 15:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mailbox',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]