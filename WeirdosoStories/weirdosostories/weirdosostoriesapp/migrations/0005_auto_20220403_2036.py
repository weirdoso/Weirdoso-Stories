# Generated by Django 3.2.12 on 2022-04-03 12:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('weirdosostoriesapp', '0004_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookpost',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
