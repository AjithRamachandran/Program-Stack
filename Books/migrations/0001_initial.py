# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-02-25 09:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='books',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500)),
                ('author', models.CharField(max_length=100)),
            ],
        ),
    ]
