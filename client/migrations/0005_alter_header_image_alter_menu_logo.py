# Generated by Django 4.2.3 on 2023-08-08 18:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0004_rename_discription_header_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='header',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images'),
        ),
        migrations.AlterField(
            model_name='menu',
            name='logo',
            field=models.ImageField(blank=True, null=True, upload_to='images'),
        ),
    ]