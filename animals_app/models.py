from django.db import models

class Kind(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name="Вид"
    )
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Вид"
        verbose_name_plural = "Виды"
class Animal(models.Model):
    title = models.CharField(
        max_length=100,
        verbose_name='Заголовок'
    )
    kind = models.CharField(
        max_length=100,
        verbose_name='Вид'
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
    create_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата подачи объявления'
    )
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Животное"
        verbose_name_plural = "Животные"

# Create your models here.
