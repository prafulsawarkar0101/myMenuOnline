# Generated by Django 4.2.3 on 2023-08-03 03:58

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='header',
            name='image',
            field=models.ImageField(blank=True, default='images/sadfrog.jpg', upload_to='images'),
        ),
        migrations.AlterField(
            model_name='menu',
            name='logo',
            field=models.ImageField(blank=True, default='images/sadfrog.jpg', upload_to='images'),
        ),
        migrations.AlterField(
            model_name='menu',
            name='menu_link',
            field=models.CharField(blank=True, default=uuid.uuid4, max_length=100),
        ),
    ]