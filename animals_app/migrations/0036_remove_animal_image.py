# Generated by Django 5.1.2 on 2024-11-19 18:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('animals_app', '0035_alter_postimage_options_remove_postimage_image_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='animal',
            name='image',
        ),
    ]