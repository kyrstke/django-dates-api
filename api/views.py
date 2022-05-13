from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from dates.models import Date
from dates.serializers import DateSerializer


@api_view(['GET', 'POST', 'DELETE'])
def api_home(request, pk):
    """
    :param request:
    :param pk:
    :return:
    """
    try:
        instance = Date.objects.get(pk=pk)
    except Date.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        instance = Date.objects.all().order_by("?").first()
        # all().order_by("?").first()
        data = {}
        if instance:
            # data = model_to_dict(instance, fields=['id', 'month', 'day', 'fact'])
            data = DateSerializer(instance).data
        return Response(data)

    elif request.method == 'POST':
        serializer = DateSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            print(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


