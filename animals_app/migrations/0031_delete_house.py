# Generated by Django 5.1.2 on 2024-11-12 19:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('animals_app', '0030_postimage_delete_image'),
    ]

    operations = [
        migrations.DeleteModel(
            name='House',
        ),
    ]