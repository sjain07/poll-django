# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-10-03 13:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20170807_1747'),
    ]

    operations = [
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=200)),
                ('MobileNo', models.CharField(max_length=10)),
            ],
        ),
    ]