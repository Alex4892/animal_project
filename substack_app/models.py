from django.db import models
from django.contrib.auth import get_user_model

from animals_app.models import Animal


User = get_user_model()


class Substack(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='substack'
    )
    animal = models.ForeignKey(
        Animal,
        on_delete=models.CASCADE
    )
    quantity = models.PositiveIntegerField(
        default=1
    )

    class Meta:
        unique_together = ('user', 'animal')
        verbose_name = "Закладка"
        verbose_name_plural = "Закладки"

    def __str__(self):
        return f"{self.user.username} - {self.animal} (x{self.quantity})"

# Create your models here.
