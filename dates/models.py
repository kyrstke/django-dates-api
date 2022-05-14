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

    def toDict(self):
        date = {
            "id": self.id,
            "month": self.month,
            "day": self.day,
            "fact": self.fact,
        }

        return date


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

    def toDict(self):
        date = {
            "id": self.id,
            "month": self.month,
            "days_checked": self.days_checked
        }

        return date

