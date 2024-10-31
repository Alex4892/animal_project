# Generated by Django 5.1.2 on 2024-10-31 19:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('animals_app', '0002_alter_animal_nickname_alter_animal_title'),
    ]

    operations = [
        migrations.CreateModel(
            name='Kind',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Вид')),
            ],
            options={
                'verbose_name': 'Жанр',
                'verbose_name_plural': 'Жанры',
            },
        ),
        migrations.AlterField(
            model_name='animal',
            name='create_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Дата подачи объявления'),
        ),
        migrations.AlterField(
            model_name='animal',
            name='description',
            field=models.TextField(max_length=500, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='animal',
            name='kind',
            field=models.CharField(max_length=100, verbose_name='Вид'),
        ),
        migrations.AlterField(
            model_name='animal',
            name='nickname',
            field=models.TextField(max_length=20, verbose_name='Кличка'),
        ),
        migrations.AlterField(
            model_name='animal',
            name='phone_number',
            field=models.CharField(max_length=15, verbose_name='Номер телефона'),
        ),
        migrations.AlterField(
            model_name='animal',
            name='signs',
            field=models.TextField(max_length=100, verbose_name='Приметы'),
        ),
        migrations.AlterField(
            model_name='animal',
            name='title',
            field=models.CharField(max_length=100, verbose_name='Заголовок'),
        ),
    ]
