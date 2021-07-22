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

class EmployeeSerializer(serializers.ModelSerializer):
    position = PositionSerializer()
    class Meta:
        model = Employee
        fields = ('__all__')





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
    
    
    
        
