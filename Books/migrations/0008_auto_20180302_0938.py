# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-03-02 04:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Books', '0007_remove_book_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='logo',
            field=models.FileField(max_length=500, null=True, upload_to=''),
        ),
    ]