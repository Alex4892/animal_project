from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Clinic(models.Model):
    name_clinic = models.TextField(
        max_length=30,
        verbose_name='Название клиники'
    )
    city = models.TextField(
        max_length=30,
        verbose_name='Город'
    )
    phone_number = models.CharField(
        max_length=15,
        verbose_name='Номер телефона'
    )
    def __str__(self):
        return self.name_clinic

    def delete(self, *args, **kwargs):
        if self.image:
            self.image.delete()
        super().delete(*args, **kwargs)

    class Meta:
        verbose_name = "Клиника"
        verbose_name_plural = "Клиники"

# Create your models here.
