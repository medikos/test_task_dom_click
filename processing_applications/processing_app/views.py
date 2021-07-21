from rest_framework.decorators import api_view, renderer_classes
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from processing_app.serializers import ApplicationtSerializer
from processing_app.models import Application




@api_view(['GET', 'POST', 'PUT'])
# @renderer_classes((JSONRenderer,))
def index(request):
    query_list = Application.objects.all()
    serializer = ApplicationtSerializer(query_list, many=True)
    return Response(serializer.data)
    

