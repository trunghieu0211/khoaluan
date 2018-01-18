from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from cosovatchats.models import Cosovatchat
from cosovatchats.serializers import CosovatchatSerializer


@api_view(['GET', 'POST'])
def cosovatchat_list(request):
    """
    List all code cosovatchats, or create a new cosovatchat.
    """
    if request.method == 'GET':
        cosovatchats = Cosovatchat.objects.all()
        serializer = CosovatchatSerializer(cosovatchats, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = CosovatchatSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
@api_view(['GET', 'PUT', 'DELETE'])
def cosovatchat_detail(request, pk):
    """
    Retrieve, update or delete a code cosovatchat.
    """
    try:
        cosovatchat = Cosovatchat.objects.get(pk=pk)
    except Cosovatchat.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = CosovatchatSerializer(cosovatchat)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = CosovatchatSerializer(cosovatchat, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        cosovatchat.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)