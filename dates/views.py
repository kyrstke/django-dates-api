import json
import calendar
import requests

from rest_framework import status
# from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser

from django.db.models import Count
from .models import Date, Month
from .serializers import DateSerializer, MonthSerializer


@api_view(['GET', 'POST'])
def get_post_dates(request):
    """
    GET: Returns the list of all dates

    POST: Fetches a fact for the date specified in request body from http://numbersapi.com/ and adds the date to the
    database
    """
    if request.method == 'GET':
        dates = Date.objects.all()
        serializer = DateSerializer(dates, many=True)

        return Response(serializer.data)

    elif request.method == 'POST':
        month_num = request.data['month']
        day = request.data['day']

        if month_num in range(1, 13) and day in range(1, 32):
            month = calendar.month_name[month_num]
            fact = requests.get(f'http://numbersapi.com/{month_num}/{day}/date')
            fact_status = fact.status_code

            if fact_status == 200:
                date = {
                    "month": month,
                    "day": day,
                    "fact": fact.text
                }
                serializer = DateSerializer(data=date)

                if serializer.is_valid():  # raise_exception=True
                    serializer.save()
                    return Response(serializer.data, status=status.HTTP_201_CREATED)

                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            else:
                return Response(status=status.HTTP_503_SERVICE_UNAVAILABLE)  # TODO: add an actual error response
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def get_popular(request):
    """
    Returns the ranking of months present in the database based on the number of
    days that have been checked

    """
    months = Date.objects.all().values('month').annotate(days_checked=Count('id')).order_by('-days_checked')
    serializer = MonthSerializer(months, many=True)

    return Response(serializer.data)


@api_view(['DELETE'])
def delete_date(request, pk):
    """
    Delete a selected date
    """
    if request.headers.get("X-API-KEY") == "SECRET_API_KEY":
        date = Date.objects.get(id=pk)
        date.delete()
    else:
        return Response(status=status.HTTP_401_UNAUTHORIZED)

    return Response(status=status.HTTP_200_OK)


