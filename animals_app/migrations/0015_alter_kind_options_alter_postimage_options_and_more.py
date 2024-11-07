# Generated by Django 5.1.2 on 2024-11-07 12:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('animals_app', '0014_alter_kind_options_postimage'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='kind',
            options={'verbose_name': 'Вид', 'verbose_name_plural': 'Виды'},
        ),
        migrations.AlterModelOptions(
            name='postimage',
            options={},
        ),
        migrations.AlterField(
            model_name='postimage',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='animals/', verbose_name='Фото'),
        ),
    ]
