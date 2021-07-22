from django.core.exceptions import ValidationError
from rest_framework import serializers
from processing_app.models import Application, Client, Employee, Position,StatusApplication


class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = StatusApplication
        fields = ('name',)

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
    client = ClientSerializer( read_only=True)
    employee = EmployeeSerializer(label='Hello')
    status  = StatusSerializer()
    class Meta:
        model = Application
        fields = ('id', 'status', 'date_created','employee','client','description', 'type')
        read_only_fields = ('date_created','id', 'client')
    
    def create(self, validated_data):
        print(self)
        
        return {1:'Hello'}
    
    
    
        
