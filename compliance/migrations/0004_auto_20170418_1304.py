# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-18 18:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('compliance', '0003_auto_20170418_1241'),
    ]

    operations = [
        migrations.AlterField(
            model_name='continuingeducationlog',
            name='repeat',
            field=models.CharField(choices=[('Biannually', 'Biannually'), ('Yearly', 'Yearly'), ('Every 2 years', 'Every 2 years'), ('Every 3 years', 'Every 3 years'), ('Every 4 years', 'Every 4 years'), ('Every 5 years', 'Every 5 years'), ('Other', 'Other')], max_length=200),
        ),
    ]
