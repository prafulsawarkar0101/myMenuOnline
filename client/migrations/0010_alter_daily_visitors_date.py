# Generated by Django 4.2.4 on 2023-08-12 03:46

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0009_remove_menu_daily_visitors_daily_visitors'),
    ]

    operations = [
        migrations.AlterField(
            model_name='daily_visitors',
            name='date',
            field=models.DateField(blank=True, default=datetime.datetime(2023, 8, 12, 3, 46, 18, 833775, tzinfo=datetime.timezone.utc), null=True),
        ),
    ]