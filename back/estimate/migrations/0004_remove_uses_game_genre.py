# Generated by Django 3.2.8 on 2021-12-06 11:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('estimate', '0003_auto_20211204_1146'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='uses',
            name='game_genre',
        ),
    ]
