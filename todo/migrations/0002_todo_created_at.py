# Generated by Django 3.2.4 on 2021-06-12 09:39

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2021, 6, 12, 14, 9, 55, 121749)),
        ),
    ]
