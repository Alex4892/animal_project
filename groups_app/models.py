from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Group(models.Model):
    name_group = models.CharField(
        max_length=100,
        verbose_name='Название группы'
    )
    link_vk = models.CharField(
        verbose_name='Ссылка в VK'
    )
    cite = models.URLField(
        blank=True,
        null=True,
        verbose_name='Сайт'
    )

    def __str__(self):
        return self.name_group

    class Meta:
        verbose_name = "Группа"
        verbose_name_plural = "Группы"

# Create your models here.
