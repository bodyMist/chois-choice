# Generated by Django 3.2.8 on 2021-12-06 01:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('component', '0003_alter_cpu_memory_bus'),
    ]

    operations = [
        migrations.RenameField(
            model_name='case',
            old_name='component_componenet',
            new_name='component_component',
        ),
    ]
