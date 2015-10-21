# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('connect_four', '0002_auto_20151017_2041'),
    ]

    operations = [
        migrations.AddField(
            model_name='board',
            name='winner',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='winner', null=True),
        ),
    ]
