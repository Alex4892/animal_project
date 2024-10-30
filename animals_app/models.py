from django.db import models

class Animal(models.Model):
    title = models.CharField(
        max_length=200
    )
    kind = models.CharField(
        max_length=100
    )
    nickname = models.TextField(
        max_length=500
    )
    description = models.TextField(
        max_length=500
    )
    phone_number = models.CharField(
        max_length=15
    )
    signs = models.TextField(
        max_length=100
    )
    create_at = models.DateTimeField(
        auto_now_add=True
    )
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Животное"
        verbose_name_plural = "Животные"

# Create your models here.
