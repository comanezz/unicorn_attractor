# -*- coding: utf-8 -*-
# Generated by Django 1.11.24 on 2020-05-20 20:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bugs', '0009_bug'),
    ]

    operations = [
        migrations.AddField(
            model_name='bug',
            name='status',
            field=models.CharField(choices=[(0, 'pending'), (1, 'Doing'), (2, 'Done')], default=0, max_length=15),
        ),
    ]
