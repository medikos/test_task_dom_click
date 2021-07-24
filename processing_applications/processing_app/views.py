from datetime import date
from rest_framework import serializers
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.exceptions import bad_request
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from rest_framework import status
from processing_app.serializers import ApplicationtSerializer, ClientSerializer,EmployeeSerializer
from processing_app.models import Application, Client,Employee




@api_view(['GET', 'POST', 'PUT', 'DELETE'])
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
    
    if request.method == 'PUT':
        data = request.data
        id_application = data.get('id')
        try:
            application_object = Application.objects.get(pk=id_application)
        except Application.DoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUEST)
         
        serializer = ApplicationtSerializer(application_object, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
        else:
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    if request.method == 'DELETE':
        data = request.data
        id = data['id']
        try:
            application_obj = Application.objects.get(pk=id)
        except Application.DoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        else:
            application_obj.delete()
            return Response(status = status.HTTP_200_OK)


            


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
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        serializer = ClientSerializer(id_client, data=data,partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(status = status.HTTP_201_CREATED)
        else:
            return Response(data=serializer.errors,status = status.HTTP_400_BAD_REQUEST)
    
    if request.method == "DELETE":
        data = request.data
        id_client  = data.get('id')
        try:
            client = Client.objects.get(pk =id_client)
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
            serializer = EmployeeSerializer(employee_obj, data=data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(status=status.HTTP_201_CREATED)
            else:
                return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    if request.method == 'DELETE':
        data = request.data
        id_employee =  data.get('id')
        try:
            employee_obj = Employee.objects.get(pk=id_employee)
        except Employee.DoesNotExist:
            return Response(status = status.HTTP_400_BAD_REQUEST)
        else:
            employee_obj.delete()
            return Response(status=status.HTTP_201_CREATED)

            

@api_view(['GET',])
def employee_detail_view(request, pk):

    try:
        employee= Employee.objects.get(pk=pk)
    except Employee.DoesNotExist:
        return Response(status = status.HTTP_400_BAD_REQUEST)
    else:
        serializer = EmployeeSerializer(employee)
        return Response(data=serializer.data, status=status.HTTP_200_OK)




    


        



    

