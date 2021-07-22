from datetime import date
from rest_framework import serializers
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from rest_framework import status
from processing_app.serializers import ApplicationtSerializer, ClientSerializer,EmployeeSerializer
from processing_app.models import Application, Client,Employee




@api_view(['GET', 'POST', 'PUT'])
# @renderer_classes((JSONRenderer,))
def application_view(request):

    if request.method == 'GET':
        query_list = Application.objects.filter_params(request.query_params)
        serializer = ApplicationtSerializer(query_list, many=True)
        return Response(serializer.data)
    
    if request.method == 'POST':
        data = request.data
        serializer = ApplicationtSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
        else:
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET',])
def application_detail_view(request, pk):
    try:
        application_object = Application.objects.get(pk=pk)
    except Application.DoesNotExist:
        return Response(status = status.HTTP_400_BAD_REQUEST)
    else:
        serializer = ApplicationtSerializer(application_object)
        return Response(data=serializer.data, status=status.HTTP_200_OK)





@api_view(['GET', 'POST', 'PUT', 'DELETE',])
def client_view(request):
    if request.method == 'GET':
        client_list = Client.objects.all()
        serializer = ClientSerializer(client_list, many=True)
        return  Response(data=serializer.data, status=status.HTTP_200_OK)
    
    if request.method == 'POST':
        data = request.data
        serializer = ClientSerializer(data=data)
        if serializer.is_valid():
            list_client = serializer.save()
            return Response(status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    if request.method == 'PUT':
        data = request.data
        try:
            id_client = Client.objects.get(pk=data['id'])
        except Client.DoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        serializer = ClientSerializer(id_client, data=data)

        if serializer.is_valid():
            serializer.save()
            return Response(status = status.HTTP_201_CREATED)
        else:
            return Response(data=serializer.errors,status = status.HTTP_400_BAD_REQUEST)
    
    if request.method == 'DELETE':
        data = request.data
        id_client  = data['id']
        try:
            client = Client.objects.get(id_client)
        except Client.DoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        
        else:
            client.delete()
            return Response(status = status.HTTP_200_OK)

@api_view(['GET',])
def client_detail_view(request, pk):
    try:
        client_obj = Client.objects.get(pk=pk)
    except Client.DoesNotExist:
        return Response(status= status.HTTP_400_BAD_REQUEST)
    
    serializer = ClientSerializer(client_obj)
    return Response(serializer.data)
        
@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def employee_view(request):
    if request.method == 'GET':
        employee_list = Employee.objects.all()
        serializer = EmployeeSerializer(employee_list, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)
    
    if request.method == 'POST':
        data = request.data
        serializer = EmployeeSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
        else:
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    if request.method == 'PUT':
        data = request.data
        id_employee = data.get('id')
        try:
            employee_obj = Employee.objects.get(pk=id_employee)
        except Employee.DoesNotExist:
            Response(status=status.HTTP_400_BAD_REQUEST)

        else:
            serializer = EmployeeSerializer(employee_obj, data=data)
            if serializer.is_valid():
                serializer.save()
                return Response(status=status.HTTP_201_CREATED)
            else:
                return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
                
            


        




@api_view(['GET',])
def employee_detail_view(request):
    pass


    


        



    

