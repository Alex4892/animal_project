# Generated by Django 5.1.2 on 2024-11-21 19:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clinics_app', '0002_alter_clinic_name_clinic'),
    ]

    operations = [
        migrations.AddField(
            model_name='clinic',
            name='adress',
            field=models.TextField(default=2, max_length=30, verbose_name='Адрес'),
            preserve_default=False,
        ),
    ]
