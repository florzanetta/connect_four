# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Board',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('row1', models.CharField(max_length=7)),
                ('row2', models.CharField(max_length=7)),
                ('row3', models.CharField(max_length=7)),
                ('row4', models.CharField(max_length=7)),
                ('row5', models.CharField(max_length=7)),
                ('row6', models.CharField(max_length=7)),
                ('next_turn', models.ForeignKey(related_name='user_next_turn', to=settings.AUTH_USER_MODEL)),
                ('user1', models.ForeignKey(related_name='user1', to=settings.AUTH_USER_MODEL)),
                ('user2', models.ForeignKey(related_name='user2', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
