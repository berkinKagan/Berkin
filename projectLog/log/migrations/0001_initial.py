# Generated by Django 4.0.5 on 2022-08-05 13:17

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('body', models.CharField(max_length=10000000000000000000000)),
            ],
        ),
    ]
