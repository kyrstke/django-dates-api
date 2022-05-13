from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class Date(models.Model):

    month = models.CharField(
        blank=False,
        null=False,
        max_length=9
    )

    day = models.IntegerField(
        blank=False,
        null=False,
        validators=[
            MinValueValidator(1),
            MaxValueValidator(31)
        ]
    )

    fact = models.TextField(
        blank=True,
        null=True
    )


class Month(models.Model):

    month = models.CharField(
        blank=False,
        null=False,
        max_length=9
    )

    days_checked = models.IntegerField(
        blank=False,
        null=False,
        validators=[
            MinValueValidator(0)
        ]
    )

