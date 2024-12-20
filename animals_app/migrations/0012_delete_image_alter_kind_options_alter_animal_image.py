# Generated by Django 5.1.2 on 2024-11-07 12:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('animals_app', '0011_image_alter_kind_options'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Image',
        ),
        migrations.AlterModelOptions(
            name='kind',
            options={'verbose_name': 'Вид', 'verbose_name_plural': 'Виды'},
        ),
        migrations.AlterField(
            model_name='animal',
            name='image',
            field=models.FileField(blank=True, null=True, upload_to='animals/', verbose_name='Фото'),
        ),
    ]
