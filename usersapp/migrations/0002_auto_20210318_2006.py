# Generated by Django 3.1.7 on 2021-03-18 20:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usersapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuser',
            name='birthday_year',
            field=models.PositiveIntegerField(blank=True),
        ),
    ]