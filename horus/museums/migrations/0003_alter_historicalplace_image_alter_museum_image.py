# Generated by Django 4.0.8 on 2023-06-23 19:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('museums', '0002_historicalplace_service_type_museum_service_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historicalplace',
            name='image',
            field=models.URLField(default='https://egymonuments.gov.eg/en/museums/egyptian-museum'),
        ),
        migrations.AlterField(
            model_name='museum',
            name='image',
            field=models.URLField(default='https://egymonuments.gov.eg/en/museums/egyptian-museum'),
        ),
    ]