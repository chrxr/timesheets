# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-12 16:02
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_auto_20160610_1724'),
    ]

    operations = [
        migrations.AddField(
            model_name='workday',
            name='days',
            field=models.CharField(blank=True, choices=[('fullDay', 'A full day'), ('halfDay', 'Half a day')], max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='workday',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Project'),
        ),
    ]
