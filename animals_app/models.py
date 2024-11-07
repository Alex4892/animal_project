from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

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

class PostImage(models.Model):
    image = models.ImageField(
        upload_to='animals/',
        blank=True,
        null=True,
        verbose_name='Фото'
    )
    images = models.ImageField(
        upload_to = 'animals/'
    )

    class Meta:
        verbose_name = "Фото"
        verbose_name_plural = "Фото"

class Animal(models.Model):
    title = models.CharField(
        max_length=100,
        verbose_name='Заголовок'
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
    phone_number = models.CharField(
        max_length=15,
        verbose_name='Номер телефона'
    )
    signs = models.TextField(
        max_length=100,
        verbose_name='Приметы'
    )
    image = models.ImageField(
        upload_to='animals/',
        blank=True,
        null=True,
        verbose_name='Фото'
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
        return self.title
    
    def delete(self, *args, **kwargs):
        if self.image:
            self.image.delete()
        super().delete(*args, **kwargs)
    
    class Meta:
        verbose_name = "Заголовок"
        verbose_name_plural = "Заголовки"

# Create your models here.
