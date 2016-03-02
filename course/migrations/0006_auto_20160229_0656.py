# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-29 06:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0005_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='content',
            name='images',
            field=models.ManyToManyField(to='course.Image'),
        ),
        migrations.AddField(
            model_name='image',
            name='position',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
