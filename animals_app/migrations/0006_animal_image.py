# Generated by Django 5.1.2 on 2024-11-03 07:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('animals_app', '0005_alter_animal_options_remove_animal_kind_animal_kind'),
    ]

    operations = [
        migrations.AddField(
            model_name='animal',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='animals/', verbose_name='Изображение'),
        ),
    ]