from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class Date(models.Model):

    month = models.CharField(
        blank=False,
        null=False,
        max_length=9
    )

    #     models.IntegerField(
    #     validators=[
    #         MinValueValidator(1),
    #         MaxValueValidator(12)
    #     ]
    # )

    day = models.IntegerField(
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

    id = models.AutoField(primary_key=True)

    month = models.CharField(
        blank=False,
        null=False,
        max_length=9
    )

    days_checked = models.IntegerField(
        validators=[
            MinValueValidator(0)
        ]
    )

