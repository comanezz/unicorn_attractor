# -*- coding: utf-8 -*-
# Generated by Django 1.11.24 on 2020-06-17 15:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bugs', '0006_auto_20200608_1927'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bug',
            options={'ordering': ('-created_date',)},
        ),
        migrations.AlterField(
            model_name='bug',
            name='status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('In progress', 'In progress'), ('Done', 'Done')], default='Pending', max_length=15),
        ),
    ]
