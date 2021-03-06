# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-29 16:18
from __future__ import unicode_literals

import ckeditor.fields
import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('betservice', '0003_auto_20161227_1611'),
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('url', models.CharField(max_length=200)),
                ('publish_date', models.DateField(default=datetime.datetime(2016, 12, 29, 16, 18, 37, 22000, tzinfo=utc))),
                ('description', models.TextField()),
                ('content', ckeditor.fields.RichTextField(null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='article',
            name='publish_date',
            field=models.DateField(default=datetime.datetime(2016, 12, 29, 16, 18, 37, 20000, tzinfo=utc)),
        ),
    ]
