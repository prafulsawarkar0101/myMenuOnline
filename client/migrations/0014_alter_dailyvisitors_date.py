# Generated by Django 4.1.7 on 2023-08-23 10:33

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0013_alter_dailyvisitors_date_alter_menu_menu_link'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dailyvisitors',
            name='date',
            field=models.DateField(blank=True, default=datetime.datetime(2023, 8, 23, 10, 33, 56, 903770, tzinfo=datetime.timezone.utc), null=True),
        ),
    ]
