# Generated by Django 3.2.8 on 2021-11-28 10:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('member', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Annotations',
            fields=[
                ('annotation_id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=20)),
                ('explain', models.TextField()),
            ],
            options={
                'db_table': 'annotations',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='BenchMark',
            fields=[
                ('benchmark_id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('score', models.FloatField()),
            ],
            options={
                'db_table': 'benchmark',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Uses',
            fields=[
                ('uses_id', models.IntegerField(primary_key=True, serialize=False)),
                ('type', models.PositiveIntegerField()),
                ('game_genre', models.PositiveIntegerField(blank=True, null=True)),
                ('name', models.CharField(blank=True, max_length=40, null=True)),
                ('least_processor', models.CharField(blank=True, max_length=100, null=True)),
                ('least_graphics', models.CharField(blank=True, max_length=100, null=True)),
                ('least_memory', models.CharField(blank=True, max_length=30, null=True)),
                ('rec_processor', models.CharField(blank=True, max_length=100, null=True)),
                ('rec_graphics', models.CharField(blank=True, max_length=100, null=True)),
                ('rec_memory', models.CharField(blank=True, max_length=30, null=True)),
            ],
            options={
                'db_table': 'uses',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Estimation',
            fields=[
                ('estimations_id', models.IntegerField(primary_key=True, serialize=False)),
                ('users', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='member.members')),
            ],
            options={
                'db_table': 'estimation',
                'managed': True,
            },
        ),
    ]
