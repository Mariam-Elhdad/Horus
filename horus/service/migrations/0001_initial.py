# Generated by Django 4.0.8 on 2023-03-04 18:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bank',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=200)),
                ('image', models.URLField()),
                ('description', models.TextField(blank=True, null=True)),
                ('link', models.URLField()),
                ('telephone', models.CharField(blank=True, max_length=25, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Hotel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=200)),
                ('image', models.URLField()),
                ('description', models.TextField(blank=True, null=True)),
                ('review', models.SmallIntegerField()),
                ('cleanlinsess_review', models.SmallIntegerField(blank=True, null=True)),
                ('service_review', models.SmallIntegerField(blank=True, null=True)),
                ('value_review', models.SmallIntegerField(blank=True, null=True)),
                ('language_spoken', models.CharField(max_length=200)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Restraunt',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=200)),
                ('image', models.URLField()),
                ('description', models.TextField(blank=True, null=True)),
                ('telephone', models.CharField(blank=True, max_length=25, null=True)),
                ('website', models.CharField(blank=True, max_length=250, null=True)),
                ('open_from', models.TimeField(blank=True, null=True)),
                ('open_to', models.TimeField(blank=True, null=True)),
                ('rating', models.SmallIntegerField()),
                ('cuisines', models.TextField(blank=True, null=True)),
                ('features', models.TextField(blank=True, null=True)),
                ('meals', models.TextField(blank=True, null=True)),
                ('type_r', models.CharField(blank=True, max_length=150, null=True)),
                ('menu', models.URLField(blank=True, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
