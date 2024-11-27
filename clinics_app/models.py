from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Clinic(models.Model):
    name_clinic = models.TextField(
        max_length=100,
        verbose_name='Название клиники'
    )
    logo = models.ImageField(
        upload_to='logos/',
        verbose_name='Лого'
    )
    city = models.CharField(
        max_length=50,
        verbose_name='Город'
    )
    adress = models.CharField(
        max_length=255,
        verbose_name='Адрес'
    )
    map_link = models.TextField(
        blank=True,
        null=True,
        verbose_name='Ссылка на клинику'
    )
    phone_number = models.CharField(
        max_length=30,
        verbose_name='Номер телефона'
    )
    cite = models.URLField(
        blank=True,
        null=True,
        verbose_name='Сайт'
    )

    def __str__(self):
        return self.name_clinic

    class Meta:
        verbose_name = "Клиника"
        verbose_name_plural = "Клиники"
