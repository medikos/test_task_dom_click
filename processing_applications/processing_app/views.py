from datetime import date
from rest_framework import serializers
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from rest_framework import status
from processing_app.serializers import ApplicationtSerializer, ClientSerializer
from processing_app.models import Application, Client




@api_view(['GET', 'POST', 'PUT'])
# @renderer_classes((JSONRenderer,))
def index(request):

    if request.method == 'GET':
        query_list = Application.objects.filter_params(request.query_params)
        serializer = ApplicationtSerializer(query_list, many=True)
        return Response(serializer.data)
    
    if request.method == 'POST':
        data = request.data
        serializer = ApplicationtSerializer(data=data, many=True)
        if serializer.is_valid():
            list_queryset = serializer.save()
            return Response(data=data, status=status.HTTP_201_CREATED)
        else:
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST', 'PUT', 'DELETE',])
def client_view(request):
    if request.method == 'GET':
        client_list = Client.objects.all()
        serializer = ClientSerializer(client_list, many=True)
        return  Response(data=serializer.data, status=status.HTTP_200_OK)
    
    if request.method == 'POST':
        data = request.data
        serializer = ClientSerializer(data=data, many=True)
        if serializer.is_valid():
            list_client = serializer.save()
            return Response(status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    if request.method == 'PUT':
        data = request.data
        id_client = Client.objects.get(pk=data['id'])
        serializer = ClientSerializer(id_client, data=data)

        if serializer.is_valid():
            serializer.save()
            return Response(status = status.HTTP_201_CREATED)
        else:
            return Response(data=serializer.errors,status = status.HTTP_400_BAD_REQUEST)


    

