# Generated by Django 3.1.6 on 2022-04-05 09:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('weirdosostoriesapp', '0007_delete_post'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='profile_pic',
            field=models.ImageField(blank=True, null=True, upload_to='images/profile/'),
        ),
    ]
