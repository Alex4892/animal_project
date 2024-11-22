from django.db import models

from django.contrib.auth import get_user_model

from animals_app.models import Animal


User = get_user_model()


class Favorite(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='favorite'
    )
    animal = models.ForeignKey(
        Animal,
        on_delete=models.CASCADE
    )

    class Meta:
        unique_together = ('user', 'animal')
        verbose_name = "Избранное"
        verbose_name_plural = "Избранные"

    def __str__(self):
        return f"{self.user.username} - {self.animal}"

# Create your models here.
