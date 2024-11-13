from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class House(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name="Цель объявления"
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Цель для нового дома"
        verbose_name_plural = "Цели для нового дома"


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
    house = models.ManyToManyField(
        House,
        verbose_name='Цель объявления'
    )

    kind = models.ManyToManyField(
        Kind,
        verbose_name='Вид животного'
    )

    description = models.TextField(
        max_length=500,
        verbose_name='Описание'
    )

    # city = models.TextField(
    #     max_length=30,
    #     verbose_name='Город'
    # )

    # phone_number = models.CharField(
    #     max_length=15,
    #     verbose_name='Номер телефона'
    # )

    # contact_people = models.CharField(
    #     max_length=100,
    #     verbose_name='Контактное лицо'
    # )

    class Meta:
        verbose_name = "Объявление"
        verbose_name_plural = "Объявления"

# Create your models here.
