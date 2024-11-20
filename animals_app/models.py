from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Target(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name="Цель объявления"
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Цель"
        verbose_name_plural = "Цели"


class Kind(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name="Вид животного"
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Вид"
        verbose_name_plural = "Виды"



class Animal(models.Model):
    target = models.ManyToManyField(
        Target,
        verbose_name='Цель объявления'
    )
    kind = models.ManyToManyField(
        Kind,
        verbose_name='Вид животного'
    )
    nickname = models.TextField(
        max_length=20,
        verbose_name='Кличка'
    )
    description = models.TextField(
        max_length=500,
        verbose_name='Описание'
    )
    signs = models.TextField(
        max_length=100,
        verbose_name='Приметы'
    )
    city = models.TextField(
        max_length=30,
        verbose_name='Город'
    )
    phone_number = models.CharField(
        max_length=15,
        verbose_name='Номер телефона'
    )
    contact_people = models.CharField(
        max_length=100,
        verbose_name='Контактное лицо'
    )
    submit = models.ForeignKey(
        User,
        related_name="animals",
        on_delete=models.CASCADE,
        verbose_name="Подающий объявление"
    )
    create_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата подачи объявления'
    )
    is_verified = models.BooleanField(
        default=False,
        verbose_name='Проверено администратором?'
    )

    def __str__(self):
        return self.nickname

    # def delete(self, *args, **kwargs):
    #     if self.image:
    #         self.image.delete()
    #     super().delete(*args, **kwargs)

    class Meta:
        verbose_name = "Объявление"
        verbose_name_plural = "Объявления"


class PostImage(models.Model):
    animal = models.ForeignKey(
        Animal,
        on_delete=models.CASCADE,
        related_name='images',
        verbose_name='Животные',
    )
    images = models.ImageField(
        upload_to='animals/',
    )

    def __str__(self):
        return f'Фото'

    class Meta:
        verbose_name = 'Файл с фотографией'
        verbose_name_plural = 'Файл с фотографиями'

# Create your models here.
