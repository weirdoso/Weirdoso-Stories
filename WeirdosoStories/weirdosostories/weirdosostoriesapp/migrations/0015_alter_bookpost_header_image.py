# Generated by Django 3.2.12 on 2022-04-14 07:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('weirdosostoriesapp', '0014_auto_20220406_0744'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookpost',
            name='header_image',
            field=models.ImageField(blank=True, null=True, upload_to='images/header/'),
        ),
    ]