# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-10-06 20:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('offer', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='offer',
            name='accepted',
            field=models.BooleanField(default=False),
        ),
    ]
