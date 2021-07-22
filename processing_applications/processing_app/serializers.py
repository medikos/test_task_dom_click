import typing
from django.core.exceptions import ValidationError
from django.db import models
from rest_framework import serializers, status
from rest_framework.utils.serializer_helpers import ReturnDict
from processing_app.models import Application, Client, Employee, Position,StatusApplication,TypeApplication

class TypeApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = TypeApplication
        fields = ('name',)

    def validate_name(self, value):
        try:
            TypeApplication.objects.get(name=value)
        except TypeApplication.DoesNotExist:
            raise serializers.ValidationError(f'Type {value} not exist')
        else:
            return value

class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = StatusApplication
        fields = ('name',)
    
    def validate_name(self, value):
        try:
            StatusApplication.objects.get(name=value)
        except StatusApplication.DoesNotExist:
            raise serializers.ValidationError(f'Status {value} not exist')
        else:
            return value
    



class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ('id', 'first_name', 'last_name', 'email', 'telegram_id')


class PositionSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Position
        fields = ('name',)
    
    def validate_name(self, value):
        try:
            Position.objects.get(name=value)
        except Position.DoesNotExist:
            raise serializers.ValidationError(f'Position {value} not exist')
        else:
            return value


class EmployeeSerializer(serializers.ModelSerializer):
    position = PositionSerializer()
    
    class Meta:
        model = Employee
        fields = ('__all__')


    def _get_position(self, position: dict):
    
        return Position.objects.get(name = position['name'])
        

    
    def create(self, validated_data: dict):
        position = validated_data.pop('position')
        position_name = position['name']
        position_object = Position.objects.get(name=position_name)
        first_name = validated_data['first_name']
        last_name = validated_data['last_name']
        return Employee.objects.create(first_name=first_name, last_name=last_name,position=position_object )
    
    def update(self, instance, validated_data):
        first_name = validated_data.get('first_name')
        last_name = validated_data.get('last_name')
        position = validated_data.get('position')

        instance.first_name = first_name  if first_name else instance.first_name
        instance.last_name = last_name if last_name else instance.last_name
        instance.position = self._get_position(position) if position else instance.position
        instance.save()
        return instance








class ApplicationtSerializer(serializers.ModelSerializer):

    date_created  =  serializers.DateField(input_formats=['%d-%m-%Y'], format='%d-%m-%Y')
    client = ClientSerializer(read_only=True)
    employee = EmployeeSerializer(read_only= True)
    status  = StatusSerializer(required=True)
    type = TypeApplicationSerializer(required=True)
    client_id = serializers.IntegerField(required=True, write_only = True)
    employee_id = serializers.IntegerField(write_only=True, required=True)
    class Meta:
        model = Application
        fields = ('id', 'status', 'date_created','employee','client','description', 'type', 'employee_id', 'client_id')
        read_only_fields = ('date_created','id', 'client')


    def validate_client_id(self, value: int):
        try:
            Client.objects.get(pk=value)
        except:
            raise serializers.ValidationError(f'Not exist client with id {value}')
        else:
            return value
    def validate_employee_id(self, value: int):
        try:
            Employee.objects.get(pk=value)
        except:
            raise serializers.ValidationError(f'Nor exist employee with id {value}')
        
        else:
            return value
    
    def _get_status(self, status: dict):
        name = status['name']
        status_object = StatusApplication.objects.get(name=name)
        return status_object
    
    def _get_type(self, type: dict):
        name = type['name']
        type_obect = TypeApplication.objects.get(name= name)
        return type_obect
    
    def _get_client(self, pk):
        client_object = Client.objects.get(pk=pk)
        return client_object 


    def _get_employee(self, pk):
        employee_object = Employee.objects.get(pk=pk)
        return employee_object


    
    def create(self, validated_data):
        status = self._get_status(validated_data['status'])
        type_ = self._get_type(validated_data['type'])
        client = self._get_client(validated_data['client_id'])
        employee =self._get_employee(validated_data['employee_id'])
        description = validated_data['description']
        return Application.objects.create(status=status, type=type_, client= client,
                                             employee=employee,description=description)
    
    def update(self, instance,validated_data):
        status = self._get_status(validated_data['status'])
        type_ = self._get_type(validated_data['type'])
        client = self._get_client(validated_data['client_id'])
        employee =self._get_employee(validated_data['employee_id'])
        description = validated_data['description']
        instance.status = status if status else instance.status
        instance.type = type_ if type_ else instance.type
        instance.client = client if client else instance.client
        instance.employee = employee if employee else instance.employee
        instance.description = description if description else instance.description
        instance.save()
        return instance


