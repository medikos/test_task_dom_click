from rest_framework.serializers import ModelSerializer
from processing_app.models import Application


class AccountSerializer(ModelSerializer):
    class Meta:
        model = Application
        fields = ('id', 'status', 'date_created', 'client', 'employee','description')
        read_only_fields = ('date_created','id', 'client')
        