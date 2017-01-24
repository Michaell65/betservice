# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-23 22:12
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('betservice', '0009_auto_20170123_2250'),
    ]

    operations = [
        migrations.AddField(
            model_name='bet',
            name='win',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='article',
            name='publish_date',
            field=models.DateField(default=datetime.datetime(2017, 1, 23, 22, 12, 50, 467000, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='bet',
            name='created',
            field=models.DateField(default=datetime.datetime(2017, 1, 23, 22, 12, 50, 473000, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='bet',
            name='date',
            field=models.DateField(default=datetime.datetime(2017, 1, 23, 22, 12, 50, 473000, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='news',
            name='publish_date',
            field=models.DateField(default=datetime.datetime(2017, 1, 23, 22, 12, 50, 470000, tzinfo=utc)),
        ),
    ]
