import json

import requests
from rest_framework import status
# from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser

from .models import Date
from .serializers import DateSerializer


@api_view(['GET', 'POST'])
def get_post_dates(request):
    """
    GET: Returns the list of all dates

    POST: Fetches a fact for a date from http://numbersapi.com/ and adds it
    """
    if request.method == 'GET':
        dates = Date.objects.all()
        serializer = DateSerializer(dates, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        print(request.data)

        data = request.data
        month = data['month']
        day = data['day']

        fact = requests.get(f'http://numbersapi.com/{month}/{day}/date')
        fact_status = fact.status_code

        if fact_status == 200:
            data["fact"] = fact.text

        serializer = DateSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def delete_date(request, pk):
    """
    Delete a selected date
    """
    author = Date.objects.get(id=pk)
    author.delete()

    return Response(status=status.HTTP_200_OK)
