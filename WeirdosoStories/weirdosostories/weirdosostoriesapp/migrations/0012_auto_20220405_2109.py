# Generated by Django 3.1.6 on 2022-04-05 13:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('weirdosostoriesapp', '0011_auto_20220405_2019'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='website_url',
            new_name='wattpad_url',
        ),
    ]