# Generated by Django 5.1.2 on 2024-11-23 10:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clinics_app', '0003_clinic_adress'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clinic',
            name='adress',
            field=models.TextField(max_length=50, verbose_name='Адрес'),
        ),
    ]
