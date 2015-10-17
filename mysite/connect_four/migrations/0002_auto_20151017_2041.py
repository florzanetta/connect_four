# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('connect_four', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='board',
            name='row1',
            field=models.CharField(max_length=7, default='-------'),
        ),
        migrations.AlterField(
            model_name='board',
            name='row2',
            field=models.CharField(max_length=7, default='-------'),
        ),
        migrations.AlterField(
            model_name='board',
            name='row3',
            field=models.CharField(max_length=7, default='-------'),
        ),
        migrations.AlterField(
            model_name='board',
            name='row4',
            field=models.CharField(max_length=7, default='-------'),
        ),
        migrations.AlterField(
            model_name='board',
            name='row5',
            field=models.CharField(max_length=7, default='-------'),
        ),
        migrations.AlterField(
            model_name='board',
            name='row6',
            field=models.CharField(max_length=7, default='-------'),
        ),
    ]
