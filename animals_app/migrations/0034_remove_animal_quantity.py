# Generated by Django 5.1.2 on 2024-11-13 12:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('animals_app', '0033_animal_quantity'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='animal',
            name='quantity',
        ),
    ]
