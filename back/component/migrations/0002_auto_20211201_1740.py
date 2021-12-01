# Generated by Django 3.2.8 on 2021-12-01 17:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('component', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='case',
            name='compatibility',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='case',
            name='size',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='component',
            name='manufacture',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='cooler',
            name='fan_size',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='cpu',
            name='basic_clock',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='cpu',
            name='max_clock',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='gpu',
            name='height',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='gpu',
            name='width',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='mainboard',
            name='graphic',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='mainboard',
            name='memory_capacity',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='power',
            name='certification',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='power',
            name='main_cable',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='power',
            name='sub_cable',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
