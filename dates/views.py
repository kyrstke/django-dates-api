import calendar
import requests

from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import Date, Month
from .serializers import DateSerializer, MonthSerializer


@api_view(['GET', 'POST'])
def get_post_date(request):
    """
    GET: Returns the list of all dates
    POST: Fetches a fact for the date specified in request body from http://numbersapi.com/ and adds the date to the
    database
    """
    if request.method == 'GET':
        dates = Date.objects.all()
        date_serializer = DateSerializer(dates, many=True)

        return Response(date_serializer.data)

    elif request.method == 'POST':

        # DATE
        month_num = int(request.data['month'])
        day = int(request.data['day'])

        # validate the numbers
        if month_num in range(1, 13) and day in range(1, 32):
            month = calendar.month_name[month_num]
            dates = Date.objects.all()

            # check if the date already exists in the database
            if dates:
                possible_duplicate = dates.filter(month=month, day=day)
            else:
                possible_duplicate = None

            if not possible_duplicate:
                fact = requests.get(f'http://numbersapi.com/{month_num}/{day}/date')

                if fact.status_code == 200:
                    date = {
                        "month": month,
                        "day": day,
                        "fact": fact.text
                    }

                    existing_month = Month.objects.all().filter(month=month)

                    if existing_month:
                        existing_month[0].days_checked += 1  # possibly [0]
                        existing_month[0].save()

                    else:
                        month_data = {
                            "month": month,
                            "days_checked": 1
                        }

                        month_serializer = MonthSerializer(data=month_data)

                        if month_serializer.is_valid():
                            month_serializer.save()

                    date_serializer = DateSerializer(data=date)

                    if date_serializer.is_valid():
                        date_serializer.save()

                        return Response(date_serializer.data, status=status.HTTP_201_CREATED)

                    return Response(date_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

                return Response(status=status.HTTP_503_SERVICE_UNAVAILABLE)

            return Response(status=status.HTTP_409_CONFLICT)

        return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def get_popular(request):
    """
    Returns the ranking of months present in the database based on the number of
    days that have been checked
    """
    # months = Date.objects.all().values('month').annotate(days_checked=Count('id')).order_by('-days_checked')
    months = Month.objects.all().order_by('-days_checked')
    serializer = MonthSerializer(months, many=True)

    return Response(serializer.data)


@api_view(['DELETE'])
def delete_date(request, pk):
    """
    Deletes a selected date
    """
    if request.headers.get("X-API-KEY") == "SECRET_API_KEY":
        date = Date.objects.filter(id=pk)
        if not date:
            return Response(status=status.HTTP_404_NOT_FOUND)
        else:

            month = Month.objects.all().filter(month=date[0].month)
            if month:
                month[0].days_checked -= 1
                if month[0].days_checked == 0:
                    month[0].delete()
                else:
                    month[0].save()
            date[0].delete()

            return Response(status=status.HTTP_200_OK)

    return Response(status=status.HTTP_401_UNAUTHORIZED)




