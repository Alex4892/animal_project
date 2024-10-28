from django.db import models

class Animal(models.Model):
    # kind = models.CharField(
    #     max_length=100
    # )
    title = models.CharField(
        max_length=200
    )
    description = models.TextField(
        max_length=500
    )
    # publication = models.CharField(
    #     max_length=100
    # )
    # publication_year = models.CharField(
    #     max_length=4
    # )
    # price = models.DecimalField(
    #     max_digits=10,
    #     decimal_places=2
    # )
    # author = models.CharField(
    #     max_length=100
    # )
    create_at = models.DateTimeField(
        auto_now_add=True
    )
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Животное"
        verbose_name_plural = "Животные"

# Create your models here.
