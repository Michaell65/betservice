# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-23 22:15
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('betservice', '0010_auto_20170123_2312'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='publish_date',
            field=models.DateField(default=datetime.datetime(2017, 1, 23, 22, 15, 4, 427000, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='bet',
            name='created',
            field=models.DateField(default=datetime.datetime(2017, 1, 23, 22, 15, 4, 431000, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='bet',
            name='date',
            field=models.DateField(default=datetime.datetime(2017, 1, 23, 22, 15, 4, 431000, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='bet',
            name='win',
            field=models.IntegerField(default=b'0'),
        ),
        migrations.AlterField(
            model_name='news',
            name='publish_date',
            field=models.DateField(default=datetime.datetime(2017, 1, 23, 22, 15, 4, 429000, tzinfo=utc)),
        ),
    ]
