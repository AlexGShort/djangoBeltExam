# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-01 16:35
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0002_user_birthdate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='birthdate',
            field=models.DateField(default=datetime.datetime(2017, 2, 1, 11, 35, 40, 316000)),
        ),
    ]
