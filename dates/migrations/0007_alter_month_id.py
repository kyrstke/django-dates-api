# Generated by Django 4.0.4 on 2022-05-13 21:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dates', '0006_month'),
    ]

    operations = [
        migrations.AlterField(
            model_name='month',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
