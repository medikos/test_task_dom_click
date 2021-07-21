from rest_framework import serializers
from processing_app.models import Application


class ApplicationtSerializer(serializers.ModelSerializer):
    date_created  =  serializers.DateField(format='%d-%m-%y')
    class Meta:
        model = Application
        fields = ('id', 'statuses', 'date_created', 'client', 'employee','description')
        read_only_fields = ('date_created','id', 'client')
