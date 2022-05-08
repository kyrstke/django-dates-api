from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class Date(models.Model):
    month = models.IntegerField(
        validators=[
            MinValueValidator(1),
            MaxValueValidator(12)
        ]
    )

    day = models.IntegerField(
        validators=[
            MinValueValidator(1),
            MaxValueValidator(12)
        ]
    )

    fact = models.TextField(blank=True, null=True)

