# Generated by Django 5.1.2 on 2024-11-19 17:55

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('animals_app', '0034_remove_animal_quantity'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='postimage',
            options={'verbose_name': 'Файл с фотографией', 'verbose_name_plural': 'Файл с фотографиями'},
        ),
        migrations.RemoveField(
            model_name='postimage',
            name='image',
        ),
        migrations.AddField(
            model_name='postimage',
            name='animal',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, related_name='images', to='animals_app.animal', verbose_name='Животные'),
            preserve_default=False,
        ),
    ]
