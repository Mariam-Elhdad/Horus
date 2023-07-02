# Generated by Django 4.0.8 on 2023-06-23 01:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0002_bank_service_type_hotel_service_type_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=200)),
                ('image', models.URLField()),
                ('description', models.TextField(blank=True, null=True)),
                ('service_type', models.CharField(default='restaurant', max_length=10)),
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
        migrations.DeleteModel(
            name='Restraunt',
        ),
    ]
