# Generated by Django 4.0.4 on 2022-05-13 18:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dates', '0004_alter_date_day'),
    ]

    operations = [
        migrations.AlterField(
            model_name='date',
            name='month',
            field=models.CharField(max_length=9),
        ),
    ]
