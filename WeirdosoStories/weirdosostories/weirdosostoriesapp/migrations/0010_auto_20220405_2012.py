# Generated by Django 3.1.6 on 2022-04-05 12:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('weirdosostoriesapp', '0009_auto_20220405_1825'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_pic',
            field=models.ImageField(blank=True, null=True, upload_to='\\images\\profile'),
        ),
    ]