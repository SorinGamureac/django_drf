# Generated by Django 3.1.7 on 2021-03-18 20:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usersapp', '0002_auto_20210318_2006'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuser',
            name='birthday_year',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]
