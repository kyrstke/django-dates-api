from rest_framework import serializers
from .models import Date, Month


class DateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Date
        fields = [
            'id',
            'month',
            'day',
            'fact',
        ]


class MonthSerializer(serializers.ModelSerializer):
    class Meta:
        model = Month
        fields = [
            'id',
            'month',
            'days_checked',
        ]

        # ordering = ['days_checked']
