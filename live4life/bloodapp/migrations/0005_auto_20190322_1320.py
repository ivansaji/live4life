# Generated by Django 2.1.7 on 2019-03-22 13:20

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('bloodapp', '0004_auto_20190322_1231'),
    ]

    operations = [
        migrations.AlterField(
            model_name='acceptor',
            name='date_added',
            field=models.DateTimeField(default=datetime.datetime(2019, 3, 22, 13, 20, 14, 696591, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='donor',
            name='date_added',
            field=models.DateTimeField(default=datetime.datetime(2019, 3, 22, 13, 20, 14, 697253, tzinfo=utc)),
        ),
    ]
