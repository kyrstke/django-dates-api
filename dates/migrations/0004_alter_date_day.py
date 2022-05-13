# Generated by Django 4.0.4 on 2022-05-13 07:37

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dates', '0003_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='date',
            name='day',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(31)]),
        ),
    ]