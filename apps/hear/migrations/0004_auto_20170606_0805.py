# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-06 02:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hear', '0003_auto_20170603_1208'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hear',
            name='artist',
            field=models.CharField(db_column='artist', max_length=255),
        ),
    ]
