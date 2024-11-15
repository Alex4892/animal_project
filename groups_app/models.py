from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Group(models.Model):
    name_group = models.TextField(
        max_length=30,
        verbose_name='Название группы'
    )
    link = models.TextField(
        max_length=30,
        verbose_name='Ссылка'
    )

    def delete(self, *args, **kwargs):
        if self.image:
            self.image.delete()
        super().delete(*args, **kwargs)

    class Meta:
        verbose_name = "Группа"
        verbose_name_plural = "Группы"

# Create your models here.
