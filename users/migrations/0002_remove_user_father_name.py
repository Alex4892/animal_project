# Generated by Django 5.1.2 on 2024-11-06 10:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='father_name',
        ),
    ]
