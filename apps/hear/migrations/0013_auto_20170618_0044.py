# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-17 18:44
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hear', '0012_auto_20170618_0043'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='melody',
            options={'get_latest_by': 'id', 'ordering': ['id'], 'verbose_name': 'Мелодия', 'verbose_name_plural': 'Мелодии'},
        ),
    ]
